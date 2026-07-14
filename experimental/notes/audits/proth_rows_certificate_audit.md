# Adversarial arithmetic + definition audit of the four certified Proth rows

## Status

AUDIT. Independent finite-arithmetic, primality-certificate, sign-condition,
and field/endpoint-bookkeeping recomputation of the four certified Proth
prime rows in `experimental/rs_mca_thresholds.tex`, at all four official
rates. Verdict headline: every printed constant reproduces, all four Proth
witnesses are valid, and the displayed signs
`F_{n,k}(B-1) >= 0 > F_{n,k}(B)` hold in every row. No arithmetic gap found.
This note audits the certificate arithmetic only; it does not re-derive the
MCA staircase theorems the rows are built on (see Nonclaims).

## The two asks this packet answers

Both asks are taken verbatim from `experimental/rs_mca_thresholds_audit.md`.

Ask (a), adversarial audit. From that file's Status section:

> "The four Proth rows are printed with enough integer data for independent
> checking, but they should still receive a separate adversarial arithmetic and
> definition audit before being promoted into Paper D or treated as final prize
> submission authority."

and from Recommended Next Steps item 2:

> "Independently verify the four Proth certificates and the displayed
> `F_{n,k}(B-1) >= 0 > F_{n,k}(B)` signs."

Ask (b), machine-readable packet. From Recommended Next Steps item 3:

> "Add a small machine-readable JSON packet for the four Proth rows."

This note answers (a); the packet
`experimental/data/certificates/proth-rows/proth_rows.json` answers (b);
`experimental/scripts/verify_proth_rows_certificate_audit.py` recomputes every
number reported here and in the packet.

## Definitions consumed (quoted from the source)

Each definition is quoted from `experimental/rs_mca_thresholds.tex` so the
audit is anchored to the exact wording, not to labels.

- Quadratic form, line 1840:
  `For \(F_{n,k}(r)=r^2-n(3r-(n-k))\), the exact boundary checks are`.
  Repeated line 3902-3904: `Put \(R=n-k\) and \[ F_{n,k}(r)=r^2-n(3r-R). \]`
  The two spellings are the same polynomial `r^2 - 3nr + n(n-k)`.
- Boundary root, line 1336-1337:
  `r_{\rm quad}(n,k)= \floor{\frac{3n-\sqrt{n(5n+4k)}}2}`, the smaller root of
  `r^2-3nr+n(n-k)=0` (line 1351).
- Official-rate form, line 1510-1511:
  `r_\rho(n)=\floor{ n\frac{3-\sqrt{5+4\rho}}2}`. Under `rho=k/n` this is the
  same real number as `r_quad(n,k)`, hence the same floor (line 1522:
  `since the displayed integer is r_{\rm quad}(n,k)`).
- Budget, line 422: `B=\floor{p\,2^{-128}}`; table caption line 1810:
  `B=\floor{p/2^{128}}=r_\rho(n)+1`.
- Sign locator, line 1868-1870:
  `They also satisfy \(F_{n,k}(B-1)\ge0>F_{n,k}(B)\).  Since
  \(F_{n,k}'(r)=2r-3n<0\) on \([0,n]\), these two signs locate its smaller
  root and give \(B-1=r_\rho(n)=r_{\rm quad}(n,k)\).`
- Proth certificate PC1, line 1857-1858:
  `p=u\,2^s+1,\qquad u\text{ odd},\qquad u<2^s,\qquad a_0^{(p-1)/2}\equiv-1\pmod p.`
- Row arithmetic PC2, line 1863-1864:
  `n\mid p-1,\qquad p<2^{256},\qquad B\,2^{128}\le p<(B+1)2^{128}`.
- Sampler and target, line 411-413: the affine MCA sampler of `\cite{ABF26}`,
  `\gamma` uniform in `\F`, target `\eps^*=2^{-128}`.
- Endpoint convention, line 419-426: safe set `\left[0,\frac Bn\right)`,
  `The endpoint \(B/n\) is unsafe`, largest safe integer radius `B-1`, first
  unsafe integer radius `B`; conversion lemma line 3886-3891 (closed integer
  Hamming ball, `r=\floor{\delta n}` errors, safe reals `[0,(n-a_0+1)/n)`).
