# Direct Sidon payment normalization audit

## Status

COUNTEREXAMPLE_NEW_FLOOR for the literal quantitative primitive-leaf
interface; OPEN GAP for the intended deployed smooth residual/direct Sidon
payment.

This packet retires the former scalar toy rows. They supplied an average fiber
size independently of their fiber tables and used either non-Boolean points or
a zero energy exponent. They therefore did not instantiate the live
Sidon-heavy definition.

The verifier now derives, and never accepts as input,

\[
M=\sum_{s:f_s>0} f_s,\qquad
L=\#\{s:f_s>0\},\qquad
\bar N=M/L.
\]

## Genuine fixed-cut witness

The replacement is the existing C9 block/trade family at \(k=5\), rebuilt as
an explicit source map on fixed-weight Boolean supports:

\[
N=20,\quad m=10,\quad
\Phi(x)=\left(|x|,\sum_t x_t t\bmod p\right),
\quad p=505020040141.
\]

There are 152 distinct supports and 121 nonempty image fibers: one fiber has
size 32 and the other 120 are singletons. Hence

\[
M=152,\qquad L=121,\qquad \bar N=\frac{152}{121}.
\]

The size-32 fiber has exact Boolean additive energy

\[
E=7776,\qquad \Delta=\frac{E}{32^3}=\frac{243}{1024}.
\]

With the fixed positive cutoff

\[
\sigma=\frac{\log(4/3)}8,\qquad
e^{-\sigma N}=0.4871392896\ldots>\Delta
\]

and logarithmic sample order \(q=3\), the singleton fibers lie outside the
cut and

\[
\mathcal G^{\rm Sid}_{q,\sigma}
=\frac1{121}\left(\frac{32}{152/121}\right)^3
=\frac{937024}{6859}.
\]

Thus

\[
\frac{\log\mathcal G^{\rm Sid}_{q,\sigma}}{Nq}
=0.0819524539508972>0.05.
\]

The generator uses bit-mask difference histograms. The independent checker
rebuilds 20-coordinate tuples and uses pair-sum histograms.

## Scope boundary

This is a genuine finite failure of the literal quantitative interface and
replays the asymptotic C9 family. It does not show that the family survives
the intended C1--C8 first-match residual, and it is not asserted to belong to
the deployed smooth-domain rows. The intended direct-Sidon hard input
therefore remains open.

## Replay

    python3 experimental/scripts/verify_sidon_direct_payment.py --emit-defaults
    python3 experimental/scripts/verify_sidon_direct_payment.py --check
    python3 -O experimental/scripts/verify_sidon_direct_payment.py --check
    python3 experimental/scripts/verify_sidon_direct_payment.py --tamper-selftest
    python3 -O experimental/scripts/verify_sidon_direct_payment.py --tamper-selftest
    python3 experimental/scripts/verify_sidon_direct_payment_check.py --check
    python3 -O experimental/scripts/verify_sidon_direct_payment_check.py --check
    python3 experimental/scripts/verify_sidon_direct_payment_check.py --tamper-selftest
    python3 -O experimental/scripts/verify_sidon_direct_payment_check.py --tamper-selftest

Observed:

    generator witness checks: 19/19; pins: 5/5
    generator tamper self-test: 14/14
    independent checks: 16/16
    independent tamper self-test: 15/15
    payload_sha256: f909a8d5f24168de45bcc867cd6bd169d9446c3b13b9e12fdb5259c4a87cdead
