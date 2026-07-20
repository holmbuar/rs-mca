# Conjectures and Barriers for RS--MCA (V4.1)

This release contains the companion paper by Przemek Chojecki, together with
the exact finite-benchmark verification materials cited in the manuscript.

## Build

Run three LaTeX passes:

```sh
pdflatex Conjectures_and_Barriers_RS_MCA_v4_1.tex
pdflatex Conjectures_and_Barriers_RS_MCA_v4_1.tex
pdflatex Conjectures_and_Barriers_RS_MCA_v4_1.tex
```

The document uses `amsart`, A4 paper, and one-inch margins.

## Verification

Python 3.11 or later is recommended. The compact checker recomputes the four
budgets, unsafe and candidate lower values, margins, necessary moment orders,
extension headrooms, correction dimensions, and endpoint fractions:

```sh
python3 verify_profile_barriers.py
```

The release archive contains the compact checker at its root, the larger
repository audit at
`experimental/scripts/verify_frontier_adjacent_v13_rows.py`, and exactly four
input packets under
`experimental/data/certificates/frontier-adjacent/`. Run the larger audit with:

```sh
python3 experimental/scripts/verify_frontier_adjacent_v13_rows.py
```

Its G6 gate performs the 21-scale periodic lower-family audit at the historical
packet pairs. Its G7 gate separately checks the moved MCA identity pairs and
the named Mersenne--31 `Gceil`, `c=2048` watch item. It does not prove either
open adjacent safe inequality. The larger verifier and four packets are verbatim copies
from repository commit `e190193cebced1d3752d068a1c24136bc69a85d9`.

The asymptotic identity discussion in V4.1 uses the exact collision-aware pole
threshold and treats identity-candidate as a lower-side hypothesis and
identity-dominant as the conjectural conclusion. Neither checker proves the
conjectural profile closure or an unrestricted smooth/circle RS--MCA frontier.
