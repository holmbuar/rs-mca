# Identity-crossing localization and upper-half lower-route cut

**Status:** PROVED / AUDIT / ROUTE CUT.

This packet audits the O7 intermediate-crossing residual isolated in
experimental/notes/thresholds/lower_reserve_unsafe_side_coverage_audit.md.
That residual asks for an unsafe construction near an identity crossing lying
strictly above the half boundary \((n+k)/2\) and below the exact deep regime.
In the fixed-rate scope printed there, this band cannot contain the identity
target crossing.

The key point is finite and elementary.  The identity coefficient field
contains the \(n\)-point domain, so its bit size
\(\beta=\log_2|\mathbb B|\) is at least \(\log_2 n\).  At every nonnegative
target superlevel,
\[
 H_2(\rho+g)-\beta g\ge\tau\ge0,
\]
and \(H_2\le1\), hence \(g\le1/\beta\le1/\log_2n\).  A fixed-rate crossing is
therefore \(O(n/\log n)=o(n)\) agreement steps from \(k+1\), while the half
boundary is a linear distance away.

The integrated challenge-restricted syndrome-secant lower formula also has
ceiling exactly one above the half boundary.  Independently, Holm Buar proves
in PR #699 the profile-list coupling lemma showing that no
dimension-\(k+1\) profile list reaches O7.  This packet does not re-claim that
result.

This does not prove the complete lower-reserve input.  It relocates the genuine
question to the shallow exact-\(k+1\) seam and keeps the O5c work in PR #699
separate.

Target sources:

- experimental/asymptotic_rs_mca_frontiers.tex, especially
  cor:intro-identity-frontier and eq:intro-target-crossing;
- experimental/notes/thresholds/lower_reserve_unsafe_side_coverage_audit.md,
  route O7;
- experimental/notes/thresholds/syndrome_secant_challenge_lower.md.

Verifier:

    python3 experimental/scripts/verify_identity_crossing_upper_half_route_cut.py

It is deterministic, stdlib-only, writes no files, checks the source anchors,
and replays finite analytic, list, and exact syndrome-secant grids.

## 1. Target-superlevel localization

Let \(n\ge2\), \(1\le k_n<n\), and let
\(D_n\subseteq\mathbb B_n\), \(|D_n|=n\).  Put
\[
 \rho_n=\frac{k_n}{n},\qquad
 \beta_n=\log_2|\mathbb B_n|,\qquad
 \tau_n=\frac1n\log_2(1+B_n^*)\ge0,
\]
and define
\[
 F_n(g)=H_2(\rho_n+g)-\beta_ng,
\]
\[
 g_{T,n}=\sup\bigl(\{g\in[0,1-\rho_n]:
 F_n(g)\ge\tau_n\}\cup\{0\}\bigr).
\]

### Theorem 1 (finite target-superlevel localization)

For every such row,
\[
 g_{T,n}\le\frac1{\beta_n}\le\frac1{\log_2n}.       \tag{1}
\]
The conclusion does not require the crossing to be interior or transverse.

#### Proof

Since \(D_n\subseteq\mathbb B_n\), one has
\(|\mathbb B_n|\ge n\), hence
\(\beta_n\ge\log_2n>0\).  For every \(g\) in the target superlevel set,
\[
 \beta_ng
 \le H_2(\rho_n+g)-\tau_n
 \le H_2(\rho_n+g)
 \le1.
\]
Thus every such \(g\) is at most \(1/\beta_n\).  The adjoined point zero
satisfies the same bound, so taking the supremum proves (1). \(\square\)

The use of \(\tau_n\ge0\) is load-bearing.  It follows from the manuscript's
literal target definition \(B_n^*\ge0\); no zero-target specialization is
being substituted.  The localization remains true at \(B_n^*=0\), although
the universal tangent floor then makes every agreement unsafe and the target
threshold is undefined.  Any threshold-bracket application below therefore
also assumes a nonzero viable budget and an independently certified safe row.

### Corollary 1.1 (fixed-rate O7 is empty)

Assume \(k_n/n\to\rho\in(0,1)\), and put the real crossing coordinate
\[
 A_{T,n}=k_n+1+g_{T,n}n.
\]
Then
\[
 A_{T,n}-(k_n+1)\le\frac n{\log_2n}=o(n),           \tag{2}
\]
and, for all sufficiently large \(n\),
\[
 2A_{T,n}\le n+k_n.                                 \tag{3}
\]
Consequently every integer agreement
\(a_n=A_{T,n}+o(n)\) also lies below the half boundary eventually.

