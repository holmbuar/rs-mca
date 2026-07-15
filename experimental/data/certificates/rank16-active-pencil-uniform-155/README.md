# Rank-16 active-pencil cap certificate

This directory freezes the source, primary, and independently implemented
replays for the rank-16 fixed-pair active-pencil theorem.

The theorem proves an occupancy cap of `155` in one source-owned active
pencil for every core `0 <= c <= 553`.  Together with the source theorem for
`554 <= c <= 832`, the cap is uniform over `0 <= c <= 832`.

It does not prove the missing active-hyperplane occupancy cap `Q <= 1424`,
eliminate the parent state, establish a recurrence payment, or change the
official score.

Replay from the repository root:

```text
ruby --disable-gems -w experimental/scripts/verify_rank16_fixed_pair_active_pencil_grid_tail_cut.rb
python3 experimental/scripts/verify_rank16_weighted_grid_extactic_dpw.py
ruby --disable-gems -w experimental/scripts/verify_rank16_weighted_grid_extactic_dpw_independent.rb
```
