# Hostile audit: q64 footprint-31 mandatory leave payment

## Verdict

The frozen theorem

```text
Q64_R31_MANDATORY_LEAVE_PAYMENT.md
sha256=d472cfef95d5292d54db34dbd5b2e76522b5af787c6076afbb293bf2ab558e51
```

and its verifier

```text
verify_q64_r31_mandatory_leave_payment.rb
sha256=1cbb1b77337d589688f1a6cafb6f93f359432e9ea4d642cf87ddddd2657e77fb
```

pass independent hostile audit.  The leave quantifier, the RS source bridge,
the old-cap replacement semantics, the disjoint subtotal, and the cap-six /
cap-seven calibration are all correct.

## 1. Leave quantifiers

Let `B` be any family of 31-subsets of a 64-set with pairwise intersection
at most 29.  Fixing an arbitrary 29-subset `A` gives exactly 35 one-point
extensions to a 30-set.  Every block containing `A` covers exactly two of
those extensions.  Different blocks cover disjoint pairs, since a repeated
extension would be a common 30-subset.  The odd number 35 therefore leaves
at least one extension uncovered for **every** `A`; no maximality or design
existence hypothesis is used.

If `L` is the 30-shadow leave, flag counting gives

```text
30 |L| >= C(64,29),
|L| >= ceil(C(64,29)/30)=46,293,943,158,009,927.
```

The used 30-shadows are disjoint and each block uses 31, so

```text
31 |B| <= C(64,30)-|L|.
```

Taking the ceiling before the outer floor is correct and yields

```text
|B| <= 50,774,002,173,301,209.
```

## 2. Literal-source bridge

For two different errors in one fixed syndrome coset, their difference is a
nonzero word of the deployed moment-kernel GRS code, of minimum distance
`K+1`.  A union of at most 32 q64 footprints supports at most

```text
32*(n/64)=32*32,768=K
```

coordinates, which is impossible.  Thus two footprint-31 errors have union
at least 33, equivalently intersection at most 29.  The same argument rules
out two different errors with one footprint, so the set-system bound counts
literal errors rather than only footprint labels.  The statement is uniform
in the fixed syndrome.

## 3. Replacement and disjoint subtotal

Only the old `r=31` cap is replaced.  The exact change is

```text
old r31 =52,267,355,178,398,304
new r31 =50,774,002,173,301,209
saving   =1,493,353,005,097,095.
```

The cumulative `r<=31` upper bound consequently decreases from
`54,024,655,287,584,031` to `52,531,302,282,486,936`.  This is a sharper
bound on an already paid population, so the same amount is correctly added
to the unpaid allowance.

The four subtotal cells are disjoint by literal labels:

```text
q64<=31;
q64=32 and q128=32..47;
q64=32 and q128=48..54;
D7: q64>=33 and q128=33..46.
```

Their caps sum to

```text
272,478,712,266,744,581,
```

leaving

```text
2,375,398,229,443,011.
```

There is no double payment and no claim that the smaller paid cap directly
bounds the residual; it enlarges the amount that a residual theorem may use.

## 4. Common-27 calibration

If every exact q128-footprint-47 support family has at most `L0` members
through each 27-core, incidence counting gives

```text
N C(47,27) <= L0 C(128,27).
```

The exact consecutive floors are

```text
L0=6: 2,309,103,404,380,482,
L0=7: 2,693,953,971,777,229.
```

Thus cap six would fit the new allowance with margin
`66,294,825,062,529`, while cap seven does not fit.  This is calibration
only; neither the source theorem nor this audit asserts cap six.

## Replay

```bash
/usr/bin/ruby --disable-gems work/verify_hostile_audit_q64_r31_mandatory_leave_payment.rb
/usr/bin/ruby --disable-gems -w work/verify_hostile_audit_q64_r31_mandatory_leave_payment.rb
```

Both runs must byte-match the expected output and emit no stderr.
