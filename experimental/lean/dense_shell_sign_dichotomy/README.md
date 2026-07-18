# Dense-shell S-cubic identity formalization

This standalone Lean 4.14 package contains the integer arithmetic shadow of
the dense-shell sign-dichotomy packet.  The D1 source packet was produced at
`6f8dae62` and integrated unchanged at `06b2a6fb`.  Its map

```text
S(a) = a(3 - 4a)^2
```

has the exact cubic expansion recorded here over `Int`.  The later
dense-shell class-charge correction was produced at `e465ee44` and integrated
at `a5750192`; it changes downstream pointwise-versus-class-sum accounting but
does not change this polynomial identity.

## Theorem map

| Source section | Lean declaration | Status |
| --- | --- | --- |
| D1, integer expansion shadow of `S(a)=a(3-4a)^2` | `s_expand` | PROVED for every `x : Int` |
| Former finite S-expansion check | `sExpandOK`, `s_expand_census` | PROVED regression for `-50 <= x <= 50` |
| D1/D2, powers-of-three denominator recursion and positivity | `P3`, `P3_pos` | DEFINITION / PROVED integer arithmetic helper |
| D2, inner-state coupling | `inner_coupling_pos`, `inner_coupling_neg` | PROVED integer arithmetic shadow |
| D2, boundary nonattainment | `P3_odd`, `no_sixth` | PROVED integer arithmetic shadow |
| D2, finite dense-word coupling check | `scan`, `isInner`, `words`, `couplingOK`, `census_B8` | PROVED regression at `B=8` only |
| D3/D4, every-depth dense-shell sign dichotomy | none | NOT FORMALIZED IN LEAN |
| D1, full S-preimage product and Vieta data | none | NOT FORMALIZED IN LEAN |
| D1, Chebyshev/arcsine orbit and mean | none | NOT FORMALIZED IN LEAN |
| D5, alternating-word closed form | `altSign`, `altN`, `alt_closed` | PROVED integer arithmetic shadow |
| D5, extremal/minimum structure beyond that closed form | none | NOT FORMALIZED IN LEAN |
| D6, certified analytic transfer tail | none | NOT FORMALIZED IN LEAN |
| Section 7 consumer emission and class-charge consequences | none | NOT FORMALIZED IN LEAN |

## Statement boundary

The theorem is deliberately stated over `Int`.  Reusing the same syntax over
`Nat` would be false: at `x = 1`, truncated subtraction makes the left side
zero and the right side nine.  Negative integers and zero need no hypotheses.

The former source comment described a finite point census followed by an
external polynomial meta-step.  A degree-at-most-three polynomial is pinned by
four distinct values once its degree bound is established, but neither that
coefficient argument nor a universal identity followed from the Boolean
census inside Lean.  `s_expand` now proves the universal integer identity
directly; `s_expand_census` remains unchanged as a regression declaration.

## Scope

This theorem expands only `x(3-4x)^2`.  It does not prove the stronger
preimage/root product `prod_{S(z)=A}(x-z)=(S(x)-A)/16`, existence or
multiplicity of roots, the associated Vieta coefficients, or the trigonometric
identity relating `S` to triple angles.  It does not prove the dense-shell sign
dichotomy, alternating-cone preservation, the arcsine integral, certified
analytic tails, shell emission, class charges, image-scale MI/MA, a direct
Sidon payment, a residual ray compiler, profile-envelope comparison, lower
reserve, a deployed row, an MCA threshold, a deep-MCA count, or a Proximity
Prize claim.

Build with the pinned toolchain:

```text
lake build
```
