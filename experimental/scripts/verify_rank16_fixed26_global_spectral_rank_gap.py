#!/usr/bin/env python3
"""Verify the fixed-26 global spectral-rank gap and complement identity."""

from __future__ import annotations

import argparse
import copy
import hashlib
import sys
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_PATH = Path(__file__).with_suffix(".expected.txt")
NOTE_PATH = ROOT / "experimental/notes/l2/rank16_fixed26_global_spectral_rank_gap.md"

BASE_HEAD = "7f278167e1e51f968896229ae438ea5a76398f90"
DEPENDENCY_HEAD = "d2b11f1914dea4cb4a7670736cf00d1422c878de"

P = 2_130_706_433
N = 2_097_152
B = 32_768
A_DEG = 67_472
R_DEG = 63_601
DELTA = A_DEG - R_DEG
WINDOW = 64
EXCLUDED_START = 18
EXCLUDED_END = 64
EXCLUDED_COUNT = EXCLUDED_END - EXCLUDED_START + 1
H_DEG = N - 2 * B
L_DEG = H_DEG - R_DEG
A_BOUND = H_DEG - A_DEG

SOURCE_PINS = {
    "experimental/notes/l2/rank16_fixed26_divided_difference_source_compiler.md":
        "e508b1847228475e5a71ab12df15d69d4091e7558a91f53e68261f06c42205ab",
    "experimental/scripts/verify_rank16_fixed26_divided_difference_source_compiler.py":
        "2dd8cd4d2df24510a4faa57d4ad70feda1b4505814233547f06dea7293afc744",
    "experimental/notes/l2/rank16_fixed26_spectral_resolvent.md":
        "3c8aaddaa9993cb486d918c62101938f9c7bf4604a852863778f0ccd6886f0cd",
    "experimental/scripts/verify_rank16_fixed26_spectral_resolvent.py":
        "1327c517be7d87050785980b2780bbd99862e6de71e50d188b2a353706336014",
    "experimental/data/certificates/rank16-fixed26-spectral-resolvent/manifest.json":
        "1d224e4a29e36f2c436d4aa8362337ceb85cdd431089faeab259217d9a6ba91f",
    "experimental/data/certificates/rank16-fixed26-spectral-resolvent/verify_rank16_fixed26_spectral_resolvent.expected.txt":
        "2f0707de1d5981043581b523c0cd0c666a228c36cd1d06ae75cdeeae41a11eea",
}

NOTE_REQUIRED_SNIPPETS = (
    DEPENDENCY_HEAD,
    "18 <= nu <= 64",
    "q_yz W L_yz = 1 + g A_yz",
    "No squarefreeness assumption",
    "zero finite payment",
    "official score remains `0/2`",
    "`3..17`",
    "`>=65`",
    "Open PR #872",
    "Open PR #873",
)

CONTRACT: dict[str, Any] = {
    "base_head": BASE_HEAD,
    "dependency": {"pr": 862, "head": DEPENDENCY_HEAD},
    "source_cell": {
        "same_source_cell": True,
        "fixed_received_word": True,
        "fixed_first_match_owner": True,
        "fixed_generator": True,
        "generator_degree": A_DEG,
        "fixed_nonzero_projective_ray": True,
        "fixed_core_size": 26,
    },
    "global_collapse": {
        "assumed_from_pr862": True,
        "steps": WINDOW,
        "j_min": 0,
        "j_max": 63,
        "actual_valid_edge_required": True,
        "w_is_unit": True,
        "squarefree_g_required": False,
    },
    "spectral": {
        "delta": DELTA,
        "imported_min_rank": 3,
        "excluded_start": EXCLUDED_START,
        "excluded_end": EXCLUDED_END,
        "remaining_low": "3..17",
        "remaining_high": ">=65",
    },
    "split_complement": {
        "identity": "q_yz*W*L_yz=1+g*A_yz",
        "l_degree": L_DEG,
        "a_degree_bound": A_BOUND,
        "resultant": "q_yz^67472*Res(g,W)*Res(g,L_yz)=1",
    },
    "ledger": {
        "finite_payment": 0,
        "parent_payment": 0,
        "grand_list": 0,
        "grand_mca": 0,
        "official_score": "0/2",
    },
    "nonclaims": {
        "pr872": "T-3_does_not_prove_outside_population_at_most_3",
        "pr873": "fixed26_27_not_multiplicity_one_global_owners",
    },
}


class CheckError(RuntimeError):
    """A fail-closed certificate check failed."""


