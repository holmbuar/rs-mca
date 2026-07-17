# Correspondence map — Paving v9.2 retained-factor lift

Source: `experimental/RS_MCA_Paving_v9.2.tex`, Appendix
`app:retained-interpolation`.

| v9.2 claim or ledger step | Lean declaration | Status |
| --- | --- | --- |
| Candidate content-plus-factor ledger `d_C + alpha (D_Z-d_C)`, with `alpha = 2 U D_Y^2`; the source audit does not establish the `D_Z-d_C` subtraction. | `ContentCharge.contentCharge`; `ContentCharge.rf3Prime_content_envelope` | Lean certifies only the real arithmetic conditional on this candidate ledger. |
| Candidate RF3' arithmetic envelope conditional on the degree-subtraction ledger: `max(1, 2 U D_Y^2) D_Z + (r+1)D_Y`. | `ContentCharge.contentCharge_le_max`; `ContentCharge.contentCharge_add_le_max_add` | Lean-certified real inequality conditional on the candidate ledger. |
| If `2 U D_Y^2 >= 1`, RF3' reduces to the coefficient printed in v9.2 RF3. | `ContentCharge.rf3Prime_reduces_to_old_of_guard` | Lean-certified equality. |
| The continuous envelope is governed by `D_Z` when `alpha <= 1` and by `alpha D_Z` when `alpha >= 1`. | `ContentCharge.contentCharge_case_split`; the two branch theorems; `ContentCharge.contentCharge_endpoints` | Lean-certified case split and endpoint equalities. |
| Global-degree fallback when no content-free subtraction is available: `d_C + alpha D_Z <= (1+alpha)D_Z`. | `ContentCharge.globalDegreeFallback` | Lean-certified real inequality; weaker than RF3' and independent of the unresolved lift. |
| RF3'' exact global-degree ceilings for the four printed rows are `274589064742753629`, `274721012201293956`, `274578888391562205`, and `274861787390263486`; each is at most `274980728111395087`. | `RF3DoublePrime.half_exact_ceiling`; `quarter_exact_ceiling`; `eighth_exact_ceiling`; `sixteenth_exact_ceiling`; `all_numerators_le_securityBudget` | Lean-certified exact rational arithmetic for the conservative fallback only; the retained lift remains unresolved. |
| Exact F7 witness: old RF3 RHS `533/50000 < 1`. | `F7Threshold.oldThreshold_eq`; `F7Threshold.oldThreshold_lt_singleton` | Lean-certified rational arithmetic. |
| Corrected RF3' RHS `111/100 > 1`; exact unabsorbed `d_C=1` charge `50503/50000 > 1`. | `F7Threshold.correctedThreshold_eq`; `F7Threshold.singleton_lt_correctedThreshold`; `F7Threshold.exactContentCharge_eq`; `F7Threshold.singleton_lt_exactContentCharge` | Lean-certified rational arithmetic. |
| Equation RF4, together with `U=ceil(D_X)`, `D_X<mA`, `A<=n`, `0<m`, and `m<=V`, rules out `V=1`. | `RF4ForcesVTwo.rf4Left`; `RF4ForcesVTwo.rf4Right`; `RF4ForcesVTwo.rf4_forces_V_ge_two` | Lean-certified natural/real arithmetic. The extra RF1 ordering/rank hypotheses are displayed in the theorem statement. |
| `V=ceil(D_Y)` and `V>=2` imply `D_Y>1`. | `RF4ForcesVTwo.DY_gt_one_of_V_ge_two` | Lean-certified ceiling consequence. |
| `ass:retained-factor-lift`: RF1--RF3' plus the polynomial/root/support data imply simultaneous explanation on a chosen support. | `Target.RetainedFactorLiftInterface`; `Target.RetainedFactorLiftTarget` | **Typed target only; unresolved and not asserted.** |
| Conditional use of the retained factor lift. | `Target.useRetainedFactorLiftTarget` | Lean-certified implication only after the target is supplied as a hypothesis. |

## Audit boundary

The package certifies the content-envelope repair, exact counterexample
arithmetic, and the RF4 nonimpact result. It does not source-verify or formalize
the Hensel/factor-lifting synthesis cited by v9.2. RF3' and the global-degree
fallback are arithmetic envelopes only; neither discharges that synthesis.
The latter still requires line-by-line verification against BCIKS and BCHKS,
represented here only by the explicit `RetainedFactorLiftTarget` proposition.
