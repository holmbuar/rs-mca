# Two-regime pole--tangent lower reserve

**Status:** PROVED.

**Hard input served:** 5 — entropy-frontier / quantitative target-reserve
crossing, unsafe lower side.

This note supersedes the proposed-manuscript-change section of
simple_pole_realizability.md and the lower-reserve item L-3 in #524.  It leaves
those integrated notes unchanged.  It builds on scottdhughes's exact
prefix/pole packets, Holm Buar's realizability analysis, and LegaSage's #524
audit anchors.

No manuscript or PDF is changed by this packet.  The paste-ready section below
gives two blocks for possible manual promotion.

## Parameters and conventions

Let \(\mathbb B\subseteq\mathbb F\) be a subfield, let
\(D\subseteq\mathbb B\) have size \(n\), and put
\[
  C=\operatorname{RS}_{\mathbb F}(D,k),\qquad
  1\le k<n,\qquad q=|\mathbb F|>n.
\]
Fix a nonempty challenge set \(\Gamma\subseteq\mathbb F\), write
\(G=|\Gamma|\), choose \(0\le\epsilon\le1\), and use the closed integer-budget
convention
\[
  B^*=\lfloor\epsilon G\rfloor.
\]
For every \(k+1\le a\le n\), set
\[
\begin{aligned}
  L(a)&=\left\lceil\binom na|\mathbb B|^{-(a-k-1)}\right\rceil,\\
  M(L)&=\left\lceil\frac{L(q-n)}{q-n+k(L-1)}\right\rceil,\\
  P(a)&=\left\lceil\frac{G}{q}M(L(a))\right\rceil,\\
  E(a)&=\min\{G,n-a+1\},\\
  U(a)&=\min\left\{G,\binom na\right\}.
\end{aligned}
\]
The numerator \(B_{C,\Gamma}^{\mathrm{MCA}}(a)\) counts distinct challenge
slopes that are support-wise MCA-bad at agreement at least \(a\).  All
explanation and nontriviality tests use the same support.

## Human-readable submission table

| claim id | status | exact content | load-bearing hypotheses | consumer |
| --- | --- | --- | --- | --- |
| combined-reserve | PROVED | \(\max\{P(a),E(a)\}\le B_{C,\Gamma}^{\mathrm{MCA}}(a)\le U(a)\) | \(\mathbb B\le\mathbb F\), \(D\subseteq\mathbb B\), \(q>n\), \(\Gamma\ne\varnothing\), \(k+1\le a\le n\) | hard input 5 lower side |
| upper-half-collapse | PROVED | \(2a>n+k\Rightarrow L(a)=P(a)=1\) | combined-reserve parameters and prefix rigidity | shallow/deep route cut |
| exact-deep | PROVED | \(3(n-a)\le n-k\Rightarrow B_{C,\Gamma}^{\mathrm{MCA}}(a)=E(a)\) | Reed--Solomon row and nonempty \(\Gamma\) | hard input 5 deep leg |
| l3-disposition | AUDIT | the pole floor cannot overshoot in the deep range | upper-half-collapse plus exact-deep | #524 L-3 |

The matching machine-readable record is
experimental/data/certificates/two_regime_lower_reserve.json.  The verifier
recomputes its grid counts and compares the entire JSON object.

## PROVED — Combined finite lower reserve

Under exactly the parameters above,
\[
  \max\{P(a),E(a)\}
  \le B_{C,\Gamma}^{\mathrm{MCA}}(a)
  \le U(a).                                             \tag{1}
\]
Consequently, if \(k+1\le a_-<a_+\le n\) satisfy
\[
  \max\{P(a_-),E(a_-)\}>B^*,
  \qquad U(a_+)\le B^*,
\]
then the closed target threshold exists and
\[
  a_-<a^*\le a_+.
\]
If \(a_+=a_-+1\), then \(a^*=a_+\).

For the pole leg, prop:exact-prefix-list gives a dimension-\((k+1)\) list of
size at least \(L(a)\).  The collision-aware simple-pole theorem converts it
to \(M(L(a))\) distinct full-field bad slopes.  Shearing the received line
translates that slope set; averaging the translates over \(\mathbb F\) gives
at least \(\lceil GM(L(a))/q\rceil=P(a)\) slopes in the arbitrary fixed set
\(\Gamma\).  This uses \(q>n\), \(D\subseteq\mathbb B\), and the fact that
\(\mathbb B\) is a subfield.

