# Effective-image MI+MA needs the `A_eff / L` compensation

## Status and lane

```text
Activity: FALSIFY / AUDIT one hard input 3 route.

PROVED:
  - exact image-compensated Fourier triangle inequality;
  - universal `A_eff / L` lower floor for the unweighted Fourier `ell^1`
    multiplier;
  - a fixed-density deep multiplicative-coset family with primitive-Q loss
    `p^2 = exp(o(N))` but unweighted EFP loss `exp(Omega(N log N))`.

COUNTEREXAMPLE_NEW_FLOOR:
  - the unweighted effective Fourier payment `(EFP)`, or unweighted effective
    `(MI)+(MA)`, cannot be required as a universal image-normalized payment on
    deep full prefix charts without separately proving effective full image.

CONDITIONAL_ON_NAMED_INPUT:
  IMAGE_COMPENSATED_EFFECTIVE_MI_MA_ON_ACTUAL_PRIMITIVE_LEAVES.
```

This packet does **not** prove that the displayed full prefix family survives the
actual C1--C8 first-match atlas.  It therefore does not refute a theorem stated
only on genuine post-deletion C9 survivors.  It cuts a broader analytic route:
proving the unweighted Fourier aggregate on every deep full chart is stronger
than image-normalized primitive Q by exactly the effective-span/image ratio.

## 1. Source labels and object discipline

The v3 source is `experimental/grande_finale.tex`.  This note uses its labels
exactly:

- `eq:effective-fourier-span` for `V_g` and `A_eff`;
- `lem:effective-span-fourier` for `(EF2)`--`(EF3)`;
- `def:effective-major-minor` for the certified effective partition;
- `def:effective-fourier-payment` for `(EFP)` and `(EF4)`;
- `def:aggregate-minor-payment` and `def:major-arc-aggregate` for `(MI)` and
  `(MA)`;
- `cor:exact-finite-fourier-constants` for `(EF7)`;
- `eq:image-ambient-scales` and `eq:full-image-certificate` for the distinction
  among realized, effective-span, and ambient scales;
- `def:primitive-q` for image-normalized max-fiber Q;
- `lem:newton-equivalence` for the power-sum/locator-coefficient dictionary;
- `thm:sidon-resolved-payment` for the already proved pointwise-flat range.

The exact support-to-slope boundary is separate.  In
`experimental/rs_mca_thresholds.tex`, `cor:exact-prefix-ray-realization` realizes
a complete prefix fiber as distinct bad slopes after a separating pole is
supplied, while `drc:thm-exact-compiler` and `drc:eq-direct-compiler` keep the
final ray projection explicit.  Nothing below silently identifies a support
fiber with a line-uniform MCA numerator.

### Denominator ledger

Every analytic claim below is at the full **prefix-support** scale:

```text
q_gen  = |B|, the locator/prefix coefficient-field size;
q_line = |F|, the received-line slope-field size;
q_chal = |Gamma|, the challenge denominator;
q_list = the list-side denominator in the active row ledger.
```

Only `q_gen` enters `A_amb = q_gen^R`.  The quantities `q_line`, `q_chal`, and
`q_list` are not used or identified with `q_gen` in this note.  In the
counterexample family `q_gen=p`; a separating pole may require a larger
`q_line`, and no challenge or list denominator is fixed.

## 2. Exact normalization

Let

```text
Omega = binom(T,m),       M = |Omega|,
Psi : Omega -> z0 + V_g,
S = Psi(Omega),           L = |S|,
A_eff = |V_g|,
barN_img = M/L,           barN_eff = M/A_eff.
```

For `z in V_g`, write

```text
N(z) = |{S in Omega : Psi(S)=z0+z}|.
```

For an effective character `chi`, use the unnormalized fixed-weight Fourier
coefficient

```text
E_m(chi) = sum_{S in Omega} chi(Psi(S)-z0).
```

Given any certified partition from `def:effective-major-minor`, put

```text
C_min = M^(-1) sum_{chi in m_eff} |E_m(chi)|,
C_maj = M^(-1) sum_{chi in M_eff} |E_m(chi)|,
kappa_l1 = 1 + C_min + C_maj
          = M^(-1) sum_{chi in dual(V_g)} |E_m(chi)|.
```

These are the exact finite constants from
`cor:exact-finite-fourier-constants`.  They use `A_eff`, not `q_gen^R`, unless
full effective span has separately been proved.

## 3. Image-compensated Fourier triangle payment

### Claim 3.1 — exact finite inequality

**Status: PROVED.**

**Normalization:** `M`, `L`, `A_eff`, and `barN_img=M/L` are exactly as in
Section 2; no `q_line`, `q_chal`, or `q_list` denominator occurs.

