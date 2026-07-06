# L1: formalization run on the KEY LEMMA

- **Status:** AUDIT / FORMALIZATION SKELETON + verified syzygy lead.
- **Contributor:** Scott Hughes, with Sage rechecks included in this packet.
- **Date:** 2026-07-06.

## What was banked

The Lean skeleton is stored at `../../lean/l1_e3_level_set/`. It formalizes the
coset level-set setup for the target inequality

```text
E3 p ell Gamma <= ell - 2
```

under the hypotheses used by the L1 notes: `ell` odd prime, `ell | p-1`,
`Gamma != 0`, no constant term, and `deg Gamma <= ell-1`. The partition
backbone is represented in Lean, but the main inequality remains an annotated
`sorry`; this is not a formal proof of the L1 ceiling.

The note `../../lean/l1_e3_level_set/NOTES.md` records the mathematical
reduction to the rank/syzygy crux `dim Syz <= K`, and the counterexample
showing that the crux is false for arbitrary pairwise-coprime co-fiber
locators. The single-`Gamma` structure is essential.

## Verified syzygy lead

With `s_k := (Gamma - c_k)/g_k`, the submitted scripts verify on the
saturating examples that every degree-bounded syzygy of the co-fiber locators
`h_k` is also a syzygy of the `s_k`:

```text
sum_k h_k q_k = 0, deg q_k <= mu_k - 2
    => sum_k s_k q_k = 0.
```

The proof identity is formal algebra: multiply the syzygy by `Gamma`, use
`h_k(Gamma-c_k) = (X^ell-w_k)s_k`, and separate the `X^ell`-shifted top part
from terms of degree at most `ell-2`.

The verifier path is:

```text
experimental/scripts/verify_l1_e3_syzygy_lead.sage
```

The same packet also records that the resulting pencil relation reframes the
problem but does not by itself cut the syzygy dimension. The remaining open
task is still the `K >= 3` rank statement `dim Syz <= K`.
