#!/usr/bin/env python3
"""Fail-closed source/proof checks for fixed-size subset packing in Lean."""

from __future__ import annotations

import argparse
import copy
import hashlib
import re
import sys
from pathlib import Path
from typing import Callable, Dict, Sequence


class VerificationError(RuntimeError):
    """A source, theorem, proof-boundary, package, or tamper check failed."""


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "experimental/lean/complete_fiber_subset_packing"
PATHS = {
    "source": ROOT / "experimental/notes/l2/dyadic_complete_fiber_slicing_route_cut.md",
    "lean": PACKAGE / "CompleteFiberSubsetPacking.lean",
    "intersection_lean": ROOT / (
        "experimental/lean/dyadic_complete_fiber_slicing/"
        "DyadicCompleteFiberSlicingTarget.lean"
    ),
    "readme": PACKAGE / "README.md",
    "audit": ROOT / "experimental/notes/l2/complete_fiber_subset_packing_formalization.md",
    "lakefile": PACKAGE / "lakefile.lean",
    "manifest": PACKAGE / "lake-manifest.json",
    "toolchain": PACKAGE / "lean-toolchain",
    "gitignore": PACKAGE / ".gitignore",
}
EXPECTED_SHA256 = {
    "source": "fba4b3541f6f6c982ae9327fcdcf14b11ba266e6ce09647f0b95d30b70369e13",
    "lean": "685c56405c480b520a3c712751a88b4d90e938ebe09a846e1e59360c486ca51f",
    "intersection_lean": "35942729e65815a01e79aacdece585598d57ccf249786d19c6562d59ae46adb8",
    "readme": "9fdcbf292d9e33c0c983825c0f8953b6c9397811def97ddccf8b0b0aabd8d21e",
    "audit": "36bba2247986e93ff9df8ba98b3e320e7bb9533db1490e07e307f19718222a96",
    "lakefile": "c27d5a8c89d1d406b74fa27359764aae4fbdd3f49729537bc83da92d6bc86ee7",
    "manifest": "845d57f2702b0644927d9f59e9e4317fab7b3f082c5e7d97f4c8fbb34cac8a5e",
    "toolchain": "db7bb24b756d745bbde83fe92718b51bd3625dae3701ba0f598d0eedcd3f3028",
    "gitignore": "5375c2c5e323f40c0031aa8c82f66bb9197214001039e6a8c9ff2a5eb3aa24a9",
}

MAIN_SIGNATURE = """theorem subsetPacking_finite_and_ncard_le
    (ground : Finset α) (objects : Set β) (block : β → Finset α)
    (e h : Nat)
    (hsub : ∀ b ∈ objects, block b ⊆ ground)
    (hcard : ∀ b ∈ objects, (block b).card = e)
    (hinter : ∀ b₁ ∈ objects, ∀ b₂ ∈ objects,
      b₁ ≠ b₂ → (block b₁ ∩ block b₂).card ≤ h)
    (he : h + 1 ≤ e) :
    objects.Finite ∧
      objects.ncard ≤ ground.card.choose (h + 1) / e.choose (h + 1) := by"""

CONNECTOR_SIGNATURE = """theorem completeFiberSubsetPacking
    (H : Subgroup Fˣ) [Fintype H] [LinearOrder H]
    (n K m c e : Nat)
    (hHcard : Fintype.card H = n)
    (hrange : 1 ≤ K ∧ K ≤ m ∧ m ≤ n)
    (hc : c ∣ n)
    (U : H → F)
    (he : (K - 1) / c + 1 ≤ e) :
    (fixedFiberPolynomialSet H K m c e U).Finite ∧
      (fixedFiberPolynomialSet H K m c e U).ncard ≤
        (powerImage H c).card.choose ((K - 1) / c + 1) /
          e.choose ((K - 1) / c + 1) := by"""

SOURCE_ANCHORS = (
    "For every two distinct\n`P,Q in L(U)`,",
    "|E_c(P) intersect E_c(Q)| <= h_c.                       (1)",
    "Consequently, for every fixed `e >= h_c+1`,",
    "#{P in L(U) : e_c(P)=e}\n  <= floor(binomial(N_c,h_c+1) / binomial(e,h_c+1)).     (2)",
    "<= floor(binomial(N_c,h_c+1) / binomial(e,h_c+1)).     (2)",
    "No `(h_c+1)`-subset of `Q_c` can occur in two equal-size\nfiber sets, proving (2) by double counting.",
    "The quantifier over `U` is universal.",
    "now proves equation (1) as\n`DyadicCompleteFiberSlicing.completeFiberIntersection`",
    "The literal Grand List theorem remains open",
    "the official score remains\n`0/2`",
)