The universal tangent floor independently gives the lower bound \(E(a)\).
The exact support atlas gives the upper bound \(U(a)\).  Taking both lower
bounds proves (1), and numerator monotonicity in \(a\) proves the threshold
bracket.

## PROVED — Upper-half collapse and exact deep numerator

For every permitted \(a\),
\[
  2a>n+k\quad\Longrightarrow\quad L(a)=P(a)=1.          \tag{2}
\]
Indeed, put \(w=a-k-1\).  Prefix rigidity says that two distinct
\(a\)-supports in one depth-\(w\) prefix fiber have Johnson distance at least
\(w+1=a-k\).  Their union would have size at least \(2a-k>n\), impossible.
Thus every such fiber has size at most one.  The positive average fiber size
is at most one, so its ceiling \(L(a)\) is one.  Since \(1\le G\le q\),
\(M(1)=1\) and \(P(a)=\lceil G/q\rceil=1\).

On the Reed--Solomon deep window,
\[
  3(n-a)\le n-k
  \quad\Longrightarrow\quad
  B_{C,\Gamma}^{\mathrm{MCA}}(a)=E(a).                 \tag{3}
\]
This is cor:exact-deep-numerator, combining the deep upper theorem with the
universal tangent floor.  Since \(n>k\), the deep hypothesis implies
\(2a>n+k\); therefore (2) also holds there.  The combined reserve is not
claimed exact outside the deep window: only \(E\) is exact in (3).

## AUDIT — Disposition of #524 L-3

The L-3 concern was that the pole expression might overshoot the true deep
numerator.  Equations (2) and (3) decide the issue without an asymptotic
approximation:

- above \(2a>n+k\), the realized pole floor is exactly the trivial value one;
- throughout \(3(n-a)\le n-k\), the tangent floor \(E(a)\) is the exact
  numerator;
- the pole floor can improve the tangent floor only in the shallow band
  \(2a\le n+k\).

Thus max\(\{P,E\}\) is a combined proved lower reserve, not an exact formula
throughout.  No field, challenge-set, denominator, rate, or endpoint
normalization is changed.

## AUDIT — Paste-ready manuscript blocks

These blocks target upstream/main at commit ea4eb07.  Semantic labels control
the replacement; line numbers identify the reviewed snapshot.

### Introduction block

Anchor: after current L714, replace the item beginning at L715 with the
following item.  In the proof-source sentence immediately following the
theorem, add prop:universal-tangent-floor and
thm:unconditional-support-envelope-bracket to the existing cref list.

~~~tex
\item For every challenge set,
      \(B_{C,\Gamma}^{\rm MCA}(a)\le
      \min\{\abs\Gamma,\binom na\}\) exactly.  When
      \(D\subseteq\B\subseteq\F\) and \(\abs\F>n\), let \(P(a)\) be
      as in \textup{(SB1)} and put
      \(E(a)=\min\{\abs\Gamma,n-a+1\}\).  Then a combined
      pole--tangent lower reserve is
      \[
             B_{C,\Gamma}^{\rm MCA}(a)\ge\max\{P(a),E(a)\}.
      \]
      The pole term satisfies \(P(a)=1\) when \(2a>n+k\), while \(E(a)\)
      is exact throughout the deep range.  At the first adjacent
      agreement \(a=k+1\), if
      \(\abs\F>\max\{\binom n{k+1},
      \binom{\binom n{k+1}}2\}\), the full-field numerator is
      exactly \(\binom n{k+1}\), and the adjacent threshold alternatives
      are the literal comparisons in \textup{(AD2)}.
~~~

### Support-envelope block

Anchor: current L6228 is the closing delimiter immediately after (SB2).
Replace the theorem and proof carrying
thm:unconditional-support-envelope-bracket with the complete block below.

