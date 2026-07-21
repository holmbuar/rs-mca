---
workboard_item: M1
row: Mersenne-31 list at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: On the exact eight-point C1-owner-complement primitive prefix leaf, certify full effective span and prove nonvacuous image-compensated absolute minor and major aggregate losses at most 1 and 69.
architecture: DIRECT
partition_digest: M31-EIGHT-POINT-C1-COMPLEMENT-V1
atom_or_cell: C9_IMAGE_COMPENSATED_EFFECTIVE_MI_MA
quantifier: Every effective character in the displayed full F_p^3 dual, partitioned by a1=0 versus a1!=0, and every routed residual prefix fiber inside the exact scoped owner complement.
projection_and_unit: Full-prefix support fibers and source-normalized absolute effective-character aggregates; no slope, codeword, or row-budget unit is inferred.
claimed_bound: (L/A_eff) C_min <= 1, (L/A_eff) C_maj <= 69, and (L/A_eff)(1+C_min+C_maj) <= 69 for M=70, L=69, A_eff=p^3.
status: PROVED
impact: LOCAL_ONLY
falsifier: Any failure of the exact 70/69/64 census, the two-sided span inverse, the identity lift, the character-count partition, or the cleared aggregate inequalities.
replay: python3 experimental/scripts/verify_m31_image_compensated_aggregates.py --check; python3 -O experimental/scripts/verify_m31_image_compensated_aggregates.py --check; normal and optimized tamper self-tests.
---

# Image-compensated effective MI+MA on one exact M31 primitive leaf

## Result and acceptance gate

**Activity:** prove one scoped instance of the compensated-aggregate route.

**Acceptance gate:** criterion **2** — bound a genuine post-C1 survivor.  The
packet uses the exact eight-point Mersenne-31 profile, removes the six explicit
C1 complete-fiber supports, proves that the resulting 64-support residual is
nonempty and prefix-injective, and then proves the image-compensated absolute
minor and major aggregate bounds on the complete slice which dominates every
residual fiber.

The proved finite constants are

\[
 M=70,\qquad L=69,\qquad A_{\rm eff}=p^3,
 \qquad p=2^{31}-1,
\]

and, for the nontrivial effective characters split as described below,

\[
 \boxed{\frac{L}{A_{\rm eff}}C_{\rm min}\le 1},\qquad
 \boxed{\frac{L}{A_{\rm eff}}C_{\rm maj}\le 69},
\]

hence

\[
 \boxed{
 \frac{L}{A_{\rm eff}}(1+C_{\rm min}+C_{\rm maj})\le69.}
 \tag{ICA}
\]

This is the absolute-value aggregate route: absolute values remain inside both
sums.  No cancellation-sensitive estimate from the separate phase lane is used.
The major set is nonempty and its whole aggregate is bounded; it is not replaced
by an interface field or an unspecified owner.

## 1. Exact leaf and denominator discipline

Let

\[
 p=2,147,483,647
\]

and let `T` be the eight residues

```text
434373082,  614288294, 1713110565, 1533195353,
1984437538, 380812851,  163046109, 1766670796.
```

The verifier and Lean module check directly that all eight are roots of
`T_(2^21)`, that they form four antipodal pairs, and that the first and last
four points are complete `T_4` fibers.  Put

\[
 \Omega=\binom T4,
 \qquad
 \Psi(S)=\left(\sum_{t\in S}t,
                \sum_{t\in S}t^2,
                \sum_{t\in S}t^3\right)\in\mathbb F_p^3.
\]

The complete enumeration is

```text
|Omega| = 70,
|Psi(Omega)| = 69,
```

with one doubled key, `(0,2,0)`, occupied by the two complete `T_4` blocks.
The explicit C1 owner consists of the six unions of two antipodal pairs, encoded
by masks

```text
15, 85, 165, 90, 170, 240.
```

Deleting precisely those supports gives the scoped post-C1 residual
`Omega^circ`.  Lean and the independent verifier prove

```text
|Omega^circ| = 64,
|Psi(Omega^circ)| = 64,
Psi is injective on Omega^circ,
mask 51 survives the earlier owner and its residual prefix fiber is a singleton.
```

