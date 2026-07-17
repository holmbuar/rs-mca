# Rank-16 integer-subcore owner certificate

Run from the repository root:

```bash
python3 experimental/scripts/verify_rank16_integer_subcore_owner.py \
  > /tmp/rank16-integer-subcore-owner.out
diff -u \
  experimental/data/certificates/rank16-integer-subcore-owner/verify_rank16_integer_subcore_owner.expected.txt \
  /tmp/rank16-integer-subcore-owner.out
python3 -O experimental/scripts/verify_rank16_integer_subcore_owner.py \
  > /tmp/rank16-integer-subcore-owner.opt.out
cmp /tmp/rank16-integer-subcore-owner.out \
  /tmp/rank16-integer-subcore-owner.opt.out
python3 experimental/scripts/verify_rank16_integer_subcore_owner.py \
  --tamper-selftest
```

The script uses only the Python standard library. It reconstructs the
integrated #838 profile file and the pending #861 ledger before applying the
new integer-subcore owner.