- Window compiler hypothesis, line 1529-1532:
  `1\le B\le M_\rho(n) \defeq\min\{r_\rho(n)+1,n-k-1\}`, applied by
  prop:appendix-certificate-verification at line 4027, with the tangent floor
  invoked at radius `B` because `B\le n-k-1` (line 1550).

## Per-row constant audit

Every printed constant is recomputed with Python big integers only (no
numpy/sympy/sage, no floating point in any pass/fail path). `k=2^40` and
the challenge set is the full field `Gamma=F_p`, so `|Gamma|=p`.

### rho = 1/2 (tex: table line 1818, p line 1828, u line 1835, F line 1844, cert line 3964, remainder line 3989)

| printed constant | printed value | recomputed | verdict |
|---|---|---|---|
| n | 2^41 | 2199023255552 | reproduces |
| p | 132540169958804033333249306710494641010898987122689 | equal | reproduces |
| bits(p) | 167 | 167 | reproduces |
| (s, a0) | (92, 3) | s=92, a0=3 valid witness (smallest) | reproduces |
| u | 26766274163673319604503 | equal, odd, u<2^92 | reproduces |
| p = u*2^s+1 | -- | holds | reproduces |
| a0^((p-1)/2) mod p | p-1 | p-1 | reproduces |
| n \| p-1, p<2^256 | -- | both hold | reproduces |
| B = floor(p/2^128) | 389500552609 | 389500552609 | reproduces |
| B* = floor(2^-128 * p) | (= B) | 389500552609 | B* = B |
| r_p = p - B*2^128 | 1381541083842484386787422633985 | equal, in (0,2^128) | reproduces |
| F_{n,k}(B-1) | 5154112775168 | 5154112775168 (>= 0) | reproduces, sign OK |
| F_{n,k}(B) | -663955886271 | -663955886271 (< 0) | reproduces, sign OK |
| r_quad = B-1 | 389500552608 | 389500552608 (F-sign locator) | reproduces |
| 1 <= B <= n-k-1 | -- | 1 <= B <= 1099511627775 | hypothesis holds |
| safe set | [0, B/2^41) | half-open, endpoint unsafe | reproduces |

### rho = 1/4 (tex: table line 1819, p line 1829, u line 1836, F line 1845, cert line 3965, remainder line 3990)

| printed constant | printed value | recomputed | verdict |
|---|---|---|---|
| n | 2^42 | 4398046511104 | reproduces |
| p | 411940680852499481698306614369841346700408394874881 | equal | reproduces |
| bits(p) | 169 | 169 | reproduces |
| (s, a0) | (93, 13) | s=93, a0=13 valid witness (smallest) | reproduces |
| u | 41595378994516821279015 | equal, odd, u<2^93 | reproduces |
| a0^((p-1)/2) mod p | p-1 | p-1 | reproduces |
| B = floor(p/2^128) | 1210584858040 | 1210584858040 | reproduces |
| B* = floor(2^-128 * p) | (= B) | 1210584858040 | B* = B |
| r_p | 2921538492713497448761933168641 | equal, in (0,2^128) | reproduces |
| F_{n,k}(B-1) | 7590647904465 | 7590647904465 (>= 0) | reproduces, sign OK |
| F_{n,k}(B) | -3182321912768 | -3182321912768 (< 0) | reproduces, sign OK |
| r_quad = B-1 | 1210584858039 | 1210584858039 | reproduces |
| 1 <= B <= n-k-1 | -- | 1 <= B <= 3298534883327 | hypothesis holds |
| safe set | [0, B/2^42) | half-open, endpoint unsafe | reproduces |

### rho = 1/8 (tex: table line 1820, p line 1830, u line 1837, F line 1846, cert line 3966, remainder line 3991)

