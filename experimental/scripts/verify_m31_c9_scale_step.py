#!/usr/bin/env python3
"""Verify the exact sixteen-root M31 C9 scale-step certificate.

Stdlib only. Recomputes the norm-one derivation, Chebyshev roots, complete
weight-eight slice, exact C1 deletion, fiber distributions, and first doubled
residual key.
"""
from __future__ import annotations
import argparse
import json
from collections import Counter, defaultdict
from math import ceil
from pathlib import Path
from typing import DefaultDict, Iterable

P = 2**31 - 1
GENERATOR = (1717986917, 1288490189)
BLOCK_BASES = [256, 768, 1280, 1792]
QUARTER_TURN_EXPONENT = 2**29


def fp2_mul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return ((a[0] * b[0] - a[1] * b[1]) % P,
            (a[0] * b[1] + a[1] * b[0]) % P)


def fp2_pow(a: tuple[int, int], exponent: int) -> tuple[int, int]:
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = fp2_mul(result, a)
        a = fp2_mul(a, a)
        exponent >>= 1
    return result


def derive_domain() -> tuple[list[int], list[int]]:
    exponents = [base + j * QUARTER_TURN_EXPONENT
                 for base in BLOCK_BASES for j in range(4)]
    return exponents, [fp2_pow(GENERATOR, e)[0] for e in exponents]


def chebyshev_double(x: int) -> int:
    return (2 * (x % P) * (x % P) + (P - 1)) % P


def chebyshev_pow_two(depth: int, x: int) -> int:
    for _ in range(depth):
        x = chebyshev_double(x)
    return x


def prefix_key(mask: int, domain: list[int]) -> tuple[int, int, int]:
    selected = [domain[i] for i in range(16) if (mask >> i) & 1]
    return (sum(selected) % P,
            sum((x * x) % P for x in selected) % P,
            sum(((x * x) % P) * x % P for x in selected) % P)


ANTIPODAL_PAIRS = ([(4 * b, 4 * b + 2) for b in range(4)]
                    + [(4 * b + 1, 4 * b + 3) for b in range(4)])


def c1_owned(mask: int) -> bool:
    return all(((mask >> a) & 1) == ((mask >> b) & 1)
               for a, b in ANTIPODAL_PAIRS)


def fiber_map(masks: Iterable[int], domain: list[int]) -> dict[tuple[int, int, int], list[int]]:
    fibers: DefaultDict[tuple[int, int, int], list[int]] = defaultdict(list)
    for mask in masks:
        fibers[prefix_key(mask, domain)].append(mask)
    return dict(fibers)


def distribution(fibers: dict[tuple[int, int, int], list[int]]) -> dict[str, int]:
    counts = Counter(len(fiber) for fiber in fibers.values())
    return {str(size): counts[size] for size in sorted(counts)}


