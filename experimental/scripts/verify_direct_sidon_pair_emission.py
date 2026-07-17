#!/usr/bin/env python3
"""Fail-closed verifier for the R28 Role 09 pair-emission packet.

Python standard library only. The zero-argument run verifies source and
statement pins, exhausts small cyclic-syndrome fixtures, checks exact
coefficient layers and literal R=1 rows, and reconstructs the cutoff constants.
The tamper self-test mutates load-bearing semantics and requires every mutation
to be rejected.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from decimal import Decimal, ROUND_HALF_UP, localcontext
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path
from typing import Callable


REPO_ROOT = Path(__file__).resolve().parents[2]
NOTE_PATH = REPO_ROOT / "experimental/notes/thresholds/direct_sidon_pair_emission.md"
CERTIFICATE_DIR = (
    REPO_ROOT / "experimental/data/certificates/direct-sidon-pair-emission"
)
MANIFEST_PATH = CERTIFICATE_DIR / "source_pins.json"
MANIFEST_SHA256 = "25d4e3960d1f0d1ef9c2dcc5f90889cd56b61d8a22d730c726af2826924dcd91"

SCHEMA = "r28-role09-signed-root-emission-source-pins-v1"
ORIGIN_MAIN = "7f278167e1e51f968896229ae438ea5a76398f90"
PR_860_HEAD = "fb54c47553d3948f3dc6e64b0a292747459fc482"
PR_872_HEAD = "37e08b4feb60714a6c9955ae408edf1742f0fc2b"
ROLE_RETURN_SHA256 = (
    "7afc4c422cfd1bd5f5a66354ae24d5899184b866137f80a65795b24b6c42a86c"
)
RANK16_TARGET = 274_854_110_496_187_592
PR_872_PAID = 274_854_110_496_187_589
PR_872_FORMAL_RESIDUAL = 3

EXPECTED_AUTHORITY = {
    "origin_main": ORIGIN_MAIN,
    "pr_860_head": PR_860_HEAD,
    "pr_872_head": PR_872_HEAD,
    "pr_872_paid_subtotal": PR_872_PAID,
    "rank16_target": RANK16_TARGET,
    "rank16_formal_residual": PR_872_FORMAL_RESIDUAL,
    "role_return_name": "r28_role09_clean_final.md",
    "role_return_sha256": ROLE_RETURN_SHA256,
}

EXPECTED_SOURCE_FILES = {
    "agents.md": "8d2d215910d27b80c38f8b67311951bbe3dd43ea32bfeb7e12828510083a157e",
    "experimental/notes/thresholds/realized_image_energy_lift.md": (
        "1bc6f170a6e97d43dd4aed68ad88e68501913ebdabcd2637662414a69ef43810"
    ),
    "experimental/scripts/verify_realized_image_energy_lift.py": (
        "70d86fe4905a9c67921d356729b4dd9a0ff5000b7c2b160ab5c90526d510e4fe"
    ),
}

EXPECTED_STATEMENT_PINS = [
    "SIGNED_ROOT_CLAIM: For every finite abelian syndrome group, sum_s f_s/Delta_s <= A_pm(N,m) by canonical signed-root emission.",
    "ODD_DIAGONAL_CLAIM: If doubling is injective on S, in particular for a vector-space codomain of odd characteristic, sum_s f_s/Delta_s <= A_2(N,m) by ternary diagonal-pair emission.",
    "CUTOFF_GAIN_CLAIM: On the literal half-density R=1 family, the exact cutoff improvement is 0.156870036510644 nats = 0.226315623737977 bits.",
    "FINITE_LEDGER_PIN: Pending PR #872 has paid subtotal 274854110496187589 = T-3; this packet adds no finite charge.",
    "NONCLAIM_PIN: This packet does not close hard input 2, any recurrence parent, Grand MCA, Grand List, or the official score.",
    "WOE_SCOPE_PIN: The ternary diagonal-pair WOE is odd-characteristic only; the all-characteristic signed-root WOE analogue is a separate unproved target using A_pm.",
]


class VerificationError(RuntimeError):
    """Raised when a fail-closed obligation is not met."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_manifest() -> dict[str, object]:
    require(MANIFEST_PATH.is_file(), "source manifest is missing")
    require(
        sha256_file(MANIFEST_PATH) == MANIFEST_SHA256,
        "source manifest hash drift",
    )
    raw = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    require(isinstance(raw, dict), "source manifest root must be an object")
    return raw


