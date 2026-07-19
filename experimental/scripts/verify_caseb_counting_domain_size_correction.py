#!/usr/bin/env python3
"""Verify the Case-B domain-size correction and corrected feasibility gate.

The audited source used q0=|B| where the support count must use n=|D|.
This verifier:
  * refutes the printed m=2e polynomial-base calibration by exact integers;
  * proves that those rows cannot reach a 2^-128 normalized slope target even
    before prefix restriction;
  * supplies corrected constant-density rows with the same ambient-field rate;
  * supplies explicit smooth multiplicative rows D=F_p^* at fixed density;
  * composes the corrected fiber floor with the collision-aware pole theorem;
  * checks the exact necessary/sufficient counting gates and the A3 density cut.

Stdlib only. No floating point is used in any acceptance-critical comparison.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
from typing import Any

SCHEMA = "rs-mca-caseb-counting-domain-size-correction-v1"
STATUS = "COUNTEREXAMPLE / PROVED EXPONENTIAL-FIELD LOWER / OPEN FIXED-EPSILON CONSTANT FRACTION"
UPSTREAM_BASE = "6f4e918f27a11995d3951f4ebe7546d4add0f345"
TARGET_BITS = 128
REPO = Path(__file__).resolve().parents[2]
NOTE = (
    REPO
    / "experimental/notes/audits/caseb_counting_domain_size_correction.md"
)
CERTIFICATE = (
    REPO
    / "experimental/data/certificates/caseb-counting-domain-size-correction"
    / "caseb_counting_domain_size_correction.json"
)

SOURCE_PINS = {
    "experimental/notes/thresholds/caseb_equidistribution.md": {
        "blob_sha1": "04a75470d173c99a45d92fb7ddefc9dabb8c9775",
        "markers": (
            "q0 = n^C",
            "m = 2e",
            "log2|G| ~ m log2 q0",
        ),
    },
    "experimental/scripts/verify_caseb_equidistribution.py": {
        "blob_sha1": "c5ef7c502108d1bed95068acab74f338cf0631c1",
        "markers": (
            "PRIZE regime: POLY-SIZE base field q0 = n^C",
            "m = 2 * e",
            "logbinom = m * logq0",
        ),
    },
    "experimental/asymptotic_rs_mca_frontiers.tex": {
        "blob_sha1": "466b35c561b6142013f32a48012b8fafda4e09c3",
        "markers": (
            r"m_N/N\in[\alpha,1-\alpha]",
            r"\label{thm:collision-aware-pole}",
            r"\frac{L(q-n)}{q-n+k(L-1)}",
            r"L_m=\lceil\binom nm\abs\B^{-w}\rceil",
        ),
    },
}


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()


def payload_sha256(value: dict[str, Any]) -> str:
    unsigned = copy.deepcopy(value)
    unsigned.pop("payload_sha256", None)
    return hashlib.sha256(canonical_bytes(unsigned)).hexdigest()


def git_blob_sha1(path: Path) -> str:
    content = path.read_bytes()
    framed = b"blob " + str(len(content)).encode() + b"\0" + content
    return hashlib.sha1(framed).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packet_binding() -> dict[str, str]:
    script = Path(__file__).resolve()
    require(NOTE.exists(), f"missing packet note: {NOTE}")
    return {
        str(NOTE.relative_to(REPO)): file_sha256(NOTE),
        str(script.relative_to(REPO)): file_sha256(script),
    }


def source_binding() -> list[dict[str, Any]]:
    return [
        {
            "path": relative,
            "blob_sha1": spec["blob_sha1"],
            "markers": list(spec["markers"]),
        }
        for relative, spec in SOURCE_PINS.items()
    ]


def verify_source_pins() -> None:
    for relative, spec in SOURCE_PINS.items():
        path = REPO / relative
        require(path.exists(), f"missing source file: {relative}")
        text = path.read_text(encoding="utf-8")
        got_blob = git_blob_sha1(path)
        require(
            got_blob == spec["blob_sha1"],
            f"source blob drift: {relative}: got {got_blob}, want {spec['blob_sha1']}",
        )
        for marker in spec["markers"]:
            require(marker in text, f"source marker absent: {relative}: {marker}")

def floor_log2_integer(value: int) -> int:
    require(value > 0, "log2 input must be positive")
    return value.bit_length() - 1


def floor_log2_ratio(numerator: int, denominator: int) -> int:
    """Exact floor(log2(numerator/denominator)) for numerator >= denominator."""
    require(numerator >= denominator > 0, "bad log-ratio inputs")
    exponent = numerator.bit_length() - denominator.bit_length()
    if numerator < (denominator << exponent):
        exponent -= 1
    while numerator >= (denominator << (exponent + 1)):
        exponent += 1
    return exponent


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, "division denominator must be positive")
    return (numerator + denominator - 1) // denominator


def collision_aware_data(
    *, total_supports: int, q0: int, e: int, n: int, m: int, w: int
) -> dict[str, Any]:
    """Compose prefix pigeonhole with theorem (4.2), using exact integers."""
    k = m - w - 1
    field_size = q0**e
    require(field_size > n, "collision-aware theorem needs |F| > n")
    list_lower = ceil_div(total_supports, q0**w)
    bad_slope_lower = ceil_div(
        list_lower * (field_size - n),
        (field_size - n) + k * (list_lower - 1),
    )
    simple_lower = ceil_div(field_size - n, k + 1)
    if list_lower >= field_size:
        # Direct algebra:
        # L(Q-n)/(Q-n+k(L-1)) >= (Q-n)/(k+1)
        # iff L >= Q-n-k, which follows from L>=Q.
        require(
            bad_slope_lower >= simple_lower,
            "collision-aware lower failed the simple Q/(k+1) consequence",
        )
    target_budget = field_size // (1 << TARGET_BITS)
    target_relevant = bad_slope_lower > target_budget
    return {
        "prefix_list_ge_ambient": list_lower >= field_size,
        "prefix_list_bits_floor": floor_log2_integer(list_lower),
        "bad_slope_lower_bits_floor": floor_log2_integer(bad_slope_lower),
        "simple_q_over_k_lower_bits_floor": floor_log2_integer(simple_lower),
        "collision_aware_ge_simple_lower": bad_slope_lower >= simple_lower,
        "normalized_loss_bits_floor": floor_log2_ratio(
            field_size, bad_slope_lower
        ),
        "target_headroom_bits_floor": floor_log2_ratio(
            bad_slope_lower * (1 << TARGET_BITS), field_size
        )
        if target_relevant
        else None,
        "target_relevant_at_2^-128": target_relevant,
    }


def comb_multiplicative(n: int, k: int) -> int:
    """Independent exact recurrence for binomial coefficients."""
    require(0 <= k <= n, "bad binomial parameters")
    k = min(k, n - k)
    value = 1
    for index in range(1, k + 1):
        value = value * (n - k + index) // index
    return value


def primes_up_to(limit: int) -> list[int]:
    """Sieve used by the independent prime-exponent binomial route."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    root = math.isqrt(limit)
    for prime in range(2, root + 1):
        if sieve[prime]:
            count = (limit - prime * prime) // prime + 1
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * count
    return [value for value in range(2, limit + 1) if sieve[value]]