~~~tex
\begin{theorem}[Unconditional exact support-envelope bracket]
\label{thm:unconditional-support-envelope-bracket}
Let \(C=\RS_\F(D,k)\), let \(D\subseteq\B\subseteq\F\), put
\(q=\abs\F>n\), fix \(\varnothing\ne\Gamma\subseteq\F\), and let
\(B^*=\floor{\eps\abs\Gamma}\).  For \(k+1\le a\le n\), define
\[
 \begin{split}
 L(a)&=\ceil{\binom na\abs\B^{-(a-k-1)}},\\
 P(a)&=\left\lceil\frac{\abs\Gamma}{q}
       \left\lceil\frac{L(a)(q-n)}
       {q-n+k(L(a)-1)}\right\rceil\right\rceil,\\
 E(a)&=\min\{\abs\Gamma,n-a+1\},\\
 U(a)&=\min\left\{\abs\Gamma,\binom na\right\}.
 \end{split}                                       \tag{SB1}
\]
If \(a_-<a_+\) satisfy
\[
       \max\{P(a_-),E(a_-)\}>B^*,\qquad U(a_+)\le B^*, \tag{SB2}
\]
then the global target threshold exists and
\[
                         a_-<a^*\le a_+.            \tag{SB3}
\]
If \(a_+=a_-+1\), then \(a^*=a_+\) exactly.  In particular,
\[
                  \binom n{k+1}\le B^*\quad\Longrightarrow\quad
                  a^*=k+1.                         \tag{SB4}
\]
Moreover,
\[
  2a>n+k\quad\Longrightarrow\quad L(a)=P(a)=1,     \tag{SB5}
\]
and on the deep window
\[
  3(n-a)\le n-k\quad\Longrightarrow\quad
  B_{C,\Gamma}^{\rm MCA}(a)=E(a).                  \tag{SB6}
\]
Thus the pole floor can improve the tangent floor only in the shallow
range \(2a\le n+k\); in the deep range the tangent floor is the exact
numerator.
These are unconditional finite comparisons; \textup{(SB2)} is the
literal target reserve and contains no asymptotic placeholder.
\end{theorem}

\begin{proof}
The exact prefix list and pole-line construction give
\(B_{C,\Gamma}^{\rm MCA}(a)\ge P(a)\) by
\cref{prop:simple-pole-lower}, while
\cref{prop:universal-tangent-floor} gives
\(B_{C,\Gamma}^{\rm MCA}(a)\ge E(a)\).  The exact support atlas gives
\(B_{C,\Gamma}^{\rm MCA}(a)\le U(a)\) by
\cref{prop:exact-support-upper}.  Thus \(a_-\) is unsafe and \(a_+\) is
safe; monotonicity proves \textup{(SB3)} and the adjacent conclusion.
For \textup{(SB4)}, the first permitted agreement is already safe.

For \textup{(SB5)}, put \(w=a-k-1\).  By
\cref{prop:prefix-rigidity-full}, two distinct \(a\)-supports in one
depth-\(w\) prefix fiber have Johnson distance at least
\(w+1=a-k\).  Their union would therefore have size at least
\(a+(a-k)=2a-k>n\), a contradiction.  Every prefix fiber has size at
most one, so the positive pigeonhole floor \(L(a)\) is one.  Since
\(\Gamma\ne\varnothing\) and \(\abs\Gamma\le q\), the definition in
\textup{(SB1)} then gives \(P(a)=1\).  Finally,
\textup{(SB6)} is \cref{cor:exact-deep-numerator}; its hypothesis implies
\(2a>n+k\) because \(n>k\), so the pole floor is indeed trivial there.
\end{proof}
~~~

## Reproduction

Run from any directory:

~~~text
python3 experimental/scripts/verify_two_regime_lower_reserve.py
~~~

The wrapper reruns verify_pole_realizability.py and then checks the current
source anchors, dependency labels, theorem formulas, paste blocks, and
non-promotion scope.  Expected final line:

~~~text
RESULT: PASS (7 packet checks; base verifier 18 checks)
~~~

## Risk limits

This packet proves only the finite comparison, the upper-half pole collapse,
and the exact deep numerator under the printed hypotheses.  It does not prove
the safe profile envelope, O5c, O7, an all-normalization crossing, an
asymptotic closure, a deployed threshold, or a prize threshold.
