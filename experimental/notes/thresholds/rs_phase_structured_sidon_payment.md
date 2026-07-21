# RS phase-structured Sidon payment on one deployed M31 leaf

```yaml
workboard_item: T
row: Mersenne-31 list analytic stress calibration
object: OTHER
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: On the explicit post-C1 owner-complement leaf, every realized p2 fiber has zero quadratic-locator phase coefficient; hence phase-aware L1 and signed collision moment are exactly zero.
architecture: DIRECT_SCOPED_LEAF
partition_digest: 66dff80464465ec96253a4c10d518dc488d29e83e9b6cd5272b2ac8a136e8f41
atom_or_cell: RS_PHASE_STRUCTURED_SIDON_PAYMENT / p2 quadratic-locator band
quantifier: all 64 supports in the displayed owner complement and all 9 realized p2 keys
projection_and_unit: phase-weighted supports over realized p2 keys; not slopes or codewords
claimed_bound: phaseAwareL1 = 0 and phaseCollisionMoment = 0
status: PROVED
impact: LOCAL_ONLY; acceptance gate criterion 2 (genuine post-C1--C8 survivor)
falsifier: any omitted owner, missing residual support, non-root domain point, non-exhaustive pair table, or nonzero realized phase coefficient
replay: python3 experimental/scripts/verify_rs_phase_structured_sidon.py; python3 -O experimental/scripts/verify_rs_phase_structured_sidon.py
```

## Result

This packet gives a cancellation-sensitive payment on one genuine deployed-calibration Reed--Solomon primitive leaf. It uses the same eight Mersenne-31 Chebyshev-domain points and the same exact C1 antipodal complete-fiber deletion as the scoped C9 leaf developed after the absolute-mass obstruction. No proxy incidence family is substituted.

Let

\[
p=2^{31}-1,
\qquad
D_8=\{x_0,\ldots,x_7\}\subset T_{2^{21}}^{-1}(0),
\]

with antipodal pairs

\[
(x_0,x_2),\ (x_1,x_3),\ (x_4,x_6),\ (x_5,x_7).
\]

The complete moving slice is the 70 four-subsets of `D_8`. The earlier C1 owner consists exactly of the six supports obtained by selecting two complete antipodal pairs. Deleting them leaves an exact 64-support owner complement. The deployed outside-weight arithmetic is also valid:

\[
981129-4=981125\le 2^{21}-8=2097144.
\]

Thus each moving support embeds into a full complement-weight support at the Mersenne-31 list calibration.

## The RS phase

For a residual support `S`, write its monic locator as

\[
Q_S(X)=\prod_{x\in S}(X-x).
\]

Because `|S|=4`, its constant term is

\[
Q_S(0)=\prod_{x\in S}x.
\]

Define the quadratic locator phase

\[
\omega(S)=\chi\!\left(Q_S(0)\right)\in\{+1,-1\},
\]

where `chi` is the quadratic character of `F_p^*`. The verifier and Lean module evaluate this phase by exact Euler criterion; every displayed locator constant is nonzero.

The coarse key is the actual second Vandermonde/power-sum coordinate

\[
\Phi_2(S)=\sum_{x\in S}x^2\pmod p.
\]

Its **realized** image on the residual has size

\[
A_{\rm eff}=L=9,
\]

not `p`, `p^R`, or any ambient target. The nine fiber sizes are

\[
8,8,8,8,16,4,4,4,4,
\]

so the integral natural scale is

\[
\left\lceil\frac{64}{9}\right\rceil=8.
\]

## Cancellation involution

Every residual support has at least one antipodal pair occupied in exactly one point. Otherwise every antipodal pair would have occupancy zero or two; at weight four the support would be one of the six deleted C1 complete-fiber supports.

Choose the first split antipodal pair and swap the selected point with its antipode. This operation:

1. stays inside the 64-support owner complement;
2. is fixed-point-free and involutive;
3. preserves `Phi_2`, because `x^2=(-x)^2`;
4. multiplies `Q_S(0)` by `-1`; and
5. flips the quadratic phase because `p=3 mod 4`, hence `chi(-1)=-1`.

The certificate prints the resulting 32 support pairs and checks that they exhaust the residual. Therefore, for every realized key `z`,

\[
a_z:=\sum_{S\in\Omega^\circ:\ \Phi_2(S)=z}\omega(S)=0.
\]

Consequently the cancellation-sensitive aggregates are exactly

\[
\sum_{z\in\Phi_2(\Omega^\circ)}|a_z|=0,
\qquad
\sum_{z\in\Phi_2(\Omega^\circ)}a_z^2=0.
\]

For comparison, the unsigned collision moment on the same realized image is

\[
\sum_z |\Phi_2^{-1}(z)|^2=576,
\qquad
\max_z |\Phi_2^{-1}(z)|=16.
\]

Thus the cancellation is invisible to absolute support mass. The exact phase-aware multiplier is one:

\[
0\le (1-1)\,M.
\]

This is the proof-direction successor to the absolute effective-dual floor: the correct local object is a phase-weighted RS locator aggregate, not the absolute mass of every dual coefficient.

## Source-label map

| Packet statement | Active source boundary |
|---|---|
| Explicit first-match owner complement | Grande Finale v4 normalized first-match/primitive-Q boundary; locally restated owner-complement condition, as required by the C9 producer interface |
| Realized-image normalization `A_eff=L` | `experimental/grande_finale.tex`, effective-image Fourier normalization and `def:sidon-paid`/`thm:primitive-q` interface |
| Cancellation-sensitive replacement | Successor named by upstream #1026: `RS_PHASE_STRUCTURED_SIDON_PAYMENT` |
| Actual M31 leaf/domain | Scoped deployed leaf of upstream #1027, restated locally; no open-PR module imported |
| Deployed row arithmetic | `tex/cs25_cap_v13_2.tex` and the live Mersenne-31 list stress-row constants in `agents.md` |

## Exact status

This packet satisfies acceptance gate **criterion 2**: it bounds a genuine post-C1 owner-complement survivor at the deployed calibration. It is stronger than a proxy-family computation because the domain, owner, residual, locator phase, and realized image are all the actual finite RS objects.

It does **not** prove a full three-coordinate C9 Sidon payment, convert the signed aggregate into an unsigned max-fiber bound, project supports to codewords or affine slopes, prove global C1--C8 exhaustion, count fixed-outside profiles, prove residual add-back or `UNIF`, or move a deployed integer ledger atom.