def factorial_valuation(n: int, prime: int) -> int:
    total = 0
    while n:
        n //= prime
        total += n
    return total


def comb_prime_exponents(n: int, k: int) -> int:
    """Independent exact binomial via Legendre exponents."""
    require(0 <= k <= n, "bad binomial parameters")
    k = min(k, n - k)
    value = 1
    for prime in primes_up_to(n):
        exponent = (
            factorial_valuation(n, prime)
            - factorial_valuation(k, prime)
            - factorial_valuation(n - k, prime)
        )
        if exponent:
            value *= prime**exponent
    return value


def is_prime(value: int) -> bool:
    """Deterministic trial-division primality test for the pinned small primes."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def half_rate_extension_degree(n: int, q0: int) -> int:
    """Largest e with q0^(2e) <= 2^n, computed by exact integers.

    Equivalently, e*log2(q0)/n <= 1/2 with the largest possible integer e.
    """
    low, high = 0, n
    target = 1 << n
    while low < high:
        middle = (low + high + 1) // 2
        if q0 ** (2 * middle) <= target:
            low = middle
        else:
            high = middle - 1
    return low


def old_row(n: int, C: int) -> dict[str, Any]:
    # The source rows use n=2^s and q0=n^C.
    s = floor_log2_integer(n)
    require(1 << s == n, "n must be a power of two")
    log2_q0 = C * s
    q0 = n**C
    e = int((n // 2) // log2_q0)
    # Match int(0.5*n/log2_q0) exactly because both inputs are integral here.
    require(e == int(0.5 * n / log2_q0), "extension-degree calibration mismatch")
    m = 2 * e
    w = 4
    k = m - w - 1
    total_supports = math.comb(n, m)
    require(
        total_supports == comb_prime_exponents(n, m),
        "domain binomial routes disagree",
    )
    ambient = q0**e
    wrong_universe_supports = math.comb(q0, m)
    require(
        wrong_universe_supports == comb_multiplicative(q0, m),
        "wrong-universe binomial routes disagree",
    )

    # Acceptance-critical comparisons are exact.
    target_budget = ambient // (1 << TARGET_BITS)
    impossible_at_target = total_supports <= target_budget
    wrong_universe_feasible = (
        ceil_div(wrong_universe_supports, q0**w) >= ambient
    )
    true_average_feasible = ceil_div(total_supports, q0**w) >= ambient

    return {
        "n": n,
        "C": C,
        "q0": q0,
        "log2_q0": log2_q0,
        "e": e,
        "m": m,
        "w": w,
        "k": k,
        "density_num": m,
        "density_den": n,
        "case_b": e <= k,
        "total_supports_bits_floor": floor_log2_integer(total_supports),
        "ambient_bits": e * log2_q0,
        "target_adjusted_ambient_bits": e * log2_q0 - TARGET_BITS,
        "wrong_universe_binom_bits_floor": floor_log2_integer(wrong_universe_supports),
        "wrong_universe_feasible": wrong_universe_feasible,
        "true_average_feasible": true_average_feasible,
        "universal_target_impossible": impossible_at_target,
        "bit_deficit_below_target_floor": (
            (e * log2_q0 - TARGET_BITS)
            - floor_log2_integer(total_supports)
        ),
    }


def corrected_row(n: int, C: int) -> dict[str, Any]:
    s = floor_log2_integer(n)
    require(1 << s == n, "n must be a power of two")
    log2_q0 = C * s
    q0 = n**C
    e = int((n // 2) // log2_q0)
    m = n // 2
    w = 4
    k = m - w - 1
    total_supports = math.comb(n, m)
    require(
        total_supports == comb_prime_exponents(n, m),
        "corrected binomial routes disagree",
    )
    ambient = q0**e
    average_numerator = total_supports
    average_denominator = q0**w

    average_floor = ceil_div(average_numerator, average_denominator)
    candidate_at_field_scale = average_floor >= ambient
    candidate_at_target_scale = average_floor > ambient // (1 << TARGET_BITS)
    row = {
        "n": n,
        "C": C,
        "q0": q0,
        "log2_q0": log2_q0,
        "e": e,
        "m": m,
        "w": w,
        "k": k,
        "density_num": m,
        "density_den": n,
        "case_b": e <= k,
        "total_supports_bits_floor": floor_log2_integer(total_supports),
        "ambient_bits": e * log2_q0,
        "average_field_scale_candidate": candidate_at_field_scale,
        "average_target_scale_candidate": candidate_at_target_scale,
        "average_surplus_bits_floor": floor_log2_ratio(
            total_supports, q0 ** (e + w)
        ),
    }
    row["collision_aware"] = collision_aware_data(
        total_supports=total_supports,
        q0=q0,
        e=e,
        n=n,
        m=m,
        w=w,
    )
    return row


def structured_prime_row(p: int) -> dict[str, Any]:
    """A literal smooth multiplicative calibration: B=F_p, D=F_p^*."""
    require(is_prime(p), f"structured calibration modulus is not prime: {p}")
    n = p - 1
    q0 = p
    e = half_rate_extension_degree(n, q0)
    m = n // 2
    w = 4
    k = m - w - 1
    total_supports = math.comb(n, m)
    require(
        total_supports == comb_prime_exponents(n, m),
        "structured binomial routes disagree",
    )
    ambient = q0**e
    average_floor = ceil_div(total_supports, q0**w)
    field_sized_average = average_floor >= ambient
    target_sized_average = average_floor > ambient // (1 << TARGET_BITS)
    row = {
        "p": p,
        "domain": "F_p^*",
        "n": n,
        "q0": q0,
        "e": e,
        "m": m,
        "w": w,
        "k": k,
        "density_num": m,
        "density_den": n,
        "case_b": e <= k,
        "half_rate_degree_exact": (
            q0 ** (2 * e) <= (1 << n) < q0 ** (2 * (e + 1))
        ),
        "total_supports_bits_floor": floor_log2_integer(total_supports),
        "ambient_bits_floor": floor_log2_integer(ambient),
        "prefix_adjusted_field_bits_floor": floor_log2_integer(q0 ** (e + w)),
        "average_field_scale_candidate": field_sized_average,
        "average_target_scale_candidate": target_sized_average,
        "average_surplus_bits_floor": floor_log2_ratio(
            total_supports, q0 ** (e + w)
        ),
    }
    row["collision_aware"] = collision_aware_data(
        total_supports=total_supports,
        q0=q0,
        e=e,
        n=n,
        m=m,
        w=w,
    )
    return row


def asymptotic_half_rate_family() -> dict[str, Any]:
    """Exact finite anchors for the elementary p->infinity proof.

    For every odd p>=61, n=p-1 and w=4:
      central binomial >= 2^n/p,
      2^(n/2) >= p^5,
      hence ceil(C(n,n/2)/p^4) >= 2^(n/2).
    Taking e maximal with p^(2e)<=2^n gives Q=p^e<=2^(n/2),
    so the prefix-list lower is at least Q.
    """
    threshold = 61
    w = 4
    n = threshold - 1
    base_entropy_gate = (1 << (n // 2)) >= threshold ** (w + 1)
    # For odd p advanced by 2, R(p)=2^((p-1)/2)/p^(w+1) satisfies
    # R(p+2)/R(p)=2*(p/(p+2))^(w+1). This is >= the p=61 ratio >1.
    monotone_ratio_gate = (
        2 * threshold ** (w + 1) > (threshold + 2) ** (w + 1)
    )
    require(base_entropy_gate, "p=61 entropy gate failed")
    require(monotone_ratio_gate, "odd-step monotonicity gate failed")

    # Exact sample sweep on genuine primes. The asymptotic proof itself is the
    # two inequalities above; this sweep is a deterministic regression.
    sample_primes = [61, 101, 251, 509, 1009, 4099]
    rows = []
    for p in sample_primes:
        require(is_prime(p), f"asymptotic sample is not prime: {p}")
        row = structured_prime_row(p)
        require(
            row["average_field_scale_candidate"],
            f"asymptotic sample prefix list does not reach the field: {p}",
        )
        require(
            row["collision_aware"]["collision_aware_ge_simple_lower"],
            f"asymptotic sample collision lower failed: {p}",
        )
        rows.append(
            {
                "p": p,
                "n": row["n"],
                "e": row["e"],
                "k": row["k"],
                "ambient_bits_floor": row["ambient_bits_floor"],
                "bad_slope_lower_bits_floor": row["collision_aware"][
                    "bad_slope_lower_bits_floor"
                ],
                "ambient_exponent_loss_bits_floor": row["collision_aware"][
                    "normalized_loss_bits_floor"
                ],
            }
        )

    return {
        "w": w,
        "threshold_p": threshold,
        "base_entropy_gate": "2^30 >= 61^5",
        "base_entropy_gate_holds": base_entropy_gate,
        "odd_step_ratio_gate": "2*61^5 > 63^5",
        "odd_step_ratio_gate_holds": monotone_ratio_gate,
        "theorem": (
            "For primes p->infinity, n=p-1, m=n/2, w=4, "
            "e=max{j:p^(2j)<=2^n}, Q=p^e, the identity-prefix list has "
            "L>=Q and theorem (4.2) gives B_MCA(m)>=ceil((Q-n)/(k+1))="
            "Q/exp(o(n)); hence every subexponential target is crossed."
        ),
        "sample_rows": rows,
    }


def gate_fixture() -> list[dict[str, Any]]:
    # Small exact rows distinguish the two logical gates:
    # any target-relevant fiber needs C(n,m) > floor(2^-tau q0^e);
    # pigeonhole supplies a field-sized depth-w fiber exactly when
    # ceil(C(n,m)/q0^w) >= q0^e.
    fixtures = [
        # impossible even with the whole support layer
        (32, 1 << 20, 10, 5, 1),
        # target-possible but average not field-sized
        (32, 64, 2, 5, 2),
        # pigeonhole supplies a field-sized fiber
        (64, 64, 2, 32, 1),
    ]
    out = []
    for n, q0, e, m, w in fixtures:
        total = math.comb(n, m)
        require(total == comb_prime_exponents(n, m), "gate binomial routes disagree")
        necessary = total > q0**e // (1 << TARGET_BITS)
        sufficient = ceil_div(total, q0**w) >= q0**e
        out.append(
            {
                "n": n,
                "q0": q0,
                "e": e,
                "m": m,
                "w": w,
                "necessary_target_gate": necessary,
                "sufficient_average_gate": sufficient,
            }
        )
    return out


def build_payload() -> dict[str, Any]:
    old = [old_row(1 << 14, 2), old_row(1 << 16, 3), old_row(1 << 18, 2)]
    corrected = [
        corrected_row(1 << 14, 2),
        corrected_row(1 << 16, 3),
        corrected_row(1 << 18, 2),
    ]
    structured = [
        structured_prime_row(1009),
        structured_prime_row(4099),
        structured_prime_row(16411),
    ]
    asymptotic_family = asymptotic_half_rate_family()

    # The old surrogate passes exactly where the true domain count fails.
    require(all(row["wrong_universe_feasible"] for row in old),
            "wrong-universe exact binomial must pass")
    require(all(not row["true_average_feasible"] for row in old), "true average must fail")
    require(all(row["universal_target_impossible"] for row in old), "old rows must be impossible")
    require(all(row["case_b"] for row in old), "old rows must remain Case B")
    require(all(row["density_num"] * 20 < row["density_den"] for row in old),
            "old rows must visibly leave fixed density")

    # The corrected rows stay in Case B, satisfy fixed density, and have a
    # pigeonhole-supplied fiber at least as large as the ambient field.
    require(all(row["average_field_scale_candidate"] for row in corrected),
            "corrected rows must supply a field-sized average fiber")
    require(all(row["average_target_scale_candidate"] for row in corrected),
            "corrected rows must pass the target gate")
    require(all(row["case_b"] for row in corrected), "corrected rows must be Case B")
    require(all(2 * row["density_num"] == row["density_den"] for row in corrected),
            "corrected rows must have density 1/2")
    require(all(row["collision_aware"]["prefix_list_ge_ambient"] for row in corrected),
            "corrected rows must feed the collision-aware field-scale regime")
    require(all(row["collision_aware"]["target_relevant_at_2^-128"] for row in corrected),
            "corrected rows must cross the printed target by theorem (4.2)")

    # The structured controls instantiate the repair on actual smooth
    # multiplicative domains D=F_p^*, not merely arbitrary n-point subsets.
    require(all(row["half_rate_degree_exact"] for row in structured),
            "structured extension degrees must be exact half-rate maxima")
    require(all(row["average_field_scale_candidate"] for row in structured),
            "structured rows must supply a field-sized average fiber")
    require(all(row["average_target_scale_candidate"] for row in structured),
            "structured rows must pass the target gate")
    require(all(row["case_b"] for row in structured),
            "structured rows must remain Case B")
    require(all(2 * row["density_num"] == row["density_den"] for row in structured),
            "structured rows must have density 1/2")
    require(all(row["collision_aware"]["prefix_list_ge_ambient"] for row in structured),
            "structured rows must feed the collision-aware field-scale regime")
    require(all(row["collision_aware"]["target_relevant_at_2^-128"] for row in structured),
            "structured rows must cross the printed target by theorem (4.2)")

    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "upstream_base": UPSTREAM_BASE,
        "target_bits": TARGET_BITS,
        "claim": (
            "The integrated Case-B polynomial-base calibration uses binom(|B|,m) "
            "where the support layer is binom(|D|,m). Its printed m=2e rows are "
            "not merely below average: the entire support layer is smaller than "
            "2^-128|F|, so no prefix fiber can be prize-relevant. The broad "
            "counting-open conclusion survives only after replacing m=2e by a "
            "fixed-density choice such as m=n/2; explicit D=F_p^* rows show "
            "that this repair is available on genuine smooth multiplicative domains. "
            "On every corrected row, the existing collision-aware pole theorem "
            "already gives more than 2^-128|F| distinct bad slopes. The same "
            "composition gives an infinite smooth multiplicative family with "
            "|F|/exp(o(n)) bad slopes, crossing every subexponential target; "
            "only fixed-epsilon constant-fraction coverage remains open."
        ),
        "independent_arithmetic_routes": {
            "domain_binomials": "math.comb = Legendre-prime-exponent reconstruction",
            "wrong_universe_binomials": "math.comb = exact multiplicative recurrence",
            "extension_degree": "integer binary search for max e with q0^(2e) <= 2^n",
        },
        "exact_gates": {
            "necessary_for_any_target_relevant_fiber": (
                "binom(n,m) > floor(q0^e / 2^tau), equivalently "
                "binom(n,m) * 2^tau > q0^e"
            ),
            "sufficient_for_a_depth_w_field_sized_fiber": (
                "ceil(binom(n,m)/q0^w) >= q0^e, equivalently "
                "binom(n,m) > q0^w * (q0^e - 1)"
            ),
            "asymptotic_boundary": (
                "if m/n->beta, e log2(q0)/n->c, and "
                "w log2(q0)/n->lambda, then c+lambda=H2(beta) is the "
                "average-fiber counting boundary"
            ),
            "general_subexponential_target_region": (
                "if c+lambda<H2(beta), then L/Q=exp(Omega(n)) and theorem "
                "(4.2) gives B_MCA(m)>=Q/exp(o(n)), crossing every "
                "T_n=exp(o(n))"
            ),
            "collision_aware_consequence": (
                "if L=ceil(binom(n,m)/q0^w) >= Q=q0^e, then theorem (4.2) "
                "gives M(L) >= ceil((Q-n)/(k+1)), k=m-w-1"
            ),
            "asymptotic_half_rate_obstruction": (
                "for primes p->infinity, D=F_p^*, m=(p-1)/2, w=4, and "
                "e maximal with p^(2e)<=2^(p-1), one has L>=Q=p^e and "
                "M(L)=Q/exp(o(p))"
            ),
        },
        "old_m_eq_2e_rows": old,
        "corrected_fixed_density_rows": corrected,
        "structured_prime_multiplicative_rows": structured,
        "asymptotic_half_rate_family": asymptotic_family,
        "gate_fixtures": gate_fixture(),
        "source_binding": source_binding(),
        "packet_binding": packet_binding(),
        "nonclaims": [
            "no fixed-epsilon constant-fraction growing-e subset-product equidistribution theorem",
            "no C7 semantic survival theorem",
            "no removal of FI-field'",
            "no deployed adjacent-row inequality",
            "no main-paper theorem or official score movement",
        ],
    }
    payload["payload_sha256"] = payload_sha256(payload)
    return payload


def write_certificate(payload: dict[str, Any]) -> None:
    CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def validate_frozen_certificate(
    frozen: dict[str, Any], expected: dict[str, Any]
) -> None:
    require(frozen.get("payload_sha256") == payload_sha256(frozen), "bad payload hash")
    require(frozen == expected, "certificate is not byte-semantically current")


def check_certificate(payload: dict[str, Any]) -> None:
    require(CERTIFICATE.exists(), f"missing certificate: {CERTIFICATE}")
    frozen = json.loads(CERTIFICATE.read_text())
    validate_frozen_certificate(frozen, payload)


def expect_rejected(
    frozen: dict[str, Any],
    expected: dict[str, Any],
    label: str,
    reason: str,
) -> None:
    try:
        validate_frozen_certificate(frozen, expected)
    except VerificationError as error:
        require(reason in str(error), f"{label} rejected for unexpected reason: {error}")
        return
    raise VerificationError(f"{label} unexpectedly accepted")


def tamper_selftest(payload: dict[str, Any]) -> int:
    mutations = 0

    bad = copy.deepcopy(payload)
    bad["old_m_eq_2e_rows"][0]["universal_target_impossible"] = False
    bad["payload_sha256"] = payload_sha256(bad)
    expect_rejected(
        bad,
        payload,
        "tamper 1",
        "certificate is not byte-semantically current",
    )
    mutations += 1

    bad = copy.deepcopy(payload)
    bad["corrected_fixed_density_rows"][1]["m"] -= 1
    expect_rejected(bad, payload, "tamper 2", "bad payload hash")
    mutations += 1

    bad = copy.deepcopy(payload)
    bad["exact_gates"]["necessary_for_any_target_relevant_fiber"] = "wrong"
    expect_rejected(bad, payload, "tamper 3", "bad payload hash")
    mutations += 1

    bad = copy.deepcopy(payload)
    bad["upstream_base"] = "0" * 40
    expect_rejected(bad, payload, "tamper 4", "bad payload hash")
    mutations += 1

    bad = copy.deepcopy(payload)
    bad["structured_prime_multiplicative_rows"][0]["p"] = 1013
    expect_rejected(bad, payload, "tamper 5", "bad payload hash")
    mutations += 1

    bad = copy.deepcopy(payload)
    bad["independent_arithmetic_routes"]["domain_binomials"] = "unchecked"
    expect_rejected(bad, payload, "tamper 6", "bad payload hash")
    mutations += 1

    bad = copy.deepcopy(payload)
    first_packet_path = sorted(bad["packet_binding"])[0]
    bad["packet_binding"][first_packet_path] = "0" * 64
    expect_rejected(bad, payload, "tamper 7", "bad payload hash")
    mutations += 1

    bad = copy.deepcopy(payload)
    bad["structured_prime_multiplicative_rows"][1]["collision_aware"][
        "target_relevant_at_2^-128"
    ] = False
    expect_rejected(bad, payload, "tamper 8", "bad payload hash")
    mutations += 1

    bad = copy.deepcopy(payload)
    bad["asymptotic_half_rate_family"]["odd_step_ratio_gate_holds"] = False
    expect_rejected(bad, payload, "tamper 9", "bad payload hash")
    mutations += 1

    return mutations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    parser.add_argument("--skip-source-pins", action="store_true")
    args = parser.parse_args()

    if not args.skip_source_pins:
        verify_source_pins()
    payload = build_payload()
    if args.write:
        write_certificate(payload)
    if args.check or not args.write:
        check_certificate(payload)

    mutations = tamper_selftest(payload) if args.tamper_selftest else 0
    print("RESULT: PASS")
    print(f"schema={SCHEMA}")
    print(f"base={UPSTREAM_BASE}")
    print("old_rows=3,all_wrong_universe_binomials_pass=true,all_true_rows_target_impossible=true")
    print("corrected_rows=3,all_fixed_density_candidates=true")
    print("structured_prime_rows=3,all_smooth_multiplicative_candidates=true")
    print("collision_aware_target_rows=6,all_cross_2^-128=true")
    print("asymptotic_half_rate_family=PROVED,subexponential_targets_crossed=true")
    print(f"source_files={len(SOURCE_PINS)}")
    if args.tamper_selftest:
        print(f"tamper_selftest=PASS,{mutations}/{mutations}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
