#!/usr/bin/env python3
"""Exact standard-library replay for the rank-16 weighted-grid theorem.

The finite scan implements only integer formulas proved in the accompanying
argument:
  * exact endpoint row/column budgets;
  * balanced direction coloring, used only through e_j <= ceil(U/d);
  * the exact line-arrangement Tjurina ledger;
  * the characteristic-valid du Plessis--Wall upper bound;
  * the divisorial/extactic near-pencil incidence cap.

No third-party package, floating point operation, or randomized step is used.
"""

from bisect import bisect_right
from hashlib import sha256

P = 2_130_706_433
N = 1_053_693
A = 72_588
H = 5_116
U = 913_633
SELECTED = 156
C_MIN = 0
C_MAX = 553


def check(condition, message):
    if not condition:
        raise RuntimeError("CHECK FAILED: " + message)


def c2(x):
    return 0 if x < 2 else x * (x - 1) // 2


def row_bound(c):
    return (A - c) // (H - c) - 1


def dpw_upper(degree, rho):
    """Characteristic-valid corrected du Plessis--Wall upper bound."""
    value = (degree - 1) * (degree - rho - 1) + rho * rho
    alpha = 2 * rho + 1 - degree
    if alpha > 0:
        value -= c2(alpha + 1)
    return value


def balanced_marked_tjurina(total, vertices=SELECTED):
    """Minimum sum binom(k_i+1,2), k_i >= 0 integral, sum k_i=total."""
    q, rem = divmod(total, vertices)
    return (vertices - rem) * c2(q + 1) + rem * c2(q + 2)


# A table makes every inversion exact and fast.  The largest color has at most
# ceil(U/(H-C_MAX)) transverse lines.
MAX_COLOR_LINES = (U + (H - C_MAX) - 1) // (H - C_MAX)
MAX_TOTAL_INCIDENCE = SELECTED * MAX_COLOR_LINES
MARKED_FLOOR = [balanced_marked_tjurina(i) for i in range(MAX_TOTAL_INCIDENCE + 1)]


def largest_total_with_tjurina_budget(budget, transverse_lines):
    if budget < 0:
        return -1
    upper_index = SELECTED * transverse_lines + 1
    return bisect_right(MARKED_FLOOR, budget, 0, upper_index) - 1


def color_cap(transverse_lines, rows, columns, use_extactic=True):
    """Maximum marked transverse incidence allowed in one reduced color.

    Returns (cap, witness_tuple).  The witness tuple records the rho branch
    attaining the relaxation maximum; it is audit data, not an existence claim.
    """
    degree = transverse_lines + rows + columns + 1
    skeleton = c2(degree) + c2(rows) + c2(columns)
    line_occupancy_cap = min(rows, columns) * transverse_lines
    best = 0
    best_data = None

    for rho in range(degree):
        upper = dpw_upper(degree, rho)
        residual_budget = upper - skeleton
        incidence_cap = largest_total_with_tjurina_budget(
            residual_budget, transverse_lines
        )
        if incidence_cap < 0:
            continue
        incidence_cap = min(incidence_cap, line_occupancy_cap)
        branch = "DPW"
        pencil_cap = None

        if use_extactic and 3 * rho < degree:
            # After stripping h divisorial arrangement lines, the remaining
            # degree is degree-h and q=rho-h.  It has >3q invariant lines, so
            # the extactic lemma makes it a pencil.  A center on the fixed
            # endpoint line is impossible; an affine center forces deletion
            # of at least rows+columns-1 skeleton lines.
            check(
                degree - rho > max(rows + 1, columns + 1, 2),
                "fixed-line pencil-center exclusion",
            )
            if rho < rows + columns - 1:
                continue
            pencil_cap = (
                transverse_lines
                + 155
                + (min(rows, columns) - 1)
                * (rho - rows - columns + 1)
            )
            incidence_cap = min(incidence_cap, pencil_cap)
            branch = "PENCIL"

        if incidence_cap > best:
            best = incidence_cap
            best_data = (
                rho,
                branch,
                degree,
                upper,
                skeleton,
                residual_budget,
                largest_total_with_tjurina_budget(
                    residual_budget, transverse_lines
                ),
                pencil_cap,
            )

    return best, best_data


