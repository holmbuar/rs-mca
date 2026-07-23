# Base-field coordinate-span confinement for RS-MCA syndrome lines

## Status and provenance

`PROVED LOCAL / ZERO PAYMENT`.

This note records the theorem layer that survived the R42 Role 13
same-author repair and an independent hostile proof audit. The proof is
source-pinned to
`fb6d9555339b43911c59c498373c43ed6c5cd391`, tree
`fa7b8d86cb5b65fed52e427648161a9397f19670`.

- repaired artifact SHA-256:
  `fa90f2e10fde920d293f7947f027ba02159f9863c8aa3e62975a1f77ba609f86`;
- hostile-audit packet SHA-256:
  `fec01fd7f9350f02f4c1a3ef31ea7899d77d365bc21183799c411e8ed0e979ec`;
- frozen audit text SHA-256:
  `f6456d6fec2ca247b75be89f335d8544eb5588d13a2b60137d8dddcc1d2d97f4`;
- hostile verdict: `ACCEPT_NARROWED`.

The packet-local delta is the intrinsic coordinate-span formulation,
same-support ratio confinement, the rank-sensitive orbit bound, the exact
rank-one anchor-grid bijection, and the rank-\((1,2)\) radial decomposition.
The source already contains the syndrome-line compiler, subfield
confinement for base-field-valued pairs, and the \(p+1\) bound for
base-rational projective lines; those are imported, not claimed as new.

The audit required two documentary qualifications. The repair's test suite
contains 27 theorem-boundary, contract, portability, and archive-tamper
checks, not 27 independent mathematical mutations. Its overlap scan is a
machine phrase/anchor scan plus manual review of returned hits, not a
machine proof of novelty.

## 1. Typed source reduction

Let \(B=\mathbb F_p\subseteq F\) be finite fields, let \(D\subseteq B\) have \(|D|=n\), and let
\[
C_B=\operatorname{RS}_B(D,k),\qquad C=\operatorname{RS}_F(D,k),\qquad R=n-k.
\]
Choose a matrix \(H\in B^{R\times n}\) of rank \(R\) with \(\ker_BH=C_B\). For \(r\in F^D\), put
\[
s(r)=Hr^{\mathsf T}\in F^R.
\]

### Extension-of-scalars check

Used over \(F\), the same matrix satisfies \(\ker_FH=C\). Indeed, choose a \(B\)-basis \(e_1,\ldots,e_m\) of \(F\). Every polynomial \(f\in F[X]_{<k}\) has a unique expansion \(f=\sum_i e_if_i\) with \(f_i\in B[X]_{<k}\). Hence
\[
H(f(x))_{x\in D}^{\mathsf T}
 =\sum_i e_iH(f_i(x))_{x\in D}^{\mathsf T}=0,
\]
so \(C\subseteq\ker_FH\). A nonzero \(R\times R\) minor over \(B\) remains nonzero over \(F\), so \(H\) has rank \(R\) over \(F\). Both spaces therefore have \(F\)-dimension \(k\), proving equality.

For \(E\subseteq D\), if \(h_x\) is the column of \(H\) indexed by \(x\), define
\[
V_E=\operatorname{span}_F\{h_x:x\in E\}.
\]
This is exactly the set of syndromes of words supported on \(E\). Because every \(h_x\) is \(B\)-valued, every \(B\)-linear map \(T:F\to F\), applied coordinatewise to \(F^R\), preserves \(V_E\):
\[
T\!\left(\sum_{x\in E}a_xh_x\right)=\sum_{x\in E}T(a_x)h_x\in V_E.
\tag{1.1}
\]

Fix agreement \(a\) and put \(t=n-a\). The frozen syndrome-line normal form says that a finite parameter \(\gamma\in F\) is genuinely MCA-bad for a syndrome pair \((y_0,y_1)\) precisely when one actual set \(E\subseteq D\), \(|E|\le t\), satisfies
\[
y_0+\gamma y_1\in V_E,
\qquad
\{y_0,y_1\}\not\subseteq V_E.
\tag{1.2}
\]
The same \(E\) occurs in both conditions.

For \(y=(y_1,\ldots,y_R)\in F^R\), define
\[
L_B(y)=\operatorname{span}_B\{y_1,\ldots,y_R\}\subseteq F,
\qquad
\rho_B(y)=\dim_B L_B(y).
\tag{1.3}
\]
Changing the \(B\)-row basis of \(H\) leaves \(L_B(y)\) unchanged: every new syndrome coordinate is a \(B\)-linear combination of the old coordinates, and the inverse row change gives the reverse inclusion. Codeword translation leaves the syndrome unchanged. Under the syndrome identification
\[
F^D/C\cong F\otimes_B(B^D/C_B)\cong F^R,
\]
\(L_B(y)\) is the smallest \(B\)-subspace \(U\subseteq F\) for which the quotient class lies in \(U\otimes_B(B^D/C_B)\). To see minimality, use the syndrome row basis to identify \(B^D/C_B\cong B^R\): membership in \(U\otimes_BB^R\) is exactly the statement that every syndrome coordinate belongs to \(U\), so every admissible \(U\) contains their \(B\)-span. Projective rescaling obeys the covariance law
\[
L_B(\lambda y)=\lambda L_B(y),\qquad \rho_B(\lambda y)=\rho_B(y)
\quad(\lambda\in F^\times);
\tag{1.4}
\]
only the rank, not the literal subspace, is invariant under arbitrary \(F^\times\)-rescaling.

