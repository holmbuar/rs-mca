import Lake
open Lake DSL

package sidonEffectiveImage where

require asymptoticSpine from "../asymptotic_spine"
require m31QRootedShell from "../m31_q_rooted_shell"

@[default_target]
lean_lib SidonEffectiveImage where
  roots := #[`SidonEffectiveImage]