def verify_contract(
    manifest: dict[str, object],
    note_text: str,
    *,
    verify_files: bool = True,
) -> tuple[int, int]:
    require(
        set(manifest) == {"schema", "authority", "repository_files", "statement_pins"},
        "source manifest schema keys",
    )
    require(manifest["schema"] == SCHEMA, "source manifest schema identifier")
    require(manifest["authority"] == EXPECTED_AUTHORITY, "authority pins")
    require(manifest["repository_files"] == EXPECTED_SOURCE_FILES, "source pin table")
    require(manifest["statement_pins"] == EXPECTED_STATEMENT_PINS, "statement pin table")

    if verify_files:
        for relative, expected in EXPECTED_SOURCE_FILES.items():
            path = REPO_ROOT / relative
            require(path.is_file(), f"source pin missing: {relative}")
            require(sha256_file(path) == expected, f"source pin drift: {relative}")

    for statement in EXPECTED_STATEMENT_PINS:
        require(
            note_text.count(statement) == 1,
            f"statement pin missing or duplicated: {statement.split(':', 1)[0]}",
        )

    require(str(PR_872_PAID) in note_text, "PR #872 paid subtotal statement")
    require("formal residual allowance:                    3" in note_text, "T-3 ledger")
    require("6,363,455,582,520 remains" not in note_text, "stale PR #861 ledger")
    require("This ternary statement is not asserted in characteristic two." in note_text,
            "odd-characteristic diagonal scope")
    require("This signed-root WOE analogue is also unproved here." in note_text,
            "all-characteristic WOE nonclaim")
    return len(EXPECTED_SOURCE_FILES), len(EXPECTED_STATEMENT_PINS)


Vector = tuple[int, ...]


@dataclass(frozen=True)
class Semantics:
    signed_root_coefficient: int = -1
    signed_tag_multiplier: int = 1
    diagonal_tag_multiplier: int = 2
    diagonal_requires_odd: bool = True
    a2_target_shift: int = 0
    apm_target_shift: int = 0
    gain_ln2_coefficient: int = 3
    gain_ln3_numerator: int = 7
    gain_ln3_denominator: int = 4


@dataclass
class Metrics:
    linear_maps: int = 0
    residual_families: int = 0
    nonempty_fibres: int = 0
    signed_fibres: int = 0
    odd_diagonal_fibres: int = 0
    coefficient_checks: int = 0


def boolean_slice(n: int, m: int) -> tuple[Vector, ...]:
    points: list[Vector] = []
    for support in combinations(range(n), m):
        support_set = set(support)
        points.append(tuple(int(i in support_set) for i in range(n)))
    return tuple(points)


def phi(vector: Vector, weights: tuple[int, ...], modulus: int) -> int:
    return sum(value * weight for value, weight in zip(vector, weights)) % modulus


def add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))


def signed_emit(left: Vector, right: Vector, root: Vector, coefficient: int) -> Vector:
    return tuple(a + b + coefficient * r for a, b, r in zip(left, right, root))


def coefficient_count(n: int, target: int, cap: int) -> int:
    if target < 0 or target > n * cap:
        return 0
    row = [0] * (target + 1)
    row[0] = 1
    for _ in range(n):
        next_row = [0] * (target + 1)
        for total, count in enumerate(row):
            if not count:
                continue
            for digit in range(cap + 1):
                if total + digit <= target:
                    next_row[total + digit] += count
        row = next_row
    return row[target]


def brute_coefficient_count(n: int, target: int, cap: int) -> int:
    return sum(
        1
        for digits in product(range(cap + 1), repeat=n)
        if sum(digits) == target
    )


def pair_data(fibre: tuple[Vector, ...]) -> tuple[set[Vector], int, Fraction]:
    counts = Counter(add(left, right) for left in fibre for right in fibre)
    support = set(counts)
    energy = sum(count * count for count in counts.values())
    size = len(fibre)
    require(energy > 0, "nonempty fibre energy")
    inverse_energy = Fraction(size**4, energy)
    require(inverse_energy <= len(support), "energy-to-support Cauchy bound")
    return support, energy, inverse_energy


