---
workboard_item: K2
row: KoalaBear MCA at 2^-128
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: Under the single finite residual hypothesis KB_TANGENT_ROOTED_Q_SHELL(3,7), every admissible received line has at most 400389155870 tangent-surviving ACTIVE_V4_BOUNDARY_PREFIX_Q slopes.
architecture: GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1
partition_digest: 4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc
atom_or_cell: U_Q=ACTIVE_V4_BOUNDARY_PREFIX_Q after SOURCE_COORDINATE_TANGENT_IMAGE deletion
quantifier: Uniform over every admissible received line over F_(p^6)
projection_and_unit: Distinct bad finite slopes per received line
claimed_bound: U_Q=400389155870 conditional on KB_TANGENT_ROOTED_Q_SHELL(3,7)
status: CONDITIONAL
impact: BANKABLE_ATOM
falsifier: An admissible line whose canonical branch-dependent Q shell table violates p^67471*max(d_e-3,0)<=7*C(1116048,e)*C(981104,e), or a failure of exact-card Q support selection, support-to-slope injectivity, or the frozen tangent deletion.
replay: python3 experimental/scripts/verify_kb_uq_boundary_prefix_tangent_rooted_shell_v1.py --check; python3 experimental/scripts/verify_kb_uq_boundary_prefix_tangent_rooted_shell_v1.py --tamper-selftest; fork CI builds experimental/lean/kb_uq_boundary_prefix
---

# KoalaBear tangent-rooted boundary-prefix Q compiler

## Verdict

**A3 CONDITIONAL CAP / BANKABLE RUNG / ROW OPEN.**  Under one named finite
pointwise hypothesis on the actual tangent-surviving Q shell table,

\[
 |Z_Q|\le U_Q=400{,}389{,}155{,}870
\]

