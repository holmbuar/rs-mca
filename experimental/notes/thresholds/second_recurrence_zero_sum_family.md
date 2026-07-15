# Exact zero-sum family at second recurrence depth

## Theorem

Let F=F_q, take the full domain D=F, and fix

    t>=3,       R=t+2,       d=2t-R=t-2,
    char(F) does not divide t.

Index syndrome coordinates from zero and consider the nonconstant line

    y_z=e_(t-1)+z e_(t+1),       z in F.                 (1)

For every t-subset S put

    Q_S(X)=product_(x in S)(X-x),
    w_x=1/Q'_S(x).

Then the complete transverse error-pair set on (1), across all weights at
most t, is exactly

    P={(z,S): |S|=t, sum_(x in S)x=0,
               z=-e_2(S), w_x=1/Q'_S(x)}.               (2)

In particular,

    |P|=binom(q,t)/q.                                    (3)

The sharp complete fixed-deficiency compiler gives

    |P|<=binom(q,d+1)=binom(q,t-1),

and this family has the exact ratio

    |P| / binom(q,t-1) = (q-t+1)/(qt)
                       -> 1/t = 1/(d+2).                 (4)

Consequently, for every fixed d>=1, the exponent d+1 in the complete pair
bound is necessary already at recurrence depth two (t=d+2, R=d+4).  This is
not only the depth-one canonical equality family.

## Status

PROVED / AUDIT.  The accompanying Lean file contains explicitly labelled
UNPROVED STATEMENT TARGETS; it is not a Lean proof.

The exact Python replay checks prime-field instances.  The proof below works
over every finite field subject to the displayed characteristic condition.

## Proof

### Barycentric moments

For a t-subset S, the standard Lagrange coefficient identity gives

    sum_(x in S) x^j/Q'_S(x)
     =0                    for 0<=j<=t-2,
     =1                    for j=t-1,
     =h_(j-t+1)(S)         for j>=t,                    (5)

where h_i is the complete homogeneous symmetric polynomial.  Thus the first
R=t+2 moments of the error in (2) are

    (0,...,0,1,e_1(S),h_2(S)).

Since h_2=e_1^2-e_2, this syndrome lies on (1) exactly when

    e_1(S)=sum S=0,       z=-e_2(S).                     (6)

### Completeness and transversality

There is no line point with support size s<t.  Its first s moments vanish, so
the s by s Vandermonde system forces all amplitudes to vanish, contradicting
the coordinate m_(t-1)=1.

At support size t, the first t moments uniquely force the barycentric
amplitudes in (5).  The next two moments then force (6).  Hence (2) is the
complete pair set, not a selected subfamily.

The locator recurrence for Q_S(X)=sum_(i=0)^t q_i X^i has two rows.  On the
line (1) they read

    q_(t-1)=0,       q_(t-2)+z q_t=0.                    (7)

The second equation changes with coefficient q_t=1 when z moves.  Therefore
the whole line is not contained in the support span: every pair in (2) is
transverse.

### Exact count

Translation by c in F maps a t-subset S bijectively to S+c and changes its
sum by t c.  Multiplication by t is bijective under the characteristic
hypothesis.  All q support-sum fibers therefore have the same size.
Partitioning all binom(q,t) supports proves (3).

Finally,

    (binom(q,t)/q) / binom(q,t-1)=(q-t+1)/(qt),

which proves (4).

## What this does and does not show

This is an interior sharpness result for the complete pair compiler.  Many
supports can have the same slope z=-e_2(S); the exact fixtures already show
this.  Since the full domain has only q field elements, the construction does
not give a distinct-slope MCA/CA numerator lower bound of order q^(d+1).

The depth-one superincreasing canonical family remains the current owner of
the exact distinct-slope numerator equality.  No sharp constant is claimed
for arbitrary depth-two lines, no target row moves, and no deployed table
changes.

## Exact replay

Run

    python3 experimental/scripts/verify_second_recurrence_zero_sum_family.py --check
    python3 -O experimental/scripts/verify_second_recurrence_zero_sum_family.py --check
    python3 experimental/scripts/verify_second_recurrence_zero_sum_family.py --tamper-selftest
    python3 -O experimental/scripts/verify_second_recurrence_zero_sum_family.py --tamper-selftest

The pinned certificate covers nine prime-field cases through q=13,
deficiencies one through five, 3,236 top supports, 6,180 lower-support
Vandermonde checks, and 828 locator-recurrence checks.