| printed constant | printed value | recomputed | verdict |
|---|---|---|---|
| n | 2^43 | 8796093022208 | reproduces |
| p | 979947269755402568812854322316630667196565607677953 | equal | reproduces |
| bits(p) | 170 | 170 | reproduces |
| (s, a0) | (95, 5) | s=95, a0=5 valid witness (smallest) | reproduces |
| u | 24737346889219389259839 | equal, odd, u<2^95 | reproduces |
| a0^((p-1)/2) mod p | p-1 | p-1 | reproduces |
| B = floor(p/2^128) | 2879806199253 | 2879806199253 | reproduces |
| B* = floor(2^-128 * p) | (= B) | 2879806199253 | B* = B |
| r_p | 2495687119199326634196634435585 | equal, in (0,2^128) | reproduces |
| F_{n,k}(B-1) | 13908181940112 | 13908181940112 (>= 0) | reproduces, sign OK |
| F_{n,k}(B) | -6720484728007 | -6720484728007 (< 0) | reproduces, sign OK |
| r_quad = B-1 | 2879806199252 | 2879806199252 | reproduces |
| 1 <= B <= n-k-1 | -- | 1 <= B <= 7696581394431 | hypothesis holds |
| safe set | [0, B/2^43) | half-open, endpoint unsafe | reproduces |

### rho = 1/16 (tex: table line 1821, p line 1831, u line 1838, F line 1847, cert line 3967, remainder line 3992)

| printed constant | printed value | recomputed | verdict |
|---|---|---|---|
| n | 2^44 | 17592186044416 | reproduces |
| p | 2121285573237585848299875619011192262679065433997313 | equal | reproduces |
| bits(p) | 171 | 171 | reproduces |
| (s, a0) | (97, 5) | s=97, a0=5 valid witness (smallest) | reproduces |
| u | 13387194060291799253121 | equal, odd, u<2^97 | reproduces |
| a0^((p-1)/2) mod p | p-1 | p-1 | reproduces |
| B = floor(p/2^128) | 6233898019554 | 6233898019554 | reproduces |
| B* = floor(2^-128 * p) | (= B) | 6233898019554 | B* = B |
| r_p | 20440865928680199099134339186689 | equal, in (0,2^128) | reproduces |
| F_{n,k}(B-1) | 19335616403905 | 19335616403905 (>= 0) | reproduces, sign OK |
| F_{n,k}(B) | -20973145690236 | -20973145690236 (< 0) | reproduces, sign OK |
| r_quad = B-1 | 6233898019553 | 6233898019553 | reproduces |
| 1 <= B <= n-k-1 | -- | 1 <= B <= 16492674416639 | hypothesis holds |
| safe set | [0, B/2^44) | half-open, endpoint unsafe | reproduces |

## Adversarial attack modes (route-scoped verdicts)

1. **Wrong field denominator / merged ledger.** VERDICT: NO ISSUE. Each row is
   a prime field `F_p`, so `q_gen = q_line = q_chal = |F| = p` and the base
   subfield equals the ambient field (no extension). The full-field affine
   sampler (line 411-412) makes `|Gamma| = |F| = p`. No large extension field
   is used to pay any deficit. There is nothing to merge.

2. **Endpoint convention mismatch (closed ball vs open).** VERDICT: NO ISSUE.
   The closed integer Hamming ball (line 3886-3888) permits `r = floor(delta n)`
   errors, giving a half-open safe set `[0, B/n)` with unsafe endpoint. The
   sign pair `F(B-1) >= 0 > F(B)`, together with `F' < 0` on `[0,n]` and
   `B <= n` (checked), places the smaller root in `(B-1, B]`, so the largest
   safe integer radius is `B-1` and the first unsafe integer radius is `B`,
   exactly as printed (P2, line 428-430). Grid vs supremum bookkeeping
   (`delta*_grid = (B-1)/n`, `delta*_sup = B/n`) is internally consistent
   (line 210-213).

3. **Off-by-one in B vs B* = floor(eps* Q_row).** VERDICT: NO ISSUE. With
   `Q_row = |Gamma| = |F| = p` and `eps* = 2^-128`, the budget
   `B* = floor(2^-128 * p) = floor(p / 2^128) = B` in every row (checked). The
   remainder identity `p = B*2^128 + r_p` with `0 < r_p < 2^128` (line 3983-3997)
   confirms `B = floor(p/2^128)` exactly. No off-by-one.