def verify_residual_family(
    n: int,
    m: int,
    modulus: int,
    weights: tuple[int, ...],
    residual: tuple[Vector, ...],
    semantics: Semantics,
    metrics: Metrics | None = None,
) -> None:
    fibres: defaultdict[int, list[Vector]] = defaultdict(list)
    for point in residual:
        fibres[phi(point, weights, modulus)].append(point)

    signed_union: set[Vector] = set()
    diagonal_union: set[Vector] = set()
    signed_inverse_energy = Fraction(0, 1)
    diagonal_inverse_energy = Fraction(0, 1)

    for syndrome in sorted(fibres):
        fibre = tuple(sorted(fibres[syndrome]))
        pair_support, _energy, inverse_energy = pair_data(fibre)
        root = min(fibre)
        signed = {
            signed_emit(left, right, root, semantics.signed_root_coefficient)
            for left in fibre
            for right in fibre
        }
        require(len(signed) == len(pair_support), "signed translation cardinality")
        for emitted in signed:
            require(all(-1 <= value <= 2 for value in emitted), "signed alphabet")
            require(sum(emitted) == m, "signed fixed-weight layer")
            require(
                phi(emitted, weights, modulus)
                == semantics.signed_tag_multiplier * syndrome % modulus,
                "signed syndrome tag",
            )
        require(signed_union.isdisjoint(signed), "signed classes are disjoint")
        signed_union.update(signed)
        signed_inverse_energy += inverse_energy

        if metrics is not None:
            metrics.nonempty_fibres += 1
            metrics.signed_fibres += 1

        diagonal_enabled = modulus % 2 == 1 or not semantics.diagonal_requires_odd
        if diagonal_enabled:
            diagonal = pair_support
            for emitted in diagonal:
                require(all(0 <= value <= 2 for value in emitted), "ternary alphabet")
                require(sum(emitted) == 2 * m, "ternary fixed-weight layer")
                require(
                    phi(emitted, weights, modulus)
                    == semantics.diagonal_tag_multiplier * syndrome % modulus,
                    "diagonal syndrome tag",
                )
            require(
                diagonal_union.isdisjoint(diagonal),
                "diagonal classes require injective doubling",
            )
            diagonal_union.update(diagonal)
            diagonal_inverse_energy += inverse_energy
            if metrics is not None:
                metrics.odd_diagonal_fibres += 1

    apm = coefficient_count(n, n + m + semantics.apm_target_shift, 3)
    require(len(signed_union) <= apm, "signed coefficient layer")
    require(signed_inverse_energy <= len(signed_union), "signed aggregate energy")

    if modulus % 2 == 1 or not semantics.diagonal_requires_odd:
        a2 = coefficient_count(n, 2 * m + semantics.a2_target_shift, 2)
        require(len(diagonal_union) <= a2, "ternary coefficient layer")
        require(diagonal_inverse_energy <= len(diagonal_union), "diagonal aggregate energy")


def verify_coefficients(semantics: Semantics) -> int:
    checks = 0
    for n in range(0, 6):
        for cap in (2, 3):
            for target in range(n * cap + 1):
                require(
                    coefficient_count(n, target, cap)
                    == brute_coefficient_count(n, target, cap),
                    "coefficient recurrence",
                )
                checks += 1

    require(
        coefficient_count(4, 4 + semantics.a2_target_shift, 2)
        == brute_coefficient_count(4, 4, 2),
        "A_2 target exponent",
    )
    require(
        coefficient_count(4, 5 + semantics.apm_target_shift, 3)
        == brute_coefficient_count(4, 5, 3),
        "A_pm target exponent",
    )
    return checks + 2


def verify_focus_fixtures(semantics: Semantics) -> None:
    verify_residual_family(
        3,
        1,
        3,
        (0, 1, 2),
        boolean_slice(3, 1),
        semantics,
    )
    verify_residual_family(
        4,
        2,
        3,
        (0, 0, 0, 0),
        boolean_slice(4, 2),
        semantics,
    )


def verify_characteristic_two_guard(semantics: Semantics) -> Vector:
    left_fibre = ((1, 1, 0, 0), (0, 0, 1, 1))
    right_fibre = ((1, 0, 1, 0), (0, 1, 0, 1))
    weights = (0, 0, 1, 1)
    require({phi(point, weights, 2) for point in left_fibre} == {0}, "char-two left tag")
    require({phi(point, weights, 2) for point in right_fibre} == {1}, "char-two right tag")
    overlap = {add(a, b) for a in left_fibre for b in left_fibre} & {
        add(a, b) for a in right_fibre for b in right_fibre
    }
    require(overlap == {(1, 1, 1, 1)}, "characteristic-two diagonal collision")
    require(semantics.diagonal_requires_odd, "unguarded characteristic-two diagonal claim")
    return next(iter(overlap))


