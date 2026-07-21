# Agents Log

This file is the working ledger for agent-created material in `experimental/`.
Use it to record every new note, script, scan, formalization stub, or audit before
the material is promoted into `tex/` or `scripts/`.

The log is not a proof-status authority. It is a coordination record: what was
added, why it might matter, and what a human or later agent should check next.
Keep entries concise and link to the relevant files.

## Entry Format

```markdown
### YYYY-MM-DD - Short title

- **Agent/model:** Name the agent or model, for example `GPT-5.5 Pro`,
  `Claude Fable 5`, or `Codex`.
- **Files added or changed:** List paths under `experimental/`, `tex/`,
  or `scripts/`.
- **Status:** PROVED / CONDITIONAL / CONJECTURAL / EXPERIMENTAL / AUDIT /
  COUNTEREXAMPLE.
- **What is being added:** State the claim, note, scan, script, proof,
  heuristic, or computation
  in one or two sentences.
- **How it is useful:** Say which paper, theorem, problem, ledger, or toy case
  the material supports.
- **What to do next:** Give the next verification, cleanup, proof step,
  experiment, or promotion decision.
```

## Entries

### 2026-07-21 - C8 common-core shortening and high-kappa owner compiler

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/notes/thresholds/c8_high_kappa_owner_or_payment.md`; `experimental/lean/asymptotic_spine/AsymptoticSpine/C8HighKappaOwner.lean`; `experimental/lean/asymptotic_spine/AsymptoticSpine.lean`; `experimental/lean/asymptotic_spine/C8_HIGH_KAPPA_OWNER_CORRESPONDENCE.md`; `experimental/lean/asymptotic_spine/README.md`; and `experimental/agents-log.md`.
- **Status:** PROVED / CONDITIONAL / AUDIT.
- **What is being added:** A stdlib-only finite compiler for slope-preserving common-core shortening, factor-one add-back to the original distinct-slope numerator, transfer of shallow `DirectRC` and `A6` payments, the factor-aware kernel law, and a high-kappa earlier-owner versus shortened-chart payment dichotomy.
- **How it is useful:** It supplies the typed C8 bridge from a shortened residual payment back to the original first-match slope cell while keeping the raw dimension, shortened dimension, residual core, supports, and slopes distinct.
- **What to do next:** Instantiate the compiler on one actual post-C1--C7 first-match C8 residual and prove either its semantic high-kappa owner or its deep natural-scale MI/MA, Sidon, or direct-ray payment; this packet does not close C8, `UNIF`, or a deployed adjacent row.
