# `lem:phi-fiber`(ii) repair certificate

## Status and scope

**COUNTEREXAMPLE / PROVED / AUDIT.  Final-tree replay recorded below.**

This isolated Mathlib package certifies two narrowly scoped facts about Paper
D v13.2's map-smooth fiber lemma:

1. the exact pre-repair Lean skeleton signature is false, by a symbolic
   `GF(16)/GF(4)` counterexample; and
2. the repaired imported theorem follows from the paper's coefficient-level
   premise when the folding polynomial is supplied as `φB : Polynomial B`.

The defect was in the old Lean skeleton, not in the paper.  The paper states
`φ ∈ B[X]` in `def:map-smooth`; the old skeleton weakened this to an arbitrary
`φ : Polynomial F` without requiring even its values on the domain to lie in
`B`.  The repaired imported theorem adds the minimal value-level premise

```lean
hQB : ∀ i, φ.eval (dom i) ∈ B
```

and the wrapper in this package derives `hQB` from `φB : Polynomial B`.

The Lean declarations are the kernel-facing part of the packet.  The
paper/statement correspondence and Git/SHA-256 pins below are source-audit
facts.  The recorded replay results distinguish the packet's two clean
principal axiom reports from an unrelated pre-existing placeholder elsewhere
in the imported `Fiber.lean` module.

## Counterexample to the exact old signature

The counterexample is symbolic rather than an enumeration:

```text
F = GF(16)
B = the embedded GF(4) subfield of F
ι = GF(4), with dom the embedding ι -> F
a = 1, N = 4, k = 1, ell2 = 3, A2 = 3
t in F outside B
phi = X + t
```

The map `phi` is degree one and has singleton fibers on the four-point domain,
so the old degree and map-smoothness premises hold.  In particular, this is not
a counterexample obtained by violating `hphi : phi.natDegree = a`.

For each `z ∈ B`, the old conclusion uses the received word

```text
u_z(x) = (x + t)^3 + z (x + t)^2.
```

Because `choose(4,3) / |B| = 1`, the conclusion requires at least one
degree-`< 2` codeword agreeing with `u_z` on at least three of the four domain
points.  The certificate proves that every such codeword has at most two
agreements.  If a degree-`< 2` polynomial `Q` agreed at three distinct points
of `B`, then

```text
(X + t)^3 + z (X + t)^2 - Q
```

would be a monic cubic with three roots in `B`.  Its `X^2` coefficient would
therefore lie in `B`, but direct symbolic expansion makes that coefficient
`t + z`, which is outside `B`.  This is the contradiction.

The exact old proposition is named
`RSCap.LemPhiFiberIIPreRepair`.  Its kernel negation is

```lean
RSCap.lem_phi_fiber_ii_pre_repair_false :
  ¬ RSCap.LemPhiFiberIIPreRepair.{0, 0}
```

The universe-zero instance is enough to refute the old universe-polymorphic
theorem declaration: such a declaration would specialize to universe zero,
where the certified `GF(16)/GF(4)` instance contradicts it.

This also shows why `hQB` is independently necessary for the repaired value-
level interface.  The counterexample satisfies the degree, domain, cardinality,
and smoothness hypotheses; it fails precisely the missing base-field tie,
since `phi(dom i) = dom i + t` lies outside `B`.

## Paper-faithful repair

The wrapper

```lean
RSCap.lem_phi_fiber_ii_of_basePolynomial
```

takes `φB : Polynomial B`, maps its coefficients into `F`, proves that
evaluation at each `B`-valued domain point remains in `B`, and invokes the
repaired `RSCap.lem_phi_fiber_ii`.  Thus the wrapper discharges the repaired
value-level premise from the coefficient-level premise actually printed in
Paper D v13.2; it does not add a new mathematical assumption to the paper
theorem.

## Statement map

