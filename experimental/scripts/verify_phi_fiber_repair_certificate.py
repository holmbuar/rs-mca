#!/usr/bin/env python3
"""Fail-closed verifier for the Lean phi-fiber repair certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Mapping


ROOT = Path(__file__).resolve().parents[2]
BASE_SHA = "4bea7abb2d9455583c8864b980e39d11d550f51d"
OLD_FIBER_BLOB = "d00a46604a3c1e8fddeb466c4370b4f7faa2afdc"
OLD_FIBER_SHA256 = "9172f177bcd2b58b80bcda06a0b1fe8e41357e6331cd8cffce9ffba8a5152368"
REPAIRED_FIBER_BLOB = "119d55c6ce1924d729594e64f92dc02b8e31aa17"
REPAIRED_FIBER_SHA256 = "efa03a962901f163206802c5241f1a9278ac574e528add7efe6cf56b47e0ab46"
TEX_BLOB = "5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb"
TEX_SHA256 = "356f1ad4b972746b664260191387b25a89a2e10fcc61962a49dc8282412f93ce"

FIBER_PATH = "experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean"
TEX_PATH = "tex/cs25_cap_v13_2.tex"
PACKAGE = "experimental/lean/cs25_phi_fiber_repair_certificate"
PACKET_PATH = f"{PACKAGE}/Cs25PhiFiberRepairCertificate.lean"
LAKEFILE_PATH = f"{PACKAGE}/lakefile.lean"
TOOLCHAIN_PATH = f"{PACKAGE}/lean-toolchain"
MANIFEST_PATH = f"{PACKAGE}/lake-manifest.json"
OLD_OBJECT_KEY = "@old-fiber-object"

FORBIDDEN = re.compile(r"\b(?:sorry|admit|axiom|native_decide)\b")

OLD_FIBER_DECL = """theorem lem_phi_fiber_ii (dom : ι → F) (hdom : Function.Injective dom)
    (B : Subfield F) [Fintype B] (hdomB : ∀ i, dom i ∈ B)
    (φ : Polynomial F) {a N k ℓ₂ A₂ : ℕ}
    (ha : 0 < a) (hφdeg : φ.natDegree = a) (haN : a * N = Fintype.card ι)
    (hsmooth : DomSmooth dom (fun x => φ.eval x) a)
    (hℓ₂ : ℓ₂ = k / a + 2) (hℓ₂N : ℓ₂ ≤ N - 1) (hA₂ : A₂ = a * ℓ₂) :
    ∃ (z : F) (_ : z ∈ B) (L : ℕ),
      (Nat.choose N ℓ₂ : ℝ) / (Fintype.card B : ℝ) ≤ (L : ℝ) ∧
      HasList (RSpoly dom (k + 1))
        (1 - (A₂ : ℝ) / Fintype.card ι)
        (fun i => (φ.eval (dom i)) ^ ℓ₂ + z * (φ.eval (dom i)) ^ (ℓ₂ - 1)) L := by"""

REPAIRED_FIBER_DECL = """theorem lem_phi_fiber_ii (dom : ι → F) (hdom : Function.Injective dom)
    (B : Subfield F) [Fintype B] (hdomB : ∀ i, dom i ∈ B)
    (φ : Polynomial F) {a N k ℓ₂ A₂ : ℕ}
    (ha : 0 < a) (hφdeg : φ.natDegree = a)
    (hQB : ∀ i, φ.eval (dom i) ∈ B)
    (haN : a * N = Fintype.card ι)
    (hsmooth : DomSmooth dom (fun x => φ.eval x) a)
    (hℓ₂ : ℓ₂ = k / a + 2) (hℓ₂N : ℓ₂ ≤ N - 1) (hA₂ : A₂ = a * ℓ₂) :
    ∃ (z : F) (_ : z ∈ B) (L : ℕ),
      (Nat.choose N ℓ₂ : ℝ) / (Fintype.card B : ℝ) ≤ (L : ℝ) ∧
      HasList (RSpoly dom (k + 1))
        (1 - (A₂ : ℝ) / Fintype.card ι)
        (fun i => (φ.eval (dom i)) ^ ℓ₂ + z * (φ.eval (dom i)) ^ (ℓ₂ - 1)) L := by"""

PRE_REPAIR_DEF = """def LemPhiFiberIIPreRepair : Prop :=
  ∀ {ι : Type u} {F : Type v} [Fintype ι] [Field F] [Fintype F],
    ∀ (dom : ι → F) (hdom : Function.Injective dom)
      (B : Subfield F) [Fintype B] (hdomB : ∀ i, dom i ∈ B)
      (φ : Polynomial F) {a N k ℓ₂ A₂ : ℕ}
      (ha : 0 < a) (hφdeg : φ.natDegree = a)
      (haN : a * N = Fintype.card ι)
      (hsmooth : DomSmooth dom (fun x => φ.eval x) a)
      (hℓ₂ : ℓ₂ = k / a + 2) (hℓ₂N : ℓ₂ ≤ N - 1)
      (hA₂ : A₂ = a * ℓ₂),
    ∃ (z : F) (_ : z ∈ B) (L : ℕ),
      (Nat.choose N ℓ₂ : ℝ) / (Fintype.card B : ℝ) ≤ (L : ℝ) ∧
      HasList (RSpoly dom (k + 1))
        (1 - (A₂ : ℝ) / Fintype.card ι)
        (fun i => (φ.eval (dom i)) ^ ℓ₂ +
          z * (φ.eval (dom i)) ^ (ℓ₂ - 1)) L"""

FALSE_THEOREM_DECL = """theorem lem_phi_fiber_ii_pre_repair_false :
    ¬ LemPhiFiberIIPreRepair.{0, 0} := by"""

HQB_FAILURE_DECL = """theorem phi_eval_not_mem_B4 (x : K4) : phi.eval (emb x) ∉ B4 := by"""

BASE_POLYNOMIAL_DECL = """theorem lem_phi_fiber_ii_of_basePolynomial
    {ι F : Type*} [Fintype ι] [Field F]
    (dom : ι → F) (hdom : Function.Injective dom)
    (B : Subfield F) [Fintype B] (hdomB : ∀ i, dom i ∈ B)
    (φB : Polynomial B) {a N k ℓ₂ A₂ : ℕ}
    (ha : 0 < a) (hφdeg : φB.natDegree = a)
    (haN : a * N = Fintype.card ι)
    (hsmooth : DomSmooth dom (fun x => (φB.map B.subtype).eval x) a)
    (hℓ₂ : ℓ₂ = k / a + 2) (hℓ₂N : ℓ₂ ≤ N - 1)
    (hA₂ : A₂ = a * ℓ₂) :
    ∃ (z : F) (_ : z ∈ B) (L : ℕ),
      (Nat.choose N ℓ₂ : ℝ) / (Fintype.card B : ℝ) ≤ (L : ℝ) ∧
      HasList (RSpoly dom (k + 1))
        (1 - (A₂ : ℝ) / Fintype.card ι)
        (fun i => ((φB.map B.subtype).eval (dom i)) ^ ℓ₂ +
          z * ((φB.map B.subtype).eval (dom i)) ^ (ℓ₂ - 1)) L := by"""


def normalized(text: str) -> str:
    return " ".join(text.split())


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def git(args: list[str], *, binary: bool = False) -> bytes | str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=not binary,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout if binary else result.stdout.strip()


def load(relative: str, overrides: Mapping[str, bytes]) -> bytes | None:
    if relative in overrides:
        return overrides[relative]
    try:
        return (ROOT / relative).read_bytes()
    except OSError:
        return None


def old_object(overrides: Mapping[str, bytes], blob: str) -> bytes | None:
    if OLD_OBJECT_KEY in overrides:
        return overrides[OLD_OBJECT_KEY]
    value = git(["cat-file", "blob", blob], binary=True)
    return value if isinstance(value, bytes) else None


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.total = 0
        self.failures: list[str] = []

    def check(self, condition: bool, label: str) -> None:
        self.total += 1
        if condition:
            self.passed += 1
        else:
            self.failures.append(label)


def verify(
    overrides: Mapping[str, bytes] | None = None,
    pins: Mapping[str, str] | None = None,
) -> Checks:
    overrides = overrides or {}
    pin_values = {
        "base": BASE_SHA,
        "old_blob": OLD_FIBER_BLOB,
        "old_sha256": OLD_FIBER_SHA256,
        "repaired_blob": REPAIRED_FIBER_BLOB,
        "repaired_sha256": REPAIRED_FIBER_SHA256,
        "tex_blob": TEX_BLOB,
        "tex_sha256": TEX_SHA256,
    }
    if pins:
        pin_values.update(pins)
    checks = Checks()

    base = pin_values["base"]
    checks.check(git(["cat-file", "-t", base]) == "commit", "base commit exists")
    checks.check(git(["merge-base", "HEAD", base]) == base, "base commit is an ancestor of HEAD")

    old_blob = pin_values["old_blob"]
    old = old_object(overrides, old_blob)
    checks.check(git(["cat-file", "-t", old_blob]) == "blob", "old Fiber Git object exists")
    checks.check(old is not None and git_blob_sha1(old) == old_blob, "old Fiber Git blob pin")
    checks.check(old is not None and sha256(old) == pin_values["old_sha256"], "old Fiber SHA256 pin")

    repaired = load(FIBER_PATH, overrides)
    checks.check(repaired is not None, "repaired Fiber exists")
    checks.check(
        repaired is not None and git_blob_sha1(repaired) == pin_values["repaired_blob"],
        "repaired Fiber Git blob pin",
    )
    checks.check(
        repaired is not None and sha256(repaired) == pin_values["repaired_sha256"],
        "repaired Fiber SHA256 pin",
    )
    checks.check(
        git(["rev-parse", f"{base}:{FIBER_PATH}"]) == pin_values["repaired_blob"],
        "base tree repaired Fiber pin",
    )

    tex = load(TEX_PATH, overrides)
    checks.check(tex is not None, "Paper D TeX exists")
    checks.check(tex is not None and git_blob_sha1(tex) == pin_values["tex_blob"], "Paper D TeX Git blob pin")
    checks.check(tex is not None and sha256(tex) == pin_values["tex_sha256"], "Paper D TeX SHA256 pin")
    checks.check(
        git(["rev-parse", f"{base}:{TEX_PATH}"]) == pin_values["tex_blob"],
        "base tree Paper D TeX pin",
    )

    old_text = old.decode("utf-8") if old is not None else ""
    repaired_text = repaired.decode("utf-8") if repaired is not None else ""
    tex_text = tex.decode("utf-8") if tex is not None else ""
    checks.check(normalized(OLD_FIBER_DECL) in normalized(old_text), "exact pre-repair Fiber declaration")
    checks.check("hQB" not in old_text, "pre-repair Fiber omits hQB")
    checks.check(normalized(REPAIRED_FIBER_DECL) in normalized(repaired_text), "exact repaired Fiber declaration")
    checks.check("(hQB : ∀ i, φ.eval (dom i) ∈ B)" in repaired_text, "repaired value-level tie")

    checks.check(r"\label{def:map-smooth}" in tex_text, "map-smooth source label")
    checks.check(r"let $\varphi\in\B[X]$ have degree $a\ge1$" in tex_text, "paper coefficient-level premise")
    checks.check(r"let $D\subseteq\B$" in tex_text, "paper base-domain premise")
    checks.check(r"\label{lem:phi-fiber}" in tex_text, "phi-fiber source label")
    checks.check(
        r"$z_A=-\eone(A)$ lies in $\B$ because $A\subseteq Q\subseteq\B$" in tex_text,
        "paper base-field proof anchor",
    )

    packet = load(PACKET_PATH, overrides)
    packet_text = packet.decode("utf-8") if packet is not None else ""
    packet_norm = normalized(packet_text)
    checks.check(packet is not None, "packet Lean exists")
    checks.check(
        re.findall(r"^import .+$", packet_text, flags=re.MULTILINE)
        == ["import cs25_cap_v12.Fiber"],
        "exact packet import set",
    )
    checks.check(FORBIDDEN.search(packet_text) is None, "packet Lean has no forbidden placeholders")
    checks.check("namespace RSCap\n" in packet_text and packet_text.rstrip().endswith("end RSCap"), "RSCap namespace wrapper")
    checks.check(packet_norm.count(normalized(PRE_REPAIR_DEF)) == 1, "exact LemPhiFiberIIPreRepair declaration")
    checks.check(packet_norm.count(normalized(FALSE_THEOREM_DECL)) == 1, "exact pre-repair falsity theorem declaration")
    checks.check(packet_norm.count(normalized(HQB_FAILURE_DECL)) == 1, "exact hQB-failure witness declaration")
    checks.check(packet_norm.count(normalized(BASE_POLYNOMIAL_DECL)) == 1, "exact base-polynomial wrapper declaration")
    checks.check("universe u v" in packet_text, "explicit universe parameters")
    checks.check(
        "have hbad := h (dom := emb) emb.injective B4 dom_in_base phi" in packet_text,
        "universe-zero counterexample application",
    )
    checks.check(
        "exact lem_phi_fiber_ii dom hdom B hdomB (φB.map B.subtype)\n    ha hφdegF hQB haN hsmooth hℓ₂ hℓ₂N hA₂" in packet_text,
        "wrapper consumes repaired hQB theorem",
    )
    checks.check(
        "exact Polynomial.eval_map_apply (p := φB) B.subtype x" in packet_text,
        "coefficient-to-value bridge",
    )
    checks.check(
        "#print axioms RSCap.lem_phi_fiber_ii_pre_repair_false" in packet_text
        and "#print axioms RSCap.lem_phi_fiber_ii_of_basePolynomial" in packet_text,
        "axiom print anchors",
    )

    lakefile = load(LAKEFILE_PATH, overrides)
    lakefile_text = lakefile.decode("utf-8") if lakefile is not None else ""
    lakefile_expected = """import Lake