def uniform_color_cap(max_transverse_lines, rows, columns, use_extactic=True):
    """Maximum of color_cap(e,rows,columns) for every 0<=e<=E."""
    best = 0
    best_data = None
    for e in range(max_transverse_lines + 1):
        value, data = color_cap(e, rows, columns, use_extactic)
        if value > best:
            best = value
            best_data = (e, data)
    return best, best_data


def feasible_grid_sizes(row_ceiling):
    """All literal row/column counts that can contain 156 simple edges."""
    for rows in range(1, row_ceiling + 1):
        for columns in range(1, row_ceiling + 1):
            if SELECTED > rows * columns:
                continue
            if SELECTED > 14 * rows or SELECTED > 14 * columns:
                continue
            yield rows, columns


# Prior direction-pair relaxation, replayed only for the c=553/554 boundary.
def balanced_pair_sum(edges, parts):
    q, rem = divmod(edges, parts)
    return parts * c2(q) + rem * q


def full_direction_upgrades(q, full_bins, pair_budget):
    if full_bins == 0:
        return 0
    if pair_budget < 0:
        return -1
    layer = max(
        ell
        for ell in range(q)
        if full_bins * ell * (ell + 1) // 2 <= pair_budget
    )
    if layer == q - 1:
        return full_bins * (q - 1)
    spent = full_bins * layer * (layer + 1) // 2
    return full_bins * layer + min(
        full_bins, (pair_budget - spent) // (layer + 1)
    )


def direction_pair_capacity(d, universe, pair_budget, q):
    full, rem = divmod(universe, d)
    if rem == 0:
        return universe + d * full_direction_upgrades(q, full, pair_budget)
    best = -1
    for partial_h in range(1, q + 1):
        partial_cost = c2(partial_h)
        if partial_cost > pair_budget:
            continue
        upgrades = full_direction_upgrades(
            q, full, pair_budget - partial_cost
        )
        value = universe + rem * (partial_h - 1) + d * upgrades
        best = max(best, value)
    return best


def old_direction_boundary(c):
    d = H - c
    tail = 62_356 + c
    rows = row_bound(c)
    shared = 2 * balanced_pair_sum(SELECTED, rows)
    budget = c2(SELECTED) - shared
    need = SELECTED * tail
    cap = direction_pair_capacity(d, U, budget, rows)
    return need, cap, cap - need


# Small exhaustive regression for the convex marked-Tjurina floor.
def compositions(total, slots):
    if slots == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, slots - 1):
            yield (first,) + rest


for slots in range(1, 6):
    for total in range(0, 12):
        brute = min(
            sum(c2(k + 1) for k in vector)
            for vector in compositions(total, slots)
        )
        check(
            brute == balanced_marked_tjurina(total, slots),
            "balanced marked-Tjurina regression",
        )

check(U == N - (2 * A - H), "tail universe")
check(row_bound(0) == 13, "c=0 row bound")
check(row_bound(296) == 13, "c=296 row bound")
check(row_bound(297) == 14, "c=297 row jump")
check(row_bound(C_MAX) == 14, "c=553 row bound")
check(MAX_COLOR_LINES == 201, "maximum balanced color size")

# Precompute the tiny family of possible row/column profiles and every E<=201.
ALL_GRID_PAIRS = sorted(
    set(feasible_grid_sizes(13)) | set(feasible_grid_sizes(14))
)
COLOR_CACHE = {}
for rows, columns in ALL_GRID_PAIRS:
    running_cap = 0
    running_data = None
    for e in range(MAX_COLOR_LINES + 1):
        value, data = color_cap(e, rows, columns, True)
        if value > running_cap:
            running_cap = value
            running_data = (e, data)
        COLOR_CACHE[(e, rows, columns)] = (running_cap, running_data)

scan_rows = []
global_minimum = None
for c in range(C_MIN, C_MAX + 1):
    d = H - c
    tail = 62_356 + c
    row_ceiling = row_bound(c)
    max_color_lines = (U + d - 1) // d

    worst_cap = -1
    worst_profile = None
    for rows, columns in feasible_grid_sizes(row_ceiling):
        cap, data = COLOR_CACHE[(max_color_lines, rows, columns)]
        if cap > worst_cap:
            worst_cap = cap
            worst_profile = (rows, columns, data)

    required = SELECTED * tail
    total_cap = d * worst_cap
    margin = required - total_cap
    check(margin > 0, "uniform c=%d margin" % c)

    record = (
        c,
        d,
        tail,
        row_ceiling,
        max_color_lines,
        worst_cap,
        worst_profile,
        required,
        total_cap,
        margin,
    )
    scan_rows.append(record)
    if global_minimum is None or margin < global_minimum[-1]:
        global_minimum = record