For every full slice and every certified effective major/minor partition,

```text
max_z N(z) / barN_img
  <= (L/A_eff) (1 + C_min + C_maj).                 (ICF)
```

The same upper bound holds for every first-match residual fiber contained in a
full-slice fiber.

**Proof.**  Formula `(EF7)` in `cor:exact-finite-fourier-constants` says

```text
max_z N(z) <= (M/A_eff)(1+C_min+C_maj).
```

Divide by `M/L`.  Earlier first-match deletion only decreases each full-slice
fiber.  No full-image certificate is used.  `square`

This identifies the exact finite **image-compensated loss**

```text
K_IC := (L/A_eff)(1+C_min+C_maj).                  (IC-loss)
```

### Claim 3.2 — sufficient image-scale MI+MA input

**Status: CONDITIONAL_ON_NAMED_INPUT.**

**Normalization:** all terms are divided by the full-slice mass `M`, then
multiplied by `L/A_eff`; the target average is `barN_img=M/L`.  Ambient
normalization `M/q_gen^R` is not substituted, and no slope/list denominator is
present.

Name the required analytic input

```text
IMAGE_COMPENSATED_EFFECTIVE_MI_MA_ON_ACTUAL_PRIMITIVE_LEAVES:

  (L/A_eff) C_min <= exp(o(N)),
  (L/A_eff) C_maj <= exp(o(N))
```

uniformly on the genuine post-C1--C8 primitive leaves, with certified lifts for
the minor characters and an actual aggregate proof for the major characters.
Then `(ICF)` gives primitive Q at image scale:

```text
max_s |Omega^circ cap Phi^(-1)(s)|
  <= exp(o(N)) M/L.
```

This is only the support max-fiber payment.  The distinct-ray compiler and the
line-local `sup_line sum_profile` ledger remain separate inputs.

## 4. The unavoidable `A_eff / L` floor

### Claim 4.1 — universal Fourier `ell^1` floor

**Status: PROVED.**

**Normalization:** `A_eff` is the size of the effective Fourier group from
`eq:effective-fourier-span`; `L` is the realized full-slice image size; the
Fourier coefficients are divided by `M`.  No ambient, slope, challenge, or list
denominator is substituted.

For every finite fixed-weight map,

```text
kappa_l1 >= A_eff / L.                             (FLOOR)
```

Equivalently,

```text
1 + C_min + C_maj >= A_eff/L
```

for **every** partition of the nontrivial effective dual.

**Proof.**  Parseval on `V_g` gives

```text
sum_chi |E_m(chi)|^2 = A_eff sum_z N(z)^2.
```

Since the `L` nonzero fiber counts sum to `M`, Cauchy--Schwarz gives

```text
sum_z N(z)^2 >= M^2/L.
```

Also `|E_m(chi)|<=M`, so

```text
M sum_chi |E_m(chi)|
  >= sum_chi |E_m(chi)|^2
  >= A_eff M^2/L.
```

Divide by `M^2`.  `square`

The factor in `(IC-loss)` is therefore always at least one.  It is not a
technical loss that can be discarded: it is the exact correction forced by
Fourier orthogonality and the realized-image census.

### Consequence 4.2 — what unweighted EFP secretly proves

**Status: PROVED.**

**Normalization:** the conclusion compares `L` only with `A_eff`.  It becomes
the ambient certificate in `eq:full-image-certificate` only when
`A_eff=q_gen^R` has separately been proved.

If unweighted `(EFP)` holds with `kappa=exp(o(N))`, or if unweighted effective
`(MI)+(MA)` give `1+C_min+C_maj=exp(o(N))`, then `(FLOOR)` forces

```text
A_eff/L = exp(o(N)).
```

Thus the unweighted route contains an effective full-image theorem.  It cannot
be treated as merely an image-normalized max-fiber estimate on a sparse
nonlinear image.

## 5. Deep smooth counterexample family

Fix `0<theta<1`.  Let `p` tend through primes and set

```text
B = F_p,
T = F_p^x,               N=p-1,
m = floor(theta N),
R = m-2
```

for all sufficiently large `p`.  Thus `1<=R<m<p`, and `T` is the full
multiplicative coset.  On `Omega=binom(T,m)`, define the genuine depth-`R`
power-sum prefix map

```text
Psi_p(S) = (sum_{t in S} t, ..., sum_{t in S} t^R) in F_p^R.
```

This is the unprofiled map from `eq:exact-power-sum-map`, with the Newton change
of coordinates justified by `lem:newton-equivalence`.

### Claim 5.1 — full effective span

**Status: PROVED.**

