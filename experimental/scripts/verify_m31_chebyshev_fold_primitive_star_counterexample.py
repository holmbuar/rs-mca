#!/usr/bin/env python3
"""Replay the exact M31 Chebyshev-fold-primitive signed-e_m route cut.

The p=127, n=32, m=5, w=2 twin-coset toy has full prefix image and
max-fiber overhead 2.08244 < the deployed M31-list calibration 8.41521, but a
rigorous lower bound on the non-T_2-fold signed-e_m L1 mass exceeds the
corresponding STAR allowance.  This refutes that uniform triangle-certificate
route, not deployed row-sharp Q.
"""
from __future__ import annotations

import argparse
import json
import os

from m31_fold_primitive_star_certificate import (
    compute_certificate,
    tamper_cases,
    validation_results,
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CERT_PATH = os.path.join(
    REPO_ROOT,
    "experimental",
    "data",
    "certificates",
    "m31-chebyshev-fold-primitive-star-counterexample",
    "m31_chebyshev_fold_primitive_star_counterexample.json",
)
CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(condition), detail))
    label = "PASS" if condition else "FAIL"
    print(f"  [{label}] {name}" + (f" ({detail})" if detail else ""))


def check_certificate(cert: dict) -> None:
    fresh = compute_certificate()
    for name, condition in validation_results(cert, fresh):
        check(name, condition)
    prefix = fresh["prefix_census"]
    calibration = fresh["deployed_calibration"]
    counterexample = fresh["fold_primitive_star_counterexample"]
    check(
        "full image",
        prefix["full_image"],
        f"{prefix['image_size']}/{prefix['ambient_size']}",
    )
    check(
        "toy atom passes",
        calibration["atom_passes"],
        f"max fiber {prefix['max_fiber']}",
    )
    check(
        "fold-primitive directions exactly t1!=0",
        fresh["toy"]["fold_iff_t1_zero"],
    )
    check(
        "fold-primitive STAR fails",
        counterexample["star_fails"],
        f"cross margin {counterexample['exact_cross_margin']}",
    )


def check_tampers(cert: dict) -> None:
    fresh = compute_certificate()
    for index, bad in enumerate(tamper_cases(cert), 1):
        failed = [name for name, ok in validation_results(bad, fresh) if not ok]
        check(f"tamper {index}", bool(failed), ",".join(failed))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    if not (args.write or args.check or args.tamper_selftest):
        args.check = True

    os.makedirs(os.path.dirname(CERT_PATH), exist_ok=True)
    if args.write:
        with open(CERT_PATH, "w", encoding="utf-8") as handle:
            json.dump(compute_certificate(), handle, indent=2, sort_keys=True)
            handle.write("\n")
        print(f"WROTE {CERT_PATH}")

    if args.check or args.tamper_selftest:
        with open(CERT_PATH, encoding="utf-8") as handle:
            certificate = json.load(handle)
        if args.check:
            check_certificate(certificate)
        if args.tamper_selftest:
            check_tampers(certificate)

    failures = [name for name, ok, _ in CHECKS if not ok]
    if failures:
        print(f"RESULT: FAIL ({len(failures)} failures: {', '.join(failures)})")
        return 1
    print(f"RESULT: PASS ({len(CHECKS)}/{len(CHECKS)} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