for every admissible received line.  With the round-1 payment
\(U'_{\rm paid}=981{,}104\), the remaining exact reserve is

\[
 274{,}980{,}327{,}721{,}258{,}113.
\]

This packet does not prove the shell hypothesis, an unconditional A1/A2 cap,
a refund family, a balanced-core payment, a zero complement, or row closure.

## Frozen row and chronology

The packet changes none of the round-1 contract:

\[
 p=2{,}130{,}706{,}433,\quad \F=\mathbf F_{p^6},\quad
 n=2{,}097{,}152,\quad k=1{,}048{,}576,
\]
\[
 a=1{,}116{,}048,\quad t=n-a=981{,}104,
\quad B^*=274{,}980{,}728{,}111{,}395{,}087.
\]

The architecture is
`GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1`, with partition digest
`4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc`
and owner order

```text
SOURCE_COORDINATE_TANGENT_IMAGE
ACTIVE_V4_BOUNDARY_PREFIX_Q
ACTIVE_V4_BALANCED_CORE
UNPAID_V4_COMPLEMENT.
```

For a received line let \(Z\) be its complete bad-slope set and let
\(\mathcal T(r)\) be the canonical round-1 source-coordinate tangent image.
The present object is exactly

\[
 Z_Q=(Z\setminus\mathcal T(r))\cap Q.
\]

The unit is distinct bad finite slopes, and every statement below is uniform
over received lines.

## Source bindings

The proof uses only the following source-bound facts; the sole new mathematical
input is the named shell hypothesis in the next section.

| Role | Source and exact anchor |
|---|---|
| frozen row, unit, workboard contract | `agents.md` at lab base `c49e45eed71af9c24e3599c2fca3b76e02692be9`, blob `30d8b9f1b4caa3c7504fe3d24fc7ce8da84de434` |
| active first-match boundary-prefix Q object | `experimental/grande_finale.tex`, `sec:primitive-leaf`, `eq:exact-power-sum-map`, and `def:primitive-q`; these define the post-earlier-owner residual and its max-fiber Q branch |
| exact MCA/CA versus sparse-pair split | `experimental/grande_finale.tex`, `thm:exact-sparsification`; `experimental/rs_mca_thresholds.tex`, `thm:exact-sparsification` and challenge form `(SP3)` |
| pointwise translation invariance | integrated theorem `RsMcaThresholds.ExactSparsification.mcaBad_sub_mem_iff`, source blob `b4a89c7aa45fc068c010ebed9cd96073e6a2ec03` |
| exact-card received-line witnesses | integrated `GrandeFinale.RSExactCardWitnessBridge.mcaBad_has_exact_support` and `rsMcaBadSlopes_eq_exactCardWitnessSlopeImage`, source blob `72eb087e6a2fbf1d269ebbcefd9a0453e8dd9fb5` |
| one noncommon support carries at most one slope | `experimental/grande_finale.tex`, `thm:canonical-partial-occupancy-atlas`, proof of `(PO6)`; equivalently the integrated first-match witness bridge |
| Q boundary support object | `experimental/grande_finale_work/q_section.tex`, `prop:q-boundary-divisor`; the open unconditional target is explicitly `conj:q-active` and `rem:q-not-proved`, blob `53e69c9c1915400f6122d57da49cce7120a9819d` |
| boundary/interior typing | `experimental/grande_finale_work/bc_section.tex`, `prop:gf-bc-slope-elimination` and `prop:gf-bc-boundary-is-q`, blob `a97fa32e13077deb757d465fb4a7a777368653e0` |
| frozen tangent deletion | upstream PR #1049 head `c15927c90091602035f617226da9ecf03cfc7316`: note blob `c17d8f0f2f72450ebda548089bb8274300e5c8d8`, row-manifest blob `15731acc39a4cc38d8175fd09535b149490f8551`, Lean blob `3c0a7c4e24478a6517da628406e0b2df24a06e9a` |

The active Q theorem itself remains open.  This packet neither imports nor
renames a legacy-M1 Q charge.

## Canonical selected-support family

The active MCA boundary chart has effective list dimension
\(K_Q=k+1=1{,}048{,}577\): the extra affine coefficient is the slope
parameter.  Thus the active-v4 notation `def:primitive-q` and
`eq:exact-power-sum-map` specializes to

\[
 w=a-K_Q=a-(k+1)=67{,}471,\qquad Q_0=p^w.
\]

For every \(\gamma\in Z_Q\), choose the public-order first exact-cardinality
support \(S_\gamma\) occurring in its active boundary-prefix Q certificate,
together with its degree-\(<k\) explanation.  Thus
\(|S_\gamma|=a\).

The map \(\gamma\mapsto S_\gamma\) is injective.  Indeed, if the same
noncommon support explained two distinct slopes \(\gamma\ne\gamma'\),
subtracting the two explanations would explain the direction coordinate on
that support; subtracting it back would explain the base coordinate too.  The
pair would then be jointly explained, contradicting MCA nontriviality.  This is
the finite support-to-slope injection used in the proof of `(PO6)` in
`thm:canonical-partial-occupancy-atlas`.

Consequently, counting the selected supports counts \(|Z_Q|\) exactly; no
support, witness, pair, selector, or coordinate multiplicity is charged.

## The one residual hypothesis

For two \(a\)-subsets \(A,S\subseteq D\), write their exchange distance as

\[
 e(A,S)=a-|A\cap S|.
\]

The total ambient shell size at exchange \(e\) from any fixed \(a\)-set is

\[
 H_e=\binom ae\binom te.
\]

### Definition: `KB_TANGENT_ROOTED_Q_SHELL(b,c)`

For every admissible received line, form exactly one of the following canonical
shell tables.

1. **Non-column-far branch.** Use the canonical round-1 translation
   \((e_0,e_1)\), put
   \(\Sigma=\operatorname{supp}(e_0)\cup\operatorname{supp}(e_1)\), and choose
   the public-order first \(a\)-subset \(A_0\subseteq D\setminus\Sigma\).
   For each \(e\), let
   \[
      d_e=|\{\gamma\in Z_Q:e(A_0,S_\gamma)=e\}|.
   \]

2. **Column-far branch.** Here the frozen contract has
   \(\mathcal T(r)=\varnothing\).  If \(Z_Q=\varnothing\), the table is empty.
   Otherwise let \(A_*\) be the selected support of the public-order first
   slope in \(Z_Q\), remove that slope, and put
   \[
      d_e=|\{\gamma\in Z_Q\setminus\{\gamma_*\}:
             e(A_*,S_\gamma)=e\}|.
   \]

The single pointwise finite hypothesis is

\[
 \boxed{
 Q_0\max(d_e-b,0)\le c\,H_e
 }
 \tag{KB-Q-shell}
\]

for every populated shell of the applicable canonical table.  There is no
expectation, line average, profile average, alternative root, or union over
translations.  The constants \(b,c\) are nonnegative integers.

## Where tangent pruning is spent

Assume the non-column-far branch.  Round 1 gives
\(|\Sigma|\le t\) and preserves every bad slope under one fixed translation.
For \(\gamma\notin\mathcal T(r)\), the translated word
\(e_\gamma=e_0+\gamma e_1\) has zero set exactly
\(D\setminus\Sigma\): outside \(\Sigma\) both coordinates vanish, while at a
point of \(\Sigma\) either \(e_1=0\ne e_0\), or the excluded ratio
\(-e_0/e_1\) is the unique vanishing slope.

Let \(h_\gamma\) be the selected degree-\(<k\) explanation on
\(S_\gamma\).  If \(|A_0\cap S_\gamma|\ge k\), then \(h_\gamma\) vanishes on
at least \(k\) distinct points and hence is zero.  It would follow that
\(S_\gamma\subseteq D\setminus\Sigma\), where both \(e_0\) and \(e_1\) are
zero; the pair would be jointly explained there.  Therefore

\[
 |A_0\cap S_\gamma|\le k-1,
 \qquad e(A_0,S_\gamma)\ge a-k+1=67{,}473=w+2.
 \tag{P1}
\]

Every exchange distance between two \(a\)-sets is at most \(t=n-a\), so only

\[
 e=67{,}473,\ldots,981{,}104
\]

can occur.  The number of live sparse-branch shells is exactly

\[
 S_{\rm sparse}=t-(w+2)+1=913{,}632.
 \tag{P2}
\]

This is the first-match pruning: shells \(0,1,\ldots,w+1\) disappear only after
\(\mathcal T(r)\) is deleted.  With \(Z\) in place of
\(Z\setminus\mathcal T(r)\), the exact-zero-set assertion and `(P1)` are false
at tangent ratios.  Thus the conditional theorem is not a verbatim bound on
the unpruned bad-slope set.

The column-far branch has no tangent translation and therefore no zero anchor.
Rooting at one actual selected support leaves at most the \(t=981{,}104\)
nonzero shells \(e=1,\ldots,t\).  This branch is why the final uniform integer
is slightly larger than the tangent-pruned sparse subcap.

## Finite shell compiler

For any nonnegative integer \(d\),

\[
 d\le b+\max(d-b,0).
\]

Summing `(KB-Q-shell)` over the applicable shells gives the following two exact
bounds.

### Non-column-far branch

Vandermonde's identity gives
\(\sum_{e=0}^tH_e=\binom na\).  Using `(P2)` and dropping only positive shell
mass,

\[
 |Z_Q|
 \le bS_{\rm sparse}
    +\left\lfloor\frac{c\binom na}{p^w}\right\rfloor.
 \tag{C-sparse}
\]

### Column-far branch

The root contributes one selected slope and
\(\sum_{e=1}^tH_e=\binom na-1\), so

\[
 |Z_Q|
 \le 1+bt
    +\left\lfloor\frac{c(\binom na-1)}{p^w}\right\rfloor.
 \tag{C-far}
\]

These are direct finite integer compilers for the actual selected-support
family.  The companion stdlib-only Lean module kernel-checks both summation
forms; the giant KoalaBear binomial quotients are replayed twice by the packet
verifier.

## Deployed specialization \((b,c)=(3,7)\)

Let \(X=\binom na\).  Independent exact computations give

\[
 \left\lfloor\frac{X}{p^w}\right\rfloor=57{,}198{,}030{,}365,
 \qquad
 \left\lceil\frac{X}{p^w}\right\rceil=57{,}198{,}030{,}366,
\]
\[
 \left\lfloor\frac{7X}{p^w}\right\rfloor
 =\left\lfloor\frac{7(X-1)}{p^w}\right\rfloor
 =400{,}386{,}212{,}557.
\]

The non-column-far tangent-pruned subcap from `(C-sparse)` is

\[
 U_Q^{\rm sparse}
 =3\cdot913{,}632+400{,}386{,}212{,}557
 =400{,}388{,}953{,}453.
\]

The column-far cap from `(C-far)`, and therefore the uniform A3 cap, is

\[
 \boxed{
 U_Q=1+3\cdot981{,}104+400{,}386{,}212{,}557
     =400{,}389{,}155{,}870.
 }
\]

The displayed compiler spends the tangent pruning in the non-column-far branch
and saves exactly

\[
 U_Q-U_Q^{\rm sparse}
 =1+3(w+1)=202{,}417
\]

relative to the generic rooted-support cap.  Uniformity nevertheless makes the
column-far branch binding.

The partial ledger is

\[
 U'_{\rm paid}+U_Q
 =981{,}104+400{,}389{,}155{,}870
 =400{,}390{,}136{,}974,
\]

leaving

\[
 B^*-(U'_{\rm paid}+U_Q)
 =274{,}980{,}327{,}721{,}258{,}113
\]

for \(U_{\rm BC}+U_{\rm new}\).

## Exact viable constant window

The uniform cap fits the current reserve
\(R=B^*-981{,}104=274{,}980{,}728{,}110{,}413{,}983\) exactly when

\[
 1+bt+\left\lfloor\frac{c(X-1)}{p^w}\right\rfloor\le R.
 \tag{W}
\]

Thus the complete nonnegative-integer window is

\[
 0\le b\le\left\lfloor\frac{R-1}{t}\right\rfloor
 =280{,}276{,}839{,}265,
\]

and, for each such \(b\),

\[
 0\le c\le c_{\max}(b):=
 \left\lfloor
   \frac{(R-bt)p^w-1}{X-1}
 \right\rfloor.
 \tag{W-exact}
\]

Useful exact boundary values are

\[
 c_{\max}(0)=4{,}807{,}520,
 \qquad b_{\max}(4{,}807{,}520)=54{,}192.
\]

At the corner \((b,c)=(54{,}192,4{,}807{,}520)\), the cap is

\[
 274{,}980{,}728{,}110{,}019{,}048,
\]

leaving \(394{,}935\).  Increasing \(b\) to \(54{,}193\) exceeds the reserve
by \(586{,}169\).  At \(b=0\), increasing \(c\) to \(4{,}807{,}521\) exceeds
the reserve by \(4{,}029{,}647{,}463\).

Hence `(3,7)` lies deep inside a nonempty viable window.  No known
support-only violation certifies a violation on the actual KoalaBear
post-tangent Q residual; such a line would be a direct falsifier of this rung.

## Independent integer replay

The verifier computes every reported integer by two independent routes.

1. **Route A:** Python's exact `math.comb`, built-in exponentiation, and direct
   quotient/remainder arithmetic.
2. **Route B:** an independent sieve to \(n\), Legendre valuations for
   \(\binom na\), prime-power reconstruction, and a separately implemented
   square-and-multiply exponentiation for \(p^w\).

The routes agree on 155,611 primes through \(n\), 105,726 nonzero prime factors
of \(X\), bit lengths 2,090,874 for \(X\) and 2,090,838 for \(p^w\), all
quotients and window endpoints above, and the following decimal encodings:

```text
sha256(decimal X)   = e2a3e4a63e81ffc3388cf4f33a6592b7ced29f14219b74d5c6d67e9b5036e066
sha256(decimal p^w) = f3cd891754f52acf2ea27de139afeccf396336284d1bb321a9a8bf4b6af9406f
sha256(decimal X mod p^w)
                    = eab3fa93125841b71210ec5881d434852033524e3e72ea9fed7aab3a91c8c465
```

As an independent pruning sanity check, both direct binomials and prime
valuations give

\[
 H_{w+1}=\binom a{w+1}\binom t{w+1}
\]

with bit length 721,939 and decimal SHA-256
`a3d7f5cb854cdbf23260eac5d24bf2c8223a9176011d08ec89590b7b537ef90b`.
Moreover

\[
 (a-w)(t-w)-(w+1)^2=953{,}462{,}079{,}457>0,
\]

so the ambient shells increase through \(e=w+1\); even the maximal viable
multiplier \(4{,}807{,}520\) times the elementary bound
\((w+2)H_{w+1}\) remains below \(p^w\).

Finally, \(p^6\) independently reproduces
\(B^*=\lfloor p^6/2^{128}\rfloor\).

## Rung-ladder audit

### A1: exact unconditional pruned row-sharp Q

Two distinct attacks did not close A1.

1. **Fixed-anchor factorization.**  Rooting a Q support and factoring its common
   intersection reduces exchange shell \(e\) to a degree-\(e-(a-k)\)
   prescribed-prefix divisor problem.  The remaining count is precisely the
   primitive boundary-divisor census identified by `prop:q-boundary-divisor`
   and left open by `conj:q-active`; the factorization does not bound its
   worst fiber.
2. **Moment/Fourier route.**  `prop:q-second-moment` gives the exact pair ledger,
   but `rem:q-not-proved` explicitly records that it is not a max-fiber theorem.
   The deployed finite margin requires a row-dependent worst-fiber statement,
   not a fixed-moment or average estimate.

### A2: unconditional nonvacuous cap below reserve

Three independent routes fail numerically or structurally.

1. The pruned shell universe and Vandermonde bound remain on the scale
   \(\binom na\), whose bit length is 2,090,874, while the reserve is below
   \(2^{59}\).
2. The directional Johnson compiler cannot separate this branch: after the
   sparse translation, the direction already agrees with zero on at least
   \(a\) coordinates, so its strict Johnson premise cannot hold.  Puncturing to
   \(\Sigma\) leaves fewer than \(k\) coordinates and the restricted RS code is
   full.
3. The affine-span/list-separation variant encounters the same common-zero
   obstruction and yields no uniform finite slope cap.

No unconditional A2 integer is claimed.

### A3: one finite residual hypothesis

`KB_TANGENT_ROOTED_Q_SHELL(3,7)` gives the proved compiler and exact viable
window above.  This is the rung delivered by the packet.

### Lower floor and refund/blowup

Two lower constructions were tested in each direction.

1. The universal tangent family is entirely contained in
   \(\mathcal T(r)\), so it produces no tangent-surviving Q floor.
2. The identity-prefix/simple-pole family has \(\mathcal T(r)=\varnothing\)
   and about the full-slice mean number of slopes, but current sources do not
   certify that those slopes lie in the active post-pruning Q cell.  Even its
   total certified slope count is far below the reserve.

No admissible family with certified active-Q membership and
\(|Z_Q|>R\) was found.  There is no `REFUND/REORDER` or `ROW REFUTATION` claim.

## Mandatory adversarial epilogue

The strongest attack found a real defect in the first draft: the tangent-zero
anchor does not exist on column-far received lines, because the frozen contract
sets \(\mathcal T(r)=\varnothing\) there.  That attack invalidated the original
all-line value \(400{,}388{,}953{,}453\).

The final theorem survives because it branches canonically.  Non-column-far
lines use the tangent-zero anchor and the exact cutoff \(e\ge w+2\); column-far
lines use one actual Q support as root and pay the leading one plus all \(t\)
nonzero shells.  Taking the larger branch gives
\(400{,}389{,}155{,}870\).

Additional attacks were checked:

- **support reuse:** two slopes on one noncommon support force joint
  explanation, so selected supports are slope-injective;
- **exact-cardinality mismatch:** selection is from the active boundary Q
  certificate and the integrated exact-card witness catalogue, not from an
  arbitrary trimmed support;
- **off-by-one:** \(w=67{,}471\), the tangent minimum is \(w+2=67{,}473\),
  and the sparse shell count is \(913{,}632\);
- **vacuity:** tangent ratios destroy the exact zero set and the shell cutoff,
  so the sparse proof does not hold verbatim with \(Z\) replacing
  \(Z\setminus\mathcal T(r)\);
- **hidden allocation:** the remaining reserve is reported but not assigned to
  BC or the complement.

The strongest unresolved risk is exactly the named shell hypothesis.  A single
admissible line violating its pointwise inequality falsifies the conditional
atom; the packet does not disguise that input as a proved Q theorem.

## Validation and nonclaims

Run from a full checkout containing this packet:

```text
python3 experimental/scripts/verify_kb_uq_boundary_prefix_tangent_rooted_shell_v1.py --check
python3 -O experimental/scripts/verify_kb_uq_boundary_prefix_tangent_rooted_shell_v1.py --check
python3 experimental/scripts/verify_kb_uq_boundary_prefix_tangent_rooted_shell_v1.py --tamper-selftest
```

The verifier is integer-only, recomputes the large arithmetic twice, checks
source/artifact pins, rejects forbidden proof markers, and mutates both a pinned
artifact and a decisive manifest integer in self-test.  The stdlib-only Lean
package formalizes the two shell-summation compilers and the deployed ledger
arithmetic.  Fork CI, not a local build, is the Lean authority.

This packet does not alter `.github/`, import Mathlib, add a `.lake` directory,
change the partition or owner order, union translations, use the legacy
`422,354,730,332` charge, claim a full Q theorem, pay BC/new, move the endpoint,
or close the row.

# CONDITIONAL
