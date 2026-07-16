#!/usr/bin/env python3
"""Verify the Paving v8 retained-factor content-root counterexample.

This exact, standard-library audit checks one pinned F_7 counterexample to
RF1--RF3, the corrected content envelope, source bindings, and the fact that
the four deployed KoalaBear rows are numerically unchanged.  It does not
prove the remaining Hensel/factor-lifting import.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAIN_TEX = ROOT / "experimental" / "RS_MCA_Paving_v8.tex"
RELEASE_TEX = (
    ROOT / "experimental" / "RS_MCA_Paving_v8_source" / "RS_MCA_Paving_v8.tex"
)
PRIOR_AUDIT = (
    ROOT
    / "experimental"
    / "notes"
    / "audits"
    / "koalabear_bchks25_parametric_list_mca_lemma_v1.md"
)


class VerificationError(RuntimeError):
    """Raised when a pinned audit condition fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


@dataclass(frozen=True)
class Counterexample:
    field_order: int
    domain: tuple[int, ...]
    n: int
    agreement: int
    radius: int
    dimension: int
    multiplicity: int
    dx: Fraction
    dy: Fraction
    dz: Fraction
    support: tuple[int, ...]
    slopes: tuple[int, ...]
    p0_values: tuple[int, ...]
    u0_values: tuple[int, ...]
    u1_values: tuple[int, ...]
    q_weighted_degree: int
    q_y_degree: int
    q_yz_degree: int


PINNED = Counterexample(
    field_order=7,
    domain=(1, 2, 4),
    n=3,
    agreement=3,
    radius=0,
    dimension=1,
    multiplicity=1,
    dx=Fraction(21, 10),
    dy=Fraction(1, 100),
    dz=Fraction(11, 10),
    support=(1, 2, 4),
    slopes=(0,),
    p0_values=(0, 0, 0),
    u0_values=(0, 0, 0),
    u1_values=(1, 2, 4),
    # Q(X,Y,Z)=Z.
    q_weighted_degree=0,
    q_y_degree=0,
    q_yz_degree=1,
)


def verify_counterexample(case: Counterexample) -> dict[str, Fraction | int]:
    p = case.field_order
    require(p == 7, "the pinned field must be F_7")
    require(len(set(case.domain)) == len(case.domain), "domain points are not distinct")
    require(all(0 <= x < p for x in case.domain), "domain point is outside F_7")
    require(case.n == len(case.domain), "n is not the domain size")
    require(case.agreement == case.n - case.radius, "A != n-r")
    require(case.radius >= 0, "radius is negative")
    require(case.dimension >= 1, "K is not positive")
    require(
        case.agreement >= case.dimension + 2,
        "preamble A>=K+2 failed",
    )
    require(case.multiplicity >= 1, "multiplicity is not positive")
    require(
        case.dx > 0 and case.dy > 0 and case.dz > 0,
        "a degree parameter is not positive",
    )
    require(case.support == case.domain, "the chosen support is not all of D")
    require(len(case.support) == case.agreement, "chosen support has the wrong size")
    require(len(set(case.slopes)) == len(case.slopes), "slopes are not distinct")

    u = ceil_fraction(case.dx)
    v = ceil_fraction(case.dy)
    w = ceil_fraction(case.dz)
    require((u, v, w) == (3, 1, 2), "unexpected ceiling triple")

    # RF1.
    require(v >= case.multiplicity, "RF1 V>=m failed")
    require(w >= v, "RF1 W>=V failed")
    require(u > case.dimension * (v - 1), "RF1 rank inequality failed")
    require(case.dx < case.multiplicity * case.agreement, "RF1 D_X<mA failed")
    require(p > v - 1, "RF1 characteristic inequality failed")

    # RF2.
    top_lhs = (case.agreement - case.dimension - 1) * (2 * u - 1)
    top_rhs = (case.n - case.dimension - 1) * (2 * case.dimension + 1)
    require((top_lhs, top_rhs) == (5, 3), "unexpected RF2 top-degree values")
    require(top_lhs > top_rhs, "RF2 top-degree inequality failed")
    require(Fraction(p) > 2 * u * case.dy, "RF2 field-size inequality failed")

    # Q=Z has the three required strict degree bounds.
    require(case.q_weighted_degree < case.dx, "Q weighted-degree bound failed")
    require(case.q_y_degree < case.dy, "Q Y-degree bound failed")
    require(case.q_yz_degree < case.dz, "Q (Y,Z)-degree bound failed")

    # For the sole slope gamma=0, P_0=0 is a root and agrees with
    # u_0+gamma*u_1 on the full chosen support.
    gamma = case.slopes[0]
    require(gamma == 0, "the pinned root slope changed")
    require(all(gamma % p == 0 for _ in case.domain), "Q(X,P_0,gamma) is nonzero")
    require(all(value == 0 for value in case.p0_values), "P_0 is not zero")
    require(
        all(
            p0 % p == (u0 + gamma * u1) % p
            for p0, u0, u1 in zip(
                case.p0_values, case.u0_values, case.u1_values, strict=True
            )
        ),
        "P_0 does not agree with u_0+gamma*u_1 on A_0",
    )

    alpha = 2 * u * case.dy * case.dy
    old_rhs = alpha * case.dz + (case.radius + 1) * case.dy
    corrected_rhs = max(Fraction(1), alpha) * case.dz + (
        case.radius + 1
    ) * case.dy
    d_content = Fraction(1)
    exact_content_charge = (
        d_content
        + alpha * (case.dz - d_content)
        + (case.radius + 1) * case.dy
    )
    require(alpha == Fraction(3, 5000), "unexpected content coefficient")
    require(old_rhs == Fraction(533, 50000), "unexpected old RF3 threshold")
    require(Fraction(len(case.slopes)) > old_rhs, "old RF3 is not triggered")
    require(corrected_rhs == Fraction(111, 100), "unexpected corrected threshold")
    require(
        Fraction(len(case.slopes)) <= corrected_rhs,
        "corrected threshold does not exclude the counterexample",
    )
    require(
        exact_content_charge == Fraction(50503, 50000),
        "unexpected exact charge at content degree one",
    )

    # Degree < K=1 means constant.  Enumerating all constants of F_7 proves
    # that no v_1 can equal u_1(x)=x on D={1,2,4}.
    matching_constants = tuple(
        constant
        for constant in range(p)
        if all(constant == value % p for value in case.u1_values)
    )
    require(not matching_constants, "the claimed failed conclusion has a witness")

    return {
        "U": u,
        "V": v,
        "W": w,
        "old_rhs": old_rhs,
        "corrected_rhs": corrected_rhs,
        "exact_content_charge": exact_content_charge,
    }


