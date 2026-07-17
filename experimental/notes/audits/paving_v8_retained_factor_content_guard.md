# Paving v8 retained-factor content-root guard

Status: `COUNTEREXAMPLE / AUDIT / REPAIR`

This note gives an exact counterexample to the universal form of RF3 in the
`Parameter-retained factor lift` assumption in `RS_MCA_Paving_v8.tex`. The
omitted condition is the coefficient needed to absorb roots of the
`Y`-content. A safe corrected global envelope is

```text
|S| > max(1, 2 U D_Y^2) D_Z + (r+1) D_Y.          (RF3')
```

This repairs only the content-root ledger. It does **not** discharge the
separate parameter-retained Hensel/factor-lifting import, so the downstream
result remains conditional.

## Exact counterexample

Work over `F_7`, with

```text
D = {1,2,4},  n=A=3,  r=0,  K=1,  m=1,
D_X=21/10,    D_Y=1/100,    D_Z=11/10,
U=3,          V=1,          W=2.
```

Take

```text
Q(X,Y,Z)=Z,
S={0},
P_0(X)=0,
A_0=D,
u_0(x)=0,
u_1(x)=x.
```

All antecedents of the displayed assumption hold:

- RF1: `V>=m`, `W>=V`, `U>K(V-1)`, `D_X<mA`, and
  `char(F_7)>V-1` become `1>=1`, `2>=1`, `3>0`, `21/10<3`, and
  `7>0`.
- RF2's top-degree comparison is `5>3`, and its field-size comparison is
  `7>2*3/100=3/50`.
- For `Q=Z`, the `(1,K,0)`-weighted degree is `0<D_X`, the `Y`-degree is
  `0<D_Y`, and the `(0,1,1)`-weighted degree is `1<D_Z`.
- `Q(X,P_0(X),0)=0`, `deg(P_0)<K`, and
  `P_0=u_0+0*u_1` on the chosen support of size `A`.
- The old RF3 right side is

```text
2*3*(1/100)^2*(11/10) + 1/100 = 533/50000 < 1 = |S|.
```

The conclusion nevertheless fails. Since `K=1`, both `v_0` and `v_1`
would have to be constant. No constant over `F_7` agrees with
`u_1(x)=x` at all three distinct points `{1,2,4}`.

The verifier enumerates all seven possible constants rather than relying on
this last observation informally.

## Root cause and corrected envelope

Let `d_C` be the degree of the `Y`-content and put

```text
alpha = 2 U D_Y^2.
```

The shared weighted-degree ledger leaves `D_Z-d_C` for the content-free
factor part. Before the final absorption step, the content-plus-factor charge
therefore has the form

```text
d_C + alpha (D_Z-d_C) + (r+1)D_Y.               (1)
```

The existing parametric audit records the analogous expression with `D_X`
and explicitly says that its last simplification uses
`2 D_X D_Y^2 >= 1`. V8 uses the conservative integer truncation `U`, but its
universal RF1--RF3 statement does not impose the corresponding guard
`2 U D_Y^2 >= 1`.

Relax the integral degree `d_C` to the real interval `0<=d_C<=D_Z`. The
following uniform bound on (1) is immediate:

- if `alpha>=1`, then (1) decreases with `d_C`, and the content/factor part is
  at most `alpha D_Z`;
- if `alpha<=1`, then (1) increases with `d_C`, and the content/factor part is
  at most `D_Z`.

Thus a safe uniform envelope is

```text
max(1, alpha) D_Z + (r+1)D_Y,
```

which is sharp for the continuous relaxation. The integer-degree maximum can
be slightly smaller when `D_Z` is nonintegral; RF3' deliberately uses the
clean continuous envelope. In the counterexample, RF3' has right side

```text
11/10 + 1/100 = 111/100,
```

so the singleton `S` no longer triggers the conclusion. At `d_C=1`, the
unabsorbed expression (1) is `50503/50000`, also already larger than `|S|`.

An alternative, narrower edit is to add `2 U D_Y^2 >= 1` to RF1. RF3' is the
cleaner source-level statement because it avoids a separate coefficient case.

## Why the four deployed rows do not move

Every application through RF4 automatically has `V>=2`. Indeed, if `V=1`,
then RF1 and positive integral `m` force `m=1`. RF4 becomes

```text
U W > n W,
```

so `U>n`. But `D_X<mA=A<=n` gives `U=ceil(D_X)<=n`, a contradiction.

Therefore RF4 implies `D_Y>1`, hence `2 U D_Y^2>1`. On that range RF3' and
the old RF3 coincide. The exact checker also replays the four printed
KoalaBear parameter rows and confirms that all four RF5 ceilings remain:

```text
274589064742726105
274721012201264929
274578888391530706
274861787390229386
```

This is a nonimpact statement about the content correction only. It does not
upgrade any conditional row to an unconditional theorem.

## Reproduction

From the repository root:

```bash
python3 experimental/scripts/verify_paving_v8_retained_factor_content_guard.py --check
python3 experimental/scripts/verify_paving_v8_retained_factor_content_guard.py --tamper-selftest
python3 experimental/RS_MCA_Paving_v8_source/verify_retained_bchks_v8.py
python3 experimental/RS_MCA_Paving_v8_source/verify_paving_mca_v8.py
```

The new checker uses only the Python standard library. It binds itself to the
two identical v8 TeX source copies and to the existing parametric audit's
load-bearing inequality.

## Integration recommendation and nonclaims

This audit does not edit the release TeX, PDF, or reproducibility hashes. A
release repair should:

1. apply RF3' to both TeX source copies;
2. state the shared `d_C+(D_Z-d_C)` degree ledger in the retained-lift remark;
3. rebuild the PDF and rerun both bundled v8 verifiers; and
4. refresh the release hashes together.

No local TeX engine is available in the current environment, so editing only
the source would leave the checked submission package inconsistent. This
note instead supplies the exact counterexample and repair for a maintainer who
can rebuild the complete package.

The audit does not claim that the cited Hensel steps support the full
arbitrary-parameter synthesis, does not discharge the retained-factor lift,
and does not change a deployed MCA threshold.