The local owner type contains constructors C1 through C8; only its C1 branch is
nonempty in this fixed profile.  The proved owner-complement equality is literal:

```text
S in Omega^circ
  <-> S in Omega and earlierOwner(S)=none.
```

This is a scoped primitive leaf, not a claim that C2--C8 are empty throughout
the deployed row.

The analytic normalization uses only

```text
q_gen = p,
M     = 70,
L     = 69,
A_eff = p^3.
```

The received-line field, challenge denominator, and list denominator are not
substituted for any of these quantities.  The displayed deployed `B_star` is
metadata only; no row charge is banked.

## 2. Full effective span and certified lifts

Use the moment column

\[
 g(t)=(t,t^2,t^3).
\]

Taking the first displayed point as base, the next three difference columns form

\[
 B=
 \begin{pmatrix}
 179915212&1278737483&1098822271\\
 887084793&0&887084793\\
 1154236547&503705255&1496952355
 \end{pmatrix}.
\]

The certificate supplies the two-sided inverse modulo `p`

\[
 B^{-1}=
 \begin{pmatrix}
 1072773236&2033842811&1680180098\\
 970446555&113640836&1821586645\\
 1074710411&2033842811&467303549
 \end{pmatrix}.
\]

Both products are checked to be the identity.  Therefore the differences
`g(t)-g(t_0)` span all of `F_p^3`, so the effective span in
`eq:effective-fourier-span` is

\[
 V_g=\mathbb F_p^3,
 \qquad A_{\rm eff}=p^3.
\]

Consequently every effective character already is an ambient character.  The
certified lift required by `def:effective-major-minor` is the identity; there is
no lift multiplicity and no open-PR adapter.

## 3. A real nonvacuous major/minor partition

Index the additive characters of `V_g=F_p^3` by
`a=(a_1,a_2,a_3) in F_p^3`.  Partition the nontrivial dual by

\[
 \mathfrak m_{\rm eff}
   =\{a:a_1=0,\ a\ne0\},
 \qquad
 \mathfrak M_{\rm eff}
   =\{a:a_1\ne0\}.
\]

The two parts are disjoint, cover every nontrivial character, and are both
nonempty.  Their exact sizes are

\[
 |\mathfrak m_{\rm eff}|=p^2-1,
 \qquad
 |\mathfrak M_{\rm eff}|=p^3-p^2.
 \tag{P}
\]

This is a certified effective partition in the sense of
`def:effective-major-minor`.  The minor lift is the identity by the full-span
certificate.  The major aggregate is the literal sum over all
`p^3-p^2` major characters; it is not an empty or symbolic major class.

For `a` in the effective dual, write

\[
 E(a)=e_4\bigl(\chi_a(g(t)-g(t_0)):t\in T\bigr).
\]

Every term in this elementary symmetric sum has modulus one and there are
`binom(8,4)=70` terms.  Therefore

\[
 |E(a)|\le70=M
 \tag{T}
\]

for every minor and major character.  With the exact finite normalizations from
`def:aggregate-minor-payment` and `def:major-arc-aggregate`, put

\[
 C_{\rm min}=M^{-1}\sum_{a\in\mathfrak m_{\rm eff}}|E(a)|,
 \qquad
 C_{\rm maj}=M^{-1}\sum_{a\in\mathfrak M_{\rm eff}}|E(a)|.
\]

Equations `(P)` and `(T)` give the **real aggregates**

\[
 C_{\rm min}\le p^2-1,
 \qquad
 C_{\rm maj}\le p^3-p^2.
 \tag{A}
\]

No pointwise cancellation or Weil estimate is asserted.

## 4. Exact image compensation

Multiplying `(A)` by `L/A_eff=69/p^3` gives

\[
 \frac{L}{A_{\rm eff}}C_{\rm min}
 \le \frac{69(p^2-1)}{p^3}<1,
\]

and

\[
 \frac{L}{A_{\rm eff}}C_{\rm maj}
 \le \frac{69(p^3-p^2)}{p^3}<69.
\]

The exact cleared inequalities checked in Lean and in the JSON replay are