def verify_exhaustive(semantics: Semantics) -> Metrics:
    metrics = Metrics()
    for n in range(1, 5):
        for modulus in (2, 3, 5):
            for weights in product(range(modulus), repeat=n):
                metrics.linear_maps += 1
                for m in range(n + 1):
                    omega = boolean_slice(n, m)
                    for mask in range(1 << len(omega)):
                        residual = tuple(
                            point for index, point in enumerate(omega) if mask >> index & 1
                        )
                        verify_residual_family(
                            n,
                            m,
                            modulus,
                            weights,
                            residual,
                            semantics,
                            metrics,
                        )
                        metrics.residual_families += 1
    return metrics


def verify_literal_r1_rows() -> tuple[tuple[int, int, int], ...]:
    rows: list[tuple[int, int, int]] = []
    for prime in (3, 5, 7, 11):
        m = (prime - 1) // 2
        points = boolean_slice(prime, m)
        weights = tuple(range(prime))
        syndromes = {phi(point, weights, prime) for point in points}
        require(len(points) == comb(prime, m), "literal R=1 slice size")
        require(len(syndromes) == prime, "literal R=1 realized image")
        rows.append((prime, len(points), len(syndromes)))
    return tuple(rows)


def rounded(value: Decimal) -> str:
    quantum = Decimal("0.000000000000001")
    return str(value.quantize(quantum, rounding=ROUND_HALF_UP))


def verify_cutoffs(semantics: Semantics) -> dict[str, str]:
    require(
        Fraction(semantics.gain_ln2_coefficient, 1) == Fraction(2, 1) - Fraction(-1, 1),
        "cutoff ln(2) coefficient identity",
    )
    require(
        -Fraction(semantics.gain_ln3_numerator, semantics.gain_ln3_denominator)
        == -Fraction(3, 4) - Fraction(1, 1),
        "cutoff ln(3) coefficient identity",
    )
    with localcontext() as context:
        context.prec = 80
        ln2 = Decimal(2).ln()
        ln3 = Decimal(3).ln()
        pair_nats = ln3 - ln2
        repaired_nats = 2 * ln2 - Decimal(3) * ln3 / Decimal(4)
        gain_nats = (
            Decimal(semantics.gain_ln2_coefficient) * ln2
            - Decimal(semantics.gain_ln3_numerator)
            * ln3
            / Decimal(semantics.gain_ln3_denominator)
        )
        require(
            abs(gain_nats - (repaired_nats - pair_nats)) < Decimal("1e-70"),
            "cutoff difference identity",
        )
        values = {
            "pair_nats": rounded(pair_nats),
            "repaired_nats": rounded(repaired_nats),
            "gain_nats": rounded(gain_nats),
            "pair_bits": rounded(pair_nats / ln2),
            "repaired_bits": rounded(repaired_nats / ln2),
            "gain_bits": rounded(gain_nats / ln2),
        }
    expected = {
        "pair_nats": "0.405465108108164",
        "repaired_nats": "0.562335144618808",
        "gain_nats": "0.156870036510644",
        "pair_bits": "0.584962500721156",
        "repaired_bits": "0.811278124459133",
        "gain_bits": "0.226315623737977",
    }
    require(values == expected, "exact cutoff constants")
    return values


def normal_run() -> None:
    manifest = load_manifest()
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    source_count, statement_count = verify_contract(manifest, note_text)
    semantics = Semantics()
    coefficient_checks = verify_coefficients(semantics)
    verify_focus_fixtures(semantics)
    overlap = verify_characteristic_two_guard(semantics)
    metrics = verify_exhaustive(semantics)
    metrics.coefficient_checks = coefficient_checks
    rows = verify_literal_r1_rows()
    cutoffs = verify_cutoffs(semantics)

    rows_text = ", ".join(f"({p}, {m}, {l})" for p, m, l in rows)
    overlap_text = "(" + ", ".join(str(value) for value in overlap) + ")"
    print("R28_ROLE09_DIRECT_SIDON_EMISSION: PASS")
    print(f"authority=origin/main@{ORIGIN_MAIN} pr860@{PR_860_HEAD} pr872@{PR_872_HEAD}")
    print(f"source_pins={source_count} statement_pins={statement_count} coefficient_checks={coefficient_checks}")
    print(
        "exhaustive="
        f"maps:{metrics.linear_maps} residual_families:{metrics.residual_families} "
        f"nonempty_fibres:{metrics.nonempty_fibres} signed:{metrics.signed_fibres} "
        f"odd_diagonal:{metrics.odd_diagonal_fibres}"
    )
    print(f"characteristic_two_guard=PASS overlap:{overlap_text}")
    print(f"literal_R1_rows={rows_text}")
    print(
        "cutoff_nats="
        f"pair:{cutoffs['pair_nats']} repaired_860:{cutoffs['repaired_nats']} "
        f"gain:{cutoffs['gain_nats']}"
    )
    print(
        "cutoff_bits="
        f"pair:{cutoffs['pair_bits']} repaired_860:{cutoffs['repaired_bits']} "
        f"gain:{cutoffs['gain_bits']}"
    )
    print(f"finite_ledger=PR872:T-3 paid:{PR_872_PAID} target:{RANK16_TARGET} new_charge:0")
    print("scope=signed-root all-characteristic; ternary diagonal-pair odd-characteristic")
    print("nonclaims=hard-input-2 OPEN; parent movement 0; official-score movement 0")
    print("RESULT=PASS")


