# M31 deployed C1--C8 owner coverage and all-key C9 loss-one census

```yaml
workboard_item: M31_C9_GLOBAL_OWNER_COMPLEMENT_AND_KEY_COVERAGE / Lane A part 1
row: Mersenne-31 list auxiliary row
object: exact local Q-profile on eight deployed T_(2^21) roots
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: every key surviving the actual local C1--C8 first-match map has a singleton full-prefix fiber
architecture: frozen eight-root weight-four slice; order C1,C2,C3,C4,C5,C6,C7,C8
partition_digest: sha256:c6a154c32e8950762a992e8631bfa49e62762d43bf374cbf8674b5c417d3952e
atom_or_cell: post-C1--C8 C9 prefix keys
quantifier: all 70 weight-four supports and all 64 surviving realized keys
projection_and_unit: support-prefix fiber cardinality; no slope projection claimed
claimed_bound: 64/64 surviving keys have full fiber 1 <= 1*2
status: PROVED / CRITERION_2
impact: removes the one-key scope restriction of upstream PR #1027 on this exact deployed local profile
falsifier: any residual mask whose full first-three-power-sum fiber is not its singleton
replay: python3 experimental/scripts/verify_m31_c9_owner_coverage.py --check
```

## Result

On the eight actual Mersenne-31 roots

```text
434373082,  614288294, 1713110565, 1533195353,
1984437538, 380812851,  163046109, 1766670796
```

let `Omega` be the complete set of four-subsets.  For a support `S`, use the
first-three-power-sum key

\[
 \Phi(S)=\left(\sum_{x\in S}x,\sum_{x\in S}x^2,\sum_{x\in S}x^3\right)
 \in \mathbb F_p^3,\qquad p=2^{31}-1.
\]

The complete slice has `70` supports and `69` realized keys.  Its only
nonsingleton key is

```text
(0,2,0) -> masks [15,240].
```

The actual local first-match order is printed and frozen before inspection:

```text
C1 -> C2 -> C3 -> C4 -> C5 -> C6 -> C7 -> C8 -> residual C9.
```

The executable census assigns the six exact antipodal-quotient supports to C1
and leaves exactly `64` supports.  Every residual key is distinct, and every one
of those `64` keys is already singleton in the **full** seventy-support slice.
Hence deletion monotonicity is not needed to obtain the full-prefix bound:

```text
full fiber size = 1 <= compilerLoss * naturalScale = 1 * 2.
```

The image-normalized cleared inequality is simultaneously

```text
1 * 69 <= 70.
```

There is no counterexample key.  This satisfies acceptance criterion **2**:
it bounds genuine post-C1--C8 survivors and removes the predecessor's one-key
scope restriction on this exact profile.

## First-match owner function

The local raw predicates are mathematical tests on the frozen profile, not
generic case labels.

| case | local raw predicate | raw hits | first-match owners |
|---|---|---:|---:|
| C1 | union of two exact antipodal fibers for `x -> x^2` | 6 | 6 |
| C2 | one complete `T_4` fiber | 2 | 0 |
| C3 | nonempty active common core planted throughout the complete slice | 0 | 0 |
| C4 | repeated selected active root | 0 | 0 |
| C5 | nontrivial active extension degree | 0 | 0 |
| C6 | vanishing `3 x 3` Jacobian minor of the first-three-power-sum map | 0 | 0 |
| C7 | nonsingleton full prefix fiber (effective-image collapse) | 2 | 0 |
| C8 | nonsingleton prefix fiber after C1--C7 deletion | 0 | 0 |
| residual | no earlier owner | — | 64 |

The two C2 raw hits and the two C7 raw hits are exactly masks `15` and `240`.
Both are complete `T_4` blocks, both lie over `(0,2,0)`, and both are already
C1-owned.  This is a genuine first-match preemption, not double charging.

The exact C1-owned masks are

```text
15, 85, 90, 165, 170, 240.
```

They are the six choices of two among the four antipodal pairs

```text
(0,2), (1,3), (4,6), (5,7).
```

C3 is empty because the intersection of all seventy supports is empty.  C4 is
empty because the eight printed roots are distinct.  C5 is empty because the
active profile has extension degree one.  C6 is empty because for the first
three selected values `a,b,c`, the checked Jacobian minor is

\[
 6(b-a)(c-a)(c-b)\ne0\pmod p.
\]

After C1--C7 deletion, the residual prefix map is injective, so C8 is empty.

## Complete key certificate

The canonical JSON contains:

- one owner-decision row for every mask of weight four;
- all eight raw-trigger truth values for each support, encoded as a bit mask;
- its first-match owner and exact prefix key;
- one key-decision row for every residual support;
- the full and residual singleton fiber masks;
- the exact loss-one and image-normalized checks.

The partition digest is

```text
sha256:c6a154c32e8950762a992e8631bfa49e62762d43bf374cbf8674b5c417d3952e
```

and the certificate file digest before CI annotation is

```text
sha256:46713b57f47456fc7b07cf5d22a8ecd6e1ea8bade1b0484b96ae9fce699c3091
```

The verifier reconstructs the domain arithmetic, Chebyshev roots, antipodal
pairs, `T_4` values, all 70 supports, all owner predicates, the priority map,
all prefix fibers, and all 64 key decisions without trusting the printed
tables.  It also rejects four independent mutations.

## Deployed embedding and denominator discipline

The local profile is embedded into the current M31 list row with

```text
n = 2,097,152
m =   981,129
w =    67,447
B* = 16,777,215.
```

Fixing `m-4=981,125` outside complement points leaves `2,097,144` available
outside the eight active coordinates.  The local natural scale is
`ceil(70/69)=2`.  This prefix support scale is not identified with the line,
challenge, or list denominator.

## Source map

| packet object | active source node |
|---|---|
| complete fixed-weight slice and primitive residual | `experimental/grande_finale.tex`, `def:primitive-leaf` |
| realized image versus ambient scale | `eq:image-ambient-scales` |
| full-prefix maximum fiber | `def:primitive-q`, `def:q-row-atom` |
| exact deployed Q target | `prop:q-exact-target` |
| power sums versus locator coefficients | `lem:newton-equivalence` |
| support-to-slope separation | `(SE2)`, `hyp:ray-compiler`, `prop:q-sp-no-ray` |
| exact completion boundary | `thm:exact-completion-certificate` |
| deployed field and row constants | `tex/cs25_cap_v13_2.tex`; integrated `M31QRootedShell.Deployed` |

Grande Finale v4 is the active completion manuscript.  The C1--C9 labels above
are used only for the exact local first-match profile inherited from the
predecessor packet.

## Explicit nonclaims

This packet proves no fixed-outside profile multiplicity bound, no received-line
`SE2` construction, no Sidon or MI+MA theorem, no row-wide residual add-back or
UNIF, no list-interior or balanced-core payment, and no adjacent-row
certificate.  It changes the scope of the local C9 key theorem, not the
deployed row verdict.

## Replay

From the repository root:

```bash
python3 experimental/scripts/verify_m31_c9_owner_coverage.py --check
python3 -O experimental/scripts/verify_m31_c9_owner_coverage.py --check
python3 experimental/scripts/verify_m31_c9_owner_coverage.py --tamper-selftest
python3 -O experimental/scripts/verify_m31_c9_owner_coverage.py --tamper-selftest
```

All four commands pass on the packet.

**Terminal result:** `PROVED_CRITERION_2_ALL_KEY_LOSS_ONE`.
