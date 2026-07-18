# Dense-shell S-cubic identity formalization

## Claim

For every integer `x`, Lean proves

```text
x(3-4x)^2 = 16x^3 - 24x^2 + 9x.
```

## Status

PROVED.

## Source audit

The exact source is D1 of
`experimental/notes/thresholds/dense_shell_sign_dichotomy.md`.  Its packet was
produced at `6f8dae62` and integrated unchanged at `06b2a6fb`.  The source
defines `S(a)=a(3-4a)^2` and uses real squared-sine states in the surrounding
analytic argument.  The displayed expansion is the direct integer arithmetic
shadow of that definition; the standalone Lean package intentionally
formalizes only this shadow.

The later dense-shell class-charge correction was produced at `e465ee44` and
integrated at `a5750192`.  It corrects downstream pointwise-versus-class-sum
accounting and does not alter the D1 cubic identity.

The former Lean declaration `s_expand_census` checked only 101 integers.  Its
comment's external point-pinning step was not a Lean proof of the universal
identity; moreover, four distinct evaluations, not five, suffice after a
degree-at-most-three bound has separately been established.  The new theorem
replaces that under-specified bridge with direct algebra for every integer.

The ambient type cannot silently be changed to `Nat`.  At `x=1`, natural
subtraction truncates, making the left side zero and the right side nine.  The
correct theorem has no hypotheses over `Int`, including at zero and negative
values.

## Lean correspondence

The declaration

```text
DenseShellSignDichotomy.s_expand
```

is in
`experimental/lean/dense_shell_sign_dichotomy/DenseShellSignDichotomy.lean`.
The existing `sExpandOK` and `s_expand_census` declarations retain their exact
types as finite regression checks.  The package README contains the complete
source-label to Lean-name status map.

## Proof outline

The proof first expands `(4x)(4x)=16x^2`, then distributes the two factors of
`3-4x`.  Associative-commutative normalization identifies the three monomials,
and Presburger arithmetic closes their integer coefficients.  It uses only the
existing Lean 4.14 core APIs and adds no dependency.

## Validation

From `experimental/lean/dense_shell_sign_dichotomy`:

```bash
lake clean
lake build
```

From the repository root:

```bash
python3 experimental/scripts/verify_dense_shell_cubic_identity.py --check
python3 experimental/scripts/verify_dense_shell_cubic_identity.py --tamper-selftest --check
```

The source verifier checks the source labels and Lean declaration, evaluates
the identity on a symmetric exact-integer range, and locks the natural-number
counterexample.  Its final result lines are recorded in the promotion log.

## Scope and nonclaims

This packet proves only the integer polynomial expansion.  It does not prove
the full S-preimage product, root existence or multiplicities, Vieta data,
`S(sin^2 t)=sin^2(3t)`, the every-depth dense-shell sign theorem, cone or
coupling arguments beyond the declarations already present, arcsine means,
analytic tail certification, shell emission, or class charges.  It does not
supply image-scale MI/MA or a direct Sidon payment, compile a residual ray,
compare the complete profile envelope, establish lower reserve, close a row or
branch, or prove an MCA threshold, charge, deep-MCA count, or Proximity Prize
claim.
