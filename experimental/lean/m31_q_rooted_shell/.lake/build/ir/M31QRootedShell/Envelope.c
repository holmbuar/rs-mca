// Lean compiler output
// Module: M31QRootedShell.Envelope
// Imports: public import Init public meta import Init public import Std
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
lean_object* lean_nat_add(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_degreeSum(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_degreeSum___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_shellSum(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_shellSum___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_excessSum(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_excessSum___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_degreeSum(lean_object* v_x_1_){
_start:
{
if (lean_obj_tag(v_x_1_) == 0)
{
lean_object* v___x_2_; 
v___x_2_ = lean_unsigned_to_nat(0u);
return v___x_2_;
}
else
{
lean_object* v_head_3_; lean_object* v_tail_4_; lean_object* v_fst_5_; lean_object* v___x_6_; lean_object* v___x_7_; 
v_head_3_ = lean_ctor_get(v_x_1_, 0);
v_tail_4_ = lean_ctor_get(v_x_1_, 1);
v_fst_5_ = lean_ctor_get(v_head_3_, 0);
v___x_6_ = lp_m31QRootedShell_M31QRootedShell_degreeSum(v_tail_4_);
v___x_7_ = lean_nat_add(v_fst_5_, v___x_6_);
lean_dec(v___x_6_);
return v___x_7_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_degreeSum___boxed(lean_object* v_x_8_){
_start:
{
lean_object* v_res_9_; 
v_res_9_ = lp_m31QRootedShell_M31QRootedShell_degreeSum(v_x_8_);
lean_dec(v_x_8_);
return v_res_9_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_shellSum(lean_object* v_x_10_){
_start:
{
if (lean_obj_tag(v_x_10_) == 0)
{
lean_object* v___x_11_; 
v___x_11_ = lean_unsigned_to_nat(0u);
return v___x_11_;
}
else
{
lean_object* v_head_12_; lean_object* v_tail_13_; lean_object* v_snd_14_; lean_object* v___x_15_; lean_object* v___x_16_; 
v_head_12_ = lean_ctor_get(v_x_10_, 0);
v_tail_13_ = lean_ctor_get(v_x_10_, 1);
v_snd_14_ = lean_ctor_get(v_head_12_, 1);
v___x_15_ = lp_m31QRootedShell_M31QRootedShell_shellSum(v_tail_13_);
v___x_16_ = lean_nat_add(v_snd_14_, v___x_15_);
lean_dec(v___x_15_);
return v___x_16_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_shellSum___boxed(lean_object* v_x_17_){
_start:
{
lean_object* v_res_18_; 
v_res_18_ = lp_m31QRootedShell_M31QRootedShell_shellSum(v_x_17_);
lean_dec(v_x_17_);
return v_res_18_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_excessSum(lean_object* v_b_19_, lean_object* v_x_20_){
_start:
{
if (lean_obj_tag(v_x_20_) == 0)
{
lean_object* v___x_21_; 
v___x_21_ = lean_unsigned_to_nat(0u);
return v___x_21_;
}
else
{
lean_object* v_head_22_; lean_object* v_tail_23_; lean_object* v_fst_24_; lean_object* v___x_25_; lean_object* v___x_26_; lean_object* v___x_27_; 
v_head_22_ = lean_ctor_get(v_x_20_, 0);
v_tail_23_ = lean_ctor_get(v_x_20_, 1);
v_fst_24_ = lean_ctor_get(v_head_22_, 0);
v___x_25_ = lean_nat_sub(v_fst_24_, v_b_19_);
v___x_26_ = lp_m31QRootedShell_M31QRootedShell_excessSum(v_b_19_, v_tail_23_);
v___x_27_ = lean_nat_add(v___x_25_, v___x_26_);
lean_dec(v___x_26_);
lean_dec(v___x_25_);
return v___x_27_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_excessSum___boxed(lean_object* v_b_28_, lean_object* v_x_29_){
_start:
{
lean_object* v_res_30_; 
v_res_30_ = lp_m31QRootedShell_M31QRootedShell_excessSum(v_b_28_, v_x_29_);
lean_dec(v_x_29_);
lean_dec(v_b_28_);
return v_res_30_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Std(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_m31QRootedShell_M31QRootedShell_Envelope(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Std(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