| Source or obligation | Lean declaration | Classification | Scope |
|---|---|---|---|
| Old universe-polymorphic skeleton signature for `lem:phi-fiber`(ii) | `RSCap.LemPhiFiberIIPreRepair` | exact proposition mirror | Preserves the old binders and omits `hQB`, exactly as the old skeleton did. |
| Falsity of the old signature | `RSCap.lem_phi_fiber_ii_pre_repair_false : ¬ LemPhiFiberIIPreRepair.{0,0}` | kernel theorem | One universe-zero instance refutes the universe-polymorphic declaration. |
| Symbolic obstruction over `GF(16)/GF(4)` | `RSCap.PhiFiberRepair.at_most_two_agreements` and supporting cubic lemmas | kernel theorems | Proves at most two agreements for every `z ∈ B` and every degree-`< 2` polynomial. |
| Concrete parameters `a=1, N=4, k=1, ell2=3, A2=3` | `RSCap.PhiFiberRepair.concrete_old_hypotheses` and `old_phi_fiber_conclusion_false` | kernel theorems | Verifies the old premises and contradicts its required three-agreement conclusion. |
| Failure of the repaired value-level premise | `RSCap.PhiFiberRepair.phi_eval_not_mem_B4` | kernel theorem | Proves `phi(dom i) ∉ B` for every domain point, isolating the omitted base-field tie. |
| Repaired value-level fiber theorem | imported `RSCap.lem_phi_fiber_ii` | kernel theorem in the pinned repaired `Fiber.lean` | Adds `hQB`; this package does not re-prove its internal locator argument. |
| Paper premise `phi ∈ B[X]` from `def:map-smooth`, used in `lem:phi-fiber`(ii) | `RSCap.lem_phi_fiber_ii_of_basePolynomial` | kernel theorem and statement bridge | Maps `Polynomial B` into `Polynomial F`, derives `hQB`, and applies the repaired theorem. |

## Immutable source pins

The current source base is commit
`4bea7abb2d9455583c8864b980e39d11d550f51d`.  The paper correspondence is
pinned by the labels `def:map-smooth` and `lem:phi-fiber` in
`tex/cs25_cap_v13_2.tex`, not by drift-prone line numbers.

| Artifact | Git blob | SHA-256 of raw blob bytes |
|---|---|---|
| Pre-repair `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` | `d00a46604a3c1e8fddeb466c4370b4f7faa2afdc` | `9172f177bcd2b58b80bcda06a0b1fe8e41357e6331cd8cffce9ffba8a5152368` |
| Repaired `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at the current source base | `119d55c6ce1924d729594e64f92dc02b8e31aa17` | `efa03a962901f163206802c5241f1a9278ac574e528add7efe6cf56b47e0ab46` |
| `tex/cs25_cap_v13_2.tex` at the current source base | `5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb` | `356f1ad4b972746b664260191387b25a89a2e10fcc61962a49dc8282412f93ce` |

The repaired Fiber and active Paper D v13.2 blobs are selected by the printed
paths at the current source-base commit.  The pre-repair Fiber is pinned
directly by its blob object so the exact refuted signature remains auditable
even after repair.

## Replay commands

From the repository root:

```bash
cd experimental/lean/cs25_phi_fiber_repair_certificate
lake build
lake env lean Cs25PhiFiberRepairCertificate.lean
```

Then, again from the repository root:

```bash
python3 experimental/scripts/verify_phi_fiber_repair_certificate.py
```

The verifier is the fail-closed source/provenance check for the exact
declarations, source labels, Git blobs, and raw SHA-256 values in this packet.

Recorded 2026-07-19 replay:

- `lake build` completed successfully with 8033 jobs.  The imported
  `cs25_cap_v12.Fiber` replay printed its pre-existing warning for the unrelated
  `lem_fiber_ii` placeholder; the new packet module built successfully.
- `lake env lean Cs25PhiFiberRepairCertificate.lean` exited zero.
- Both principal axiom reports contain exactly `propext`, `Classical.choice`,
  and `Quot.sound`, with no `sorryAx`.
- The verifier returned `RESULT: PASS (43/43)`; its self-test caught
  `13/13` protected-artifact mutations and returned the same `43/43` pass.

## Nonclaims

This packet does **not** claim:

- a proof of `lem_fiber_ii`;
- a proof of the general map-smooth cap theorem;
- a general-`K` decorated-charge theorem;
- a defect in Paper D v13.2's `def:map-smooth` or `lem:phi-fiber`;
- any result beyond the exact old-signature counterexample and the
  coefficient-to-value repair wrapper described above.