Indeed, (2) is (1).  Moreover,
\[
 n+k_n-2A_{T,n}
 =n-k_n-2-2g_{T,n}n.
\]
After division by \(n\), the first term tends to \(1-\rho>0\), while
\(2/n+2g_{T,n}\to0\).  This proves (3), with a linear margin that absorbs
any \(o(n)\) rounding or reserve displacement.

The O7 premise in the integrated coverage audit assumes both fixed rate and
\[
 \frac{n+k_n}{2}<a_n<
 \left\lceil\frac{2n+k_n}{3}\right\rceil.
\]
Corollary 1.1 shows that its left inequality is eventually impossible.
The appropriate verdict is therefore

    O7: EMPTY IN FIXED-RATE IDENTITY-CROSSING SCOPE.

It is not an open request for a new upper-half construction.

### Corollary 1.2 (varying-rate guard)

If an above-half identity crossing is allowed along a varying-rate sequence,
then
\[
 n-k_n<2g_{T,n}n+2
 \le\frac{2n}{\beta_n}+2
 \le\frac{2n}{\log_2n}+2=o(n).                      \tag{4}
\]
Thus even in that extension the whole interval from \(k_n+1\) to the alleged
upper-half crossing has sublinear width.  An unsafe \(k_n+1\) anchor would
already meet the threshold bracket's \(o(n)\) lower-localization requirement.
Equation (4) does not itself prove that the anchor is unsafe.

## 2. Relationship to PR #699

Holm Buar proves in PR #699 the min-distance coupling statement that every
relevant dimension-\(k+1\) profile list has size at most one above
\(2a>n+k\), and develops the O5c quotient/Chebyshev/remainder conversions.
That result is logically independent of Theorem 1: crossing localization uses
only \(D_n\subseteq\mathbb B_n\), nonnegativity of the target, and
\(H_2\le1\).

This packet uses the profile-list fact only as an audited consistency check.
It neither consumes PR #699 as a load-bearing input nor makes a new O5c claim.

## 3. The syndrome-secant lower formula also collapses

Use the notation of the integrated challenge-restricted syndrome-secant
theorem:
\[
 R=n-k,\qquad t=n-a,\qquad N_t=\binom nt,
\]
\[
 S_t(q)=\sum_{j=0}^t
 \binom tj\binom{n-t}{t-j}q^{\max(j,2t-R)}.
\]
For a nonempty challenge set of size \(1\le G\le q\), its raw lower quantity
is
\[
 X_{\rm sec}=
 \frac{G N_t q^{2t}(q^R-q^t)}
 {q^{2R}S_t(q)},                                    \tag{5}
\]
and the certified lower numerator is \(\lceil X_{\rm sec}\rceil\).

### Theorem 2 (upper-half syndrome-secant route cut)

If \(2a>n+k\), then
\[
 0<X_{\rm sec}<1,\qquad
 \lceil X_{\rm sec}\rceil=1.                        \tag{6}
\]

#### Proof

The upper-half condition is \(2t<R\).  Hence
\(\max(j,2t-R)=j\) for every \(0\le j\le t\), and \(q^j\ge1\).  Vandermonde's
identity therefore gives
\[
 S_t(q)\ge
 \sum_{j=0}^t\binom tj\binom{n-t}{t-j}
 =\binom nt=N_t.
\]
Using \(G\le q\) and \(q^R-q^t<q^R\) in (5),
\[
 X_{\rm sec}
 <\frac{G N_t q^{2t}q^R}{q^{2R}N_t}
 =Gq^{2t-R}
 \le q^{1+2t-R}
 \le1,
\]
where the last inequality uses the integer gap \(2t<R\).  It is positive
because \(G>0\), \(q>1\), and \(t<R\).  This proves (6).
\(\square\)

Theorem 2 concerns the value supplied by this particular lower-bound
compiler.  It does not say that the true MCA numerator is one.  The universal
tangent floor can still be larger.  The strict half-boundary hypothesis is
essential: for example, \(q=3,n=3,k=1,a=2,G=3\) has \(2a=n+k\), raw
value \(6/5\), and ceiling two.  The case \(t=0\) is included in Theorem 2:
\(N_t=S_t(q)=1\) and the raw quantity remains strictly between zero and one.
The argument also includes \(q=n\) and invokes no collision-aware pole
compiler; that separate compiler requires \(q>n\).

## 4. What replaces O7

