# Quadratic-completion family at third recurrence depth

## Theorem

Fix d>=1, put

    t=d+3,       R=t+3,       2t-R=d,

and let q tend to infinity through prime powers of characteristic different
from 2 and 3, with q>=t.  On the full domain D=F_q consider

    y_z=e_(t-1)+z e_(t+2),       z in F_q.               (1)

The complete transverse error-pair set of weight at most t is

    P={(z,S): |S|=t, e_1(S)=e_2(S)=0,
               z=e_3(S), w_x=1/Q'_S(x)}.                (2)

It satisfies

    |P|=q^(d+1)/t!+O_d(q^d).                             (3)

Consequently,

    |P| / binom(q,d+1)
      =1/(t(t-1))+O_d(1/q)
      =1/((d+3)(d+2))+O_d(1/q).                         (4)

Thus the polynomial degree d+1 in the sharp complete fixed-deficiency bound
is necessary at recurrence depth three as well as depths one and two.

## Status

PROVED / AUDIT.  The accompanying Lean declarations are explicitly UNPROVED
STATEMENT TARGETS and are not a Lean proof.

The finite replay is over prime fields.  The proof uses only standard
quadratic-character and Schwartz-Zippel facts and applies to all finite fields
in the stated characteristic range.

## Exact description of the pair set

For a t-subset S, barycentric amplitudes w_x=1/Q'_S(x) have moments

    m_0=...=m_(t-2)=0,       m_(t-1)=1,
    m_t=h_1=e_1,
    m_(t+1)=h_2=e_1^2-e_2,
    m_(t+2)=h_3=e_1^3-2e_1e_2+e_3.                     (5)

Therefore the syndrome lies on (1) exactly when e_1=e_2=0, in which case
z=e_3.  As in the depth-two family, the first s moments rule out every
support size s<t by an invertible Vandermonde system.  At size t they uniquely
force the barycentric amplitudes.  This proves completeness of (2).

There are three locator-recurrence rows.  On (1), they successively read

    q_(t-1)=0,       q_(t-2)=0,       q_(t-3)+z q_t=0.

Moving z changes the last row with coefficient q_t=1.  Hence every pair is
transverse.

## Quadratic completion

Put m=t-2=d+1.  For an m-subset A write

    s=e_1(A),       u=e_2(A),

and define

    B_A(X)=X^2+sX+(s^2-u).                               (6)

If B_A has two distinct roots outside A, their union with A is a t-subset
whose first two elementary symmetric sums vanish.  Conversely, if S occurs
in (2) and A is any m-subset of S, the complementary two roots have monic
polynomial (6).  Thus, if G is the number of valid A,

    G=binom(t,2)|P|.                                     (7)

The discriminant of (6) is

    Delta(A)=4e_2(A)-3e_1(A)^2.                          (8)

Let chi be the quadratic character, extended by chi(0)=0.  Before enforcing
distinct coordinates or root avoidance, the indicator of a split,
square-free quadratic is

    (1+chi(Delta)-1_(Delta=0))/2.                        (9)

## Character-sum estimate

Work first with ordered m-tuples.  Hold the first m-1 entries fixed, write
their first two symmetric sums as sigma and eta, and call the last entry x.
Then

    Delta(x)=-3x^2-2 sigma x+(4 eta-3 sigma^2),          (10)

whose discriminant as a quadratic in x is

    16(3 eta-2 sigma^2).                                (11)

For a nondegenerate prefix, the exact one-variable quadratic-character sum
is plus or minus one.  For a degenerate prefix it has magnitude q-1.  The
polynomial 3 eta-2 sigma^2 is nonzero: the coefficient of the square of any
prefix variable is -2.  Schwartz-Zippel therefore leaves only
O_m(q^(m-2)) degenerate prefixes.  Summing (10) over the last coordinate gives

    sum_(a in F_q^m) chi(Delta(a))=O_m(q^(m-1)).         (12)

The locus Delta=0 also has O_m(q^(m-1)) points.  Removing tuples with repeated
coordinates costs O_m(q^(m-1)), so (9), divided by m!, gives

    #{m-subsets A: B_A split and square-free}
      =(1/2)binom(q,m)+O_m(q^(m-1)).                    (13)

It remains to remove completions whose quadratic root lies in A.  For a
fixed coordinate a_i, the condition B_A(a_i)=0 is a nonzero quadratic
polynomial in the ordered tuple: specializing all other coordinates to zero
leaves 3a_i^2.  Schwartz-Zippel and a union bound over i again cost only
O_m(q^(m-1)).  Hence

    G=(1/2)binom(q,m)+O_m(q^(m-1)).                      (14)

Combining (7), m=t-2=d+1, and

    2 m! binom(t,2)=t!

proves (3).  Dividing by binom(q,d+1) proves (4).

## Scope

The count in (3) is not an exact finite formula; small fields can have strong
congruence effects and even empty fixtures.  Repeated slopes also occur, so
this is a sharpness theorem for the complete pair compiler, not a
q^(d+1)-scale distinct-slope MCA/CA lower bound.

The elementary quadratic-completion proof does not extend verbatim to higher
depth.  The separate note all_depth_sparse_split_sharpness.md now supplies an
all-depth theorem using Morse monodromy and finite-field Chebotarev; the
present packet retains the stronger elementary O_d(q^d) error at depth three.

## Exact replay

Run

    python3 experimental/scripts/verify_third_recurrence_quadratic_completion.py --check
    python3 -O experimental/scripts/verify_third_recurrence_quadratic_completion.py --check
    python3 experimental/scripts/verify_third_recurrence_quadratic_completion.py --tamper-selftest
    python3 -O experimental/scripts/verify_third_recurrence_quadratic_completion.py --tamper-selftest

The pinned cases verify the complete support description, all lower-support
Vandermonde obstructions, the quadratic-completion double count, collision
removal, and the exact one-variable character-sum identity.