def expect_rejected(name: str, action: Callable[[], None]) -> str:
    try:
        action()
    except VerificationError:
        return name
    raise VerificationError(f"semantic mutation was not rejected: {name}")


def tamper_selftest() -> None:
    manifest = load_manifest()
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    clean = Semantics()
    verify_contract(manifest, note_text)
    verify_coefficients(clean)
    verify_focus_fixtures(clean)
    verify_characteristic_two_guard(clean)
    verify_cutoffs(clean)

    rejected: list[str] = []
    rejected.append(expect_rejected(
        "signed-root-translation",
        lambda: verify_focus_fixtures(replace(clean, signed_root_coefficient=0)),
    ))
    rejected.append(expect_rejected(
        "signed-syndrome-tag",
        lambda: verify_focus_fixtures(replace(clean, signed_tag_multiplier=2)),
    ))
    rejected.append(expect_rejected(
        "diagonal-syndrome-tag",
        lambda: verify_focus_fixtures(replace(clean, diagonal_tag_multiplier=1)),
    ))
    rejected.append(expect_rejected(
        "characteristic-two-diagonal",
        lambda: verify_characteristic_two_guard(replace(clean, diagonal_requires_odd=False)),
    ))
    rejected.append(expect_rejected(
        "A2-target-exponent",
        lambda: verify_coefficients(replace(clean, a2_target_shift=1)),
    ))
    rejected.append(expect_rejected(
        "Apm-target-exponent",
        lambda: verify_coefficients(replace(clean, apm_target_shift=1)),
    ))
    rejected.append(expect_rejected(
        "cutoff-exponent",
        lambda: verify_cutoffs(replace(clean, gain_ln2_coefficient=2)),
    ))

    source_mutation = copy.deepcopy(manifest)
    source_table = source_mutation["repository_files"]
    require(isinstance(source_table, dict), "tamper source table type")
    source_table["agents.md"] = "0" * 64
    rejected.append(expect_rejected(
        "source-hash",
        lambda: verify_contract(source_mutation, note_text, verify_files=False),
    ))

    statement_mutation = copy.deepcopy(manifest)
    statement_table = statement_mutation["statement_pins"]
    require(isinstance(statement_table, list), "tamper statement table type")
    statement_table[0] = str(statement_table[0]).replace("A_pm", "A_2")
    rejected.append(expect_rejected(
        "statement-pin",
        lambda: verify_contract(statement_mutation, note_text, verify_files=False),
    ))

    ledger_mutation = copy.deepcopy(manifest)
    authority = ledger_mutation["authority"]
    require(isinstance(authority, dict), "tamper authority type")
    authority["pr_872_paid_subtotal"] = 274_847_747_040_605_072
    rejected.append(expect_rejected(
        "stale-ledger",
        lambda: verify_contract(ledger_mutation, note_text, verify_files=False),
    ))

    woe_mutation = note_text.replace(
        EXPECTED_STATEMENT_PINS[-1],
        EXPECTED_STATEMENT_PINS[-1].replace("separate unproved", "proved ternary"),
    )
    rejected.append(expect_rejected(
        "WOE-characteristic-scope",
        lambda: verify_contract(manifest, woe_mutation, verify_files=False),
    ))

    print("R28_ROLE09_DIRECT_SIDON_EMISSION_TAMPER: PASS")
    print(f"semantic_mutations_rejected={len(rejected)}/{len(rejected)}")
    print("mutations=" + ",".join(rejected))
    print("RESULT=PASS")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="mutate load-bearing semantics and require rejection",
    )
    args = parser.parse_args()
    if args.tamper_selftest:
        tamper_selftest()
    else:
        normal_run()


if __name__ == "__main__":
    main()
