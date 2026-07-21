# M31 rooted-shell lane: semantic C1--C8 owner-or-envelope interface

## Claim

Fix one executable ordered C1--C8 owner function **before** the received line is
chosen.  For one received line, one prefix target, one anchor, and one rooted
shell of semantic explanation states, the theorem target is

```text
q_prof^w * max(d_e(A)-3,0) <= 7 H_e
or
one shell explanation has a certified earlier paid slope owner.       (SO3+7)
```

The second branch is not a support label.  It carries the complete chain

```text
received line
  -> explanation state
  -> witness
  -> explaining codeword
  -> codeword ray
  -> distinct slope in a deduplicated line-local owner image.
```

For every owner profile the two denominators remain separate:

```text
natural prefix denominator = q_prof^w,
MCA slope denominator      = q_slope.
```

The exact owner numerator `U_owner` is required to satisfy

```text
# distinct owner slopes <= U_owner <= q_slope,
U_owner <= loss_owner * (1 + ceil(M_profile / q_prof^w)).
```

No equality between `q_prof^w` and `q_slope` is assumed.

The stdlib-only Lean module
`experimental/lean/m31_q_rooted_shell/M31QRootedShell/SemanticOwner.lean`
formalizes this statement, its actual-residual consequence, and the mandatory
`F_241` regression.  It imports PR #1005's rooted-shell arithmetic and does not
reprove the rooted-shell summation reduction or either support-only
counterexample.

## Status

```text
PROVED SEMANTIC INTERFACE AND COMPILERS
CONDITIONAL SEMANTIC SO3+7 INPUT
MANDATORY F_241 REGRESSION
OPEN DEPLOYED M31 RESIDUAL
```

The packet proves the exact logical and budget interfaces.  It does **not**
construct the deployed row's C1--C8 semantic triggers and does not prove
`(SO3+7)` for every actual Mersenne-31 shell.

## Exact objects

### Fixed-before-line owner function

`FixedOwnerFunction` contains eight Boolean trigger functions and the literal
nested first-match order

```text
C1 -> C2 -> C3 -> C4 -> C5 -> C6 -> C7 -> C8 -> residual.
```

The function is a field of the global `PaidOwnerLedger`; the received line is
an input contained in each explanation state, not an argument used to choose a
new owner function.

### Semantic chain

`SemanticChain` prints all maps and compatibility laws:

```text
lineOf          : explanation -> received line
witnessOf       : explanation -> witness
supportOfWitness: witness -> support
codewordOfWitness: witness -> explaining codeword
rayOfCodeword   : codeword -> ray
slopeOfRay      : ray -> slope
```

It also carries direct explanation projections and proves that they agree with
the displayed chain.  A positive owner classification must prove the
explanation satisfies the application-side validity predicate.

### Natural scale and exact slope budget

`NaturalProfileScale` records

```text
q_prof, w, M_profile, loss_owner,
```

with natural denominator `q_prof^w` and finite natural numerator

```text
loss_owner * (1 + ceil(M_profile / q_prof^w)).
```

`ExactSlopeBudget` separately records

```text
U_owner / q_slope,
```

including positivity of `q_slope` and `U_owner <= q_slope`.
`PaidSlopeProfile` carries a duplicate-free line-local slope list and proves
its cardinality is at most `U_owner`, which in turn is at most the natural
profile numerator.

### Rooted semantic shell

`RootedShell` contains valid explanation states on one received line.  Every
neighbor has the fixed prefix target and fixed exchange distance from the
anchor, and support projections are duplicate-free.  Thus
`neighbors.length` is the rooted degree `d_e(A)` without conflating support
multiplicity with explanation or slope multiplicity.

`IsActualPostC1C8Residual` states that the executable first-match projector
returns `none` on every neighbor.

## Proved compiler statements

### Actual residual consequence

`semantic_three_plus_seven_on_actual_residual` proves:

```text
IsActualPostC1C8Residual
and SemanticEnvelopeOrOwner(q_prof^w,3,7,H_e)
  ==> q_prof^w * max(d_e(A)-3,0) <= 7 H_e.
```

The proof is fail-closed.  On an actual residual, the certified-owner branch is
impossible because any owner certificate includes an equality
`classify explanation = some owner`.

### Violation-to-owner branch