DEPLOYED_ROWS = (
    # rate denominator, r, m, U, V, W, printed RF5 ceiling
    (2, 611982, 119, 176735230, 169, 27525, 274589064742726105),
    (4, 1045433, 104, 109378776, 209, 29028, 274721012201264929),
    (8, 1352390, 90, 67028580, 256, 31500, 274578888391530706),
    (16, 1569744, 78, 41137824, 314, 34101, 274861787390229386),
)


def verify_deployed_rows() -> None:
    n = 1 << 21
    tiny = Fraction(1, 1 << 64)
    for denominator, radius, multiplicity, u, v, w, expected in DEPLOYED_ROWS:
        agreement = n - radius
        dimension = n // denominator
        dy = Fraction(v - 1) + tiny
        dz = Fraction(w - 1) + tiny
        alpha = 2 * u * dy * dy

        require(u == multiplicity * agreement, "deployed U=mA identity failed")
        require(v >= multiplicity and w >= v, "deployed RF1 ordering failed")
        require(u > dimension * (v - 1), "deployed RF1 rank inequality failed")
        require(v >= 2 and dy > 1 and alpha > 1, "deployed content guard failed")

        old_rhs = alpha * dz + (radius + 1) * dy
        corrected_rhs = max(Fraction(1), alpha) * dz + (radius + 1) * dy
        require(corrected_rhs == old_rhs, "corrected deployed threshold changed")
        require(ceil_fraction(corrected_rhs) == expected, "deployed RF5 ceiling changed")


def verify_source_bindings() -> None:
    main_text = MAIN_TEX.read_text(encoding="utf-8")
    release_text = RELEASE_TEX.read_text(encoding="utf-8")
    require(main_text == release_text, "the two v8 TeX source copies differ")
    for needle in (
        r"\label{ass:retained-factor-lift}",
        r"\abs S>2U D_Y^2D_Z+(r+1)D_Y",
        "Summing over the factor pairs uses",
        "content roots",
    ):
        require(needle in main_text, f"v8 source binding missing: {needle}")

    for denominator, radius, multiplicity, u, v, w, expected in DEPLOYED_ROWS:
        rate = f"1/{denominator}"
        parameter_row = f"{rate}&{radius}&{multiplicity}&{u}&{v}&{w}"
        result_row = f"{rate}&{expected}&"
        require(
            parameter_row in main_text,
            f"v8 RF6 parameter row is not source-bound: {rate}",
        )
        require(
            result_row in main_text,
            f"v8 RF7 result row is not source-bound: {rate}",
        )

    prior_text = PRIOR_AUDIT.read_text(encoding="utf-8")
    require(
        "where the last inequality uses `2D_XD_Y^2 >= 1`" in prior_text,
        "prior audit no longer exposes the load-bearing content guard",
    )


def run_tamper_selftest() -> int:
    cases = (
        ("field-pin", replace(PINNED, field_order=5), "pinned field"),
        (
            "duplicate-domain",
            replace(PINNED, domain=(1, 1, 4)),
            "domain points are not distinct",
        ),
        ("RF1-D_X", replace(PINNED, dx=Fraction(3)), "RF1 D_X<mA failed"),
        (
            "constant-u1",
            replace(PINNED, u1_values=(0, 0, 0)),
            "failed conclusion has a witness",
        ),
        ("Q-degree", replace(PINNED, q_yz_degree=2), "Q (Y,Z)-degree bound"),
    )
    rejected = 0
    for name, candidate, expected_reason in cases:
        try:
            verify_counterexample(candidate)
        except VerificationError as exc:
            require(
                expected_reason in str(exc),
                f"tamper {name} failed for the wrong reason: {exc}",
            )
            rejected += 1
        else:
            raise VerificationError(f"tamper accepted: {name}")
    require(rejected == len(cases), "not every tamper was rejected")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    if args.tamper_selftest:
        rejected = run_tamper_selftest()
        print(
            "PAVING_V8_RETAINED_FACTOR_CONTENT_GUARD_TAMPER_PASS "
            f"rejected={rejected}/{rejected}"
        )
        return 0

    result = verify_counterexample(PINNED)
    verify_deployed_rows()
    verify_source_bindings()
    print("PAVING_V8_RETAINED_FACTOR_CONTENT_GUARD_PASS")
    print(
        "counterexample: old=%s < |S|=1; corrected=%s; exact-content-charge=%s"
        % (
            result["old_rhs"],
            result["corrected_rhs"],
            result["exact_content_charge"],
        )
    )
    print("deployed rows: 4/4 RF5 ceilings unchanged (content coefficient > 1)")
    print("NOTE: the remaining retained-factor/Hensel import is not discharged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