**Normalization:** `q_gen=p`, `A_eff=p^R`; `q_line`, `q_chal`, and `q_list` are
not fixed.

One has

```text
V_g = F_p^R,             A_eff=p^R.
```

Indeed, an annihilating effective character would give a polynomial
`P(X)=sum_{j=1}^R a_j X^j` constant on all `p-1` nonzero field elements.  Since
`deg(P)<=R<=p-3`, the polynomial `P-c` has more roots than its degree and is
zero.  Its zero constant term then forces `c=0` and every `a_j=0`.

### Claim 5.2 — image-normalized primitive Q is subexponentially paid

**Status: PROVED for the full prefix chart.**

**Normalization:**

```text
M=binom(N,m),  L=|Psi_p(Omega)|,
barN_img=M/L,  A_eff=p^R.
```

No ambient average `M/p^R` replaces `M/L`.

Every fiber has size at most `p^2`.  The first `R=m-2` power sums determine the
first `m-2` elementary locator coefficients.  A monic degree-`m` locator in that
fiber is therefore determined after choosing only its last two coefficients,
of which there are at most `p^2` choices.  Consequently

```text
max_z N(z) <= p^2,
M/p^2 <= L <= M,
max_z N(z)/(M/L) <= p^2 = exp(o(N)),
0 <= log M-log L <= 2 log p = o(N).
```

Thus this deep smooth chart lies exactly at the realized-image frontier and
satisfies image-normalized Q with subexponential loss.

### Claim 5.3 — unweighted EFP fails by a superexponential-in-`N` factor

**Status: COUNTEREXAMPLE_NEW_FLOOR.**

**Normalization:** the failed inequality is the unweighted effective aggregate

```text
sum_{chi != 1 in dual(V_g)} |E_m(chi)|
  <= exp(o(N)) M.
```

The target being paid is nevertheless `barN_img=M/L`, not `M/p^R`.

By `(FLOOR)`, every effective major/minor partition obeys

```text
1+C_min+C_maj >= A_eff/L >= p^R/M.
```

Stirling's formula gives

```text
log(A_eff/L)
  >= R log p - log binom(N,m)
  = theta N log N - N h(theta) + O(N),
```

which is not `o(N)`.  Hence no partition can prove unweighted EFP or unweighted
MI+MA with subexponential loss on this family, although image-normalized Q is
already paid by `p^2`.

This is the explicit falsifier requested for the broader conjecture

```text
UNWEIGHTED_EFP_ON_EVERY_DEEP_SMOOTH_IMAGE_FRONTIER_CHART.
```

The new floor is `A_eff/L`, and the repaired triangle-method target is `(ICF)`.

## 6. Exact `p=11` Lean regression

The stdlib-only package `experimental/lean/sidon_effective_image/` checks the
finite row

```text
p=11, T=F_11^x, N=10, m=5, R=3.
```

It proves by executable finite reduction:

```text
M=252,
L=251,
max fiber=2,
2L<2M  (equivalently the image-normalized Q loss is <2),
A_eff=11^3=1331,
A_eff>5L,
```

and records the unique double target `0` with supports

```text
{1,3,4,5,9},  {2,6,7,8,10}.
```

It also verifies an explicit inverse for three generator differences, certifying
that the effective span is all of `F_11^3`.  This finite package checks the toy
falsifier geometry only.  It does not formalize complex Fourier analysis,
Parseval, asymptotics, first-match survival, or the ray compiler.

## 7. Exact remaining obligation

The useful hard-input-3 target after this route cut is:

```text
CONDITIONAL_ON_NAMED_INPUT:
IMAGE_COMPENSATED_EFFECTIVE_MI_MA_ON_ACTUAL_PRIMITIVE_LEAVES
```

For each genuine post-C1--C8 leaf, one must do one of the following at the
printed image scale:

1. prove `(L/A_eff)C_min` and `(L/A_eff)C_maj` are `exp(o(N))`, with certified
   lifts and a real major aggregate;
2. prove direct image-normalized primitive Q; or
3. classify the sparse-image profile into an earlier paid semantic owner.

A proof must still preserve actual first-match survival, the realized profile
census, residual-to-full add-back where used, the separate distinct-ray
compiler, and `sup_line sum_profile`.  This packet supplies none of those global
interfaces.

## 8. Nonclaims

- No theorem about all actual C9 survivors.
- No ambient FI theorem.
- No claim that `A_eff=q_gen^R` on arbitrary charts.
- No automatic conversion of a dual major locus into a primal paid cell.
- No identification of `q_gen`, `q_line`, `q_chal`, or `q_list`.
- No deployed-row integer certificate, MCA threshold, list threshold, or prize
  claim.