`violation_forces_certified_earlier_owner` proves:

```text
SemanticEnvelopeOrOwner(Q,b,c,H_e)
and c H_e < Q * max(d_e(A)-b,0)
  ==> a concrete neighbor has an EarlierOwnerCertificate.
```

`EarlierOwnerCertificate.preserves_chain` exposes every arrow from witness to
distinct slope.  `EarlierOwnerCertificate.budget_chain` exposes the exact
slope numerator, the slope denominator ceiling, and the natural profile
payment.

These are line-local statements.  They do not replace
`sup_line sum_profile` by `sum_profile sup_line` and do not merge an earlier
owner numerator with the C9 prefix-support count.

## Mandatory `F_241` regression

The packet imports the exact multiplicative counterexample from PR #1005:

```text
field              F_241,
domain             <235> of order 20,
m                  10,
w                  2,
prefix target      (e1,e2)=(92,135),
Q                  241^2=58,081,
H_6                44,100,
rooted degree      10,
Q(10-3)-7H_6       97,867 > 0.
```

The existing packet also proves that the fifteen-member support proxy has
trivial dihedral stabilizers and empty common core.  Those facts remain route
cuts only.

The new theorem `f241_semantic_target_forces_certified_owner` proves:

> Any instance of `(SO3+7)` on the ten-neighbor `F_241` shell must return a
> certified earlier paid slope owner.

The theorem `f241_all_residual_rejects_semantic_target` proves:

> If every neighbor is declared post-C1--C8 residual, `(SO3+7)` is false on the
> packet.

Finally, `f241_owner_free_function_rejects_semantic_target` executes the fixed
all-false C1--C8 classifier and rejects it.  This is the formal regression
preventing support-only quotient/dihedral symmetry and planted-core pruning
from being accepted as semantic ownership.

## Existing proof authority

This packet depends on:

- `experimental/grande_finale.tex`, especially the row-sharp-Q atom, semantic
  first-match ledger, natural profile scales, and exact completion grammar;
- `experimental/notes/thresholds/m31_q_rooted_shell_envelope.md`, the proved
  rooted-shell compiler and exact deployed arithmetic from PR #1005;
- `experimental/notes/thresholds/m31_q_three_plus_seven_multiplicative_counterexample.md`,
  the mandatory `F_241` support-only route cut from PR #1005;
- the active exact-prefix-ray chain, used here only as the type discipline that
  a support/explaining codeword must reach an actual distinct slope.

## Ledger impact

The next C9 theorem can no longer use an untyped phrase such as “routes to C1”
or “has quotient symmetry.”  A positive branch must construct
`EarlierOwnerCertificate`, hence:

1. select the fixed C1--C8 first match;
2. prove the explanation state is valid for its received line;
3. preserve witness, codeword, ray, and slope;
4. place the slope in a deduplicated line-local owner image;
5. print `U_owner/q_slope`; and
6. compare `U_owner` with the owner's own `q_prof^w` natural scale.

The actual C9 residual is then the executable `none` fiber of that same owner
function.  On this fiber the only remaining branch of `(SO3+7)` is the local
`3+7` inequality.

## Validation

The package is stdlib-only on Lean `v4.31.0`.  It must be built only by the
fork draft-PR GitHub Actions workflow.  No local Lean build is part of this
packet.  The source-to-Lean audit is
`experimental/lean/m31_q_rooted_shell/SEMANTIC_OWNER_CORRESPONDENCE.md`.

## Nonclaims

This packet does not prove:

- the deployed Mersenne-31 C1--C8 owner function;
- `(SO3+7)` on every actual deployed residual shell;
- row-sharp Q or an adjacent safe list/MCA row;
- a complete first-match atlas or summed exact-completion ledger;
- that any displayed `F_241` support is an actual RS explanation on a received
  line;
- that support-level quotient/dihedral symmetry or planted-core pruning is a
  semantic owner.

## Next mathematical step

Instantiate one row-uniform `PaidOwnerLedger` from the active C1--C8 theorem
producers.  Every positive trigger must carry its exact line-local slope budget.
Then prove `(SO3+7)` for every semantic rooted shell.  The `F_241` packet must
either receive a genuine earlier owner under that instantiation or remain a
rejected nonsemantic support packet; it may not be silently deleted by a
support-only rule.
