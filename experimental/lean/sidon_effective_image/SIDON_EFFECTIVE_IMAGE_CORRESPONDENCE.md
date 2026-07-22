# Sidon effective-image correspondence

**Package:** `experimental/lean/sidon_effective_image/`
**Lean:** `v4.31.0`, stdlib only
**Status:** `FINITE REGRESSION / COUNTEREXAMPLE_NEW_FLOOR / AWAITING_FORK_CI`

## Source theorem nodes

The research note
`experimental/notes/thresholds/sidon_effective_image_mi_ma_l1_floor.md`
attacks the claimed equivalence, not the validity, of the following sufficient
interfaces in `experimental/grande_finale.tex`:

- `eq:effective-fourier-span`;
- `lem:effective-span-fourier`;
- `def:effective-fourier-payment`;
- `def:aggregate-minor-payment`;
- `def:major-arc-aggregate`;
- `prop:effective-mi-ma-flatness`;
- `cor:exact-finite-fourier-constants`.

The direct comparison target is:

- `def:sidon-heavy`;
- `def:sidon-paid-cell`;
- `def:primitive-q`;
- `eq:image-ambient-scales`;
- `eq:full-image-certificate`.

## Declaration map

| Lean declaration | Mathematical content |
|---|---|
| `half_slice_shapes` | exact census of all 70 four-subsets of eight coordinates |
| `representative_shapes` | exact 35 representatives of complement-paired middle characters |
| `middle_walsh_magnitudes_exact` | every selected Krawtchouk coefficient has magnitude 6 |
| `middle_absolute_mass_exact` | selected middle-weight absolute mass is 210 |
| `effective_representative_shapes` | coordinate-zero gauge enumerates 128 classes, 127 nontrivial |
| `full_absolute_mass_exact` | complete nontrivial effective-dual mass is 490 |
| `singleton_fibers`, `max_fiber_exact` | realized-image fibers are singletons |
| `image_normalized_q_exact` | exact finite image-normalized Q equality `1 * 70 = 70` |
| `ambient_image_gap_polynomial` | finite full-image comparison `256 <= 9 * 70` |
| `effective_image_gap_polynomial` | finite effective-image comparison `128 <= 9 * 70` |
| `kappa_floor_of_middle_mass` | middle classes alone force `kappa >= 4` |
| `kappa_floor_of_full_mass` | the complete effective dual forces `kappa >= 8` |
| `kappa_seven_fails` | exact finite falsification of `kappa = 7` |
| `kappa_eight_exact_balance` | full mass exactly equals `(8-1)M` |
| `kappa_three_fails` | exact finite falsification of `kappa = 3` |

## Proof boundary

The Lean module certifies only the finite `N=8`, `m=4` arithmetic and executable
census.  It does not formalize:

- the general `N=4r` Krawtchouk identity;
- the exponential asymptotic floor;
- finite-field character theory;
- an RS Vandermonde or rational phase;
- C1--C8 semantic survival;
- Sidon-heavy moments as real-valued inequalities;
- a ray compiler or a distinct-slope numerator.

Those boundaries are explicit in the research note.  No local Lean build is to
be used; the fork draft-PR workflow is authoritative.

## Census

Intended source census before CI:

```text
sorry: 0
custom axioms: 0
Mathlib imports: 0
unsafe declarations: 0
```

Green CI will certify compilation only.  Statement correspondence must still be
audited against the note and the exact v3 labels above.
