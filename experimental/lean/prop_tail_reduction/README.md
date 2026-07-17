# prop_tail_reduction

Statement-level Lean layer for the (PROP-TAIL) discharge (stdlib-only, no
mathlib, no `sorry`): kernel-checks the claim's exact/finite arithmetic core
via `decide` on `Int`/`Nat`/`List` data — the polynomial identity behind
`theta~(t) <= 1/5`, its sign-corollary inequality, the window constant
`289/256 <= 57/50`, and two rational-data tables (the deep-grid
`rho_prop@i<17(j)` gate and the `V_17` vs. `tau*` crossover at `n=62`).

Transcription caveat: the two tables transcribe COMPUTED floating-point
values (printed decimals) to exact rationals at printed precision. The
kernel checks each table's internal consistency (threshold + strict
monotonicity) — not the correctness of the floating computation that
produced the decimals.

Out of scope, kept informal (all analytic content): the trig reduction
`theta~(t) = sqrt3 sin(2 pi t/3)/(6+3 cos(2 pi t/3))` and the substitution
`x = cos(2 pi t/3)`; the squaring step; `tau* = 3*log(1.02560749...)`
(transcendental); all contraction-rate / Birkhoff / CLT arguments.

Predecessor package (same conventions): `experimental/lean/inv_tail_closure/`.
Note: `experimental/notes/thresholds/dense_shell_inv_tail_closure.md` S7.
Verifier: `experimental/scripts/verify_dense_shell_inv_tail_closure.py`, V13.