```text
69 * (p^2 - 1)       <= p^3,
69 * (p^3 - p^2)     <= 69 * p^3,
1 + (p^2 - 1) + (p^3 - p^2) = p^3.
```

The corresponding cleared slacks are

```text
p^3 - 69*(p^2-1)
  = 9903519982241649175216259071,

69*p^3 - 69*(p^3-p^2)
  = 318206334975137022021.
```

Adding the trivial character proves `(ICA)` exactly.  By
`lem:effective-span-fourier`, every full prefix fiber is therefore at most

\[
 \frac{M}{A_{\rm eff}}(1+C_{\rm min}+C_{\rm maj}),
\]

and every residual fiber is smaller because the residual is a subfamily of the
full slice.  Dividing by the realized full-slice average `M/L` gives the exact
image-compensated multiplier at most `69` on this genuine scoped residual leaf.
The independently checked residual injectivity is stronger, but it is not used
to fake the aggregate proof.

For this fixed deployed leaf the losses are absolute constants.  The packet does
not promote that finite statement to a uniform asymptotic family theorem; such a
promotion still requires an actual family of semantic survivors and its profile
census.

## 5. Source-label map

| Packet step | Grande Finale v4 source node | Use here |
|---|---|---|
| Effective target | `eq:effective-fourier-span` | The explicit two-sided inverse proves `V_g=F_p^3`, hence `A_eff=p^3`. |
| Fourier inversion and triangle | `lem:effective-span-fourier` | Supplies the full-fiber inequality and ambient-lift existence. |
| Certified split | `def:effective-major-minor` | The `a1=0` / `a1!=0` split is disjoint, exhaustive, nonvacuous, and uses identity lifts. |
| Minor aggregate | `def:aggregate-minor-payment` | The literal absolute minor sum is bounded by `(p^2-1)M`. |
| Major aggregate | `def:major-arc-aggregate` | The literal absolute major sum is bounded by `(p^3-p^2)M`. |
| Cardinality aggregate bound | `lem:sparse-major-payment` | The same triangle principle, applied to the exact major count. |
| MI+MA consumer | `prop:effective-mi-ma-flatness` | The present note uses its Fourier triangle core, with the required `L/A_eff` image compensation made explicit. |

The exact compensated normalization is the successor obligation isolated by the
normalization-floor packet; no statement from that open packet is imported into
Lean.

## 6. Replay

Canonical certificate:

```text
experimental/data/certificates/
  sidon-effective-image-image-compensated-aggregates/
  m31_image_compensated_aggregates.json
```

Independent stdlib verifier:

```text
python3 experimental/scripts/verify_m31_image_compensated_aggregates.py --check
python3 -O experimental/scripts/verify_m31_image_compensated_aggregates.py --check
python3 experimental/scripts/verify_m31_image_compensated_aggregates.py --tamper-selftest
python3 -O experimental/scripts/verify_m31_image_compensated_aggregates.py --tamper-selftest
```

All four commands pass.  The normal and optimized checks independently recover
`70`, `69`, `64`, `64`, the two-sided inverse, the exact character counts, and
the three cleared aggregate inequalities.  Both mutation modes reject `10/10`
tampered certificates.

## 7. Explicit nonclaims

- No exhaustive deployed fixed-before-line C1--C8 atlas.
- No claim that only C1 is nonempty outside this scoped profile.
- No all-key M31 prefix theorem and no row-sharp `U_Q` value.
- No support-to-slope `(SE2)` certificate, ray compiler, codeword count, or MCA/list numerator.
- No profile multiplicity, residual add-back, line-local `UNIF`, or adjacent-row sum.
- No cancellation-sensitive phase theorem; this packet keeps absolute values inside both aggregates.
- No uniform asymptotic survivor family; the exact constants are proved only for the displayed finite leaf.
- No use of `M31C9RowSharp`, `HalfSliceFalsifier`, or any other open-PR Lean module.
- No stable-paper edit, deployed endpoint, official score, or prize claim.

The scoped compensated-aggregate route is proved; global C9 completion remains
conditional on actual owner/key coverage, slope projection, profile accounting,
and row summation.
