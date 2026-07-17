# Direct Sidon pair-emission certificate

This directory freezes the source and statement pins plus the expected output
for the narrow R28 Role 09 packet.

Run from the repository root:

```bash
python3 experimental/scripts/verify_direct_sidon_pair_emission.py \
  > /tmp/direct-sidon-pair-emission.out
diff -u \
  experimental/data/certificates/direct-sidon-pair-emission/verify_direct_sidon_pair_emission.expected.txt \
  /tmp/direct-sidon-pair-emission.out
python3 -O experimental/scripts/verify_direct_sidon_pair_emission.py \
  > /tmp/direct-sidon-pair-emission.opt.out
cmp /tmp/direct-sidon-pair-emission.out \
  /tmp/direct-sidon-pair-emission.opt.out
python3 experimental/scripts/verify_direct_sidon_pair_emission.py \
  --tamper-selftest
python3 -m py_compile \
  experimental/scripts/verify_direct_sidon_pair_emission.py
```

The verifier uses only the Python standard library and contains no network or
subprocess calls. It checks arbitrary residual families on small exact source
fixtures, not only the displayed decimal constants.

The packet claims only:

1. the all-characteristic canonical signed-root emission;
2. the odd-characteristic ternary diagonal-pair emission; and
3. the exact half-density cutoff improvement recorded in the note.

It supplies no weighted occupied-emission theorem, finite ledger charge,
recurrence-parent movement, hard-input-2 closure, or official-score movement.
