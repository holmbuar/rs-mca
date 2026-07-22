# Correspondence: M31 quotient-band shell floor and mixing

## Source statement

The source theorem is
`experimental/notes/thresholds/m31_quotient_band_swap_census_t16_mixing.md`.
It concerns only the pinned `c=2048`, `(u,v)=(0,1)` quotient profile on the
1,022-point punctured quotient domain and only support-level depth-32 locator
prefixes.

## Lean statements

`Witnesses.lean` checks:

- the exact Mersenne prime, norm-one generator, 1,024 quotient labels, and two
  punctures;
- the fourteen intact 64-point classes and the 31-point core;
- the round-2 full-class correction `42, 315, 700`, plus
  `C(14,7)=3,432` class selections and the exact restricted shell counts
  `49, 441, 1,225, 1,225, 441, 49, 1`;
- direct depth-63 equality for one deficiency-192 representative;
- the finite premise that every intact class locator differs from the class-5
  locator only in its constant coefficient;
- `H_192`, `4 H_192 < p^32`, the quotient average floors, and the exact
  coefficient-four compiler total `15,004,052`;
- the twelve exact intact `T_16` fibers, their two power-sum identities, the
  two 479-point supports, deficiency `96`, and direct equality of the first
  `47` nonleading locator coefficients with inequality at coefficient `48`.

`M31QuotientBandMixing.lean` re-exports the packet-level floor/window and
off-lattice witness statements.

## Paper-to-kernel boundary

The note's Proposition 2.1 uses the following elementary degree argument.
Every intact block locator has the form `F_64 - lambda`. Two monic
degree-seven products in `F_64` differ in `F_64`-degree at most six. After the
degree-31 core is multiplied in, the locator difference has degree at most
`31 + 6*64 = 415`, so degree-479 locators share their first `63` nonleading
coefficients.

Lean kernel-checks every finite premise of this argument, the arithmetic
`31 + 6*64 = 415` and `479 - 415 - 1 = 63`, and a direct representative
locator equality. The generic polynomial-degree inference is audited in the
source note rather than encoded as a reusable polynomial library theorem.

For the off-lattice witness, Lean also performs the full direct locator
multiplications, so the `T_16` composition correspondence is independently
checked at the final quotient-label level.

## Nonclaims

No theorem in this package asserts a uniform band cap, a non-full
deficiency-64 neighbor, a shell degree of 5,192, first-match survival,
received-word realization, codeword/ray/slope projection, or a row-global
payment.