open Lake DSL
package «cs25_phi_fiber_repair_certificate»
require «cs25_cap_v12» from "../cs25_cap_v12"
@[default_target]
lean_lib Cs25PhiFiberRepairCertificate"""
    checks.check(lakefile is not None, "lakefile exists")
    checks.check(normalized(lakefile_text) == normalized(lakefile_expected), "exact lakefile metadata")

    toolchain = load(TOOLCHAIN_PATH, overrides)
    checks.check(toolchain == b"leanprover/lean4:v4.28.0\n", "exact Lean toolchain metadata")

    manifest_bytes = load(MANIFEST_PATH, overrides)
    try:
        manifest = json.loads(manifest_bytes) if manifest_bytes is not None else None
    except (json.JSONDecodeError, UnicodeDecodeError):
        manifest = None
    checks.check(isinstance(manifest, dict), "manifest is valid JSON")
    checks.check(isinstance(manifest, dict) and manifest.get("name") == "cs25_phi_fiber_repair_certificate", "manifest package name")
    checks.check(isinstance(manifest, dict) and manifest.get("lakeDir") == ".lake", "manifest Lake directory")
    packages = manifest.get("packages", []) if isinstance(manifest, dict) else []
    local_deps = [row for row in packages if isinstance(row, dict) and row.get("name") == "cs25_cap_v12"]
    checks.check(
        len(local_deps) == 1
        and local_deps[0].get("type") == "path"
        and local_deps[0].get("dir") == "../cs25_cap_v12"
        and local_deps[0].get("configFile") == "lakefile.toml",
        "manifest local package dependency",
    )
    mathlib = [row for row in packages if isinstance(row, dict) and row.get("name") == "mathlib"]
    checks.check(
        len(mathlib) == 1
        and mathlib[0].get("rev") == "8f9d9cff6bd728b17a24e163c9402775d9e6a365"
        and mathlib[0].get("inputRev") == "v4.28.0",
        "manifest Mathlib pin",
    )

    return checks


def mutate_once(data: bytes, old: bytes, new: bytes) -> bytes:
    if data.count(old) != 1:
        raise RuntimeError(f"tamper target occurs {data.count(old)} times, expected once")
    return data.replace(old, new, 1)


def tamper_selftest() -> tuple[int, int]:
    files = {
        path: (ROOT / path).read_bytes()
        for path in (FIBER_PATH, TEX_PATH, PACKET_PATH, LAKEFILE_PATH, TOOLCHAIN_PATH, MANIFEST_PATH)
    }
    old = old_object({}, OLD_FIBER_BLOB)
    if old is None:
        raise RuntimeError("missing old Fiber object for tamper self-test")

    cases: list[tuple[str, Mapping[str, bytes], Mapping[str, str]]] = [
        ("base SHA", {}, {"base": "0" * 40}),
        ("old Fiber artifact", {OLD_OBJECT_KEY: old + b"\n"}, {}),
        ("repaired Fiber artifact", {FIBER_PATH: files[FIBER_PATH] + b"\n"}, {}),
        ("TeX artifact", {TEX_PATH: files[TEX_PATH] + b"\n"}, {}),
        (
            "packet Lean artifact",
            {
                PACKET_PATH: mutate_once(
                    files[PACKET_PATH],
                    b"import cs25_cap_v12.Fiber",
                    b"import cs25_cap_v12.CircleCode",
                )
            },
            {},
        ),
        (
            "pre-repair definition",
            {
                PACKET_PATH: mutate_once(
                    files[PACKET_PATH],
                    b"      (haN : a * N =",
                    b"      (haN : a + N =",
                )
            },
            {},
        ),
        (
            "falsity theorem",
            {PACKET_PATH: mutate_once(files[PACKET_PATH], b"LemPhiFiberIIPreRepair.{0, 0}", b"LemPhiFiberIIPreRepair.{1, 0}")},
            {},
        ),
        (
            "hQB-failure witness",
            {
                PACKET_PATH: mutate_once(
                    files[PACKET_PATH],
                    "phi.eval (emb x) ∉ B4".encode(),
                    "phi.eval (emb x) ∈ B4".encode(),
                )
            },
            {},
        ),
        (
            "base-polynomial wrapper",
            {
                PACKET_PATH: mutate_once(
                    files[PACKET_PATH],
                    "(φB : Polynomial B)".encode(),
                    "(φB : Polynomial F)".encode(),
                )
            },
            {},
        ),
        (
            "forbidden token gate",
            {PACKET_PATH: files[PACKET_PATH] + b"\naxiom injected : True\n"},
            {},
        ),
        (
            "lakefile metadata",
            {LAKEFILE_PATH: mutate_once(files[LAKEFILE_PATH], b"@[default_target]", b"@[test_driver]")},
            {},
        ),
        (
            "toolchain metadata",
            {TOOLCHAIN_PATH: b"leanprover/lean4:v4.27.0\n"},
            {},
        ),
        (
            "manifest metadata",
            {MANIFEST_PATH: mutate_once(files[MANIFEST_PATH], b'"name": "cs25_phi_fiber_repair_certificate"', b'"name": "wrong_package"')},
            {},
        ),
    ]
    caught = 0
    for _, overrides, pins in cases:
        if verify(overrides, pins).failures:
            caught += 1
    return caught, len(cases)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    if args.tamper_selftest:
        try:
            caught, total = tamper_selftest()
        except (OSError, RuntimeError) as error:
            print(f"tamper-selftest: FAIL ({error})")
            return 1
        print(f"tamper-selftest: caught {caught}/{total}")
        if caught != total:
            return 1

    result = verify()
    if result.failures:
        if not args.check:
            for failure in result.failures:
                print(f"FAIL: {failure}")
        print(f"RESULT: FAIL ({result.passed}/{result.total})")
        return 1
    print(f"RESULT: PASS ({result.passed}/{result.total})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
