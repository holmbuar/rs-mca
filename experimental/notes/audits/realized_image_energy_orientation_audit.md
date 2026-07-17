# Realized-image entropy orientation audit

## Claim

This packet audits the complement-orbit step used to prove the entropy bounds
in `experimental/notes/thresholds/realized_image_energy_lift.md`.  It finds a
fixed-point obstruction to the original deterministic-selector wording and
repairs the proof by conditioning on explicit random orientation bits.

## Status

```text
implicit deterministic-balanced-selector subclaim: COUNTEREXAMPLE
original entropy proof step:                         FIXED
displayed inequalities (3) and (4):                 NO ISSUE after repair
hard input 2 (image-scale MI/MA or Sidon payment):  OPEN
```

The repair changes no theorem statement, exponent, or downstream constant.
It does not establish the signed multi-class inverse theorem, a major-arc
aggregate, or a complete direct Sidon payment.

## Exact failure mode

The cardinality-augmented image carries the complement involution

```text
J(u) = Phi_tilde(1)-u.
```

The old proof sentence paired every image point with its complement and then
used one representative selector both for coordinate balance and for
deterministic recovery.  This overlooks fixed points of `J`.

Take the exact fixture

```text
N = 2,
G = Z/2Z,
Phi = 0,
F = Omega_1 = {(1,0),(0,1)}.
```

The augmented image is

```text
S_tilde = {(0,0),(1,0),(2,0)},
```

and `(1,0)` is fixed by `J`.  Complement pairing forces the representatives
of `(0,0)` and `(2,0)`, while the fixed syndrome has exactly two choices:

| representative at `(1,0)` | coordinate-one totals over `S_tilde` | marginals |
|---|---:|---:|
| `(1,0)` | `(2,1)` | `(2/3,1/3)` |
| `(0,1)` | `(1,2)` | `(1/3,2/3)` |

Thus neither deterministic selector has coordinate marginals `1/2`.  The
deterministic-balanced-selector inference is false even in dimension two.
This counterexample attacks only that proof inference, not inequalities
(3)--(4).

## Repair

Put

```text
Phi_tilde(x) = (|x|,Phi(x)),
S_tilde = Phi_tilde({0,1}^N),
L_tilde = |S_tilde|.
```

Decompose `S_tilde` into two-cycles and fixed points under `J`.  Choose
complementary representatives on each two-cycle.  At every fixed point choose
one representative and let an independent fair bit reverse its orientation.
Write `O` for the collection of these bits and `tau_o` for the deterministic
selector after fixing `O=o`.  With `U` uniform on `S_tilde`, independent of
`O`, set `Y=tau_O(U)`.

The two-cycles balance coordinatewise, and averaging the fair orientation at
each fixed point balances its two complementary representatives.  Therefore
every coordinate of `Y` has marginal `1/2`.

For the one-copy bound, let `X` be uniform on the fixed augmented fiber `F`.
For each fixed `o`, the map

```text
(x,u) |-> x+tau_o(u)
```

is injective: applying `Phi_tilde` gives `s_tilde+u`, so the fixed fiber
syndrome `s_tilde` recovers `u`, then the chosen representative and `x`.

Because `(X,U)` is uniform on `F x S_tilde`, this injection gives

```text
H(X+Y | O) = log_2(f L_tilde).
```

Since conditioning cannot increase entropy and `L<=L_tilde`,

```text
log_2(fL) <= H(X+Y | O) <= H(X+Y).
```

Coordinate subadditivity and the marginal balance of `Y` then give (3).

For the two-copy bound put `A=X_1+X_2`.  Renyi monotonicity gives

```text
H(A) >= H_2^Renyi(A) = log_2(f^4/E(F)) = log_2(f/Delta(F)).
```

For each fixed `o`, the map `(a,u)|->a+tau_o(u)` is injective by the same
augmented-syndrome recovery.  Hence

```text
H(A+Y | O) = H(A)+log_2(L_tilde)
            >= log_2(f L_tilde/Delta(F)).
```

Conditioning, coordinate subadditivity, and concavity of the coordinate
entropy function `g` give (4).  Random balance and deterministic recovery are
therefore used in compatible places: balance after averaging `O`, recovery
after conditioning on `O`.

## Exact regression certificate

The verifier exhausts the dimension-two fixture and records:

```text
complement fixed points:             1
balanced deterministic selectors:   0 / 2
one-copy injection sizes:            6 / 6 for each orientation
two-copy injection sizes:            9 / 9 for each orientation
mixed coordinate totals:             (3,3) over 6 (orientation,syndrome) pairs
E(F):                                6
Delta(F):                            3/4
H(X_1+X_2):                          3/2 >= log_2(8/3)
```

All verifier gates use explicit fail-closed checks; Python optimization cannot
erase them.  Reproduce with

```bash
python3 experimental/scripts/verify_realized_image_energy_lift.py
python3 -O experimental/scripts/verify_realized_image_energy_lift.py
python3 experimental/scripts/verify_realized_image_energy_lift.py --tamper-selftest
python3 -O experimental/scripts/verify_realized_image_energy_lift.py --tamper-selftest
```

The theorem run reports `76,243` checks.  The tamper self-test rejects both
deterministic selectors.

## Ledger impact

This is an adversarial audit of the image-scale/Sidon lane, hard input 2 in
`agents.md`.  It closes one entropy-lift proof defect without paying the full
hard input.  The next useful attack is the transition from this single-fiber
lift to the signed multi-class amplification or the claimed major-arc routing;
neither is certified here.