def recompute() -> dict[str, object]:
    exponents, domain = derive_domain()
    assert fp2_mul(GENERATOR, (GENERATOR[0], (-GENERATOR[1]) % P)) == (1, 0)
    assert fp2_pow(GENERATOR, 2**30) == (P - 1, 0)
    assert fp2_pow(GENERATOR, 2**31) == (1, 0)
    assert len(domain) == len(set(domain)) == 16
    assert all(chebyshev_pow_two(21, x) == 0 for x in domain)
    t4_values = [chebyshev_pow_two(2, domain[4 * b]) for b in range(4)]
    assert all(all(chebyshev_pow_two(2, x) == t4_values[b]
                   for x in domain[4*b:4*b+4]) for b in range(4))
    assert all((domain[a] + domain[b]) % P == 0 for a, b in ANTIPODAL_PAIRS)

    full_masks = [m for m in range(1 << 16) if m.bit_count() == 8]
    residual_masks = [m for m in full_masks if not c1_owned(m)]
    full_fibers = fiber_map(full_masks, domain)
    residual_fibers = fiber_map(residual_masks, domain)
    first_mask = residual_masks[0]
    first_key = prefix_key(first_mask, domain)
    first_fiber = residual_fibers[first_key]
    assert first_mask == 383
    assert first_fiber == [383, 61808]
    assert full_fibers[first_key] == first_fiber

    return {
        "schema": "rs-mca.m31-c9-scale-step.v1",
        "status": "COUNTEREXAMPLE_NEW_FLOOR",
        "acceptance_gate": {
            "criterion": 4,
            "name": "statement-changing counterexample / new obstruction floor",
            "terminal": "M31_C9_SCALE_STEP_T4_BLOCK_SWAP_DOUBLING",
            "statement": "After exact C1 antipodal-quotient deletion on the sixteen-root weight-eight slice, the first realized residual key has fiber size two; loss-one injectivity fails at the next domain scale."
        },
        "source_pins": {
            "fork_main": "b410c7ee14488bb751c5a89df10cb5b0323e3669",
            "upstream_main": "a3017697ad1594521d2779fe1d83bccd45d4c06e",
            "grande_finale_blob": "8a5d9791900ca9eed773feba146b92ad296704ce",
            "rs_mca_thresholds_blob": "01302a797c502a05ed0b11ba949b8756e0aa2b22"
        },
        "field": {
            "prime": P,
            "generator": {"re": GENERATOR[0], "im": GENERATOR[1]},
            "generator_norm": 1,
            "generator_half_order_power": {"exponent": 2**30, "value": {"re": P-1, "im": 0}},
            "generator_full_order_power": {"exponent": 2**31, "value": {"re": 1, "im": 0}}
        },
        "domain": {
            "chebyshev_degree": 2**21,
            "block_bases": BLOCK_BASES,
            "quarter_turn_exponent": QUARTER_TURN_EXPONENT,
            "exponents": exponents,
            "points": domain,
            "t4_values": t4_values,
            "antipodal_index_pairs": [list(pair) for pair in ANTIPODAL_PAIRS]
        },
        "slice": {
            "dimension": 16, "weight": 8,
            "support_order": "ascending 16-bit mask",
            "full_support_count": len(full_masks),
            "full_image_count": len(full_fibers),
            "full_fiber_distribution": distribution(full_fibers),
            "full_max_fiber": max(map(len, full_fibers.values())),
            "full_integral_average_ceiling": ceil(len(full_masks) / len(full_fibers))
        },
        "c1_owner": {
            "definition": "mask is a union of four antipodal pairs",
            "owned_support_count": len(full_masks) - len(residual_masks),
            "residual_support_count": len(residual_masks),
            "residual_image_count": len(residual_fibers),
            "residual_fiber_distribution": distribution(residual_fibers),
            "residual_max_fiber": max(map(len, residual_fibers.values())),
            "residual_integral_average_ceiling": ceil(len(residual_masks) / len(residual_fibers))
        },
        "first_growth": {
            "first_residual_mask": first_mask,
            "mate_mask": first_fiber[1],
            "key": list(first_key),
            "full_fiber": full_fibers[first_key],
            "residual_fiber": first_fiber,
            "first_mask_support": [i for i in range(16) if (first_mask >> i) & 1],
            "mate_mask_support": [i for i in range(16) if (first_fiber[1] >> i) & 1],
            "common_support": [i for i in range(16) if ((first_mask & first_fiber[1]) >> i) & 1],
            "swapped_t4_blocks": [[0,1,2,3],[12,13,14,15]]
        },
        "deployed_row": {
            "row": "Mersenne-31 list", "target_epsilon": "2^-100",
            "agreement": 1116023, "B_star": 16777215,
            "prefix_depth": 67447, "complement_weight": 981129,
            "active_weight": 8, "fixed_outside_weight": 981121,
            "outside_available": 2097136, "availability_holds": True
        },
        "nonclaims": [
            "No exhaustive fixed-before-line C1-C8 owner theorem for the full deployed row.",
            "No received-word or line-level list/MCA numerator is constructed.",
            "No profile multiplicity, residual add-back, SE2/ray compiler, UNIF, or adjacent-row certificate.",
            "The residual max-two census is exact only for the displayed sixteen-root active slice."
        ]
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path,
        default=Path(__file__).resolve().parents[1] / "data/certificates/m31-c9-scale-step/m31_c9_scale_step.json")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = json.loads(args.certificate.read_text(encoding="utf-8"))
    actual = recompute()
    if expected != actual:
        print("FAIL: certificate mismatch")
        return 1
    if args.check:
        print("PASS: M31 C9 sixteen-root scale-step certificate")
        print("full: 12870 supports, 12457 keys, max fiber 6")
        print("residual: 12800 supports, 12416 keys, max fiber 2")
        print("first residual fiber: key (1625092085,1544193364,2053033192)")
        print("masks: 383 and 61808")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
