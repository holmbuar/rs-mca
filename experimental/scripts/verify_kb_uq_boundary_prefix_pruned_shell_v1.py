#!/usr/bin/env python3
"""Replay the KoalaBear tangent-pruned boundary-prefix Q packet.

Two independent integer routes recompute the binomial coefficient, boundary
shell terms, and exact quotient guards without materializing the omitted tails.
The checker also validates source Git-blob pins, artifact
SHA-256 pins, PR_BODY.md grammar, and a mutation self-test.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable


CERTIFICATE = Path(
    "experimental/data/certificates/"
    "kb-uq-boundary-prefix-pruned-shell-v1/manifest.json"
)


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def ceil_div(a: int, b: int) -> int:
    require(a >= 0 and b > 0, "ceil_div domain")
    return (a + b - 1) // b


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    stop = math.isqrt(limit)
    for p in range(2, stop + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [i for i, flag in enumerate(sieve) if flag]


def valuation_factorial(n: int, p: int) -> int:
    total = 0
    while n:
        n //= p
        total += n
    return total


def balanced_product(values: Iterable[int]) -> int:
    work = list(values)
    if not work:
        return 1
    while len(work) > 1:
        nxt: list[int] = []
        for i in range(0, len(work) - 1, 2):
            nxt.append(work[i] * work[i + 1])
        if len(work) % 2:
            nxt.append(work[-1])
        work = nxt
    return work[0]


def binomial_prime_factor(n: int, r: int) -> int:
    r = min(r, n - r)
    require(0 <= r <= n, "binomial route-B domain")
    factors: list[int] = []
    for p in primes_upto(n):
        exponent = (
            valuation_factorial(n, p)
            - valuation_factorial(r, p)
            - valuation_factorial(n - r, p)
        )
        if exponent:
            factors.append(pow(p, exponent))
    return balanced_product(factors)


def binary_pow(base: int, exponent: int) -> int:
    require(base >= 0 and exponent >= 0, "binary_pow domain")
    result = 1
    factor = base
    e = exponent
    while e:
        if e & 1:
            result *= factor
        factor *= factor
        e >>= 1
    return result


def shell_term_math(a: int, j: int, e: int) -> int:
    return math.comb(a, e) * math.comb(j, e)


def shell_term_prime_factor(a: int, j: int, e: int) -> int:
    return binomial_prime_factor(a, e) * binomial_prime_factor(j, e)


def low_shell_upper(a: int, j: int, e: int, top_term: int) -> int:
    """Upper-bound sum_{i=0}^e H_i by (e+1)H_e.

    The shell ratio H_(i+1)/H_i decreases with i.  The endpoint check below
    therefore certifies that H_0,...,H_e is increasing.
    """
    if e == 0:
        return top_term
    require(
        (a - (e - 1)) * (j - (e - 1)) > e * e,
        f"shell terms are not increasing through H_{e}",
    )
    return (e + 1) * top_term


def scaled_tail_floor(
    c: int, choose: int, q0: int, omitted_upper: int, label: str
) -> int:
    """Compute floor(c(choose-omitted)/q0) without materializing omitted.

    `omitted_upper` is a proved upper bound for the nonnegative omitted low
    shells.  If c*omitted_upper is below the remainder of c*choose modulo q0,
    subtraction cannot cross a quotient boundary, so the quotient is exact.
    """
    require(c >= 0, f"negative multiplier: {label}")
    if c == 0:
        return 0
    quotient, remainder = divmod(c * choose, q0)
    require(c * omitted_upper < remainder, f"tail quotient guard failed: {label}")
    return quotient


def derive_packet(
    contract: dict[str, int], choose: int, q0: int, h_w: int, h_w1: int,
    field_cardinality: int,
) -> dict[str, Any]:
    n = contract["n"]
    k = contract["k"]
    a = contract["a"]
    j = n - a
    w = a - (k + 1)
    reserve = contract["B_star"] - contract["tangent_charge"]

    low_w_upper = low_shell_upper(a, j, w, h_w)
    low_w1_upper = low_shell_upper(a, j, w + 1, h_w1)
    floor_full, remainder = divmod(choose, q0)
    ceil_full = floor_full + (1 if remainder else 0)

    r_cf = j - w
    r_sp = j - w - 1

    tail_cf_1 = scaled_tail_floor(1, choose, q0, low_w_upper, "CF c=1")
    tail_sp_1 = scaled_tail_floor(1, choose, q0, low_w1_upper, "SP c=1")

    def cf_scaled(c: int) -> int:
        return scaled_tail_floor(c, choose, q0, low_w_upper, f"CF c={c}")

    def u_cf(b: int, c: int) -> int:
        return 1 + b * r_cf + cf_scaled(c)

    lower = ceil_full

    # The complete b=0 multiplier window is certified by the candidate and its
    # two adjacent endpoint inequalities, not by materializing the huge tail.
    c_max_estimate = (reserve * q0 - 1) // choose
    require(u_cf(0, 0) < lower, "b=0 lower endpoint c=0")
    require(lower <= u_cf(0, 1), "b=0 lower endpoint c=1")
    require(u_cf(0, c_max_estimate) <= reserve, "b=0 upper endpoint")
    require(reserve < u_cf(0, c_max_estimate + 1), "b=0 first excluded")

    b_min_c0 = ceil_div(lower - 1, r_cf)
    b_max_c0 = (reserve - 1) // r_cf

    full_scaled = cf_scaled(c_max_estimate)
    b_min_full = ceil_div(max(0, lower - 1 - full_scaled), r_cf)
    b_max_full = (reserve - 1 - full_scaled) // r_cf

    u_last_full = u_cf(b_max_full, c_max_estimate)
    u_first_excluded_full = u_cf(b_max_full + 1, c_max_estimate)

    separation_lhs = n + k * (lower * (lower - 1) // 2)

    return {
        "j": j,
        "K": k + 1,
        "w": w,
        "first_boundary_exchange": w + 1,
        "first_sparse_exchange": a - (k - 1),
        "r_cf": r_cf,
        "r_sp": r_sp,
        "choose_bits": choose.bit_length(),
        "q0_bits": q0.bit_length(),
        "remainder_bits": remainder.bit_length(),
        "low_w_upper_bits": low_w_upper.bit_length(),
        "low_w1_upper_bits": low_w1_upper.bit_length(),
        "low_w_upper_lt_remainder": low_w_upper < remainder,
        "low_w1_upper_lt_remainder": low_w1_upper < remainder,
        "floor_full": floor_full,
        "ceil_full": ceil_full,
        "tail_cf_floor": tail_cf_1,
        "tail_sp_floor": tail_sp_1,
        "u_0_1_cf": 1 + tail_cf_1,
        "u_0_1_sp": tail_sp_1,
        "u_0_1": max(1 + tail_cf_1, tail_sp_1),
        "remaining_after_u": reserve - max(1 + tail_cf_1, tail_sp_1),
        "window_b0": (1, c_max_estimate),
        "window_c0": (b_min_c0, b_max_c0),
        "window_c_full": (b_min_full, b_max_full),
        "u_last_full": u_last_full,
        "u_first_excluded_full": u_first_excluded_full,
        "last_full_margin": reserve - u_last_full,
        "first_excluded_excess": u_first_excluded_full - reserve,
        "field_cardinality": field_cardinality,
        "separation_lhs": separation_lhs,
        "separation_margin": field_cardinality - separation_lhs,
    }


def compute_route_a(contract: dict[str, int]) -> dict[str, Any]:
    p = contract["p"]
    n = contract["n"]
    a = contract["a"]
    j = n - a
    w = a - (contract["k"] + 1)
    choose = math.comb(n, j)
    q0 = pow(p, w)
    h_w = shell_term_math(a, j, w)
    h_w1 = shell_term_math(a, j, w + 1)
    field_cardinality = pow(p, contract["extension_degree"])
    return derive_packet(contract, choose, q0, h_w, h_w1, field_cardinality)


def compute_route_b(contract: dict[str, int]) -> dict[str, Any]:
    p = contract["p"]
    n = contract["n"]
    a = contract["a"]
    j = n - a
    w = a - (contract["k"] + 1)
    choose = binomial_prime_factor(n, j)
    q0 = binary_pow(p, w)
    h_w = shell_term_prime_factor(a, j, w)
    h_w1 = shell_term_prime_factor(a, j, w + 1)
    field_cardinality = binary_pow(p, contract["extension_degree"])
    return derive_packet(contract, choose, q0, h_w, h_w1, field_cardinality)


def compute_replay(contract: dict[str, int]) -> dict[str, Any]:
    route_a = compute_route_a(contract)
    route_b = compute_route_b(contract)
    for key in route_a:
        require(route_a[key] == route_b[key], f"independent route mismatch: {key}")
    return {"route_a": route_a, "route_b": route_b}

def path_component(container: Any, part: str, dotted: str) -> str | int:
    if isinstance(container, list):
        require(part.isdigit(), f"non-numeric list index in path: {dotted}")
        index = int(part)
        require(0 <= index < len(container), f"list index out of range in path: {dotted}")
        return index
    require(isinstance(container, dict), f"cannot descend through path: {dotted}")
    return part


def get_path(data: dict[str, Any], dotted: str) -> Any:
    value: Any = data
    for part in dotted.split("."):
        value = value[path_component(value, part, dotted)]
    return value


def set_path(data: dict[str, Any], dotted: str, value: Any) -> None:
    target: Any = data
    parts = dotted.split(".")
    for part in parts[:-1]:
        target = target[path_component(target, part, dotted)]
    target[path_component(target, parts[-1], dotted)] = value


def validate_pr_body(root: Path) -> None:
    path = root / "PR_BODY.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    require(len(lines) == 7, "PR_BODY.md must contain exactly seven lines")
    require(len(lines[0].split()) <= 6, "PR title exceeds six words")
    require(lines[1].startswith("STATUS: "), "PR status line missing")
    bullets = lines[2:]
    labels = ["Claim", "Status", "Verifier", "Consumers", "Risk-limits"]
    require(len(bullets) == 5, "PR body must contain five bullets")
    for line, label in zip(bullets, labels):
        require(line.startswith(f"- {label}:"), f"PR bullet order: {label}")
        require(len(line[2:].split()) <= 50, f"PR bullet exceeds 50 words: {label}")
    forbidden = ("branch", "draft", " ci ", "session")
    lowered = "\n".join(lines).lower()
    for token in forbidden:
        require(token not in lowered, f"forbidden PR process wording: {token!r}")


def validate_lean_sources(root: Path) -> None:
    package = root / "experimental/lean/kb_uq_boundary_prefix"
    lean_files = sorted(package.rglob("*.lean"))
    require(bool(lean_files), "Lean package has no .lean files")
    forbidden = ("sorry", "admit", "native_decide", "axiom ", "import Mathlib")
    for path in lean_files:
        text = path.read_text(encoding="utf-8")
        for token in forbidden:
            require(token not in text, f"forbidden Lean token {token!r} in {path}")
    require(not any(".lake" in path.parts for path in package.rglob("*")), ".lake artifact present")


def validate(
    data: dict[str, Any], replay: dict[str, Any], root: Path, *, check_hashes: bool
) -> int:
    checks = 0

    expected_scalars: dict[str, Any] = {
        "schema": "kb-uq-boundary-prefix-pruned-shell-v1",
        "status": "PROVED_PRUNING_CONDITIONAL_CAP_PROVED_LOWER_FLOOR_NO_REFUND",
        "workboard_item": "K2",
        "row": "KoalaBear MCA at 2^-128",
        "object": "MCA",
        "target_epsilon": "2^-128",
        "architecture": "GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1",
        "partition_digest": "4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc",
        "source_pin_policy": "EXACT_GIT_BLOBS_STRICT_IN_REPOSITORY_CHECKOUT",
        "owner_order.0": "SOURCE_COORDINATE_TANGENT_IMAGE",
        "owner_order.1": "ACTIVE_V4_BOUNDARY_PREFIX_Q",
        "owner_order.2": "ACTIVE_V4_BALANCED_CORE",
        "owner_order.3": "UNPAID_V4_COMPLEMENT",
        "contract.p": 2130706433,
        "contract.extension_degree": 6,
        "contract.n": 2097152,
        "contract.k": 1048576,
        "contract.a": 1116048,
        "contract.j": 981104,
        "contract.K": 1048577,
        "contract.w": 67471,
        "contract.B_star": 274980728111395087,
        "contract.tangent_charge": 981104,
        "contract.reserve": 274980728110413983,
        "result.hypothesis": "KB_V4_PRUNED_Q_ROOTED_SHELL",
        "result.b": 0,
        "result.c": 1,
        "result.first_boundary_exchange": 67472,
        "result.first_sparse_exchange": 67473,
        "result.column_far_shell_count": 913633,
        "result.sparse_shell_count": 913632,
        "result.full_floor": 57198030365,
        "result.full_ceiling": 57198030366,
        "result.column_far_tail_floor": 57198030365,
        "result.sparse_tail_floor": 57198030365,
        "result.column_far_cap": 57198030366,
        "result.sparse_cap": 57198030365,
        "result.conditional_U_Q": 57198030366,
        "result.certified_lower_floor": 57198030366,
        "result.remaining_reserve": 274980670912383617,
        "window.b0.c_min": 1,
        "window.b0.c_max": 4807520,
        "window.c0.b_min": 62606,
        "window.c0.b_max": 300975039332,
        "window.c4807520.b_min": 0,
        "window.c4807520.b_max": 58194,
        "window.last_admitted.cap": 274980728109989882,
        "window.last_admitted.margin": 424101,
        "window.first_excluded.cap": 274980728110903515,
        "window.first_excluded.excess": 489532,
        "lower_floor.separation_lhs": 1715268316138129359421571072,
        "lower_floor.field_cardinality": 93571093019388561295270373781649880353786165192103559169,
        "lower_floor.separation_margin": 93571093019388561295270373779934612037648035832681988097,
        "lower_floor.relation": ">=",
        "terminal": "OPEN GAP",
    }
    for dotted, expected in expected_scalars.items():
        require(get_path(data, dotted) == expected, f"certificate mismatch: {dotted}")
        checks += 1

    a = replay["route_a"]
    arithmetic_map = {
        "contract.j": a["j"],
        "contract.K": a["K"],
        "contract.w": a["w"],
        "result.first_boundary_exchange": a["first_boundary_exchange"],
        "result.first_sparse_exchange": a["first_sparse_exchange"],
        "result.column_far_shell_count": a["r_cf"],
        "result.sparse_shell_count": a["r_sp"],
        "result.full_floor": a["floor_full"],
        "result.full_ceiling": a["ceil_full"],
        "result.column_far_tail_floor": a["tail_cf_floor"],
        "result.sparse_tail_floor": a["tail_sp_floor"],
        "result.column_far_cap": a["u_0_1_cf"],
        "result.sparse_cap": a["u_0_1_sp"],
        "result.conditional_U_Q": a["u_0_1"],
        "result.remaining_reserve": a["remaining_after_u"],
        "window.last_admitted.cap": a["u_last_full"],
        "window.first_excluded.cap": a["u_first_excluded_full"],
        "window.last_admitted.margin": a["last_full_margin"],
        "window.first_excluded.excess": a["first_excluded_excess"],
        "lower_floor.separation_lhs": a["separation_lhs"],
        "lower_floor.field_cardinality": a["field_cardinality"],
        "lower_floor.separation_margin": a["separation_margin"],
    }
    for dotted, computed in arithmetic_map.items():
        require(get_path(data, dotted) == computed, f"arithmetic mismatch: {dotted}")
        checks += 1

    require(a["low_w_upper_lt_remainder"], "low-shell upper through w reaches the remainder")
    checks += 1
    require(a["low_w1_upper_lt_remainder"], "low-shell upper through w+1 reaches the remainder")
    checks += 1
    require(tuple(data["window"]["b0"].values()) == a["window_b0"], "b=0 window")
    checks += 1
    require(tuple(data["window"]["c0"].values()) == a["window_c0"], "c=0 window")
    checks += 1
    require(
        tuple(data["window"]["c4807520"].values()) == a["window_c_full"],
        "c=4807520 window",
    )
    checks += 1

    require(data["result"]["conditional_U_Q"] <= data["contract"]["reserve"], "cap exceeds reserve")
    checks += 1
    require(data["result"]["certified_lower_floor"] <= data["result"]["conditional_U_Q"], "window refuted by floor")
    checks += 1
    require(data["lower_floor"]["separation_lhs"] < data["lower_floor"]["field_cardinality"], "separation fails")
    checks += 1

    if check_hashes:
        source_pins = data["source_git_blobs"]
        expected_local_pins = {
            "experimental/grande_finale.tex":
                "8a5d9791900ca9eed773feba146b92ad296704ce",
            "experimental/rs_mca_thresholds.tex":
                "01302a797c502a05ed0b11ba949b8756e0aa2b22",
            "experimental/lean/rs_mca_thresholds/RsMcaThresholds/ExactSparsification.lean":
                "b4a89c7aa45fc068c010ebed9cd96073e6a2ec03",
            "experimental/lean/grande_finale/GrandeFinale/RSExactSupportUpper.lean":
                "314a7406221433582129dcdda865945ab2036672",
            "experimental/lean/grande_finale/GrandeFinale/SyndromeLine.lean":
                "d93e93e8dd6f1d5f121b03fcfc4f1baad501689c",
            "experimental/lean/grande_finale/GrandeFinale/PrefixPigeonhole.lean":
                "55eb966c883a825a5b413a467cf8cf33f8db629d",
            "experimental/lean/grande_finale/GrandeFinale/ExactPrefixList.lean":
                "e9c655772faf83bacfb62300127f68789298482e",
            "experimental/lean/grande_finale/GrandeFinale/PrefixRigidityPacking.lean":
                "130d8b07edef41e1a264bff10819a774dee13d9d",
            "experimental/lean/grande_finale/GrandeFinale/ScalarExtensionListLine.lean":
                "781c9e91e5d3a41e3c92c25c9a3371759e9af276",
            "experimental/lean/grande_finale/GrandeFinale/SeparatingPole.lean":
                "be7c084db1ed8ed409ea7759790d8a5aa9c1fc36",
            "experimental/lean/grande_finale/GrandeFinale/CollisionAwarePole.lean":
                "4b477c437b46da26ad27bfad739d2fcd59f28b6a",
            "experimental/lean/grande_finale/GrandeFinale/ExactListLine.lean":
                "c3642f07e260ec11f8f032d523d1f95843f3d580",
        }
        require(source_pins["local"] == expected_local_pins, "local source-pin table")
        checks += len(expected_local_pins)
        # A packet-only replay validates the connector-certified blob table.  In
        # a repository checkout, `agents.md` is present and every inherited
        # source blob is additionally recomputed from local bytes.
        if (root / "agents.md").is_file():
            for rel, expected in expected_local_pins.items():
                path = root / rel
                require(path.is_file(), f"missing pinned source: {rel}")
                require(
                    git_blob_sha1(path.read_bytes()) == expected,
                    f"source pin mismatch: {rel}",
                )
                checks += 1
        external = source_pins["external_round1"]
        require(external["head_sha"] == "c15927c90091602035f617226da9ecf03cfc7316", "round-1 head pin")
        checks += 1
        require(external["note_blob"] == "c17d8f0f2f72450ebda548089bb8274300e5c8d8", "round-1 note pin")
        checks += 1
        require(external["row_manifest_blob"] == "15731acc39a4cc38d8175fd09535b149490f8551", "round-1 manifest pin")
        checks += 1

        for rel, expected in data["artifact_sha256"].items():
            path = root / rel
            require(path.is_file(), f"missing artifact: {rel}")
            require(sha256_file(path) == expected, f"artifact hash mismatch: {rel}")
            checks += 1

        validate_pr_body(root)
        checks += 1
        validate_lean_sources(root)
        checks += 1

        note = (root / "experimental/notes/frontier-adjacent/kb_uq_boundary_prefix_pruned_shell_v1.md").read_text(encoding="utf-8")
        require(note.startswith("---\nworkboard_item: K2\n"), "note YAML header")
        checks += 1
        require(note.rstrip().endswith("# OPEN GAP"), "note terminal verdict")
        checks += 1

    return checks


def load_certificate(root: Path) -> dict[str, Any]:
    path = root / CERTIFICATE
    require(path.is_file(), f"missing certificate: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def tamper_selftest(data: dict[str, Any], replay: dict[str, Any], root: Path) -> int:
    mutations: list[tuple[str, Any]] = [
        ("contract.p", 2130706434),
        ("contract.n", 2097151),
        ("contract.a", 1116047),
        ("contract.reserve", 274980728110413984),
        ("partition_digest", "0" * 64),
        ("result.first_sparse_exchange", 67472),
        ("result.column_far_cap", 57198030365),
        ("result.sparse_cap", 57198030366),
        ("result.conditional_U_Q", 57198030365),
        ("result.certified_lower_floor", 57198030367),
        ("window.b0.c_max", 4807521),
        ("window.c0.b_min", 62605),
        ("window.c4807520.b_max", 58195),
        ("window.first_excluded.excess", 489531),
        ("lower_floor.separation_lhs", 1715268316138129359421571073),
        ("source_git_blobs.external_round1.note_blob", "0" * 40),
    ]
    artifact_key = next(iter(data["artifact_sha256"]))
    rejected = 0
    for dotted, value in mutations:
        trial = copy.deepcopy(data)
        set_path(trial, dotted, value)
        try:
            validate(trial, replay, root, check_hashes=True)
        except VerificationError:
            rejected += 1
        else:
            raise VerificationError(f"tamper was accepted: {dotted}")

    trial = copy.deepcopy(data)
    trial["artifact_sha256"][artifact_key] = "0" * 64
    try:
        validate(trial, replay, root, check_hashes=True)
    except VerificationError:
        rejected += 1
    else:
        raise VerificationError("artifact-hash tamper was accepted")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    try:
        data = load_certificate(root)
        replay = compute_replay(data["contract"])
        if args.check:
            checks = validate(data, replay, root, check_hashes=True)
            print(f"RESULT: PASS ({checks} checks)")
        else:
            validate(data, replay, root, check_hashes=True)
            rejected = tamper_selftest(data, replay, root)
            print(f"RESULT: PASS (tamper self-test rejected {rejected} mutations)")
    except (VerificationError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"RESULT: FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