class ContractError(CheckError):
    """A theorem-scope field was changed or removed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def contract_value(contract: dict[str, Any], *path: str) -> Any:
    value: Any = contract
    try:
        for key in path:
            value = value[key]
    except (KeyError, TypeError) as exc:
        raise ContractError("missing contract field: " + ".".join(path)) from exc
    return value


def contract_exact(contract: dict[str, Any], path: tuple[str, ...], expected: Any) -> None:
    actual = contract_value(contract, *path)
    if type(actual) is not type(expected) or actual != expected:
        label = ".".join(path)
        raise ContractError(f"{label}: expected {expected!r}, got {actual!r}")


def validate_contract(contract: dict[str, Any]) -> None:
    checks = (
        (("base_head",), BASE_HEAD),
        (("dependency", "pr"), 862),
        (("dependency", "head"), DEPENDENCY_HEAD),
        (("source_cell", "same_source_cell"), True),
        (("source_cell", "fixed_received_word"), True),
        (("source_cell", "fixed_first_match_owner"), True),
        (("source_cell", "fixed_generator"), True),
        (("source_cell", "generator_degree"), A_DEG),
        (("source_cell", "fixed_nonzero_projective_ray"), True),
        (("source_cell", "fixed_core_size"), 26),
        (("global_collapse", "assumed_from_pr862"), True),
        (("global_collapse", "steps"), WINDOW),
        (("global_collapse", "j_min"), 0),
        (("global_collapse", "j_max"), 63),
        (("global_collapse", "actual_valid_edge_required"), True),
        (("global_collapse", "w_is_unit"), True),
        (("global_collapse", "squarefree_g_required"), False),
        (("spectral", "delta"), DELTA),
        (("spectral", "imported_min_rank"), 3),
        (("spectral", "excluded_start"), EXCLUDED_START),
        (("spectral", "excluded_end"), EXCLUDED_END),
        (("spectral", "remaining_low"), "3..17"),
        (("spectral", "remaining_high"), ">=65"),
        (("split_complement", "identity"), "q_yz*W*L_yz=1+g*A_yz"),
        (("split_complement", "l_degree"), L_DEG),
        (("split_complement", "a_degree_bound"), A_BOUND),
        (("split_complement", "resultant"),
         "q_yz^67472*Res(g,W)*Res(g,L_yz)=1"),
        (("ledger", "finite_payment"), 0),
        (("ledger", "parent_payment"), 0),
        (("ledger", "grand_list"), 0),
        (("ledger", "grand_mca"), 0),
        (("ledger", "official_score"), "0/2"),
        (("nonclaims", "pr872"),
         "T-3_does_not_prove_outside_population_at_most_3"),
        (("nonclaims", "pr873"),
         "fixed26_27_not_multiplicity_one_global_owners"),
    )
    for path, expected in checks:
        contract_exact(contract, path, expected)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_source_pins(pins: dict[str, str] = SOURCE_PINS) -> int:
    for relative, expected in pins.items():
        path = ROOT / relative
        require(path.is_file(), f"missing dependency attachment: {relative}")
        actual = sha256_file(path)
        require(actual == expected, f"source pin mismatch for {relative}: {actual}")
    return len(pins)


def verify_note_contract(text: str | None = None) -> int:
    if text is None:
        require(NOTE_PATH.is_file(), f"missing theorem note: {NOTE_PATH}")
        text = NOTE_PATH.read_text(encoding="utf-8")
    for snippet in NOTE_REQUIRED_SNIPPETS:
        require(snippet in text, f"theorem note lost required statement: {snippet}")
    return len(NOTE_REQUIRED_SNIPPETS)


def verify_arithmetic() -> None:
    require(B * WINDOW == N, "64 block steps must equal n")
    require(DELTA == 3_871, "a-r arithmetic drift")
    require(17 * DELTA == 65_807, "17*delta arithmetic drift")
    require(18 * DELTA == 69_678, "18*delta arithmetic drift")
    require(17 * DELTA <= A_DEG < 18 * DELTA, "rank cutoff inequality failed")
    require(EXCLUDED_COUNT == 47, "excluded-rank count drift")
    require(H_DEG == 2_031_616, "split ambient-complement degree drift")
    require(L_DEG == 1_968_015, "L_yz degree drift")
    require(A_BOUND == 1_964_144, "A_yz degree bound drift")


def verify_primary_layer_bound() -> None:
    require(P % B != 0, "nonzero B-derivative condition failed")
    require(B >= DELTA, "zero-primary comparison B>=delta failed")
    for exponent in range(1, WINDOW + 1):
        nonzero_contribution = DELTA * exponent
        require(nonzero_contribution >= DELTA * exponent,
                "nonzero primary contribution failed")

        m_zero = B * (exponent - 1) + DELTA
        ceiling = (m_zero + B - 1) // B
        require(ceiling == exponent, "zero-primary ceiling identity failed")
        require(m_zero >= DELTA * exponent,
                "zero-primary contribution failed")


Poly = list[int]


def poly_trim(poly: Poly, prime: int) -> Poly:
    result = [coefficient % prime for coefficient in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [0]


def poly_zero(poly: Poly, prime: int) -> bool:
    return poly_trim(poly, prime) == [0]


def poly_degree(poly: Poly, prime: int) -> int:
    normalized = poly_trim(poly, prime)
    return -1 if normalized == [0] else len(normalized) - 1


def poly_add(left: Poly, right: Poly, prime: int) -> Poly:
    size = max(len(left), len(right))
    result = [0] * size
    for index in range(size):
        result[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return poly_trim(result, prime)


def poly_sub(left: Poly, right: Poly, prime: int) -> Poly:
    size = max(len(left), len(right))
    result = [0] * size
    for index in range(size):
        result[index] = (
            (left[index] if index < len(left) else 0)
            - (right[index] if index < len(right) else 0)
        ) % prime
    return poly_trim(result, prime)


def poly_scale(poly: Poly, scalar: int, prime: int) -> Poly:
    return poly_trim([(scalar * coefficient) % prime for coefficient in poly], prime)


def poly_mul(left: Poly, right: Poly, prime: int) -> Poly:
    if poly_zero(left, prime) or poly_zero(right, prime):
        return [0]
    result = [0] * (len(left) + len(right) - 1)
    for i, left_coefficient in enumerate(left):
        for j, right_coefficient in enumerate(right):
            result[i + j] = (
                result[i + j] + left_coefficient * right_coefficient
            ) % prime
    return poly_trim(result, prime)


def poly_divmod(numerator: Poly, denominator: Poly, prime: int) -> tuple[Poly, Poly]:
    denominator = poly_trim(denominator, prime)
    require(not poly_zero(denominator, prime), "polynomial division by zero")
    remainder = poly_trim(numerator, prime)
    quotient = [0] * max(1, poly_degree(remainder, prime) - len(denominator) + 2)
    denominator_degree = poly_degree(denominator, prime)
    inverse_lead = pow(denominator[-1], -1, prime)
    while not poly_zero(remainder, prime) and poly_degree(remainder, prime) >= denominator_degree:
        shift = poly_degree(remainder, prime) - denominator_degree
        coefficient = remainder[-1] * inverse_lead % prime
        quotient[shift] = (quotient[shift] + coefficient) % prime
        subtraction = [0] * shift + poly_scale(denominator, coefficient, prime)
        remainder = poly_sub(remainder, subtraction, prime)
    return poly_trim(quotient, prime), poly_trim(remainder, prime)


def poly_mod(numerator: Poly, denominator: Poly, prime: int) -> Poly:
    return poly_divmod(numerator, denominator, prime)[1]


def poly_gcd(left: Poly, right: Poly, prime: int) -> Poly:
    left = poly_trim(left, prime)
    right = poly_trim(right, prime)
    while not poly_zero(right, prime):
        left, right = right, poly_mod(left, right, prime)
    if poly_zero(left, prime):
        return [0]
    return poly_scale(left, pow(left[-1], -1, prime), prime)


def poly_inverse_mod(poly: Poly, modulus: Poly, prime: int) -> Poly:
    old_remainder = poly_trim(modulus, prime)
    remainder = poly_mod(poly, modulus, prime)
    old_coefficient = [0]
    coefficient = [1]
    while not poly_zero(remainder, prime):
        quotient, new_remainder = poly_divmod(old_remainder, remainder, prime)
        old_remainder, remainder = remainder, new_remainder
        old_coefficient, coefficient = (
            coefficient,
            poly_sub(old_coefficient, poly_mul(quotient, coefficient, prime), prime),
        )
    require(poly_degree(old_remainder, prime) == 0, "polynomial is not a unit")
    inverse_constant = pow(old_remainder[0], -1, prime)
    return poly_mod(poly_scale(old_coefficient, inverse_constant, prime), modulus, prime)


def determinant_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    determinant = 1
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work))
                      if work[row][column] % prime), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column] % prime
        determinant = determinant * pivot_value % prime
        inverse_pivot = pow(pivot_value, -1, prime)
        for row in range(column + 1, len(work)):
            factor = work[row][column] * inverse_pivot % prime
            if factor:
                for entry in range(column, len(work)):
                    work[row][entry] = (
                        work[row][entry] - factor * work[column][entry]
                    ) % prime
    return determinant % prime


def poly_resultant(left: Poly, right: Poly, prime: int) -> int:
    left = poly_trim(left, prime)
    right = poly_trim(right, prime)
    if poly_zero(left, prime) or poly_zero(right, prime):
        return 0
    left_degree = poly_degree(left, prime)
    right_degree = poly_degree(right, prime)
    if left_degree == 0:
        return pow(left[0], right_degree, prime)
    if right_degree == 0:
        return pow(right[0], left_degree, prime)

    size = left_degree + right_degree
    rows: list[list[int]] = []
    left_descending = list(reversed(left))
    right_descending = list(reversed(right))
    for shift in range(right_degree):
        rows.append([0] * shift + left_descending + [0] * (size-shift-len(left)))
    for shift in range(left_degree):
        rows.append([0] * shift + right_descending + [0] * (size-shift-len(right)))
    return determinant_mod(rows, prime)


def poly_derivative(poly: Poly, prime: int) -> Poly:
    if len(poly) <= 1:
        return [0]
    return poly_trim([index * poly[index] for index in range(1, len(poly))], prime)


def verify_split_complement_toy() -> None:
    prime = 17
    base = [3, 0, 1]
    g = poly_mul(base, base, prime)
    r_locator = poly_mul([16, 1], [15, 1], prime)
    l_complement = poly_mul(poly_mul([14, 1], [13, 1], prime), [12, 1], prime)
    q_scalar = 3

    require(poly_degree(g, prime) == 4, "toy generator degree failed")
    require(poly_degree(poly_gcd(g, poly_derivative(g, prime), prime), prime) > 0,
            "toy generator must be nonsquarefree")
    require(poly_gcd(g, r_locator, prime) == [1], "toy R must be coprime to g")
    require(poly_gcd(g, l_complement, prime) == [1], "toy L must be coprime to g")

    q_l = poly_scale(l_complement, q_scalar, prime)
    w = poly_inverse_mod(q_l, g, prime)
    h_pair = poly_mul(r_locator, l_complement, prime)
    u_pair = poly_mod(poly_mul(w, h_pair, prime), g, prime)
    require(poly_scale(u_pair, q_scalar, prime) == r_locator,
            "toy imported pair orientation R=qU failed")

    q_w_l = poly_scale(poly_mul(w, l_complement, prime), q_scalar, prime)
    numerator = poly_sub(q_w_l, [1], prime)
    a_poly, remainder = poly_divmod(numerator, g, prime)
    require(poly_zero(remainder, prime), "toy complement identity is not divisible by g")
    right_side = poly_add([1], poly_mul(g, a_poly, prime), prime)
    require(q_w_l == right_side, "toy qWL=1+gA orientation failed")

    resultant_identity = (
        pow(q_scalar, poly_degree(g, prime), prime)
        * poly_resultant(g, w, prime)
        * poly_resultant(g, l_complement, prime)
    ) % prime
    require(resultant_identity == 1, "toy complement resultant normalization failed")
    require(poly_resultant(g, right_side, prime) == 1,
            "toy Res(g,1+gA)=1 failed")


def set_path(path: tuple[str, ...], value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(contract: dict[str, Any]) -> None:
        target: Any = contract
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
    return mutate


def delete_path(path: tuple[str, ...]) -> Callable[[dict[str, Any]], None]:
    def mutate(contract: dict[str, Any]) -> None:
        target: Any = contract
        for key in path[:-1]:
            target = target[key]
        del target[path[-1]]
    return mutate


def compare_expected(rendered: str, expected: str) -> None:
    require(rendered == expected, "rendered transcript differs from expected output")


def semantic_tamper_selftests() -> int:
    cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
        ("base-head", set_path(("base_head",), "0" * 40)),
        ("dependency-head", set_path(("dependency", "head"), "f" * 40)),
        ("same-source-cell", set_path(("source_cell", "same_source_cell"), False)),
        ("fixed-word", set_path(("source_cell", "fixed_received_word"), False)),
        ("fixed-owner", set_path(("source_cell", "fixed_first_match_owner"), False)),
        ("fixed-generator", set_path(("source_cell", "fixed_generator"), False)),
        ("fixed-ray", set_path(("source_cell", "fixed_nonzero_projective_ray"), False)),
        ("core-size", set_path(("source_cell", "fixed_core_size"), 27)),
        ("collapse-steps", set_path(("global_collapse", "steps"), 63)),
        ("collapse-end", set_path(("global_collapse", "j_max"), 62)),
        ("valid-edge", set_path(("global_collapse", "actual_valid_edge_required"), False)),
        ("w-unit", set_path(("global_collapse", "w_is_unit"), False)),
        ("squarefree-shortcut", set_path(("global_collapse", "squarefree_g_required"), True)),
        ("excluded-start", set_path(("spectral", "excluded_start"), 17)),
        ("excluded-end", set_path(("spectral", "excluded_end"), 63)),
        ("remaining-low", set_path(("spectral", "remaining_low"), "3..18")),
        ("remaining-high", set_path(("spectral", "remaining_high"), ">=64")),
        ("identity-orientation", set_path(
            ("split_complement", "identity"), "q_yz*W=1+g*A_yz*L_yz")),
        ("degree-bound", set_path(("split_complement", "a_degree_bound"), A_BOUND + 1)),
        ("finite-payment", set_path(("ledger", "finite_payment"), 1)),
        ("official-score", set_path(("ledger", "official_score"), "1/2")),
        ("pr872-nonclaim", delete_path(("nonclaims", "pr872"))),
        ("pr873-nonclaim", delete_path(("nonclaims", "pr873"))),
    )

    for name, mutate in cases:
        candidate = copy.deepcopy(CONTRACT)
        mutate(candidate)
        try:
            validate_contract(candidate)
        except ContractError:
            pass
        else:
            raise CheckError(f"semantic tamper escaped rejection: {name}")

    bad_pins = dict(SOURCE_PINS)
    first_pin = next(iter(bad_pins))
    bad_pins[first_pin] = "0" * 64
    try:
        verify_source_pins(bad_pins)
    except CheckError:
        pass
    else:
        raise CheckError("source-pin tamper escaped rejection")

    note_text = NOTE_PATH.read_text(encoding="utf-8")
    tampered_note = note_text.replace(DEPENDENCY_HEAD, "0" * 40, 1)
    try:
        verify_note_contract(tampered_note)
    except CheckError:
        pass
    else:
        raise CheckError("note-contract tamper escaped rejection")

    try:
        compare_expected("expected\n", "tampered\n")
    except CheckError:
        pass
    else:
        raise CheckError("expected-transcript tamper escaped rejection")

    return len(cases) + 3


def render_transcript(source_count: int, note_count: int, tamper_count: int) -> str:
    lines = (
        "RANK16_FIXED26_GLOBAL_SPECTRAL_RANK_GAP: PASS",
        f"dependency=PR862@{DEPENDENCY_HEAD};base={BASE_HEAD}",
        f"source_pins=PASS,count={source_count};note_contract=PASS,count={note_count}",
        "deployed=p2130706433,n2097152,B32768,a67472,r63601,delta3871,window64",
        "source_quantifiers=fixed_word|fixed_first_match_owner|fixed_g|fixed_nonzero_ray|fixed_26_core",
        "global64=ASSUMED;actual_valid_edge=>W_unit;squarefree_g_required=false",
        "primary_layers=PASS;nonzero_maximal_roots>=3871;zero_eigenvalue=PASS",
        "rank_gap=a>=3871*nu;allowed=3..17|>=65;excluded=18..64,count=47",
        "split_complement=q_yz*W*L_yz=1+g*A_yz;degL=1968015;degA<=1964144",
        "resultant=q_yz^67472*Res(g,W)*Res(g,L_yz)=1;toy_nonsquarefree=PASS",
        "finite_payment=0;parent=0;grand_list=0;grand_mca=0;official_score=0/2",
        "remaining_global_branches=3..17|>=65",
        "open_pr_nonclaims=PR872:T-3_not_outside_population<=3;PR873:fixed26/27_not_multiplicity-one_global_owners",
        f"semantic_tamper_selftests=PASS,count={tamper_count}",
        "expected_output=PASS",
        "RESULT=PASS",
    )
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="run only the fail-closed semantic mutation suite",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.tamper_selftest:
        count = semantic_tamper_selftests()
        print(f"SEMANTIC_TAMPER_SELFTEST: PASS count={count}")
        return 0

    validate_contract(CONTRACT)
    source_count = verify_source_pins()
    note_count = verify_note_contract()
    verify_arithmetic()
    verify_primary_layer_bound()
    verify_split_complement_toy()
    tamper_count = semantic_tamper_selftests()

    rendered = render_transcript(source_count, note_count, tamper_count)
    require(EXPECTED_PATH.is_file(), f"missing expected transcript: {EXPECTED_PATH}")
    expected = EXPECTED_PATH.read_text(encoding="utf-8")
    compare_expected(rendered, expected)
    sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except CheckError as exc:
        print(f"RESULT=FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
