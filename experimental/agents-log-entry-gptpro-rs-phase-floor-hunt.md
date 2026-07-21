## 2026-07-21 — `gptpro/rs-phase-floor-hunt`

- **Workboard / gate:** T; criterion 4; `COUNTEREXAMPLE_NEW_FLOOR`.
- **Result:** the degree-one affine-basis RS trace-phase family has a split-balanced cyclotomic block with exact coherent signed mass `(H_(p,r)^2/p) binom(2r,r)`. For fixed odd `p`, exact image compensation still leaves `exp((log 2)N/p-O_p(log N))`; for fixed `r>=2` and growing odd `p`, the raw block cost is `exp(Omega_r(N log N))`.
- **Finite falsifier:** `p=3,r=5`: `M=L=155117520`, `A_eff=22876792454961`, coherent block mass `48105090057024>2A_eff`, source-payment floor `kappa>=310122`, and exact cross-histogram debt `-25228452719583`.
- **Route cut / next input:** kill `PHASE_HISTOGRAM_LOCAL_MI_MA`; require `ACTUAL_LEAF_CROSS_HISTOGRAM_CANCELLATION_OR_DIRECT_SIDON` on a genuine post-C1--C8 leaf.
- **Validation:** stdlib verifier exhausts the `p=3,r=2` phase/support regression; Lean 4.31.0 module has zero `sorry`, zero custom axioms, no repository imports; fork CI record is in the audit note.