PROOF_ANCHORS = (
    "private theorem finset_mul_choose_le",
    "(↑blocks : Set (Finset α)).PairwiseDisjoint",
    "have hTsubA : T ⊆ A := (Finset.mem_powersetCard.mp hTA).1",
    "Finset.card_biUnion hdisj",
    "rw [Finset.card_powersetCard, hcard A hA]",
    "have hinj : Set.InjOn block objects",
    "himageFinite.of_finite_image hinj",
    "Finset.card_image_of_injOn hblockInj",
    "have hden : 0 < e.choose (h + 1) := Nat.choose_pos he",
    "Nat.le_div_iff_mul_le hden",
    "Set.ncard_eq_toFinset_card objects hobjectsFinite",
    "noncomputable def fixedFiberPolynomialSet",
    "(completeFiberSet H c (canonicalSupport H m U P)).card = e",
    "theorem completeFiberSubsetPacking",
    "(ground := powerImage H c)",
    "(objects := fixedFiberPolynomialSet H K m c e U)",
    "(block := fun P => completeFiberSet H c (canonicalSupport H m U P))",
    "exact completeFiberIntersection H n K m c hHcard hrange hc U P Q",
)

README_ANCHORS = (
    "# Complete-fiber subset-packing formalization map",
    "Equation (2), fixed-size subset-packing kernel",
    "`CompleteFiberSubsetPacking.subsetPacking_finite_and_ncard_le` | PROVED",
    "`CompleteFiberSubsetPacking.completeFiberSubsetPacking` | PROVED",
    "first proves that the object set is\nfinite",
    "#objects <= floor(choose(#ground, h_c + 1) / choose(e, h_c + 1))",
    "does not appear in the exported theorem signature",
    "[propext, Classical.choice, Quot.sound]",
    "defines the fixed-`e`\nset of received-list polynomials",
    "definitionally the source's\n`N_c = |Q_c|`",
    "does not separately prove the\nnormalization `(powerImage H c).card = n / c`",
    "Equation (3), deployed\narithmetic",
)

AUDIT_ANCHORS = (
    "## Status\n\nPROVED",
    "fixed-size subset-packing compiler used for\nequation (2)",
    "`CompleteFiberSubsetPacking.subsetPacking_finite_and_ncard_le`",
    "`CompleteFiberSubsetPacking.completeFiberSubsetPacking`",
    "It concludes both that `objects` is finite",
    "no `DecidableEq alpha` or\n`DecidableEq beta` parameter",
    "the block map is injective on `objects`",
    "`Finset.card_biUnion` and `Finset.card_powersetCard`",
    "`Nat.choose_pos` makes the denominator positive",
    "[propext, Classical.choice, Quot.sound]",
    "## Source connector",
    "`DyadicCompleteFiberSlicing.completeFiberIntersection`",
    "The numerator\n`(powerImage H c).card` is exactly the source definition `N_c = |Q_c|`",
    "source-specific equation-(2) wrapper",
    "does not separately formalize the\ngroup-cardinality rewrite `(powerImage H c).card = n/c`",
    "No Johnson-ball packing theorem (equation (3))",
    "Grand List, Grand MCA",
)


def read_bundle() -> Dict[str, str]:
    bundle: Dict[str, str] = {}
    for key, path in PATHS.items():
        try:
            bundle[key] = path.read_text(encoding="utf-8")
        except OSError as error:
            raise VerificationError(
                f"cannot read {path.relative_to(ROOT)}: {error}"
            ) from error
    return bundle