# Exact replay points and inverse-convexity boundary checks.
check(global_minimum[0] == 12, "minimum-margin core")
check(global_minimum[-1] == 460_544, "minimum uniform margin")
check(global_minimum[5] == 1_816, "minimum-row color cap")
check(balanced_marked_tjurina(1_816) == 11_496, "c=12 lower ledger")
check(balanced_marked_tjurina(1_817) == 11_508, "c=12 next ledger")

c553 = scan_rows[553]
check(c553[5] == 2_029, "c=553 color cap")
check(c553[8] == 9_258_327, "c=553 total color cap")
check(c553[9] == 555_477, "c=553 new margin")
check(balanced_marked_tjurina(2_029) == 14_210, "c=553 lower ledger")
check(balanced_marked_tjurina(2_030) == 14_224, "c=553 next ledger")

# The adjacent frozen boundary, independently replayed.
old553 = old_direction_boundary(553)
old554 = old_direction_boundary(554)
check(old553 == (9_813_804, 9_814_582, 778), "old c=553 boundary")
check(old554 == (9_813_960, 9_813_232, -728), "old c=554 boundary")

# The new color argument also remains consistent on the adjacent c=554 row.
d554 = H - 554
tail554 = 62_356 + 554
E554 = (U + d554 - 1) // d554
worst554 = max(
    COLOR_CACHE[(E554, rows, columns)][0]
    for rows, columns in feasible_grid_sizes(row_bound(554))
)
new554 = (SELECTED * tail554, d554 * worst554)
check(new554 == (9_813_960, 9_256_298), "new c=554 consistency")

# Tamper test: deleting the extactic/divisorial forcing reopens c=553.
no_extactic_553, no_extactic_data = uniform_color_cap(201, 14, 14, False)
check(no_extactic_553 == 2_766, "no-extactic tamper cap")
check((H - 553) * no_extactic_553 >= SELECTED * (62_356 + 553),
      "extactic forcing is load-bearing")

# Hash the entire exact scan ledger, including the optimizing branch data.
ledger_text = "\n".join(repr(row) for row in scan_rows) + "\n"
ledger_hash = sha256(ledger_text.encode("ascii")).hexdigest()

print("RANK16_WEIGHTED_GRID_EXTACTIC_DPW: PASS")
print("field_p=%d selected=%d cores=%d..%d" % (P, SELECTED, C_MIN, C_MAX))
print("tail_universe=%d max_balanced_color_lines=%d" % (U, MAX_COLOR_LINES))
print("feasible_grid_pairs=%s" % (ALL_GRID_PAIRS,))
print(
    "uniform_min=c%d,d%d,b%d,R%d,E%d,color_cap%d,need%d,total_cap%d,margin%d"
    % (
        global_minimum[0],
        global_minimum[1],
        global_minimum[2],
        global_minimum[3],
        global_minimum[4],
        global_minimum[5],
        global_minimum[7],
        global_minimum[8],
        global_minimum[9],
    )
)
print("uniform_min_profile=%r" % (global_minimum[6],))
print(
    "c553_new=need%d,total_cap%d,margin%d,profile%r"
    % (c553[7], c553[8], c553[9], c553[6])
)
print(
    "c553_old=need%d,cap%d,cap_minus_need%d"
    % old553
)
print(
    "c554_old=need%d,cap%d,cap_minus_need%d"
    % old554
)
print(
    "c554_new_consistency=need%d,total_cap%d,margin%d"
    % (new554[0], new554[1], new554[0] - new554[1])
)
print(
    "tamper_without_extactic=c553_color_cap%d,total_cap%d,need%d,closure=false"
    % (
        no_extactic_553,
        (H - 553) * no_extactic_553,
        SELECTED * (62_356 + 553),
    )
)
print("scan_sha256=%s" % ledger_hash)