## 2. Projective bad sets and basis changes

For \([\alpha:\beta]\in\mathbb P^1(F)\), call the parameter projectively bad when some \(E\), \(|E|\le t\), satisfies
\[
\alpha y_0+\beta y_1\in V_E,
\qquad
\{y_0,y_1\}\not\subseteq V_E.
\tag{2.1}
\]
The official affine chart is \([1:\gamma]\); \([0:1]\) is its point at infinity.

When \(y_0,y_1\) are \(F\)-independent, (2.1) depends only on their two-dimensional syndrome plane. Replacing the ordered basis by another \(F\)-basis merely applies a projective bijection to the parameter set, while the transversality condition is unchanged. Consequently every basis-specific upper bound below may be minimized over all ordered \(F\)-bases of the same plane.

## 3. Same-support ratio confinement

### Theorem 3.1

Assume \(y_0,y_1\ne0\). Every genuinely bad nonzero finite parameter satisfies
\[
\gamma\in L_B(y_0)L_B(y_1)^{-1}
:=\{vw^{-1}:0\ne v\in L_B(y_0),\ 0\ne w\in L_B(y_1)\}.
\tag{3.1}
\]
The conclusion uses the same witness \(E\) as (1.2).

If \(s=\rho_B(y_0)\) and \(u=\rho_B(y_1)\), then
\[
|Z_{\rm aff}(y_0,y_1;t)|
\le 1+\frac{(p^s-1)(p^u-1)}{p-1}.
\tag{3.2}
\]
For an \(F\)-independent pair,
\[
|Z_{\mathbb P}(y_0,y_1;t)|
\le 2+\frac{(p^s-1)(p^u-1)}{p-1}.
\tag{3.3}
\]
Thus, for a two-dimensional syndrome plane \(P\),
\[
|Z_{\mathbb P}(P;t)|
\le
\min_{(x,y)\text{ an ordered }F\text{-basis of }P}
\left(2+\frac{(p^{\rho_B(x)}-1)(p^{\rho_B(y)}-1)}{p-1}\right).
\tag{3.4}
\]

### Proof

Fix a bad \(\gamma\ne0\) and one witness \(E\). Put \(U_i=L_B(y_i)\). If \(U_0\cap\gamma U_1=\{0\}\), define on the direct sum \(U_0\oplus\gamma U_1\) a \(B\)-linear projection that fixes \(U_0\) and kills \(\gamma U_1\), and extend it to a \(B\)-linear map on \(F\). Applying it coordinatewise to (1.2), using (1.1), gives \(y_0\in V_E\). The complementary projection gives \(\gamma y_1\in V_E\), hence \(y_1\in V_E\), contradicting transversality. Therefore
\[
U_0\cap\gamma U_1\ne\{0\}.
\]
Choose \(0\ne v=\gamma w\) with \(v\in U_0\), \(w\in U_1\). Then \(\gamma=v/w\), proving (3.1).

The diagonal action
\[
c\cdot(v,w)=(cv,cw),\qquad c\in B^\times,
\]
on \((U_0\setminus\{0\})\times(U_1\setminus\{0\})\) is free, every orbit has exactly \(p-1\) elements, and \(v/w\) is constant on each orbit. Hence the ratio set has size at most
\[
\frac{(p^s-1)(p^u-1)}{p-1}.
\]
Adding the affine parameter \(0\) proves (3.2). Adding the two projective endpoints proves (3.3). Basis invariance from Section 2 proves (3.4). ∎

### Exact exceptional cases

- If \(y_0=y_1=0\), there is no bad affine or projective parameter.
- If \(y_1=0\ne y_0\), no finite parameter is bad; projectively the unique zero combination \([0:1]\) is bad.
- If \(y_0=0\ne y_1\), the affine bad set is exactly \(\{0\}\), the unique zero combination.
- More generally, if \(y_0,y_1\) are \(F\)-dependent and not both zero, the projective bad set consists exactly of their unique zero combination. In particular its size is one.

For the last assertion, every nonzero combination is a scalar multiple of the common nonzero syndrome. Membership in \(V_E\) would then put both generators in \(V_E\), violating transversality. The zero combination is witnessed by \(E=\varnothing\).

