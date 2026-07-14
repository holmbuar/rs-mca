# All-depth sparse-splitting sharpness

## Theorem

Fix integers d,r>=1 and put

    t=d+r,       R=t+r=2t-d.                             (1)

Fix a prime p with p not dividing t(t-1), and let q=p^nu tend to infinity.
On the full domain D=F_q consider the syndrome line

    y_z=e_(t-1)+z e_(t+r-1),       z in F_q.             (2)

The complete transverse pair set of weight at most t is exactly

    P={(z,S): |S|=t,
               e_1(S)=...=e_(r-1)(S)=0,
               z=(-1)^(r+1)e_r(S),
               w_x=1/Q'_S(x)}.                          (3)

It satisfies

    |P|=q^(d+1)/t!+O_(t,p)(q^(d+1/2)).                  (4)

Therefore the ratio to the sharp complete fixed-deficiency upper bound is

    |P|/binom(q,d+1)
      =(d+1)!/t!+O_(t,p)(q^(-1/2)).                     (5)

In particular, the polynomial exponent d+1 is necessary at every fixed
recurrence depth r.  The positive limiting constant is

    (d+1)!/(d+r)!
      =1/((d+2)(d+3)...(d+r)).                          (6)

## Status

PROVED / LITERATURE-DEPENDENT / AUDIT.  The proof invokes the Morse-polynomial
monodromy theorem and finite-field Chebotarev.  The accompanying Lean module
contains only UNPROVED STATEMENT TARGETS.

This theorem is asymptotic with d, r, and p fixed.  It is not uniform when the
recurrence depth grows with q.

## Exact pair description

For a t-subset S, the barycentric amplitudes have moments

    m_0=...=m_(t-2)=0,       m_(t-1+j)=h_j(S).           (7)

The line (2) therefore forces h_1=...=h_(r-1)=0.  The
triangular relation between complete and elementary symmetric polynomials
makes this equivalent to

    e_1=...=e_(r-1)=0.                                  (8)

Under (8), the same relation gives

    h_r=(-1)^(r+1)e_r,

which proves the slope formula in (3).  Supports smaller than t are impossible
by the initial Vandermonde system, and size-t amplitudes are unique.

The last of the r locator recurrences is

    q_(t-r)+z q_t=0.

Because q_t=1, moving z changes this recurrence.  Every pair in (3) is
transverse.

## Sparse-polynomial translation

The locator of S is

    Q_S(X)=X^t-e_1X^(t-1)+e_2X^(t-2)-... .

Condition (8) says precisely that Q_S belongs to the d+1 parameter family

    F_a(X)=X^t+a_dX^d+a_(d-1)X^(d-1)+...+a_0.           (9)

Conversely, every square-free polynomial in (9) that splits completely over
F_q supplies one unique t-subset in (3).  Its slope is z=-a_d.  Thus |P| is
the number of coefficient vectors a in F_q^(d+1) for which F_a has splitting
type (1,1,...,1).

## Geometric monodromy

Over an algebraic closure of F_p, restrict (9) to

    a_2=...=a_d=0,       a_1=c nonzero,       a_0=-T.

The resulting polynomial is

    f(X)-T=X^t+cX-T.                                    (10)

Its derivative tX^(t-1)+c has t-1 simple roots because p does not divide
t(t-1).  At a critical point beta,

    f(beta)=c(t-1)beta/t,

so distinct critical points have distinct critical values.  Hence f is Morse.
Serre's Morse-polynomial theorem gives geometric Galois group S_t for (10).

The monodromy of a good parameter slice is a subgroup of the geometric
monodromy of the full family (9).  Since the slice already has S_t and the
full group acts on the same t roots, the full geometric group is exactly S_t.
It follows at once that the arithmetic group is also S_t and the splitting
field has no enlarged constant field.

## Chebotarev count

Remove the discriminant hypersurface from A^(d+1).  On this normal open set,
the identity conjugacy class in S_t is exactly the completely split,
square-free specialization type.  Finite-field Chebotarev in dimension d+1
therefore gives

    |P|=(1/|S_t|)q^(d+1)+O_(t,p)(q^(d+1-1/2)),

which is (4).  Equation (5) follows from

    binom(q,d+1)=q^(d+1)/(d+1)!+O_d(q^d).

## Relation to the elementary packets

For r=1, (3) is the canonical depth-one family.  For r=2, translation of
support sums gives the stronger exact formula binom(q,t)/q and limiting ratio
1/t.  For r=3, quadratic completion gives the stronger error O_d(q^d) and
limiting ratio 1/(t(t-1)).  Equations (4)--(6) recover both leading constants.

Those elementary packets remain useful because they avoid Chebotarev and
give sharper finite information.  The present theorem supplies the missing
all-depth bridge.

## Scope

The full-domain construction has only q possible slopes and often repeats
them.  It proves exponent sharpness for the complete pair compiler, not a
q^(d+1)-scale distinct-slope MCA/CA numerator lower bound.  It does not certify
growing d or r, alter a target row, or move a deployed table.

## Sources

- Jean-Pierre Serre, Topics in Galois Theory, Theorem 4.4.5.
- Tianhao Wang, Splitting of Polynomial Families via Galois Theory,
  Theorem 3.7 and Corollary 3.8.
