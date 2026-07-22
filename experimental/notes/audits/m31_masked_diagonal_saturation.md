# M31 masked diagonal saturation: successive minima close the padding terminal

## Status

**PROVED `MASKED_DIAGONAL_SATURATION` / #1014 UNMASKED COUNTERPACKET
RETAINED / MERSENNE-31 LIST ROW OPEN / LEDGER MOVEMENT ZERO.**

This is the exact successor packet to
`experimental/notes/audits/m31_padding_bridge_audit.md` (upstream PR #1014).
That audit correctly refutes direct transport of the already named low
actual-error Forney rows through the canonical padding factors.  The present
packet does not retract that counterexample.  It proves a different and
stronger invariant statement: after passing to the coordinatewise
`Q_i`-divisible submodule, the successive minima can only increase, while the
diagonal map subtracts the same exact padding degree from every minimum.
Together with the source theorem's largest-index floor and the primitive padded
row's total-degree identity, this forces a new canonical padded rank-three
frame with exactly the old deployed bounds.

Consequently the blocked bands

```text
j <= 960,363
j <= 918,833
```

are not merely narrowed.  They are covered uniformly for every marked source
key at every interior weight `j <= R`.

The theorem is pointwise on the existing `259,881` marked rank-46 source keys.
It changes no source key, codeword, ordered first-agreement selector, root-status
mask, semantic owner, refund, or signed occupancy credit.  It pays only the
algebraic terminal `UNPAID_MASKED_DIAGONAL_SATURATION`; common-core add-back,
the rank-two coloop branch, row-sharp `U_Q`, list-interior coverage, and the
adjacent safe row remain open.

## 1. Deployed source object

Use the Mersenne-31 adjacent list-row constants

```text
p  = 2^31-1,
n  = 2^21              = 2,097,152,
K  = 2^20              = 1,048,576,
a  = 1,116,023,
w  = a-K               = 67,447,
R  = n-a               = 981,129,
B* = 16,777,215.
```

The occupancy-sensitive source theorem in
`experimental/notes/thresholds/m31_canonical_popov_rank46_compiler.md` keeps the
signed identity

```text
|L_R(y)| = 16,517,335 + Xi_46
```

and proves that a forbidden list forces

```text
Xi_46 >= 259,881.
```

It therefore supplies at least `259,881` distinct marked source keys

```text
(j, ordered 45-anchor tuple, distinguished extra support),
```

without discarding the unused-capacity credits in equation (5.4) of that note.
Fix one such key.  Divide the common actual-error locator from its 46 columns.
The resulting primitive actual-error locator row is

```text
P=(P_1,...,P_46),       deg P_i=e=j-c,
```

where `c` is the common actual-error-core degree.  Its syzygy module has rank
45 and ordered Forney indices

```text
mu_1 <= ... <= mu_45.
```

The inherited non-surjectivity theorem gives the load-bearing last-index floor

```text
mu_45 >= K-j+1.                                      (1.1)
```

The canonical first-`a` selector supplies, in each column, a discarded-
agreement padding locator `Q_i` of the common degree

```text
d=R-j.
```

Put

```text
W_i=P_i Q_i.
```

Every `Q_i` and every root-status mask is determined by the same fixed ordered
domain and first-agreement stopping rule already attached to the source key.

## 2. The #1014 diagonal bridge

Theorem 2.1 of the predecessor audit proves the exact module isomorphism

```text
Delta_Q : Syz(W) -> DSat_Q(Syz(P)),
Delta_Q(B_1,...,B_46)=(Q_1B_1,...,Q_46B_46),
```

where

```text
DSat_Q(Syz(P))
  ={A in Syz(P): Q_i divides A_i for every i}.
```

Because all `Q_i` have degree `d`, every nonzero row degree is shifted by
exactly `d`.

Let

```text
nu_1 <= ... <= nu_45
```

be the successive minima of the diagonal-divisible submodule in the ambient
actual-error degree filtration.  Let

```text
lambda_1 <= ... <= lambda_45
```

be the Forney indices of `Syz(W)`.  The exact shift gives

```text
nu_i=lambda_i+d                                        (2.1)
```

for every `i`.

The `RS[F_11,D,4]` counterpacket in the predecessor audit proves that a named
minimal actual-error row need not lie in `DSat_Q(Syz(P))`.  Equation (2.1) does
not assert otherwise.  The rows realizing `nu_i` and `lambda_i` may be new
linear combinations.

## 3. General lemma: successive minima under a full-rank submodule

### Lemma 3.1 (successive-minimum monotonicity)

Let `F` be a field, let `R=F[X]`, and let `N subset M subset R^t` be free
`R`-modules of the same finite rank `r`.  Use vector degree

```text
deg(v)=max_i deg(v_i)
```

and write the ordered minimal-basis degrees of `M` and `N` as

```text
alpha_1 <= ... <= alpha_r,
beta_1  <= ... <= beta_r.
```

Then

```text
beta_k >= alpha_k                  for every 1 <= k <= r. (3.1)
```

**Proof.**  For a free polynomial module `L`, define its `k`-th successive
minimum by

```text
sigma_k(L)=min {s : L contains k R-linearly independent rows of degree <=s}.
```

The predictable-degree theorem for a row-reduced minimal basis identifies
`sigma_k(L)` with its `k`-th ordered basis degree.  Every independent
`k`-tuple in `N` is also an independent `k`-tuple in `M`, so the admissible set
for `N` is contained in the admissible set for `M`.  Hence

```text
sigma_k(N) >= sigma_k(M),
```

which is (3.1). `QED`

Apply the lemma to

```text
N=DSat_Q(Syz(P)) subset Syz(P)=M.
```

The diagonal bridge shows that `N` has the same rank 45.  Therefore

```text
nu_i >= mu_i                       for every i.           (3.2)
```

This is the missing invariant in the predecessor packet.  It does not transport
a particular actual-error basis; it compares the intrinsic successive minima
of the two modules.

## 4. Uniform masked last-index floor

Combining (1.1), (2.1), and (3.2) at the largest index gives

```text
lambda_45+d = nu_45 >= mu_45 >= K-j+1.
```

Since `d=R-j`, the weight cancels exactly:

```text
lambda_45 >= K-R+1 = 67,448.                           (4.1)
```

This is valid at every interior weight `j<=R`, including both bands in which
direct transport of the old rows is degree-impossible.

The cancellation is the central point.  A large padding degree blocks a low
actual-error row from being directly divisible by all `Q_i`, but the same large
degree is subtracted from the intrinsic masked minimum when it is pulled back
to the padded module.

## 5. Primitive padded total degree and the rank-46 bound

The row `W` may have an additional common gcd formed by mixed-status or common
padding roots.  Divide it out and call the primitive padded row `W'`.  This
changes no syzygy module:

```text
Syz(W')=Syz(W).
```

Every entry before this last division has degree

```text
e+d=(j-c)+(R-j)=R-c,
```

so the primitive row degree `E` satisfies

```text
E <= R.
```

For a primitive 46-column polynomial row, the Forney-index sum is its row
degree.  Hence

```text
sum_(i=1)^45 lambda_i = E <= R.                         (5.1)
```

Using (4.1),

```text
sum_(i=1)^44 lambda_i
  <= R-67,448
   = 913,681.                                           (5.2)
```

The exact ordered-sequence extremizer from the rank-46 source theorem now
applies unchanged.  Since

```text
913,681 = 44*20,765 + 21,
```

and the remainder `21` is smaller than `44-k` for `k=1,2,3`, one obtains

```text
lambda_1                         <= 20,765,
lambda_1+lambda_2                <= 41,530,
lambda_1+lambda_2+lambda_3       <= 62,295 < 67,447.     (5.3)
```

For the third inequality, the integer contradiction is especially transparent:
if the first three summed to at least `62,296`, then
`lambda_3>=20,766`; the remaining 41 indices through `lambda_44` are each at
least `20,766`, so

```text
sum_(i=1)^44 lambda_i
  >= 62,296 + 41*20,766
   = 913,702
   > 913,681,
```

contradicting (5.2).

Thus every marked source key has three independent **canonical padded** syzygy
rows whose combined degree is below the shifted-locator cutoff.  Under the
diagonal map their masked degrees satisfy the exact shifted bound

```text
nu_1+nu_2+nu_3
 =lambda_1+lambda_2+lambda_3+3(R-j)
 <=62,295+3(R-j).                                      (5.4)
```

Equations (5.3)--(5.4) are the required masked diagonal-saturation certificate.

## 6. Source-key and ledger preservation

The construction is pointwise and does not repartition the source family.  For
each marked key it performs only this operation:

```text
same marked key and metadata
  -> attach the intrinsic padded minimal frame supplied by (5.3).
```

In particular it retains, literally:

1. the received center and exact codewords;
2. the exact weight `j`, ordered domain, ordered 45 anchors, and distinguished
   extra support;
3. the canonical first-`a` selector;
4. every actual-error and discarded-agreement root-status mask;
5. the already supplied semantic owner, if any;
6. every refund vector; and
7. every signed occupancy-credit vector.

No source key is selected, deleted, duplicated, or merged.  Therefore the list
of source-key identifiers and its length are unchanged, the `259,881` floor is
unchanged, and every signed aggregate remains unchanged.  In particular the
exact crossing

```text
16,517,335 + 259,881 = 16,777,216 = B*+1
```

and the allowance `259,880` are preserved rather than recomputed with credits
dropped.

This is a transport theorem for the algebraic certificate, not a new semantic
owner.  It can be inserted at the existing padding terminal without touching
the queued semantic-owner modules owned by upstream #1009 and fork PR #64.

## 7. Relation to the predecessor counterpacket

The predecessor's two `F_11` orderings remain a mandatory regression:

```text
same actual-error frame
  does not determine direct divisibility of its named minimal row.
```

The present theorem proves instead:

```text
full-rank masked submodule
  has intrinsic successive minima no smaller than the ambient module;
exact common degree shift
  converts its last-index floor into a weight-independent padded floor;
primitive padded total degree
  forces a new low rank-three padded frame.
```

There is no contradiction.  The old minimal row may fail to transport while a
different minimal basis of the masked/padded module realizes (5.3).

## 8. Lean certificate

The stdlib-only module

```text
experimental/lean/m31_q_rooted_shell/
  M31QRootedShell/MaskedDiagonalSaturation.lean
```

kernel-checks:

- every deployed constant in (4.1)--(5.4);
- the shifted last-index deduction from explicit source, inclusion, and shift
  premises;
- the prefix-44 cap and all three rank-46 integer bounds;
- the exact contradiction thresholds `913704`, `913703`, and `913702`;
- coverage of both direct-transport blocked bands;
- the exact signed crossing and `259,881` source-key floor; and
- a typed list compiler preserving source IDs, ordered selectors, root masks,
  semantic owners, refunds, signed credit vectors, and both aggregate sums.

The module deliberately does not introduce polynomial rings, row-reduced bases,
or Forney theory.  Lemma 3.1 and the polynomial deductions are proved in this
note; Lean checks the complete deployed arithmetic and metadata-preservation
compiler under those explicit premises.  The source/Lean boundary is recorded
in `MASKED_DIAGONAL_SATURATION_CORRESPONDENCE.md`.

## 9. Verdict and remaining obligations

```text
PROVED_MASKED_DIAGONAL_SATURATION
```

The predecessor terminal

```text
UNPAID_MASKED_DIAGONAL_SATURATION
```

is discharged on all marked rank-46 source keys.  The next terminals remain,
unchanged:

```text
UNPAID_COMMON_CORE_ADD_BACK
UNPAID_RANK2_COLOOP
UNPAID_ROW_SHARP_Q
UNPAID_LIST_INTERIOR_COVERAGE
UNPAID_ADJACENT_ROW_CLOSURE.
```

No completion atom is banked in this packet because the padded rank-three frame
still needs the already separated common-core/coloop compiler and a disjoint
owner/payment.  No stable-paper TeX, deployed radius, official score, or prize
claim changes.
