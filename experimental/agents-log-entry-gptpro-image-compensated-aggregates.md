### 2026-07-21 - M31 image-compensated effective aggregates

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/lean/sidon_effective_image/`, `experimental/notes/thresholds/sidon_effective_image_image_compensated_aggregates.md`, `experimental/notes/audits/sidon_effective_image_image_compensated_aggregates_audit.md`, `experimental/data/certificates/sidon-effective-image-image-compensated-aggregates/m31_image_compensated_aggregates.json`, and `experimental/scripts/verify_m31_image_compensated_aggregates.py`.
- **Status:** PROVED / LOCAL_ONLY.
- **What is being added:** On the exact eight-point Mersenne-31 C1-owner-complement primitive leaf, the packet proves full effective span, a nonempty certified minor/major split, and exact image-compensated absolute aggregate losses at most `1` and `69`, with full multiplier `69`.
- **How it is useful:** This discharges the compensated-aggregate route on one genuine scoped post-C1 survivor (acceptance criterion 2), independently of the phase-cancellation route and without importing open-PR Lean modules.
- **What to do next:** Prove exhaustive deployed owner/key coverage and slope projection, or extend the exact aggregate argument to a uniform family of genuine post-C1--C8 survivors before using it in profile add-back or a row sum.
