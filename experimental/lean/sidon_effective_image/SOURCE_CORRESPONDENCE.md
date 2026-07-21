# Sidon effective-image finite regression: source correspondence

## Scope

This package is the finite checker for Section 6 of
`experimental/notes/audits/sidon_effective_image_mi_ma_normalization_floor.md`.
It uses only Lean/Std and natural-number arithmetic modulo `11`.

It does not formalize Parseval, Cauchy--Schwarz, the asymptotic prime family,
semantic C1--C8 survival, residual add-back, or the completed-ray compiler.
Those claims remain source-level mathematics with the status printed in the
note.

## Theorem map

The single fail-closed theorem `SidonEffectiveImage.packet_check` certifies every
clause below in one kernel-decided conjunction.

| `packetCheck` clause | Source-level meaning | Status |
|---|---|---|
| `supports.length == 252` | `M=binom(10,5)=252` | finite regression |
| support shape gate | complete generated fixed-weight slice consists of duplicate-free five-subsets | finite regression |
| `image.length == 251` | realized power-sum image has `L=251` targets | finite regression |
| `maxFiber == 2` | exact full-slice maximum fiber is two | finite regression |
| unique-double-target gates | zero is the only doubled syndrome and the two printed supports form that fiber | finite regression |
| cleared Q-loss gate | image-normalized loss `maxFiber*L/M` is below two | finite regression |
| `maxFiber <= p^2` | toy instance of the two-free locator-coefficient census | finite regression |
| three basis-value gates | moment-column differences are the printed vectors | finite regression |
| `fullSpanCheck` | an explicit inverse represents every vector of `F_11^3` | finite regression |
| `allVec3.length == 1331` | `A_eff=11^3=1331` | finite regression |
| final sparse-image gate | exact inequality `A_eff>5L` | finite regression |

## Build contract

The package is an independent Lake package rooted at
`experimental/lean/sidon_effective_image/`.  The fork draft-PR Lean workflow is
the authoritative build.  No local Lean build is claimed.

## Sorry and axiom census

```text
sorry declarations: 0
axiom declarations: 0
native-evaluation proof steps: 0
Mathlib imports: 0
external packages: 0
```

The file imports only the Lean `Std` root.  `packet_check` is closed by kernel
reduction using `by decide`; compilation proves that decidable finite gate, not
the source-level Parseval or asymptotic argument.
