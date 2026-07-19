# Phi-fiber Lean skeleton repair certificate

Date: 2026-07-19. Status: **COUNTEREXAMPLE / PROVED / AUDIT; final-tree replay recorded**.

## Claim

The old Lean skeleton for Paper D's `lem:phi-fiber`(ii) omitted the paper's
requirement that the folding polynomial be defined over the base field.  Its
exact universe-polymorphic proposition is false.  The isolated package
`experimental/lean/cs25_phi_fiber_repair_certificate/` supplies a symbolic
kernel certificate of falsity at universe zero and a paper-faithful wrapper for
the repaired theorem.

This is a Lean-statement defect, not a paper defect.  At current source base
`4bea7abb2d9455583c8864b980e39d11d550f51d`, Paper D v13.2's
`def:map-smooth` requires `phi ∈ B[X]`, and `lem:phi-fiber` uses that setting.
The repaired Lean theorem requires the corresponding value-level fact
`hQB : ∀ i, phi.eval (dom i) ∈ B`; the new wrapper derives it from a polynomial
`phiB : Polynomial B`.

Credit: Adam Mohammed A Latif identified the missing base-field hypothesis,
supplied the original `GF(16)/GF(4)` counterexample argument, and repaired the
imported theorem in #881.  This packet machine-checks that negative argument
and adds the coefficient-level bridge.

## Exact counterexample

Take an embedding `GF(4) -> GF(16)`, let `B` be its image, choose
`t ∈ GF(16) \ B`, and set

```text
ι = GF(4)              dom = the embedding into GF(16)
a = 1                  N = 4
k = 1                  ell2 = 3
A2 = 3                 phi = X + t
```

The old hypotheses hold: `dom` is injective and `B`-valued, `phi` has exact
degree `a=1`, `a*N=|ι|`, every fiber of `phi` on the domain has size one,
`ell2=k/a+2`, `ell2<=N-1`, and `A2=a*ell2`.

For a proposed `z ∈ B`, the old conclusion requires at least
`choose(4,3)/|B| = 1` Reed--Solomon codeword of degree `< k+1 = 2` within
relative radius `1-3/4`; equivalently it requires at least three agreements
with

```text
u_z(x) = (x+t)^3 + z(x+t)^2.
```

The certificate proves a maximum of two agreements.  Three distinct base-field
agreements would make

```text
d(X) = (X+t)^3 + z(X+t)^2 - Q(X)
```

a monic cubic with three roots in `B`, forcing its quadratic coefficient into
`B`.  Symbolic characteristic-two expansion gives `coeff(d,2)=t+z`, which is
not in `B`.  Therefore no qualifying `Q` exists.

The counterexample satisfies the polynomial-degree premise.  Thus `hQB` is an
independently necessary interface condition; it is not implied by degree,
domain containment, cardinality, or map-smoothness.

## Universe and statement fidelity

The packet mirrors the exact old proposition as
`RSCap.LemPhiFiberIIPreRepair`.  The exported negation has the precise shape

```lean
RSCap.lem_phi_fiber_ii_pre_repair_false :
  ¬ RSCap.LemPhiFiberIIPreRepair.{0, 0}
```

The old theorem was universe-polymorphic.  If it were valid, it would
specialize to the universe-zero proposition above.  The concrete
`GF(16)/GF(4)` contradiction at universe zero therefore refutes the old theorem
declaration; no claim about higher-universe finite fields is needed.

## Statement map

