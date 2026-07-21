#!/usr/bin/env python3
"""Auxiliary Python replay for the M31 rooted-shell packet.

This script is retained for exploration, certificate regeneration, and hostile
replay. It is not the proof validator. The authoritative validation is the
stdlib-only Lean package under experimental/lean/m31_q_rooted_shell, built by
the fork draft-PR GitHub Action.

Zero-argument mode regenerates every exact integer and exhaustive toy census,
then compares the result with the shipped JSON certificate. Pure Python 3
stdlib; exit 0 means PASS.

The proved finite lemma is this. Let F be a family of m-subsets in one
prefix fibre, and assume distinct members have exchange distance e>w. Put
H_e = C(m,e) C(n-m,e), Q=p^w, R=min(m,n-m)-w, and
  d_e(A)=#{B in F minus {A}: d(A,B)=e}.
If for every A and e>w,
  Q * max(d_e(A)-3,0) <= 7 H_e,
then
  |F| <= 1 + 3R + floor(7 C(n,m)/Q).
At the binding Mersenne-31 list row the right side is 16,696,786, leaving
80,429 integers below B*=16,777,215.

The exhaustive toy census additionally shows:
  * the 3+7 condition holds on seven faithful/pruned small rows;
  * the stronger 2+7 condition is false on a faithful Chebyshev row.
These toy checks are measurements/counterexamples to candidate strengthenings,
not a deployed proof.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
from typing import Dict, List, Sequence, Tuple

HERE = os.path.dirname(os.path.abspath(__file__))
CERT_PATH = os.path.normpath(
    os.path.join(
        HERE,
        "..",
        "data",
        "certificates",
        "m31-q-rooted-shell-envelope",
        "m31_q_rooted_shell_envelope.json",
    )
)
NOTE_PATH = os.path.normpath(
    os.path.join(
        HERE,
        "..",
        "notes",
        "thresholds",
        "m31_q_rooted_shell_envelope.md",
    )
)

P_M31 = 2**31 - 1
N_DEP = 2**21
W_DEP = 67447
BSTAR = 2**24 - 1


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def prime_factors(n: int) -> List[int]:
    out: List[int] = []
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            out.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        out.append(x)
    return out


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise ValueError(f"no primitive root modulo {p}")


def subgroup(p: int, n: int) -> Tuple[int, ...]:
    if (p - 1) % n != 0:
        raise ValueError("n must divide p-1")
    g = primitive_root(p)
    root = pow(g, (p - 1) // n, p)
    vals = tuple(pow(root, i, p) for i in range(n))
    if len(set(vals)) != n:
        raise AssertionError("subgroup generator has wrong order")
    return vals


Pair = Tuple[int, int]


def fp2_mul(x: Pair, y: Pair, p: int) -> Pair:
    a, b = x
    c, d = y
    return ((a * c - b * d) % p, (a * d + b * c) % p)


def fp2_pow(x: Pair, e: int, p: int) -> Pair:
    out = (1, 0)
    base = x
    k = e
    while k:
        if k & 1:
            out = fp2_mul(out, base, p)
        base = fp2_mul(base, base, p)
        k >>= 1
    return out


def fp2_inv(x: Pair, p: int) -> Pair:
    a, b = x
    den = (a * a + b * b) % p
    if den == 0:
        raise ZeroDivisionError
    inv = pow(den, p - 2, p)
    return (a * inv % p, -b * inv % p)


def norm_one_generator(p: int) -> Pair:
    if p % 4 != 3:
        raise ValueError("this deterministic model assumes p=3 mod 4")
    order = p + 1
    factors = prime_factors(order)
    for t in range(1, p):
        den = (1 + t * t) % p
        if den == 0:
            continue
        den_inv = pow(den, p - 2, p)
        u = ((1 - t * t) * den_inv % p, 2 * t * den_inv % p)
        if u == (1, 0):
            continue
        if all(fp2_pow(u, order // q, p) != (1, 0) for q in factors):
            if fp2_pow(u, order, p) != (1, 0):
                raise AssertionError("bad norm-one generator")
            return u
    raise ValueError(f"no norm-one generator for p={p}")


def chebyshev_twin_coset_domain(p: int, n: int, offset: int) -> Tuple[int, ...]:
    """Return the x-coordinate image of g^offset H union g^-offset H."""
    if (p + 1) % n != 0:
        raise ValueError("n must divide p+1")
    u = norm_one_generator(p)
    step = (p + 1) // n
    hgen = fp2_pow(u, step, p)
    h_group = [fp2_pow(hgen, i, p) for i in range(n)]
    g = fp2_pow(u, offset, p)
    gi = fp2_inv(g, p)
    torus = [fp2_mul(g, h, p) for h in h_group] + [fp2_mul(gi, h, p) for h in h_group]
    xs = [a for a, _ in torus]
    counts = Counter(xs)
    if len(counts) != n or set(counts.values()) != {2}:
        raise AssertionError(
            f"twin coset is not 2-to-1: p={p}, n={n}, offset={offset}"
        )
    seen = set()
    out = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            out.append(x)
    if set((-x) % p for x in out) != set(out):
        raise AssertionError("Chebyshev domain is not stable under negation")
    t2_counts = Counter((2 * x * x - 1) % p for x in out)
    if len(t2_counts) != n // 2 or set(t2_counts.values()) != {2}:
        raise AssertionError("T_2 is not exactly two-to-one on the twin coset")
    dset = set(out)
    if all((x * y) % p in dset for x in out for y in out):
        raise AssertionError("faithful Chebyshev control accidentally product-closed")
    return tuple(out)


def elementary_prefix(
    values: Sequence[int], support: Sequence[int], w: int, p: int
) -> Tuple[int, ...]:
    e = [1] + [0] * w
    for idx in support:
        x = values[idx]
        for j in range(w, 0, -1):
            e[j] = (e[j] + x * e[j - 1]) % p
    return tuple(e[1:])


def negation_partner(values: Sequence[int], p: int) -> Dict[int, int]:
    by_value = {x: i for i, x in enumerate(values)}
    return {i: by_value[(-x) % p] for i, x in enumerate(values)}


def cheb_is_quotient(support: frozenset[int], partner: Dict[int, int]) -> bool:
    return all(partner[i] in support for i in support)


def mult_is_quotient(support: frozenset[int], n: int) -> bool:
    for q in prime_factors(n):
        step = n // q
        if all((i + step) % n in support for i in support):
            return True
    return False


def h_shell(n: int, m: int, e: int) -> int:
    return comb(m, e) * comb(n - m, e)


def frac_record(x: Fraction) -> Dict[str, object]:
    return {
        "numerator": x.numerator,
        "denominator": x.denominator,
        "decimal": float(x),
    }


def canonical_digest(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def prune_and_measure(
    *,
    p: int,
    values: Sequence[int],
    m: int,
    w: int,
    quotient_predicate,
    row_name: str,
) -> Tuple[Dict[str, object], Dict[str, object] | None]:
    n = len(values)
    q = p**w
    fibers: Dict[Tuple[int, ...], List[frozenset[int]]] = defaultdict(list)
    for support in combinations(range(n), m):
        fs = frozenset(support)
        if quotient_predicate(fs):
            continue
        fibers[elementary_prefix(values, support, w, p)].append(fs)

    residual: Dict[Tuple[int, ...], List[frozenset[int]]] = {}
    planted_keys = 0
    for key, members in fibers.items():
        common = set(members[0])
        for support in members[1:]:
            common.intersection_update(support)
        if common:
            planted_keys += 1
            continue
        residual[key] = members

    if not residual:
        raise AssertionError(f"no residual fibres in {row_name}")

    max_b2 = Fraction(0, 1)
    max_b3 = Fraction(0, 1)
    first_counterexample = None
    max_fiber = 0

    for key in sorted(residual):
        members = residual[key]
        max_fiber = max(max_fiber, len(members))
        for ai, anchor in enumerate(members):
            degrees: Counter[int] = Counter()
            for bj, other in enumerate(members):
                if ai == bj:
                    continue
                distance = m - len(anchor.intersection(other))
                if distance <= w:
                    raise AssertionError(
                        f"prefix rigidity failed in {row_name}: distance {distance} <= w={w}"
                    )
                degrees[distance] += 1
            for distance, degree in sorted(degrees.items()):
                shell = h_shell(n, m, distance)
                r2 = Fraction(max(degree - 2, 0) * q, shell)
                r3 = Fraction(max(degree - 3, 0) * q, shell)
                max_b2 = max(max_b2, r2)
                max_b3 = max(max_b3, r3)
                if first_counterexample is None and r2 > 7 and r3 <= 7:
                    neighbors = [
                        sorted(other)
                        for bj, other in enumerate(members)
                        if ai != bj and m - len(anchor.intersection(other)) == distance
                    ]
                    first_counterexample = {
                        "row": row_name,
                        "prefix_key": list(key),
                        "residual_fiber_size": len(members),
                        "anchor_indices": sorted(anchor),
                        "anchor_values": [values[i] for i in sorted(anchor)],
                        "exchange_distance": distance,
                        "degree": degree,
                        "ambient_shell_size": shell,
                        "two_plus_seven_lhs": (degree - 2) * q,
                        "three_plus_seven_lhs": max(degree - 3, 0) * q,
                        "seven_H": 7 * shell,
                        "neighbors_indices": neighbors,
                        "neighbors_digest": canonical_digest(neighbors),
                    }

    if max_b3 > 7:
        raise AssertionError(f"3+7 failed in toy row {row_name}: {max_b3}")

    summary = {
        "row": row_name,
        "p": p,
        "n": n,
        "m": m,
        "w": w,
        "total_supports": comb(n, m),
        "primitive_prefix_keys": len(fibers),
        "planted_keys_removed": planted_keys,
        "residual_prefix_keys": len(residual),
        "max_residual_fiber": max_fiber,
        "max_required_coefficient_b2": frac_record(max_b2),
        "max_required_coefficient_b3": frac_record(max_b3),
        "three_plus_seven_holds": max_b3 <= 7,
    }
    return summary, first_counterexample


def deployed_row(
    name: str,
    m: int,
    *,
    c: int,
    q: int,
    compute_peak: bool,
) -> Dict[str, object]:
    n = N_DEP
    p = P_M31
    w = W_DEP
    r = min(m, n - m) - w
    bound = 1 + 3 * r + (7 * c) // q
    avg_floor, rem = divmod(c, q)
    avg_ceil = avg_floor + (1 if rem else 0)

    peak = None
    if compute_peak:
        e_peak = (m * (n - m) - 1) // (n + 2) + 1
        hp = h_shell(n, m, e_peak)
        peak = {
            "e": e_peak,
            "H_over_Q_floor": hp // q,
            "H_over_Q_ceil": ceil_div(hp, q),
            "three_plus_seven_degree_ceiling": 3 + (7 * hp) // q,
            "H_bit_length": hp.bit_length(),
        }

    b_table = []
    for b in [0, 1, 2, 3, 4, 18]:
        available = BSTAR - 1 - b * r
        kappa_display = available * (q / c)
        b_table.append(
            {
                "b": b,
                "kappa_to_fit_decimal": round(kappa_display, 9),
                "integer_coefficient_7_fits": 7 * c <= available * q,
            }
        )

    return {
        "name": name,
        "p": p,
        "n": n,
        "m": m,
        "w": w,
        "Q_bit_length": q.bit_length(),
        "C_bit_length": c.bit_length(),
        "Bstar": BSTAR,
        "admissible_shell_count_R": r,
        "avg_floor": avg_floor,
        "avg_ceil": avg_ceil,
        "three_plus_seven_bound": bound,
        "integer_reserve": BSTAR - bound,
        "naive_same_shell_star_from_Bstar_plus_one": ceil_div(BSTAR, r),
        "peak_shell": peak,
        "b_kappa_table": b_table,
    }


def generate_certificate() -> Dict[str, object]:
    q_dep = P_M31**W_DEP
    m_list = 981129
    c_list = comb(N_DEP, m_list)
    m_mca = m_list - 1
    c_mca_num = c_list * m_list
    c_mca_den = N_DEP - m_list + 1
    if c_mca_num % c_mca_den != 0:
        raise AssertionError("adjacent binomial recurrence is not integral")
    c_mca = c_mca_num // c_mca_den
    deployed = {
        "M31_list": deployed_row(
            "Mersenne-31 list", m_list, c=c_list, q=q_dep, compute_peak=True
        ),
        "M31_MCA": deployed_row(
            "Mersenne-31 MCA", m_mca, c=c_mca, q=q_dep, compute_peak=False
        ),
    }

    cheb_rows = []
    counterexample = None
    p, n, w = 127, 16, 1
    for offset in (1, 2, 3):
        values = chebyshev_twin_coset_domain(p, n, offset)
        partner = negation_partner(values, p)
        for m in (8, 9):
            row, cex = prune_and_measure(
                p=p,
                values=values,
                m=m,
                w=w,
                quotient_predicate=lambda support, partner=partner: cheb_is_quotient(
                    support, partner
                ),
                row_name=f"Chebyshev p={p},n={n},m={m},w={w},offset={offset}",
            )
            row["domain_values"] = list(values)
            cheb_rows.append(row)
            if counterexample is None and cex is not None:
                counterexample = cex
                counterexample["domain_values"] = list(values)

    values = subgroup(101, 20)
    mult_row, _ = prune_and_measure(
        p=101,
        values=values,
        m=12,
        w=2,
        quotient_predicate=lambda support: mult_is_quotient(support, 20),
        row_name="multiplicative p=101,n=20,m=12,w=2",
    )
    mult_row["domain_values"] = list(values)

    if counterexample is None:
        raise AssertionError("expected a faithful 2+7 counterexample")
    if not (
        counterexample["two_plus_seven_lhs"] > counterexample["seven_H"]
        and counterexample["three_plus_seven_lhs"] <= counterexample["seven_H"]
    ):
        raise AssertionError("counterexample guard failed")

    certificate: Dict[str, object] = {
        "schema": "m31-q-rooted-shell-envelope-v1",
        "status": {
            "general_lemma": "PROVED",
            "deployed_arithmetic": "PROVED_EXACT",
            "two_plus_seven": "COUNTEREXAMPLE_ON_FAITHFUL_TOY",
            "three_plus_seven_toys": "EXHAUSTIVE_MEASUREMENT",
            "deployed_row_sharp_q": "OPEN",
        },
        "theorem": {
            "shell_size": "H_e = C(m,e) C(n-m,e)",
            "hypothesis": "p^w * max(d_e(A)-3,0) <= 7 H_e for every anchor A and e>w",
            "conclusion": "|F| <= 1 + 3(min(m,n-m)-w) + floor(7 C(n,m)/p^w)",
            "contrapositive": "if |F| exceeds the displayed bound, every anchor has a shell with p^w(d_e(A)-3)>7H_e",
        },
        "deployed": deployed,
        "toy_rows": cheb_rows + [mult_row],
        "two_plus_seven_counterexample": counterexample,
    }
    certificate["payload_sha256"] = canonical_digest(certificate)
    return certificate


def verify_certificate(
    cert: Dict[str, object], expected: Dict[str, object]
) -> List[str]:
    failures = []
    if cert != expected:
        failures.append("certificate does not byte-semantically match exact regeneration")
    try:
        if cert["deployed"]["M31_list"]["three_plus_seven_bound"] != 16696786:
            failures.append("M31-list bound changed")
        if cert["deployed"]["M31_list"]["integer_reserve"] != 80429:
            failures.append("M31-list reserve changed")
        if cert["deployed"]["M31_MCA"]["three_plus_seven_bound"] != 15009938:
            failures.append("M31-MCA bound changed")
        if cert["deployed"]["M31_MCA"]["integer_reserve"] != 1767277:
            failures.append("M31-MCA reserve changed")
        if cert["deployed"]["M31_list"]["peak_shell"]["e"] != 522119:
            failures.append("M31-list peak shell changed")
        if cert["deployed"]["M31_list"]["peak_shell"]["H_over_Q_floor"] != 2206:
            failures.append("M31-list peak baseline changed")
        if not all(row["three_plus_seven_holds"] for row in cert["toy_rows"]):
            failures.append("3+7 toy gate failed")
        cex = cert["two_plus_seven_counterexample"]
        if not (
            cex["two_plus_seven_lhs"]
            > cex["seven_H"]
            >= cex["three_plus_seven_lhs"]
        ):
            failures.append("2+7 counterexample inequalities changed")
    except (KeyError, TypeError):
        failures.append("certificate structure malformed")
    return failures


def tamper_selftest(expected: Dict[str, object]) -> None:
    mutations = []
    x = copy.deepcopy(expected)
    x["deployed"]["M31_list"]["Bstar"] += 1
    mutations.append(("Bstar", x))
    x = copy.deepcopy(expected)
    x["deployed"]["M31_list"]["peak_shell"]["e"] += 1
    mutations.append(("peak shell", x))
    x = copy.deepcopy(expected)
    x["two_plus_seven_counterexample"]["degree"] -= 1
    mutations.append(("counterexample degree", x))
    x = copy.deepcopy(expected)
    x["toy_rows"][0]["three_plus_seven_holds"] = False
    mutations.append(("toy verdict", x))
    for name, mutated in mutations:
        if not verify_certificate(mutated, expected):
            raise AssertionError(f"tamper was not rejected: {name}")
    print(f"TAMPER SELFTEST: PASS ({len(mutations)}/{len(mutations)})")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true", help="write exact certificate")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    expected = generate_certificate()
    if args.emit:
        os.makedirs(os.path.dirname(CERT_PATH), exist_ok=True)
        with open(CERT_PATH, "w", encoding="utf-8") as handle:
            json.dump(expected, handle, indent=2, sort_keys=True)
            handle.write("\n")
        print(f"EMIT: {CERT_PATH}")

    if not os.path.exists(CERT_PATH):
        print(f"FAIL: missing certificate {CERT_PATH}", file=sys.stderr)
        return 1
    with open(CERT_PATH, encoding="utf-8") as handle:
        cert = json.load(handle)
    failures = verify_certificate(cert, expected)
    if not os.path.exists(NOTE_PATH):
        failures.append(f"missing note {NOTE_PATH}")
    else:
        with open(NOTE_PATH, encoding="utf-8") as handle:
            note = handle.read()
        required_note_literals = [
            "16,696,786",
            "80,429",
            "15,009,938",
            "1,767,277",
            "e_peak = floor((m(n-m)-1)/(n+2))+1 = 522,119",
            "127(6-2)=508 > 7*64=448",
            "127(6-3)=381 <=448",
            "c674ee4d16ded9401adea1c9141b6ebf22fd6cb06a39a0c9dfb676811f41b962",
        ]
        for literal in required_note_literals:
            if literal not in note:
                failures.append(f"note drift: missing literal {literal!r}")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    if args.tamper_selftest:
        tamper_selftest(expected)

    list_row = expected["deployed"]["M31_list"]
    mca_row = expected["deployed"]["M31_MCA"]
    cex = expected["two_plus_seven_counterexample"]
    print("RESULT: PASS")
    print(
        "M31-list: bound={three_plus_seven_bound}, reserve={integer_reserve}, "
        "peak e={peak_shell[e]}, peak H/Q floor={peak_shell[H_over_Q_floor]}".format(
            **list_row
        )
    )
    print(
        f"M31-MCA:  bound={mca_row['three_plus_seven_bound']}, "
        f"reserve={mca_row['integer_reserve']}"
    )
    print(
        f"2+7 counterexample: {cex['row']}, key={cex['prefix_key']}, "
        f"e={cex['exchange_distance']}, degree={cex['degree']}, "
        f"lhs2={cex['two_plus_seven_lhs']} > 7H={cex['seven_H']} >= "
        f"lhs3={cex['three_plus_seven_lhs']}"
    )
    print(f"toy rows checked: {len(expected['toy_rows'])}; all 3+7 PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
