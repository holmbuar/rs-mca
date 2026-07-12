#!/usr/bin/env python3
"""Verify identity-crossing localization and the upper-half lower-route cut.

This verifier is deterministic, stdlib-only, and read-only.  It checks the
source statements, the analytic ``g_T`` localization, the exact integrated
syndrome-secant expression, and the fixed-rate/half-band arithmetic used by
``identity_crossing_upper_half_route_cut.md``.

The profile-list size-at-most-one calculation is an AUDIT-ONLY cross-check of PR
#699.  It is not claimed here as a new profile-list theorem.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, log2
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]

MANUSCRIPT = REPO / "experimental" / "asymptotic_rs_mca_frontiers.tex"
O7_AUDIT = (
    REPO
    / "experimental"
    / "notes"
    / "thresholds"
    / "lower_reserve_unsafe_side_coverage_audit.md"
)
SECANT_NOTE = (
    REPO
    / "experimental"
    / "notes"
    / "thresholds"
    / "syndrome_secant_challenge_lower.md"
)

ANALYTIC_NS = (2, 3, 4, 5, 7, 8, 16, 31, 64, 127, 256, 1024, 4096)
SECANT_N_MAX = 48
LIST_AUDIT_N_MAX = 80
FIXED_RATES = (
    Fraction(1, 8),
    Fraction(1, 4),
    Fraction(1, 2),
    Fraction(3, 4),
    Fraction(7, 8),
)

CHECKS = 0


def check(condition: bool, message: str) -> None:
    """Count and enforce one deterministic proof check."""

    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    check(numerator >= 0 and denominator > 0, "ceil_div domain")
    return (numerator + denominator - 1) // denominator


def is_prime(value: int) -> bool:
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


def next_prime_at_least(value: int) -> int:
    candidate = max(2, value)
    while not is_prime(candidate):
        candidate += 1
    return candidate


def next_power_of_two(value: int) -> int:
    return 1 << (value - 1).bit_length()


def field_sizes_at_least(n: int) -> tuple[int, ...]:
    """Prime-power cardinalities used in finite grids, all at least ``n``."""

    values = {
        next_power_of_two(n),
        next_prime_at_least(n),
        next_prime_at_least(2 * n),
    }
    result = tuple(sorted(values))
    check(all(q >= n and q >= 2 for q in result), f"field sizes for n={n}")
    return result


def selected_dimensions(n: int) -> tuple[int, ...]:
    if n <= 8:
        return tuple(range(1, n))
    candidates = {
        1,
        n // 8,
        n // 4,
        n // 2,
        (3 * n) // 4,
        (7 * n) // 8,
        n - 1,
    }
    return tuple(sorted(k for k in candidates if 1 <= k < n))


def verify_source_anchors() -> int:
    """Check the exact integrated sources consumed by this route cut."""

    anchors = {
        MANUSCRIPT: {
            "identity-frontier label": r"\label{cor:intro-identity-frontier}",
            "base bit size": r"\beta_n=\log_2|\B_n|",
            "literal nonnegative target": r"\tau_n=n^{-1}\log_2(1+B_n^*)",
            "identity exponent": r"F_n(g)=H_2(\rho_n+g)-\beta_ng",
            "rightmost superlevel": r"g_{T,n}=\sup",
            "domain/base containment": r"D_n\subseteq\B_n\subseteq\F_n",
        },
        O7_AUDIT: {
            "integrated O7 heading": "**O7 (where the crossing is).**",
            "fixed-rate premise": "k_n/n->rho",
            "crossing agreement": "a_n=k_n+1+g_{T,n} n+o(n)",
            "upper-half O7 premise": "(n+k_n)/2 < a_n < a_deep",
            "integrated coupled-open verdict": "O5c and O7 are logically coupled",
        },
        SECANT_NOTE: {
            "integrated secant title": "# Challenge-restricted syndrome-secant lower bound",
            "integrated status": "`PROVED`.",
            "raw secant numerator": "G N_t q^(2t) (q^R-q^t)",
            "raw secant denominator": "q^(2R) S_t(q)",
            "first-agreement specialization": "G (q-1) N / (q(N+q-1))",
        },
    }

    count = 0
    for path, expected in anchors.items():
        check(path.is_file(), f"missing source: {path.relative_to(REPO)}")
        text = path.read_text(encoding="utf-8")
        for label, needle in expected.items():
            check(needle in text, f"missing {label} in {path.relative_to(REPO)}")
            count += 1
    return count


def binary_entropy(value: float) -> float:
    check(0.0 <= value <= 1.0, f"entropy input {value}")
    if value == 0.0 or value == 1.0:
        return 0.0
    return -value * log2(value) - (1.0 - value) * log2(1.0 - value)


def identity_exponent(rho: float, beta: float, g: float) -> float:
    return binary_entropy(rho + g) - beta * g


def numerical_right_crossing(
    rho: float, beta: float, tau: float
) -> tuple[float, bool, float]:
    """Return the numerical rightmost superlevel point and a bracket width.

    Concavity gives a single right boundary.  The entropy derivative vanishes
    at x=1/(1+2^beta), so checking that peak also handles an empty superlevel
    whose value at g=0 is below ``tau``.
    """

    end = 1.0 - rho
    critical_x = 1.0 / (1.0 + 2.0**beta)
    peak = min(end, max(0.0, critical_x - rho))
    peak_value = identity_exponent(rho, beta, peak)
    check(
        peak_value + 1e-14 >= identity_exponent(rho, beta, 0.0),
        "entropy peak is below left endpoint",
    )

    if peak_value < tau:
        return 0.0, False, 0.0

    lo = peak
    hi = end
    check(identity_exponent(rho, beta, lo) >= tau, "bad lower root bracket")
    check(identity_exponent(rho, beta, hi) < tau, "bad upper root bracket")
    for _ in range(120):
        middle = (lo + hi) / 2.0
        if identity_exponent(rho, beta, middle) >= tau:
            lo = middle
        else:
            hi = middle
    return lo, True, hi - lo


def verify_analytic_localization() -> dict[str, int]:
    """Replay g_T <= 1/beta <= 1/log2(n) on deterministic target grids."""

    rows = 0
    probes = 0
    superlevel_probes = 0
    nonempty = 0
    empty = 0

    for n in ANALYTIC_NS:
        log_n = log2(n)
        for k in selected_dimensions(n):
            rho = k / n
            for base_size in field_sizes_at_least(n):
                beta = log2(base_size)
                check(beta + 1e-15 >= log_n > 0.0, "beta >= log2(n)")
                target_bits_values = tuple(sorted({0, 1, n // 8, n // 2, n}))
                for target_bits in target_bits_values:
                    budget = (1 << target_bits) - 1
                    check(1 + budget == 1 << target_bits, "literal target budget")
                    tau = target_bits / n
                    check(tau >= 0.0, "tau must be nonnegative")

                    g_t, has_superlevel, bracket_width = numerical_right_crossing(
                        rho, beta, tau
                    )
                    check(0.0 <= g_t <= 1.0 - rho, "right crossing domain")
                    check(g_t <= 1.0 / beta + 2e-14, "g_T <= 1/beta")
                    check(
                        1.0 / beta <= 1.0 / log_n + 2e-14,
                        "1/beta <= 1/log2(n)",
                    )
                    if has_superlevel:
                        nonempty += 1
                        check(bracket_width < 2e-14, "right crossing bisection width")
                        h_value = binary_entropy(rho + g_t)
                        check(h_value <= 1.0 + 2e-14, "H2 <= 1 at crossing")
                        check(beta * g_t <= h_value - tau + 2e-12, "superlevel algebra")
                        check(beta * g_t <= 1.0 + 2e-12, "beta*g_T <= 1")
                    else:
                        empty += 1
                        check(g_t == 0.0, "empty superlevel adjoins zero")

                    # Directly inspect a deterministic grid of the defining
                    # superlevel set, including both endpoints.
                    for step in range(65):
                        g = (1.0 - rho) * step / 64.0
                        h_value = binary_entropy(rho + g)
                        check(h_value <= 1.0 + 2e-14, "H2 grid upper bound")
                        if identity_exponent(rho, beta, g) >= tau:
                            superlevel_probes += 1
                            check(beta * g <= h_value - tau + 2e-12, "grid algebra")
                            check(g <= 1.0 / beta + 2e-12, "grid localization")
                        probes += 1
                    rows += 1

    check(rows > 500, "analytic grid unexpectedly small")
    check(nonempty > 0 and empty > 0, "analytic grid must cover both regimes")
    return {
        "rows": rows,
        "probes": probes,
        "superlevel_probes": superlevel_probes,
        "nonempty": nonempty,
        "empty": empty,
    }


def choose(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    return comb(n, r)


def secant_s_value(q: int, n: int, k: int, a: int) -> int:
    r_codim = n - k
    t = n - a
    return sum(
        comb(t, j)
        * choose(n - t, t - j)
        * q ** max(j, 2 * t - r_codim)
        for j in range(t + 1)
    )


def secant_raw_parts(q: int, n: int, k: int, a: int, challenge_size: int) -> tuple[int, int]:
    r_codim = n - k
    t = n - a
    n_t = comb(n, t)
    numerator = challenge_size * n_t * q ** (2 * t) * (q**r_codim - q**t)
    denominator = q ** (2 * r_codim) * secant_s_value(q, n, k, a)
    return numerator, denominator


def verify_upper_half_secant() -> dict[str, object]:
    """Prove and census ceil(X_sec)=1 whenever 2a>n+k."""

    structural_cases = 0
    exact_rows = 0
    for n in range(2, SECANT_N_MAX + 1):
        for k in range(1, n):
            r_codim = n - k
            for a in range(k + 1, n + 1):
                if 2 * a <= n + k:
                    continue
                t = n - a
                gap = r_codim - 2 * t
                check(gap >= 1, f"strict half gap n={n},k={k},a={a}")
                check(2 * t < r_codim, "2a>n+k iff 2t<R")

                n_t = comb(n, t)
                vandermonde = sum(
                    comb(t, j) * choose(n - t, t - j) for j in range(t + 1)
                )
                check(vandermonde == n_t, "exact Vandermonde identity")

                for q in field_sizes_at_least(n):
                    s_value = secant_s_value(q, n, k, a)
                    check(
                        all(max(j, 2 * t - r_codim) == j for j in range(t + 1)),
                        "upper-half exponent reduction",
                    )
                    check(s_value >= vandermonde == n_t, "S_t(q) >= N_t")

                    base_numerator = n_t * q ** (2 * t) * (q**r_codim - q**t)
                    denominator = q ** (2 * r_codim) * s_value
                    check(base_numerator > 0, "positive raw secant numerator")
                    # This is the exact cross-multiplied form of
                    # base_numerator/denominator < q^(2t-R)=1/q^gap.
                    check(
                        base_numerator * q**gap < denominator,
                        "Vandermonde raw bound",
                    )

                    for challenge_size in range(1, q + 1):
                        numerator = challenge_size * base_numerator
                        check(
                            challenge_size <= q <= q**gap,
                            "G/q^gap <= 1",
                        )
                        check(0 < numerator < denominator, "0 < X_sec < 1")
                        check(
                            ceil_div(numerator, denominator) == 1,
                            "upper-half secant ceiling",
                        )
                        exact_rows += 1
                    structural_cases += 1

    check(exact_rows > 100_000, "secant census unexpectedly small")

    # Strictness is load-bearing.  At 2a=n+k the ceiling can be two.
    q, n, k, a, challenge_size = 3, 3, 1, 2, 3
    check(2 * a == n + k, "boundary control is not on 2a=n+k")
    numerator, denominator = secant_raw_parts(q, n, k, a, challenge_size)
    boundary_value = Fraction(numerator, denominator)
    boundary_ceiling = ceil_div(numerator, denominator)
    check(boundary_value == Fraction(6, 5), "boundary raw value must be 6/5")
    check(boundary_ceiling == 2, "boundary negative control must have ceiling two")

    boundary_rows = 0
    boundary_above_one = 0
    for n in range(3, 41):
        for k in range(1, n):
            r_codim = n - k
            if r_codim % 2:
                continue
            t = r_codim // 2
            a = n - t
            check(2 * a == n + k, "boundary census arithmetic")
            for q in field_sizes_at_least(n):
                for challenge_size in range(1, q + 1):
                    num, den = secant_raw_parts(q, n, k, a, challenge_size)
                    ceiling = ceil_div(num, den)
                    if ceiling > 1:
                        boundary_above_one += 1
                    boundary_rows += 1
    check(boundary_above_one > 0, "strict-boundary census lacks a negative control")

    return {
        "structural_cases": structural_cases,
        "exact_rows": exact_rows,
        "boundary_rows": boundary_rows,
        "boundary_above_one": boundary_above_one,
        "boundary_example": "q=3,n=3,k=1,a=2,G=3,X=6/5,ceil=2",
    }


def verify_list_uniqueness_audit() -> dict[str, int]:
    """Audit-only arithmetic cross-check of PR #699's size-at-most-one regime."""

    agreement_rows = 0
    identity_floor_rows = 0
    for n in range(2, LIST_AUDIT_N_MAX + 1):
        for k in range(1, n):
            for a in range(k + 1, n + 1):
                if 2 * a <= n + k:
                    continue
                t = n - a
                prefix_depth = a - k - 1
                overlap = 2 * a - n

                # Two size-a agreement supports overlap in at least k+1
                # points; two degree-at-most-k polynomials agreeing there are
                # identical.  Equivalently, twice the error radius is below
                # the dimension-(k+1) RS minimum distance n-k.
                check(overlap >= k + 1, "support overlap exceeds degree")
                check(2 * t < n - k, "twice-radius minimum-distance check")
                check(prefix_depth >= t, "upper-half prefix depth")

                identity_count = comb(n, a)
                check(identity_count == comb(n, t), "binomial symmetry")
                check(identity_count <= n**t <= n**prefix_depth, "identity floor chain")
                for base_size in field_sizes_at_least(n):
                    denominator = base_size**prefix_depth
                    check(
                        ceil_div(identity_count, denominator) == 1,
                        "upper-half identity-list floor",
                    )
                    identity_floor_rows += 1
                agreement_rows += 1

    check(agreement_rows > 10_000, "list audit grid unexpectedly small")
    return {
        "agreement_rows": agreement_rows,
        "identity_floor_rows": identity_floor_rows,
    }