def verify_bundle(bundle: Dict[str, str]) -> int:
    checks = 0

    def require(condition: bool, message: str) -> None:
        nonlocal checks
        if not condition:
            raise VerificationError(message)
        checks += 1

    for key, expected in EXPECTED_SHA256.items():
        actual = hashlib.sha256(bundle[key].encode("utf-8")).hexdigest()
        require(actual == expected, f"pinned {key} artifact changed")

    source = bundle["source"]
    lean = bundle["lean"]
    intersection_lean = bundle["intersection_lean"]
    readme = bundle["readme"]
    audit = bundle["audit"]
    lakefile = bundle["lakefile"]
    manifest = bundle["manifest"]
    toolchain = bundle["toolchain"]
    gitignore = bundle["gitignore"]

    for anchor in SOURCE_ANCHORS:
        require(source.count(anchor) == 1, f"source boundary changed: {anchor!r}")
    require(lean.count(MAIN_SIGNATURE) == 1, "exact main declaration changed or duplicated")
    require(
        lean.count(CONNECTOR_SIGNATURE) == 1,
        "exact source connector changed or duplicated",
    )
    require(
        lean.count("theorem subsetPacking_finite_and_ncard_le") == 1,
        "main theorem name duplicated",
    )
    require(
        lean.count("theorem completeFiberSubsetPacking") == 1,
        "source connector name duplicated",
    )
    for anchor in PROOF_ANCHORS:
        require(lean.count(anchor) == 1, f"proof anchor changed: {anchor!r}")
    require(
        lean.count("local instance : DecidableEq α := Classical.decEq α") == 1,
        "local decidable-equality elaboration instance changed",
    )
    require(
        re.search(r"\b(?:sorry|admit|axiom|opaque|sorryAx|native_decide)\b", lean) is None,
        "placeholder, custom axiom, opaque declaration, or native_decide found",
    )
    require(
        re.search(
            r"\b(?:sorry|admit|axiom|opaque|sorryAx|native_decide)\b",
            intersection_lean,
        )
        is None,
        "equation-(1) dependency contains a placeholder or custom axiom",
    )
    require(
        intersection_lean.count("theorem completeFiberIntersection") == 1,
        "equation-(1) dependency declaration changed or duplicated",
    )
    for anchor in README_ANCHORS:
        require(readme.count(anchor) == 1, f"README boundary changed: {anchor!r}")
    for anchor in AUDIT_ANCHORS:
        require(audit.count(anchor) == 1, f"audit boundary changed: {anchor!r}")

    require(
        lakefile == """import Lake

open Lake DSL

package complete_fiber_subset_packing where

require dyadic_complete_fiber_slicing from "../dyadic_complete_fiber_slicing"

@[default_target]
lean_lib CompleteFiberSubsetPacking where
  roots := #[`CompleteFiberSubsetPacking]
""",
        "Lake root/library lock changed",
    )
    require(toolchain == "leanprover/lean4:v4.28.0\n", "Lean toolchain lock changed")
    require(gitignore == "/.lake/\n", "build-artifact ignore changed")
    require(
        manifest.count('"type": "path"') == 1
        and manifest.count('"name": "dyadic_complete_fiber_slicing"') == 1
        and manifest.count('"dir": "../dyadic_complete_fiber_slicing"') == 1
        and manifest.count('"rev": "8f9d9cff6bd728b17a24e163c9402775d9e6a365"') == 1
        and manifest.count('"inputRev": "v4.28.0"') == 2
        and '"name": "complete_fiber_subset_packing"' in manifest,
        "Mathlib manifest pin or package identity changed",
    )
    return checks


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise VerificationError(f"tamper target is not unique: {old!r}")
    return text.replace(old, new, 1)


