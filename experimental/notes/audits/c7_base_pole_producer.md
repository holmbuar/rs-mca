# C7 base-pole producer

**Status:** `PROVED LOCAL / CONDITIONAL GLOBAL USE / AUDIT`

**Lean modules:**

- `AsymptoticSpine.C7BasePoleProducer`
- `AsymptoticSpine.C7BasePoleWitnessProducer`

**Source theorem:**
`experimental/notes/thresholds/aperiodic_one_ray_saturation.md`

## Scope

For one received base-pole line and one fixed prefix value, the source theorem
partitions exact-agreement witnesses by locator constant coefficient

```text
C_d = {S in Fib_w(z) : c_m(S) = d}.
```

Every nonempty cell has final slope image `{-d}`, and at most `q - 1` such
coefficients are realized. Given a supplied earlier-owner slope image `E`, the
C7 first-match slope image is therefore

```text
Z_C7 = {-d : C_d is nonempty} \ E.
```

The Lean packet formalizes this deletion-aware finite interface and pays one
unit for each surviving singleton slope. It deliberately does not duplicate
the uniform closed-ledger interface in PR #987.

## Exact PROVED statements

`C7BasePoleProducer.lean` proves:

- membership in `basePoleC7AssignedSlopes earlier raw` is exactly membership in
  `raw` together with exclusion from `earlier`;
- deletion preserves `Nodup`;
- the second ordered first-match leaf of `[earlier, raw]` is exactly the
  post-deletion C7 list;
- singleton C7 cells flatten exactly to the surviving slope list;
- `basePoleC7DirectBudget` equals the number of surviving slopes;
- the direct budget is at most the raw slope census and hence at most any
  supplied `qMinusOne` bound;
- finite fixtures for partial deletion and complete earlier-owner absorption.

`C7BasePoleWitnessProducer.lean` proves:

- realized constant-coefficient fibres are duplicate-free and
  witness-exhaustive;
- every witness in one coefficient fibre has the prescribed single final
  slope;
- the constructed raw slope list is exactly the witness slope image;
- injectivity of the coefficient-to-slope law makes that list duplicate-free;
- every assigned post-deletion C7 slope is rooted in an actual witness and is
  excluded from the supplied earlier slope image;
- the rooted direct budget is at most the source-side `q - 1` census;
- an executable four-witness fixture leaves exactly two slopes after deletion.

## Semantic ownership boundary

The packet proves payment only after an earlier-owner slope list is supplied.
It does **not** prove that C7 is nonempty independently of the global semantic
atlas. A raw one-slope collapse may be wholly absorbed by an earlier owner; the
`basePoleC7_absorbed_fixture` records this boundary directly.

## Proof and CI census

Fork validation PR `holmbuar/rs-mca#41`, head
`f12220c3a1a8b122a2472a1f1cab606464468e29`:

- complete `experimental/lean/asymptotic_spine` build: **PASS, 29 jobs**
- `sorry` / `sorryAx`: **0**
- `axiom` declarations introduced by this packet: **0**
- custom axioms: **none**
- Mathlib imports: **none**
- printed packet dependencies: only Lean foundations `propext` and
  `Quot.sound` (some individual statements use only `propext`)

A green build establishes compilation only. The source-to-Lean audit above
checks that the finite structure fields correspond to the source witness
catalogue, constant coefficient, exact slope law, injectivity of negation, and
`q - 1` realized-coefficient bound; the finite-field algebra itself remains in
the proved source theorem rather than being reproved here.

## Conditional / open

The following remain conditional or absent:

- construction and certification of the earlier semantic owner image;
- a fixed-before-line exhaustive C1--C9 atlas;
- nonempty C7 survival on every received line;
- row-wide `sup_line sum_profile` uniformity;
- residual-to-full comparison, C8 ray compilation, and C9 Sidon/MI--MA;
- envelope-to-target comparison and row closure.

No Python verifier is included: the Lean executable fixtures and package CI are
the lightweight replay for this narrow packet.