The actual fixed-rate identity crossing coordinate is shallow and satisfies
\[
 A_{T,n}-(k_n+1)=O(n/\log n)=o(n).
\]
Hence an exact unsafe certificate at \(k_n+1\) is already close enough for the
asymptotic lower side.  The integrated syndrome-secant theorem supplies the
finite criterion
\[
 \left\lceil
 \frac{G(q-1)\binom n{k+1}}
 {q\bigl(\binom n{k+1}+q-1\bigr)}
 \right\rceil>B^*.                                  \tag{7}
\]
Whenever (7) holds, \(k+1\) is a valid unsafe anchor within \(o(n)\) of the
identity crossing.  To consume it in a threshold bracket, assume in addition
\(1\le B^*<G\) and a certified safe upper agreement.

The two terminal targets need no O7 construction.  At \(B^*=0\) no agreement
is safe; at \(B^*=G\), the numerator is always at most \(G\) and the threshold
starts at \(k+1\).

For a row sequence put \(q_n=|\mathbb F_n|\),
\(G_n=|\Gamma_n|\), and
\(B_n^*=\lfloor\epsilon_nG_n\rfloor\).  If
\(k_n/n\to\rho\in(0,1)\), \(\log q_n=o(n)\), and
\(\limsup\epsilon_n<1\), the integrated theorem proves that (7) holds
eventually, with \(q,G,B^*\) in (7) read as \(q_n,G_n,B_n^*\), uniformly in
the nonempty challenge sets.  In that scope the
unsafe lower-side localization formerly assigned to O7 is paid at \(k_n+1\);
this statement does not supply the safe side or threshold existence.

Outside that scope, for nonterminal normalizations
\(1\le B_n^*<G_n\) where (7) is not certified, the remaining problem is the
exact \(k+1\) seam or another explicit shallow lower construction.  It is not
an upper-half intermediate crossing.

## 5. Audit impact

The integrated lower-reserve coverage audit currently counts O5c and O7 as
two coupled OPEN routes.  The corrected classification is:

| Route | Corrected status | Reason |
|---|---|---|
| upper-half profile-list size-at-most-one coupling | **OUT OF SCOPE; PROVED IN PR #699** | credited, not claimed or consumed here |
| O5c quotient/Chebyshev/remainder conversions | **OUT OF SCOPE; PARTIAL IN PR #699** | deep remainder remains open there |
| O7 fixed-rate upper-half identity crossing | **EMPTY IN SCOPE** | Theorem 1 and Corollary 1.1 |
| fixed-rate shallow unsafe localization under \(\log q=o(n)\), \(\limsup\epsilon<1\) | **PAID LOWER LEG** | exact \(k+1\) syndrome criterion plus (2); safe leg separate |
| other nonterminal field/target normalizations | **OPEN EXACT \(k+1\) SEAM** | (7), an exact safe ceiling, or another shallow certificate decides the seam |

This correction does not unconditionalize the full frontiers theorem, prove
the closed safe envelope, or discharge O5c.  It removes one impossible
geometric location from hard input 5 and states the surviving lower-side
question at the correct agreement scale.

## 6. Claim ledger

| Claim | Status |
|---|---|
| \(g_{T,n}\le1/\beta_n\le1/\log_2n\) for every nonnegative target superlevel | **PROVED** |
| Fixed-rate identity crossings lie below half and \(o(n)\) from \(k+1\) | **PROVED** |
| An above-half varying-rate crossing forces \(n-k_n=o(n)\) | **PROVED** |
| PR #699 profile-list size-at-most-one coupling is consistent with the localization | **AUDIT ONLY / NOT RE-CLAIMED** |
| Integrated syndrome-secant lower formula has ceiling one above half | **PROVED** |
| O7 as printed in the coverage audit is a genuine fixed-rate open band | **REFUTED / EMPTY IN SCOPE** |
| Exact \(k+1\) unsafe lower anchor for nonterminal targets under the integrated subexponential-\(q\) hypotheses | **PROVED LOWER LEG** |
| Exact \(k+1\) seam decision for remaining nonterminal field and target normalizations | **OPEN** |
| O5c, closed safe envelope, full hard input 5, or prize threshold | **NOT CLAIMED** |

## 7. Reproduction

From the repository root:

    python3 experimental/scripts/verify_identity_crossing_upper_half_route_cut.py

The verifier prints the checked parameter families, exact object, theorem
targets, and final PASS status.  It uses no randomness and emits no files.
