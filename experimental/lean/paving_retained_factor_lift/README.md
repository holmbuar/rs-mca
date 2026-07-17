# Paving v9.2 retained-factor-lift companion

This standalone Lean 4 package certifies the proved elementary kernels around
the RF3' content-root repair for
`experimental/RS_MCA_Paving_v9.2.tex`. It intentionally lives outside
`experimental/lean/grande_finale`: it accompanies the isolated conditional
appendix rather than the Grande Finale frontier library.

## Certified scope

- `ContentCharge.lean` proves over the reals
  `d + alpha*(D-d) <= max 1 alpha * D` for `0 <= d <= D` (in fact for every
  real `alpha`), together with the two coefficient branches, endpoint equalities,
  the additive allowance, and the RF3' specialization
  `alpha = 2 U D_Y^2`. It separately proves the weaker global-degree fallback
  `d + alpha*D <= (1+alpha)*D`; this fallback does not use the specialized
  content-free degree subtraction.
- `F7Threshold.lean` checks the exact rational counterexample arithmetic:
  the old threshold is `533/50000 < 1`, RF3' is `111/100 > 1`, and the
  unabsorbed charge at content degree one is `50503/50000 > 1`.
- `RF3DoublePrime.lean` checks the conservative RF3'' global-degree threshold
  at all four printed parameter rows. It proves the exact ceiling brackets for
  numerators `274589064742753629`, `274721012201293956`,
  `274578888391562205`, and `274861787390263486`, and proves each is at most
  the budget `274980728111395087`.
- `RF4ForcesVTwo.lean` defines both finite RF4 sums and proves, with the
  ceiling/degree hypotheses displayed, that strict RF4 forces `V >= 2`; it
  also records the translation `V = ceil(D_Y)`, `V >= 2` implies `D_Y > 1`.
- `Target.lean` records the unresolved retained-factor lift as a `Prop`
  interface. It is not an axiom: its sole consumer requires it explicitly as
  a hypothesis.

`CORRESPONDENCE.md` maps these declarations to the v9.2 labels and separates
Lean-certified arithmetic from the unresolved source audit.

## Build

```sh
cd experimental/lean/paving_retained_factor_lift
lake update
lake exe cache get
lake build
```

The package pins Lean/Mathlib `v4.28.0`, matching nearby Mathlib-based
standalone companions. No theorem contains `sorry`, `admit`, an axiom, or a
hidden factor-lifting proof.

## Nonclaims

This package does not formalize finite-field polynomials, content-free
factorization, regular specialization, Hensel lifting, BCIKS Claims
5.6--5.11/A.1--A.2, or BCHKS Section 3.2. In particular it does not
discharge `ass:retained-factor-lift`, prove the conditional retained-degree MCA
bound, or upgrade any KoalaBear row to unconditional status. Neither RF3' nor
the global-degree fallback is represented as discharging the retained lift.
