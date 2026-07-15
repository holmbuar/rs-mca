# q64 footprint 31: mandatory 30-shadow leave

**Status:** PROVED source-valid replacement for the old q64-footprint-31
packing cap.  This theorem saves `1,493,353,005,097,095` entries in the
official one-row ledger.  It is an unconditional payment, not a residual
conjecture.

## 1. Set-system theorem

Let `B` be a family of 31-subsets of a 64-set such that no two members
contain the same 30-subset.  Equivalently, distinct members have union at
least 33.  Let `L` be the family of 30-subsets contained in no member of
`B`.

Fix a 29-subset `A`.  It has exactly

```text
64-29=35
```

extensions to a 30-subset.  A block `B in B` containing `A` has two points
outside `A` and covers exactly the two 30-extensions obtained by choosing
one of them.  Different blocks containing `A` cover disjoint pairs of
extensions, because a shared 30-extension would lie in two blocks.

The 35 extensions therefore cannot all be partitioned into such pairs.  At
least one is in `L`.  Double-counting flags `(A,T)` with

```text
A subset T in L,  |A|=29, |T|=30
```

gives

```text
30 |L| >= binom(64,29),
|L| >= ceil(binom(64,29)/30).                         (1)
```

Every block contains 31 different 30-subsets, and these shadows are
pairwise disjoint.  Hence

```text
31 |B| <= binom(64,30)-|L|,                           (2)
```

and (1)--(2) prove

```text
|B| <= floor((binom(64,30)-ceil(binom(64,29)/30))/31)
     = 50,774,002,173,301,209.                        (3)
```

The earlier raw shadow cap was

```text
floor(binom(64,30)/31)=52,267,355,178,398,304,
```

so the exact saving is

```text
1,493,353,005,097,095.                                (4)
```

No design-existence assumption occurs: the leave is forced locally by the
odd number 35.

## 2. Literal RS source bridge

At q64 the deployed constants are

```text
n=2^21, K=2^20, L=n/64=32768, K=32L.
```

For two different errors in one fixed syndrome coset, their difference is
a nonzero word of the `[n,n-K,K+1]` moment-kernel GRS code.  If their q64
footprints had union at most 32, that difference would be supported on at
most `32L=K` coordinates, contradicting distance `K+1`.  Thus distinct
q64-footprint-31 errors give a family satisfying the hypothesis above.
Two errors cannot share one footprint for the same reason.  Equation (3)
therefore counts literal errors, not only abstract supports.

All q64 footprints of sizes 0 through 30 retain their previously frozen
caps.  Replacing only the size-31 entry changes the cumulative q64 payment
from

```text
54,024,655,287,584,031
```

to

```text
52,531,302,282,486,936.                               (5)
```

The smaller number is a sharper upper bound on the paid population; the
difference becomes additional residual allowance.

## 3. Compiler consequence

Combine (5) with the three disjoint frozen payments

```text
q64=32, q128=32..47        59,604,759,736,923,812
q64=32, q128=48..54       155,264,635,132,828,620
D7, q128=33..46             5,078,015,114,505,213.
```

The new unconditional subtotal and remaining allowance are

```text
paid =272,478,712,266,744,581,
T-paid=2,375,398,229,443,011.                          (6)
```

For the still-open q128-r47 common-27 owner, a uniform exact multiplicity
cap `L0` would give

```text
M47 <= floor(L0 binom(128,27)/binom(47,27)).           (7)
```

The consecutive compiler values are

```text
L0=6: 2,309,103,404,380,482 < T-paid,
L0=7: 2,693,953,971,777,229 > T-paid.                  (8)
```

Thus six is the new exact closing threshold, with conditional margin

```text
66,294,825,062,529.                                   (9)
```

Equations (7)--(9) are calibration only: this note does not assert the
uniform cap six.  It proves the unconditional q64 leave payment (3)--(6).

## 4. Replay

Run

```text
ruby --disable-gems -w work/verify_q64_r31_mandatory_leave_payment.rb
```

The verifier checks the exact integers, reconstructs the old q64 cap vector,
and exhausts all small odd-extension analogues of the leave double count.