| Paper/audit node | Lean node | Evidence status | Audit conclusion |
|---|---|---|---|
| `def:map-smooth`: `phi ∈ B[X]`, `D ⊆ B`, complete uniform fibers | imported `RSCap.DomSmooth` plus the wrapper input `phiB : Polynomial B` | source statement plus kernel bridge | The paper includes the base-field tie missing from the old skeleton. |
| `lem:phi-fiber`(ii), coefficient-level premise | `RSCap.lem_phi_fiber_ii_of_basePolynomial` | kernel theorem | Evaluation after mapping coefficients through `B.subtype` supplies `hQB` and invokes the repaired theorem. |
| Exact old Lean signature | `RSCap.LemPhiFiberIIPreRepair` | exact proposition mirror | The omission is isolated without weakening or strengthening other binders. |
| Old signature is false | `RSCap.lem_phi_fiber_ii_pre_repair_false` | kernel theorem at universes `{0,0}` | `COUNTEREXAMPLE` to the old skeleton, not to the paper. |
| Repaired premise fails on the witness | `RSCap.PhiFiberRepair.phi_eval_not_mem_B4` | kernel theorem | Every `phi(dom i)` lies outside `B`; the omitted base-field tie is isolated directly. |
| At most two agreements in the concrete instance | `RSCap.PhiFiberRepair.at_most_two_agreements` | kernel theorem | Contradicts the old conclusion's required three agreements. |
| Repaired value-level theorem | imported `RSCap.lem_phi_fiber_ii` | kernel theorem in repaired `Fiber.lean` | `hQB` closes the old skeleton's missing base-field interface. |

## Source provenance

Current source base:

```text
4bea7abb2d9455583c8864b980e39d11d550f51d
```

Paper source anchors at that base are the labels `def:map-smooth` and
`lem:phi-fiber` in `tex/cs25_cap_v13_2.tex`.

| Object | Git blob | Raw SHA-256 |
|---|---|---|
| Old `Fiber.lean` | `d00a46604a3c1e8fddeb466c4370b4f7faa2afdc` | `9172f177bcd2b58b80bcda06a0b1fe8e41357e6331cd8cffce9ffba8a5152368` |
| Repaired `Fiber.lean` | `119d55c6ce1924d729594e64f92dc02b8e31aa17` | `efa03a962901f163206802c5241f1a9278ac574e528add7efe6cf56b47e0ab46` |
| `tex/cs25_cap_v13_2.tex` | `5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb` | `356f1ad4b972746b664260191387b25a89a2e10fcc61962a49dc8282412f93ce` |

The repaired Fiber and TeX blob identities are resolved by their repository
paths at the source-base commit.  The old Fiber is retained as a direct blob
pin.  `Raw SHA-256` means SHA-256 over the exact bytes returned by
`git cat-file blob <object>`.

Provenance replay:

```bash
git rev-parse 4bea7abb2d9455583c8864b980e39d11d550f51d:experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean
git rev-parse 4bea7abb2d9455583c8864b980e39d11d550f51d:tex/cs25_cap_v13_2.tex
git cat-file blob d00a46604a3c1e8fddeb466c4370b4f7faa2afdc | shasum -a 256
git cat-file blob 119d55c6ce1924d729594e64f92dc02b8e31aa17 | shasum -a 256
git cat-file blob 5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb | shasum -a 256
```

## Kernel and verifier replay

From the repository root:

```bash
cd experimental/lean/cs25_phi_fiber_repair_certificate
lake build
lake env lean Cs25PhiFiberRepairCertificate.lean
```

Then, again from the repository root:

```bash
python3 experimental/scripts/verify_phi_fiber_repair_certificate.py
```

Recorded replay on 2026-07-19:

- `lake build` completed successfully with 8033 jobs.  The imported
  `cs25_cap_v12.Fiber` replay retained its pre-existing warning for the
  unrelated `lem_fiber_ii` placeholder; the new module built successfully.
- The direct Lean command exited zero.  The two principal axiom reports list
  exactly `propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx`.
- The verifier passed `43/43` checks.  Its tamper self-test caught `13/13`
  mutations and then passed the same `43/43` checks.

## Audit disposition

**FIXED.**  The old Lean skeleton's missing base-field tie is refuted by an
exact symbolic finite-field instance.  The repaired theorem exposes the needed
value-level hypothesis, and the coefficient-level wrapper recovers that
hypothesis from the premise already present in Paper D.

## Nonclaims

This audit does not claim:

- a proof of `lem_fiber_ii`;
- a proof of the general map-smooth cap theorem;
- a general-`K` decorated-charge result;
- a counterexample to `def:map-smooth` or `lem:phi-fiber` in the paper;
- a promotion or edit to Paper D;
- any theorem beyond the old-signature negation and paper-faithful wrapper
  represented in this isolated packet.