def tamper_selftest(bundle: Dict[str, str]) -> int:
    mutations: Sequence[tuple[str, Callable[[Dict[str, str]], None]]] = (
        (
            "source bound",
            lambda b: b.__setitem__(
                "source",
                replace_once(
                    b["source"],
                    "binomial(N_c,h_c+1) / binomial(e,h_c+1)",
                    "binomial(N_c,h_c) / binomial(e,h_c)",
                ),
            ),
        ),
        (
            "source score",
            lambda b: b.__setitem__(
                "source", replace_once(b["source"], "official score remains `0/2`", "official score is `2/2`")
            ),
        ),
        (
            "main theorem name",
            lambda b: b.__setitem__(
                "lean",
                replace_once(
                    b["lean"],
                    "theorem subsetPacking_finite_and_ncard_le",
                    "theorem subsetPacking_claim",
                ),
            ),
        ),
        (
            "source connector name",
            lambda b: b.__setitem__(
                "lean",
                replace_once(
                    b["lean"],
                    "theorem completeFiberSubsetPacking",
                    "theorem completeFiberSubsetPackingClaim",
                ),
            ),
        ),
        (
            "source connector threshold",
            lambda b: b.__setitem__(
                "lean",
                replace_once(
                    b["lean"],
                    "(he : (K - 1) / c + 1 ≤ e)",
                    "(he : (K - 1) / c ≤ e)",
                ),
            ),
        ),
        (
            "source connector ground",
            lambda b: b.__setitem__(
                "lean",
                replace_once(
                    b["lean"],
                    "(ground := powerImage H c)",
                    "(ground := powerImage H (c + 1))",
                ),
            ),
        ),
        (
            "source connector equation1 call",
            lambda b: b.__setitem__(
                "lean",
                replace_once(
                    b["lean"],
                    "completeFiberIntersection H n K m c hHcard hrange hc U P Q",
                    "completeFiberIntersection H n K m c hHcard hrange hc U Q P",
                ),
            ),
        ),
        (
            "drop finiteness conclusion",
            lambda b: b.__setitem__(
                "lean", replace_once(b["lean"], "objects.Finite ∧\n", "True ∧\n")
            ),
        ),
        (
            "weaken exact block size",
            lambda b: b.__setitem__(
                "lean",
                replace_once(
                    b["lean"],
                    "(hcard : ∀ b ∈ objects, (block b).card = e)",
                    "(hcard : ∀ b ∈ objects, (block b).card ≤ e)",
                ),
            ),
        ),
        (
            "change intersection threshold",
            lambda b: b.__setitem__(
                "lean",
                replace_once(
                    b["lean"],
                    "b₁ ≠ b₂ → (block b₁ ∩ block b₂).card ≤ h)",
                    "b₁ ≠ b₂ → (block b₁ ∩ block b₂).card ≤ h + 1)",
                ),
            ),
        ),
        (
            "change denominator",
            lambda b: b.__setitem__(
                "lean",
                replace_once(
                    b["lean"],
                    "e.choose (h + 1) := by",
                    "e.choose h := by",
                ),
            ),
        ),
        (
            "break disjoint union",
            lambda b: b.__setitem__(
                "lean",
                replace_once(b["lean"], "Finset.card_biUnion hdisj", "Finset.card_biUnion (by simp)"),
            ),
        ),
        (
            "break choose positivity",
            lambda b: b.__setitem__(
                "lean",
                replace_once(b["lean"], "Nat.choose_pos he", "Nat.zero_lt_succ _"),
            ),
        ),
        (
            "proof placeholder",
            lambda b: b.__setitem__(
                "lean",
                replace_once(b["lean"], "  classical\n  have hinj", "  sorry\n  classical\n  have hinj"),
            ),
        ),
        (
            "custom axiom",
            lambda b: b.__setitem__("lean", "axiom hiddenPacking : False\n" + b["lean"]),
        ),
        (
            "hidden section assumption",
            lambda b: b.__setitem__(
                "lean",
                replace_once(
                    b["lean"],
                    "variable {α β : Type*}\n",
                    "class HiddenAssumption : Prop where out : False\n"
                    "variable [HiddenAssumption]\nvariable {α β : Type*}\n",
                ),
            ),
        ),
        (
            "README normalization boundary",
            lambda b: b.__setitem__(
                "readme",
                replace_once(
                    b["readme"],
                    "does not separately prove the\nnormalization",
                    "also proves the\nnormalization",
                ),
            ),
        ),
        (
            "README equation3 overclaim",
            lambda b: b.__setitem__(
                "readme",
                replace_once(
                    b["readme"],
                    "Equation (3), deployed\narithmetic",
                    "Equation (3) and deployed\narithmetic",
                ),
            ),
        ),
        (
            "audit status",
            lambda b: b.__setitem__(
                "audit", replace_once(b["audit"], "## Status\n\nPROVED", "## Status\n\nCONDITIONAL")
            ),
        ),
        (
            "audit normalization boundary",
            lambda b: b.__setitem__(
                "audit",
                replace_once(
                    b["audit"],
                    "does not separately formalize the\ngroup-cardinality rewrite",
                    "also formalizes the\ngroup-cardinality rewrite",
                ),
            ),
        ),
        (
            "equation1 dependency placeholder",
            lambda b: b.__setitem__(
                "intersection_lean",
                replace_once(
                    b["intersection_lean"],
                    "theorem completeFiberIntersection",
                    "axiom completeFiberIntersection",
                ),
            ),
        ),
        (
            "drop package root",
            lambda b: b.__setitem__(
                "lakefile", replace_once(b["lakefile"], "  roots := #[`CompleteFiberSubsetPacking]\n", "")
            ),
        ),
        (
            "drop equation1 package dependency",
            lambda b: b.__setitem__(
                "lakefile",
                replace_once(
                    b["lakefile"],
                    'require dyadic_complete_fiber_slicing from "../dyadic_complete_fiber_slicing"\n',
                    "",
                ),
            ),
        ),
        (
            "change Mathlib revision",
            lambda b: b.__setitem__(
                "manifest",
                replace_once(b["manifest"], "8f9d9cff6bd728b17a24e163c9402775d9e6a365", "0" * 40),
            ),
        ),
        (
            "change Lean toolchain",
            lambda b: b.__setitem__(
                "toolchain", replace_once(b["toolchain"], "v4.28.0", "v4.27.0")
            ),
        ),
        (
            "unignore build artifacts",
            lambda b: b.__setitem__("gitignore", ""),
        ),
    )
    caught = 0
    for name, mutate in mutations:
        altered = copy.deepcopy(bundle)
        mutate(altered)
        try:
            verify_bundle(altered)
        except VerificationError:
            caught += 1
        else:
            raise VerificationError(f"tamper was not detected: {name}")
    if caught != len(mutations):
        raise VerificationError("tamper suite did not run completely")
    return caught


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args(argv)
    if not args.check and not args.tamper_selftest:
        parser.error("pass --check and/or --tamper-selftest")
    try:
        bundle = read_bundle()
        checks = verify_bundle(bundle)
        if args.tamper_selftest:
            caught = tamper_selftest(bundle)
            print(f"tamper-selftest: caught {caught}/{caught}")
        print(f"RESULT: PASS ({checks}/{checks})")
        return 0
    except VerificationError as error:
        print(f"RESULT: FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