4. **Definition drift between certificate F and theorem F.** VERDICT: NO ISSUE.
   `F_{n,k}(r) = r^2 - n(3r - (n-k))` (line 1840) and
   `F_{n,k}(r) = r^2 - n(3r - R)` with `R = n-k` (line 3902-3904) are the same
   polynomial `r^2 - 3nr + n(n-k)`, which is exactly the quadratic whose smaller
   root defines `r_quad` (line 1351) and `r_rho` (line 1510). No drift between
   the certificate section and the staircase theorem it feeds.

5. **A printed constant that does not reproduce.** VERDICT: NO ISSUE. All 143
   recomputations agree with the printed values (verifier `RESULT: PASS
   (143/143)`), including the four field orders, the four odd coefficients `u`,
   the boundary values `F(B-1)`, `F(B)`, the four remainders `r_p`, the bit
   lengths, and `B`.

6. **A Proth certificate whose witness fails.** VERDICT: NO ISSUE. For each row
   `a0^((p-1)/2) == -1 (mod p)` holds with the printed `a0 in {3, 13, 5, 5}`,
   `u` is odd with `u < 2^s`, so `2^s > sqrt(p)` and Proth's theorem certifies
   primality. Each printed `a0` is also the smallest witness `a >= 2`, and a
   fixed-base Miller-Rabin cross-check (bases 2..37) independently returns prime
   for all four `p`.

### Advisory (not a gap): compute r_quad by sign, never by integer sqrt

The paper locates the boundary by the sign condition, which is the correct
choice: evaluating the printed closed form as `floor((3n - isqrt(n(5n+4k)))/2)`
with an integer square root **overshoots by 1** for `rho in {1/2, 1/4, 1/8}`
(it is correct only for `rho = 1/16`), because the discriminant is a non-square
and the sqrt-floor does not commute with the outer halving. The rigorous value
`r_quad = ` largest `r` with `F_{n,k}(r) >= 0` equals `B-1` in all four rows,
matching the paper. This is only a warning for any future implementation or
Lean port: keep the F-sign locator, do not substitute an isqrt closed form.
The manuscript itself is unaffected.

## Hypotheses that must travel with the conclusion (visibility)

The safe-set conclusion `[0, B/n)` is not a consequence of the arithmetic
alone. It is produced by cor:prize-window-compiler (line 1526-1554) via
prop:appendix-certificate-verification (line 4015-4030), whose stated
hypothesis is `1 <= B <= M_rho(n) = min(r_rho(n)+1, n-k-1)`. Because
`B = r_rho(n)+1` here, the binding constraint is `B <= n-k-1`, needed so the
universal tangent floor applies at radius `B` (line 1550). This audit checks
`1 <= B <= n-k-1` for all four rows (it holds), and records it explicitly so
it is not dropped on promotion.

## Nonclaims

- This is an arithmetic and definition audit. It does **not** re-prove the
  MCA mean-overlap staircase (thm:quadratic-mean-overlap, cor:mean-overlap-exact,
  cor:prize-rate-overlap), the universal tangent floor
  (prop:universal-tangent-floor), or the window/endpoint compilers. Those
  theorems are what convert `F(B-1) >= 0 > F(B)` into the exact safe set; the
  audit only confirms the finite inputs they consume are correct.
- Primality rests on Proth's theorem via the recorded witness. The fixed-base
  Miller-Rabin cross-check is corroboration, not a standalone proof at 167-171
  bits.
- Scope is the four prime-field Proth rows only. The `F_{17^32}` deep-regime
  row (cor:intro-f17-row) is an extension-field row and is out of scope here.
- No priority or novelty claim is assessed; the manuscript itself notes the
  numerical consequences also follow from the cited literature (line 446-450).
  This audit takes no position on attribution.

## Reproduce

```
python3 experimental/scripts/verify_proth_rows_certificate_audit.py
python3 experimental/scripts/verify_proth_rows_certificate_audit.py --tamper-selftest
```

The first prints `RESULT: PASS (143/143)`; the second corrupts each guarded
datum in turn and confirms every corruption is caught. Data packet:
`experimental/data/certificates/proth-rows/proth_rows.json`.
