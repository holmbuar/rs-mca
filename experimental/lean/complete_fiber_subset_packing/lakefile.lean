import Lake

open Lake DSL

package complete_fiber_subset_packing where

require dyadic_complete_fiber_slicing from "../dyadic_complete_fiber_slicing"

@[default_target]
lean_lib CompleteFiberSubsetPacking where
  roots := #[`CompleteFiberSubsetPacking]
