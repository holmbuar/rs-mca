# Rank-16 fixed-core global-owner counterexample certificate

Run from the repository root:

```bash
python3 experimental/scripts/verify_rank16_fixed_core_global_owner_counterexample.py \
  > /tmp/rank16-fixed-core-owner-counterexample.out
diff -u \
  experimental/data/certificates/rank16-fixed-core-global-owner-counterexample/verify_rank16_fixed_core_global_owner_counterexample.expected.txt \
  /tmp/rank16-fixed-core-owner-counterexample.out
python3 -O experimental/scripts/verify_rank16_fixed_core_global_owner_counterexample.py \
  > /tmp/rank16-fixed-core-owner-counterexample.opt.out
cmp /tmp/rank16-fixed-core-owner-counterexample.out \
  /tmp/rank16-fixed-core-owner-counterexample.opt.out
python3 experimental/scripts/verify_rank16_fixed_core_global_owner_counterexample.py \
  --tamper-selftest
```

The verifier uses only the Python standard library.
