# L post-Johnson conversion contract

This stdlib-only Lean package is the decidable arithmetic shadow of
`experimental/notes/thresholds/m31_postjohnson_conversion_contract.md`.
It contains no Mathlib import, `sorry`, axiom, or coding-theory theorem stub.

## Certified finite statements

`LPostJohnsonContract.Deployed` checks:

- the Mersenne-31 field order, full-domain row constants, and the distinct
  floor/ceiling values at `2^-100`;
- the exact finite-`q`, list-size-`16777215` Johnson boundary for
  `C⁺ = RS(k+1)` and the one-step convention audit for `C = RS(k)`;
- the direct Johnson deficit and standard shortening-plus-Johnson route cut;
- the CS25 integer window, including maximal CA numerator `16777214` and its
  one-count ceiling loss;
- the BCHKS25 strict-input congruence and the exact `q-1` route-cut margin; and
- the literal repository-transcription arithmetic for GCXK25, whose theorem
  use remains source-sign guarded in the note.

## Correspondence boundary

The Lean declarations certify only the exact natural-number identities and
inequalities printed in the source note and JSON certificate.  The implications
from CA or MCA hypotheses to list/MCA bounds are cited theorem uses in
`open-proximity.tex`; they are neither re-proved nor axiomatized here.

The packet code is always `C = RS_F(D,k)`, degree `< k`.  At the CS25 theorem
use only, the output code is the containing `C⁺ = RS_F(D,k+1)`; the ordinary
list-row conclusion for `C` then follows by set inclusion.

## Build target

```text
lake build LPostJohnsonContract
```