## 4. Rank-one projective strata

A projective syndrome point \([y]\) has coefficient rank one when \(\rho_B(y)=1\).

### Corollary 4.1: secants

If a two-dimensional syndrome plane contains two distinct rank-one projective points, choose representatives \(x,y\) of those points and rescale them independently into \(B^R\setminus\{0\}\). They form an \(F\)-basis. Their \(F\)-line is therefore a \(B\)-rational projective line: its rank-one points are exactly \([ax+by]\) with \([a:b]\in\mathbb P^1(B)\), hence there are \(p+1\) of them. In this normalized chart, (3.1) confines every nonendpoint bad parameter to \(B^\times\), so
\[
|Z_{\mathbb P}|\le(p-1)+2=p+1.
\tag{4.1}
\]
The normalized chart has at most \(p\) bad finite parameters. That \(p\) bound is chart-specific; an arbitrary pre-existing affine chart is safely bounded by the projective value \(p+1\).

This separates the projective strata as follows:

1. dependent syndrome pairs: the zero-combination case above;
2. rank-one secant planes: at least two rank-one points, closed by (4.1);
3. rank-one tangent planes: exactly one rank-one point, compiled exactly in Section 5 but not numerically closed;
4. rank-one-disjoint planes: no rank-one projective point, not bounded by the anchor compiler.

The numerical \(p+1\) stratum overlaps the frozen source statement for \(B\)-rational lines and is not claimed as packet-new.

## 5. Exact rank-one anchor compiler

Let \(x,y\in F^R\) be \(F\)-independent, assume \(\rho_B(x)=1\), and rescale \(x\) so that \(x\in B^R\setminus\{0\}\). Let \(U=L_B(y)\) have \(B\)-basis \(u_1,\ldots,u_r\). Expanding every coordinate of \(y\) in this basis gives unique vectors \(v_j\in B^R\) such that
\[
y=\sum_{j=1}^r u_jv_j.
\tag{5.1}
\]
The vectors \(v_1,\ldots,v_r\) are \(B\)-linearly independent: their row rank equals the dimension of the span of the coordinate coefficient columns, and those columns span \(B^r\) because the coordinates of \(y\) span all of \(U\).

Define
\[
\mathcal G_t(x;v_1,\ldots,v_r)=
\left\{c\in B^r\setminus\{0\}:\begin{array}{l}
\exists E\subseteq D,\ |E|\le t,\ x\notin V_E,\\
v_j+c_jx\in V_E\quad(1\le j\le r)
\end{array}\right\}.
\tag{5.2}
\]
Then
\[
c\longmapsto\left(\sum_{j=1}^r c_ju_j\right)^{-1}
\tag{5.3}
\]
is a bijection from \(\mathcal G_t\) onto the bad finite parameters \(\gamma\ne0\) in the normalized chart \(x+\gamma y\).

### Proof

Let \(\gamma\ne0\) be bad through \(E\), and put \(z=\gamma^{-1}\). Multiplying the incidence by \(z\) gives
\[
zx+y\in V_E.
\tag{5.4}
\]
Transversality forces \(x\notin V_E\): if \(x\in V_E\), then (5.4) gives \(y\in V_E\). If \(z\notin U\), then \(Bz\cap U=\{0\}\). A \(B\)-linear projection fixing \(Bz\) and killing \(U\), applied coordinatewise to (5.4), gives \(zx\in V_E\), hence \(x\in V_E\), contradiction. Thus \(z\in U\setminus\{0\}\).

Write uniquely \(z=\sum_jc_ju_j\). Extend each dual coordinate functional on \(U\) to a \(B\)-linear map \(F\to F\). Applying the \(j\)-th functional coordinatewise to
\[
zx+y=\sum_j u_j(c_jx+v_j)\in V_E
\]
and using (1.1) gives \(c_jx+v_j\in V_E\) for every \(j\), on the same \(E\). Hence \(c\in\mathcal G_t\).

Conversely, if one \(E\) satisfies (5.2), multiply the \(j\)-th membership by \(u_j\) and sum. This gives \(zx+y\in V_E\), where \(z=\sum_jc_ju_j\ne0\), and therefore \(x+z^{-1}y\in V_E\). Since \(x\notin V_E\), the incidence is transverse. Uniqueness of the coefficient vector and field inversion proves bijectivity. ∎

### Exact endpoint identities

Let
\[
I_x=\mathbf 1\{\exists E,\ |E|\le t:\ x\in V_E,\ y\notin V_E\},
\tag{5.5}
\]
\[
I_y=\mathbf 1\{\exists E,\ |E|\le t:\ y\in V_E,\ x\notin V_E\}.
\tag{5.6}
\]
Then exactly
\[
|Z_{\rm aff}(x,y;t)|=I_x+|\mathcal G_t|,
\qquad
|Z_{\mathbb P}(x,y;t)|=I_x+|\mathcal G_t|+I_y.
\tag{5.7}
\]
Here \(I_x\) is \(\gamma=0\), while \(I_y\) is the projective point at infinity. For a different affine parameterization, use the projective equality and delete that chart's own point at infinity.