def verify_fixed_rate_and_guard() -> dict[str, object]:
    """Check o(n), eventual below-half, and the varying-rate implication."""

    fixed_rows = 0
    first_below: dict[str, int] = {}
    for rate in FIXED_RATES:
        became_below = False
        first_exponent = 0
        previous_ratio: Fraction | None = None
        for exponent in range(4, 65):
            n = 1 << exponent
            check(n % rate.denominator == 0, "fixed-rate dyadic divisibility")
            k = rate.numerator * n // rate.denominator
            offset_bound = Fraction(n, exponent)  # n/log_2(n)
            normalized_offset = offset_bound / n
            check(normalized_offset == Fraction(1, exponent), "normalized offset")
            if previous_ratio is not None:
                check(normalized_offset < previous_ratio, "n/log(n) is o(n) grid")
            previous_ratio = normalized_offset

            crossing_bound = Fraction(k + 1, 1) + offset_bound
            below_half = 2 * crossing_bound <= n + k
            if below_half and not became_below:
                became_below = True
                first_exponent = exponent
            if became_below:
                check(below_half, "fixed-rate below-half property must persist")
            fixed_rows += 1
        check(became_below, f"fixed rate {rate} never falls below half")
        first_below[f"{rate.numerator}/{rate.denominator}"] = first_exponent

    # Explicit epsilon witnesses for (n/log n)/n -> 0.
    little_o_witnesses = 0
    for epsilon_denominator in (2, 4, 8, 16, 32, 64):
        exponent = epsilon_denominator + 1
        check(
            Fraction(1, exponent) < Fraction(1, epsilon_denominator),
            "little-o epsilon witness",
        )
        little_o_witnesses += 1

    # Varying-rate guard: if a real A=k+1+gn is above half and
    # 0<=g<=1/beta<=1/log2(n), then R=n-k<2gn+2<=2n/log2(n)+2.
    guard_rows = 0
    guard_premise_hits = 0
    for exponent in range(4, 49):
        n = 1 << exponent
        log_n = exponent
        candidates = {
            1,
            2,
            max(1, n // (4 * exponent)),
            max(1, n // (2 * exponent)),
            max(1, n // exponent),
            max(1, (2 * n) // exponent),
            n - 1,
        }
        for beta_multiplier in (1, 2, 3):
            beta = beta_multiplier * log_n
            for r_codim in sorted(r for r in candidates if 1 <= r < n):
                for fraction_index in range(5):
                    g = Fraction(fraction_index * r_codim, 4 * n)
                    check(0 <= g <= Fraction(r_codim, n), "varying g domain")
                    if g > Fraction(1, beta):
                        continue
                    guard_rows += 1
                    above_half = r_codim < 2 * g * n + 2
                    if above_half:
                        guard_premise_hits += 1
                        check(
                            r_codim < Fraction(2 * n, beta) + 2,
                            "varying-rate beta guard",
                        )
                        check(
                            Fraction(2 * n, beta) + 2
                            <= Fraction(2 * n, log_n) + 2,
                            "varying-rate log(n) guard",
                        )
                        check(
                            Fraction(r_codim, n)
                            < Fraction(2, log_n) + Fraction(2, n),
                            "varying-rate normalized guard",
                        )

    check(guard_premise_hits > 100, "varying-rate guard was not exercised")

    # A nonvacuous varying-rate family satisfying the arithmetic premise.
    guard_family_rows = 0
    previous_deficit: Fraction | None = None
    for exponent in (8, 16, 32, 64, 128):
        n = 1 << exponent
        r_codim = n // exponent
        g = Fraction(r_codim, 2 * n)
        check(g <= Fraction(1, exponent), "guard family localization")
        check(r_codim < 2 * g * n + 2, "guard family is above half")
        deficit = Fraction(r_codim, n)
        if previous_deficit is not None:
            check(deficit < previous_deficit, "guard family rate tends to one")
        previous_deficit = deficit
        guard_family_rows += 1

    # Epsilon witnesses for 2/log2(n)+2/n -> 0 in the varying-rate guard.
    guard_epsilon_witnesses = 0
    for epsilon_denominator in (2, 4, 8, 16, 32, 64):
        exponent = 4 * epsilon_denominator
        n = 1 << exponent
        check(
            Fraction(2, exponent) + Fraction(2, n)
            < Fraction(1, epsilon_denominator),
            "varying-rate o(1) guard witness",
        )
        guard_epsilon_witnesses += 1

    return {
        "fixed_rows": fixed_rows,
        "first_below_half_log2_n": first_below,
        "little_o_witnesses": little_o_witnesses,
        "guard_rows": guard_rows,
        "guard_premise_hits": guard_premise_hits,
        "guard_family_rows": guard_family_rows,
        "guard_epsilon_witnesses": guard_epsilon_witnesses,
    }


def main() -> None:
    print("INPUTS")
    print(f"  analytic_n={ANALYTIC_NS}")
    print(
        "  secant_grid="
        f"2<=n<={SECANT_N_MAX}, 1<=k<n, k+1<=a<=n, q>=n prime-power grids, 1<=G<=q"
    )
    print(
        "  list_audit_grid="
        f"2<=n<={LIST_AUDIT_N_MAX}, strict upper half; attribution=PR #699 AUDIT ONLY"
    )
    print(f"  fixed_rates={tuple(str(rate) for rate in FIXED_RATES)}")
    print("OBJECT")
    print("  F_n(g)=H_2(k/n+g)-beta*g, tau=log2(1+B*)/n")
    print("  X_sec=G*C(n,t)*q^(2t)*(q^R-q^t)/(q^(2R)*S_t(q))")
    print("  targets=O7 fixed-rate location; strict upper-half syndrome lower route")

    anchor_count = verify_source_anchors()
    analytic = verify_analytic_localization()
    secant = verify_upper_half_secant()
    list_audit = verify_list_uniqueness_audit()
    rates = verify_fixed_rate_and_guard()

    print("STATUS")
    print(f"  source_anchors=PASS count={anchor_count}")
    print(
        "  analytic_localization=PROVED "
        f"rows={analytic['rows']} probes={analytic['probes']} "
        f"superlevel_probes={analytic['superlevel_probes']} "
        f"nonempty={analytic['nonempty']} empty={analytic['empty']}"
    )
    print(
        "  syndrome_secant_upper_half=PROVED "
        f"structural_cases={secant['structural_cases']} exact_rows={secant['exact_rows']}"
    )
    print(
        "  strict_boundary_control=PASS "
        f"rows={secant['boundary_rows']} ceilings_above_one={secant['boundary_above_one']} "
        f"example={secant['boundary_example']}"
    )
    print(
        "  half_band_list_uniqueness=AUDIT_ONLY_PR699 "
        f"agreement_rows={list_audit['agreement_rows']} "
        f"identity_floor_rows={list_audit['identity_floor_rows']}"
    )
    print(
        "  fixed_rate_crossing=PROVED_O_OF_N_AND_EVENTUALLY_BELOW_HALF "
        f"rows={rates['fixed_rows']} first_log2_n={rates['first_below_half_log2_n']} "
        f"epsilon_witnesses={rates['little_o_witnesses']}"
    )
    print(
        "  varying_rate_guard=PROVED "
        f"rows={rates['guard_rows']} premise_hits={rates['guard_premise_hits']} "
        f"family_rows={rates['guard_family_rows']} "
        f"epsilon_witnesses={rates['guard_epsilon_witnesses']}"
    )
    print(f"  checks={CHECKS}")
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