## 6. Exact radial compiler for rank profile \((1,2)\)

Assume \(r=2\). Let
\[
\mathcal D=\{(1,m):m\in B\}\cup\{(0,1)\},
\tag{6.1}
\]
the full set of \(p+1\) normalized directions in \(\mathbb P^1(B)\). Every \(c\in B^2\setminus\{0\}\) has a unique factorization
\[
c=ad,
\qquad a\in B^\times,\ d\in\mathcal D.
\tag{6.2}
\]
For \(d=(d_1,d_2)\), put
\[
w_d=d_2v_1-d_1v_2.
\tag{6.3}
\]
Because \(v_1,v_2\) are \(B\)-independent, \(w_d\ne0\) for every \(d\in\mathcal D\). Let \(j(d)=1\) when \(d_1\ne0\), and \(j(d)=2\) otherwise. Define
\[
\mathcal R_d=
\left\{a\in B^\times:\begin{array}{l}
\exists E\subseteq D,\ |E|\le t,\ x\notin V_E,\\
w_d\in V_E,\\
v_{j(d)}+ad_{j(d)}x\in V_E
\end{array}\right\}.
\tag{6.4}
\]
Then
\[
\mathcal G_t
=\bigsqcup_{d\in\mathcal D}\{ad:a\in\mathcal R_d\},
\qquad
|\mathcal G_t|=\sum_{d\in\mathcal D}|\mathcal R_d|.
\tag{6.5}
\]

### Proof

Put \(A_i=v_i+ad_ix\). If both component conditions \(A_1,A_2\in V_E\) hold, then
\[
d_2A_1-d_1A_2=d_2v_1-d_1v_2=w_d\in V_E.
\tag{6.6}
\]
Conversely, if \(d_1\ne0\), membership of \(A_1\) and \(w_d\) recovers
\[
A_2=d_1^{-1}(d_2A_1-w_d)\in V_E.
\]
If \(d_1=0\), then \(d=(0,1)\), \(w_d=v_1=A_1\), and the selected condition is \(A_2\in V_E\). Thus (6.4) is equivalent to the two component conditions on one literal common support. The unique factorization (6.2) makes the union disjoint and preserves distinct parameter counting.

The scalar \(a=0\) is excluded because it gives \(c=0\), hence \(z=\gamma^{-1}=0\). This is the projective-infinity branch whose actual badness is governed separately by \(I_y\); it is not a finite nonzero parameter. Directions with either coordinate zero are included in \(\mathcal D\). ∎

## 7. KoalaBear specialization and exact nonclosure

For the deployed row,
\[
\begin{aligned}
p&=2^{31}-2^{24}+1=2{,}130{,}706{,}433,\\
|F|=p^6&=93{,}571{,}093{,}019{,}388{,}561{,}295{,}270{,}373{,}781{,}649{,}880{,}353{,}786{,}165{,}192{,}103{,}559{,}169,\\
n&=2^{21}=2{,}097{,}152,\\
k&=2^{20}=1{,}048{,}576,\\
a&=1{,}116{,}048,\qquad t=n-a=981{,}104,\\
B^*&=\left\lfloor p^6/2^{128}\right\rfloor=274{,}980{,}728{,}111{,}395{,}087.
\end{aligned}
\]
The closed radius is \(t/n=61{,}319/131{,}072\).

Rank-one secant planes obey
\[
|Z_{\mathbb P}|\le p+1=2{,}130{,}706{,}434,
\]
with margin
\[
B^*-(p+1)=274{,}980{,}725{,}980{,}688{,}653.
\]
For rank profile \((1,2)\), the raw projective orbit bound is
\[
p^2+1=4{,}539{,}909{,}903{,}627{,}583{,}490>B^*.
\]
Define
\[
M_{12}=\left\lfloor\frac{B^*-2}{p+1}\right\rfloor=129{,}056{,}130.
\]
A theorem \(|\mathcal R_d|\le M_{12}\) for every one of the \(p+1\) directions would imply
\[
|Z_{\mathbb P}|\le2+(p+1)M_{12}
=274{,}980{,}726{,}538{,}140{,}422<B^*,
\]
with margin \(1{,}573{,}254{,}665\). Increasing \(M_{12}\) by one makes this uniform implication fail. No such occupancy theorem is proved here.

The repaired theorem closes dependent syndrome pairs and rank-one secant planes. It exactly compiles rank-one tangent planes, but it supplies no deployed bound for the resulting grids. It proves neither the official KoalaBear row nor any ledger payment, endpoint movement, PR action, or score change.
