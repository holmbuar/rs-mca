// Lean compiler output
// Module: KbM1SourceBoundBridge
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
lean_object* l_List_reverse___redArg(lean_object*);
lean_object* lean_nat_to_int(lean_object*);
uint8_t lean_nat_dec_le(lean_object*, lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* l_Repr_addAppParen(lean_object*, lean_object*);
uint8_t lean_nat_dec_le(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_basePrime;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_extensionDegree;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_domainSize;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_codeDimension;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_agreement;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentCharge;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_budget;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_remainingBudget;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_legacyM1Paid;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_List_mapTR_loop___at___00KbM1SourceBoundBridge_tangentImageEnvelope_spec__0___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentImageEnvelope___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentImageEnvelope(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_List_mapTR_loop___at___00KbM1SourceBoundBridge_tangentImageEnvelope_spec__0(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_List_filterTR_loop___at___00KbM1SourceBoundBridge_paidEnvelope_spec__0___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_paidEnvelope___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_paidEnvelope(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_List_filterTR_loop___at___00KbM1SourceBoundBridge_paidEnvelope_spec__0(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorIdx(uint8_t);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorIdx___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_toCtorIdx(uint8_t);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_toCtorIdx___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim(lean_object*, lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ofNat(lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ofNat___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instDecidableEqOwner(uint8_t, uint8_t);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instDecidableEqOwner___boxed(lean_object*, lean_object*);
static const lean_string_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 33, .m_capacity = 33, .m_length = 32, .m_data = "KbM1SourceBoundBridge.Owner.paid"};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__0 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__0_value;
static const lean_ctor_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__0_value)}};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__1 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__1_value;
static const lean_string_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 30, .m_capacity = 30, .m_length = 29, .m_data = "KbM1SourceBoundBridge.Owner.q"};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__2 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__2_value;
static const lean_ctor_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__2_value)}};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__3 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__3_value;
static const lean_string_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 31, .m_capacity = 31, .m_length = 30, .m_data = "KbM1SourceBoundBridge.Owner.bc"};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__4 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__4_value;
static const lean_ctor_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__4_value)}};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__5 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__5_value;
static const lean_string_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 32, .m_capacity = 32, .m_length = 31, .m_data = "KbM1SourceBoundBridge.Owner.new"};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__6 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__6_value;
static const lean_ctor_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__6_value)}};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__7 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__7_value;
static const lean_string_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 36, .m_capacity = 36, .m_length = 35, .m_data = "KbM1SourceBoundBridge.Owner.outside"};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__8 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__8_value;
static const lean_ctor_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__8_value)}};
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__9 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__9_value;
static lean_once_cell_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10;
static lean_once_cell_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11;
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr(uint8_t, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___boxed(lean_object*, lean_object*);
static const lean_closure_object lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___boxed, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner___closed__0 = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner___closed__0_value;
LEAN_EXPORT const lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner = (const lean_object*)&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner___closed__0_value;
LEAN_EXPORT uint8_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner___redArg(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner___redArg___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_basePrime(void){
_start:
{
lean_object* v___x_1_; 
v___x_1_ = lean_unsigned_to_nat(2130706433u);
return v___x_1_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_extensionDegree(void){
_start:
{
lean_object* v___x_2_; 
v___x_2_ = lean_unsigned_to_nat(6u);
return v___x_2_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_domainSize(void){
_start:
{
lean_object* v___x_3_; 
v___x_3_ = lean_unsigned_to_nat(2097152u);
return v___x_3_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_codeDimension(void){
_start:
{
lean_object* v___x_4_; 
v___x_4_ = lean_unsigned_to_nat(1048576u);
return v___x_4_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_agreement(void){
_start:
{
lean_object* v___x_5_; 
v___x_5_ = lean_unsigned_to_nat(1116048u);
return v___x_5_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentCharge(void){
_start:
{
lean_object* v___x_6_; 
v___x_6_ = lean_unsigned_to_nat(981104u);
return v___x_6_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_budget(void){
_start:
{
lean_object* v___x_7_; 
v___x_7_ = lean_cstr_to_nat("274980728111395087");
return v___x_7_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_remainingBudget(void){
_start:
{
lean_object* v___x_8_; 
v___x_8_ = lean_cstr_to_nat("274980728110413983");
return v___x_8_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_legacyM1Paid(void){
_start:
{
lean_object* v___x_9_; 
v___x_9_ = lean_cstr_to_nat("422354730332");
return v___x_9_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_List_mapTR_loop___at___00KbM1SourceBoundBridge_tangentImageEnvelope_spec__0___redArg(lean_object* v___x_10_, lean_object* v_a_11_, lean_object* v_a_12_){
_start:
{
if (lean_obj_tag(v_a_11_) == 0)
{
lean_object* v___x_13_; 
lean_dec(v___x_10_);
v___x_13_ = l_List_reverse___redArg(v_a_12_);
return v___x_13_;
}
else
{
lean_object* v_head_14_; lean_object* v_tail_15_; lean_object* v___x_17_; uint8_t v_isShared_18_; uint8_t v_isSharedCheck_24_; 
v_head_14_ = lean_ctor_get(v_a_11_, 0);
v_tail_15_ = lean_ctor_get(v_a_11_, 1);
v_isSharedCheck_24_ = !lean_is_exclusive(v_a_11_);
if (v_isSharedCheck_24_ == 0)
{
v___x_17_ = v_a_11_;
v_isShared_18_ = v_isSharedCheck_24_;
goto v_resetjp_16_;
}
else
{
lean_inc(v_tail_15_);
lean_inc(v_head_14_);
lean_dec(v_a_11_);
v___x_17_ = lean_box(0);
v_isShared_18_ = v_isSharedCheck_24_;
goto v_resetjp_16_;
}
v_resetjp_16_:
{
lean_object* v___x_19_; lean_object* v___x_21_; 
lean_inc(v___x_10_);
v___x_19_ = lean_apply_1(v___x_10_, v_head_14_);
if (v_isShared_18_ == 0)
{
lean_ctor_set(v___x_17_, 1, v_a_12_);
lean_ctor_set(v___x_17_, 0, v___x_19_);
v___x_21_ = v___x_17_;
goto v_reusejp_20_;
}
else
{
lean_object* v_reuseFailAlloc_23_; 
v_reuseFailAlloc_23_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_23_, 0, v___x_19_);
lean_ctor_set(v_reuseFailAlloc_23_, 1, v_a_12_);
v___x_21_ = v_reuseFailAlloc_23_;
goto v_reusejp_20_;
}
v_reusejp_20_:
{
v_a_11_ = v_tail_15_;
v_a_12_ = v___x_21_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentImageEnvelope___redArg(lean_object* v_data_25_){
_start:
{
lean_object* v_eligible_26_; lean_object* v_slopeAt_27_; lean_object* v___x_28_; lean_object* v___x_29_; 
v_eligible_26_ = lean_ctor_get(v_data_25_, 0);
lean_inc(v_eligible_26_);
v_slopeAt_27_ = lean_ctor_get(v_data_25_, 1);
lean_inc(v_slopeAt_27_);
lean_dec_ref(v_data_25_);
v___x_28_ = lean_box(0);
v___x_29_ = lp_kbM1SourceBoundBridge_List_mapTR_loop___at___00KbM1SourceBoundBridge_tangentImageEnvelope_spec__0___redArg(v_slopeAt_27_, v_eligible_26_, v___x_28_);
return v___x_29_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentImageEnvelope(lean_object* v_D_30_, lean_object* v_F_31_, lean_object* v_data_32_){
_start:
{
lean_object* v___x_33_; 
v___x_33_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentImageEnvelope___redArg(v_data_32_);
return v___x_33_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_List_mapTR_loop___at___00KbM1SourceBoundBridge_tangentImageEnvelope_spec__0(lean_object* v_D_34_, lean_object* v_F_35_, lean_object* v___x_36_, lean_object* v_a_37_, lean_object* v_a_38_){
_start:
{
lean_object* v___x_39_; 
v___x_39_ = lp_kbM1SourceBoundBridge_List_mapTR_loop___at___00KbM1SourceBoundBridge_tangentImageEnvelope_spec__0___redArg(v___x_36_, v_a_37_, v_a_38_);
return v___x_39_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_List_filterTR_loop___at___00KbM1SourceBoundBridge_paidEnvelope_spec__0___redArg(lean_object* v_bad_40_, lean_object* v_a_41_, lean_object* v_a_42_){
_start:
{
if (lean_obj_tag(v_a_41_) == 0)
{
lean_object* v___x_43_; 
lean_dec_ref(v_bad_40_);
v___x_43_ = l_List_reverse___redArg(v_a_42_);
return v___x_43_;
}
else
{
lean_object* v_head_44_; lean_object* v_tail_45_; lean_object* v___x_47_; uint8_t v_isShared_48_; uint8_t v_isSharedCheck_56_; 
v_head_44_ = lean_ctor_get(v_a_41_, 0);
v_tail_45_ = lean_ctor_get(v_a_41_, 1);
v_isSharedCheck_56_ = !lean_is_exclusive(v_a_41_);
if (v_isSharedCheck_56_ == 0)
{
v___x_47_ = v_a_41_;
v_isShared_48_ = v_isSharedCheck_56_;
goto v_resetjp_46_;
}
else
{
lean_inc(v_tail_45_);
lean_inc(v_head_44_);
lean_dec(v_a_41_);
v___x_47_ = lean_box(0);
v_isShared_48_ = v_isSharedCheck_56_;
goto v_resetjp_46_;
}
v_resetjp_46_:
{
lean_object* v___x_49_; uint8_t v___x_50_; 
lean_inc_ref(v_bad_40_);
lean_inc(v_head_44_);
v___x_49_ = lean_apply_1(v_bad_40_, v_head_44_);
v___x_50_ = lean_unbox(v___x_49_);
if (v___x_50_ == 0)
{
lean_del_object(v___x_47_);
lean_dec(v_head_44_);
v_a_41_ = v_tail_45_;
goto _start;
}
else
{
lean_object* v___x_53_; 
if (v_isShared_48_ == 0)
{
lean_ctor_set(v___x_47_, 1, v_a_42_);
v___x_53_ = v___x_47_;
goto v_reusejp_52_;
}
else
{
lean_object* v_reuseFailAlloc_55_; 
v_reuseFailAlloc_55_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_55_, 0, v_head_44_);
lean_ctor_set(v_reuseFailAlloc_55_, 1, v_a_42_);
v___x_53_ = v_reuseFailAlloc_55_;
goto v_reusejp_52_;
}
v_reusejp_52_:
{
v_a_41_ = v_tail_45_;
v_a_42_ = v___x_53_;
goto _start;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_paidEnvelope___redArg(lean_object* v_bad_57_, lean_object* v_data_58_){
_start:
{
lean_object* v___x_59_; lean_object* v___x_60_; lean_object* v___x_61_; 
v___x_59_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentImageEnvelope___redArg(v_data_58_);
v___x_60_ = lean_box(0);
v___x_61_ = lp_kbM1SourceBoundBridge_List_filterTR_loop___at___00KbM1SourceBoundBridge_paidEnvelope_spec__0___redArg(v_bad_57_, v___x_59_, v___x_60_);
return v___x_61_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_paidEnvelope(lean_object* v_D_62_, lean_object* v_F_63_, lean_object* v_bad_64_, lean_object* v_data_65_){
_start:
{
lean_object* v___x_66_; 
v___x_66_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_paidEnvelope___redArg(v_bad_64_, v_data_65_);
return v___x_66_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_List_filterTR_loop___at___00KbM1SourceBoundBridge_paidEnvelope_spec__0(lean_object* v_F_67_, lean_object* v_bad_68_, lean_object* v_a_69_, lean_object* v_a_70_){
_start:
{
lean_object* v___x_71_; 
v___x_71_ = lp_kbM1SourceBoundBridge_List_filterTR_loop___at___00KbM1SourceBoundBridge_paidEnvelope_spec__0___redArg(v_bad_68_, v_a_69_, v_a_70_);
return v___x_71_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorIdx(uint8_t v_x_72_){
_start:
{
switch(v_x_72_)
{
case 0:
{
lean_object* v___x_73_; 
v___x_73_ = lean_unsigned_to_nat(0u);
return v___x_73_;
}
case 1:
{
lean_object* v___x_74_; 
v___x_74_ = lean_unsigned_to_nat(1u);
return v___x_74_;
}
case 2:
{
lean_object* v___x_75_; 
v___x_75_ = lean_unsigned_to_nat(2u);
return v___x_75_;
}
case 3:
{
lean_object* v___x_76_; 
v___x_76_ = lean_unsigned_to_nat(3u);
return v___x_76_;
}
default: 
{
lean_object* v___x_77_; 
v___x_77_ = lean_unsigned_to_nat(4u);
return v___x_77_;
}
}
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorIdx___boxed(lean_object* v_x_78_){
_start:
{
uint8_t v_x_boxed_79_; lean_object* v_res_80_; 
v_x_boxed_79_ = lean_unbox(v_x_78_);
v_res_80_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorIdx(v_x_boxed_79_);
return v_res_80_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_toCtorIdx(uint8_t v_x_81_){
_start:
{
lean_object* v___x_82_; 
v___x_82_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorIdx(v_x_81_);
return v___x_82_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_toCtorIdx___boxed(lean_object* v_x_83_){
_start:
{
uint8_t v_x_4__boxed_84_; lean_object* v_res_85_; 
v_x_4__boxed_84_ = lean_unbox(v_x_83_);
v_res_85_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_toCtorIdx(v_x_4__boxed_84_);
return v_res_85_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim___redArg(lean_object* v_k_86_){
_start:
{
lean_inc(v_k_86_);
return v_k_86_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim___redArg___boxed(lean_object* v_k_87_){
_start:
{
lean_object* v_res_88_; 
v_res_88_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim___redArg(v_k_87_);
lean_dec(v_k_87_);
return v_res_88_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim(lean_object* v_motive_89_, lean_object* v_ctorIdx_90_, uint8_t v_t_91_, lean_object* v_h_92_, lean_object* v_k_93_){
_start:
{
lean_inc(v_k_93_);
return v_k_93_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim___boxed(lean_object* v_motive_94_, lean_object* v_ctorIdx_95_, lean_object* v_t_96_, lean_object* v_h_97_, lean_object* v_k_98_){
_start:
{
uint8_t v_t_boxed_99_; lean_object* v_res_100_; 
v_t_boxed_99_ = lean_unbox(v_t_96_);
v_res_100_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorElim(v_motive_94_, v_ctorIdx_95_, v_t_boxed_99_, v_h_97_, v_k_98_);
lean_dec(v_k_98_);
lean_dec(v_ctorIdx_95_);
return v_res_100_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim___redArg(lean_object* v_paid_101_){
_start:
{
lean_inc(v_paid_101_);
return v_paid_101_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim___redArg___boxed(lean_object* v_paid_102_){
_start:
{
lean_object* v_res_103_; 
v_res_103_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim___redArg(v_paid_102_);
lean_dec(v_paid_102_);
return v_res_103_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim(lean_object* v_motive_104_, uint8_t v_t_105_, lean_object* v_h_106_, lean_object* v_paid_107_){
_start:
{
lean_inc(v_paid_107_);
return v_paid_107_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim___boxed(lean_object* v_motive_108_, lean_object* v_t_109_, lean_object* v_h_110_, lean_object* v_paid_111_){
_start:
{
uint8_t v_t_boxed_112_; lean_object* v_res_113_; 
v_t_boxed_112_ = lean_unbox(v_t_109_);
v_res_113_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_paid_elim(v_motive_108_, v_t_boxed_112_, v_h_110_, v_paid_111_);
lean_dec(v_paid_111_);
return v_res_113_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim___redArg(lean_object* v_q_114_){
_start:
{
lean_inc(v_q_114_);
return v_q_114_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim___redArg___boxed(lean_object* v_q_115_){
_start:
{
lean_object* v_res_116_; 
v_res_116_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim___redArg(v_q_115_);
lean_dec(v_q_115_);
return v_res_116_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim(lean_object* v_motive_117_, uint8_t v_t_118_, lean_object* v_h_119_, lean_object* v_q_120_){
_start:
{
lean_inc(v_q_120_);
return v_q_120_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim___boxed(lean_object* v_motive_121_, lean_object* v_t_122_, lean_object* v_h_123_, lean_object* v_q_124_){
_start:
{
uint8_t v_t_boxed_125_; lean_object* v_res_126_; 
v_t_boxed_125_ = lean_unbox(v_t_122_);
v_res_126_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_q_elim(v_motive_121_, v_t_boxed_125_, v_h_123_, v_q_124_);
lean_dec(v_q_124_);
return v_res_126_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim___redArg(lean_object* v_bc_127_){
_start:
{
lean_inc(v_bc_127_);
return v_bc_127_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim___redArg___boxed(lean_object* v_bc_128_){
_start:
{
lean_object* v_res_129_; 
v_res_129_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim___redArg(v_bc_128_);
lean_dec(v_bc_128_);
return v_res_129_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim(lean_object* v_motive_130_, uint8_t v_t_131_, lean_object* v_h_132_, lean_object* v_bc_133_){
_start:
{
lean_inc(v_bc_133_);
return v_bc_133_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim___boxed(lean_object* v_motive_134_, lean_object* v_t_135_, lean_object* v_h_136_, lean_object* v_bc_137_){
_start:
{
uint8_t v_t_boxed_138_; lean_object* v_res_139_; 
v_t_boxed_138_ = lean_unbox(v_t_135_);
v_res_139_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_bc_elim(v_motive_134_, v_t_boxed_138_, v_h_136_, v_bc_137_);
lean_dec(v_bc_137_);
return v_res_139_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim___redArg(lean_object* v_new_140_){
_start:
{
lean_inc(v_new_140_);
return v_new_140_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim___redArg___boxed(lean_object* v_new_141_){
_start:
{
lean_object* v_res_142_; 
v_res_142_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim___redArg(v_new_141_);
lean_dec(v_new_141_);
return v_res_142_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim(lean_object* v_motive_143_, uint8_t v_t_144_, lean_object* v_h_145_, lean_object* v_new_146_){
_start:
{
lean_inc(v_new_146_);
return v_new_146_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim___boxed(lean_object* v_motive_147_, lean_object* v_t_148_, lean_object* v_h_149_, lean_object* v_new_150_){
_start:
{
uint8_t v_t_boxed_151_; lean_object* v_res_152_; 
v_t_boxed_151_ = lean_unbox(v_t_148_);
v_res_152_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_new_elim(v_motive_147_, v_t_boxed_151_, v_h_149_, v_new_150_);
lean_dec(v_new_150_);
return v_res_152_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim___redArg(lean_object* v_outside_153_){
_start:
{
lean_inc(v_outside_153_);
return v_outside_153_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim___redArg___boxed(lean_object* v_outside_154_){
_start:
{
lean_object* v_res_155_; 
v_res_155_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim___redArg(v_outside_154_);
lean_dec(v_outside_154_);
return v_res_155_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim(lean_object* v_motive_156_, uint8_t v_t_157_, lean_object* v_h_158_, lean_object* v_outside_159_){
_start:
{
lean_inc(v_outside_159_);
return v_outside_159_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim___boxed(lean_object* v_motive_160_, lean_object* v_t_161_, lean_object* v_h_162_, lean_object* v_outside_163_){
_start:
{
uint8_t v_t_boxed_164_; lean_object* v_res_165_; 
v_t_boxed_164_ = lean_unbox(v_t_161_);
v_res_165_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_outside_elim(v_motive_160_, v_t_boxed_164_, v_h_162_, v_outside_163_);
lean_dec(v_outside_163_);
return v_res_165_;
}
}
LEAN_EXPORT uint8_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ofNat(lean_object* v_n_166_){
_start:
{
lean_object* v___x_167_; uint8_t v___x_168_; 
v___x_167_ = lean_unsigned_to_nat(1u);
v___x_168_ = lean_nat_dec_le(v_n_166_, v___x_167_);
if (v___x_168_ == 0)
{
lean_object* v___x_169_; uint8_t v___x_170_; 
v___x_169_ = lean_unsigned_to_nat(2u);
v___x_170_ = lean_nat_dec_le(v_n_166_, v___x_169_);
if (v___x_170_ == 0)
{
lean_object* v___x_171_; uint8_t v___x_172_; 
v___x_171_ = lean_unsigned_to_nat(3u);
v___x_172_ = lean_nat_dec_le(v_n_166_, v___x_171_);
if (v___x_172_ == 0)
{
uint8_t v___x_173_; 
v___x_173_ = 4;
return v___x_173_;
}
else
{
uint8_t v___x_174_; 
v___x_174_ = 3;
return v___x_174_;
}
}
else
{
uint8_t v___x_175_; 
v___x_175_ = 2;
return v___x_175_;
}
}
else
{
lean_object* v___x_176_; uint8_t v___x_177_; 
v___x_176_ = lean_unsigned_to_nat(0u);
v___x_177_ = lean_nat_dec_le(v_n_166_, v___x_176_);
if (v___x_177_ == 0)
{
uint8_t v___x_178_; 
v___x_178_ = 1;
return v___x_178_;
}
else
{
uint8_t v___x_179_; 
v___x_179_ = 0;
return v___x_179_;
}
}
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ofNat___boxed(lean_object* v_n_180_){
_start:
{
uint8_t v_res_181_; lean_object* v_r_182_; 
v_res_181_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ofNat(v_n_180_);
lean_dec(v_n_180_);
v_r_182_ = lean_box(v_res_181_);
return v_r_182_;
}
}
LEAN_EXPORT uint8_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instDecidableEqOwner(uint8_t v_x_183_, uint8_t v_y_184_){
_start:
{
lean_object* v___x_185_; lean_object* v___x_186_; uint8_t v___x_187_; 
v___x_185_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorIdx(v_x_183_);
v___x_186_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_Owner_ctorIdx(v_y_184_);
v___x_187_ = lean_nat_dec_eq(v___x_185_, v___x_186_);
lean_dec(v___x_186_);
lean_dec(v___x_185_);
return v___x_187_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instDecidableEqOwner___boxed(lean_object* v_x_188_, lean_object* v_y_189_){
_start:
{
uint8_t v_x_13__boxed_190_; uint8_t v_y_14__boxed_191_; uint8_t v_res_192_; lean_object* v_r_193_; 
v_x_13__boxed_190_ = lean_unbox(v_x_188_);
v_y_14__boxed_191_ = lean_unbox(v_y_189_);
v_res_192_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instDecidableEqOwner(v_x_13__boxed_190_, v_y_14__boxed_191_);
v_r_193_ = lean_box(v_res_192_);
return v_r_193_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10(void){
_start:
{
lean_object* v___x_209_; lean_object* v___x_210_; 
v___x_209_ = lean_unsigned_to_nat(2u);
v___x_210_ = lean_nat_to_int(v___x_209_);
return v___x_210_;
}
}
static lean_object* _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11(void){
_start:
{
lean_object* v___x_211_; lean_object* v___x_212_; 
v___x_211_ = lean_unsigned_to_nat(1u);
v___x_212_ = lean_nat_to_int(v___x_211_);
return v___x_212_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr(uint8_t v_x_213_, lean_object* v_prec_214_){
_start:
{
lean_object* v___y_216_; lean_object* v___y_223_; lean_object* v___y_230_; lean_object* v___y_237_; lean_object* v___y_244_; 
switch(v_x_213_)
{
case 0:
{
lean_object* v___x_250_; uint8_t v___x_251_; 
v___x_250_ = lean_unsigned_to_nat(1024u);
v___x_251_ = lean_nat_dec_le(v___x_250_, v_prec_214_);
if (v___x_251_ == 0)
{
lean_object* v___x_252_; 
v___x_252_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10);
v___y_216_ = v___x_252_;
goto v___jp_215_;
}
else
{
lean_object* v___x_253_; 
v___x_253_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11);
v___y_216_ = v___x_253_;
goto v___jp_215_;
}
}
case 1:
{
lean_object* v___x_254_; uint8_t v___x_255_; 
v___x_254_ = lean_unsigned_to_nat(1024u);
v___x_255_ = lean_nat_dec_le(v___x_254_, v_prec_214_);
if (v___x_255_ == 0)
{
lean_object* v___x_256_; 
v___x_256_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10);
v___y_223_ = v___x_256_;
goto v___jp_222_;
}
else
{
lean_object* v___x_257_; 
v___x_257_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11);
v___y_223_ = v___x_257_;
goto v___jp_222_;
}
}
case 2:
{
lean_object* v___x_258_; uint8_t v___x_259_; 
v___x_258_ = lean_unsigned_to_nat(1024u);
v___x_259_ = lean_nat_dec_le(v___x_258_, v_prec_214_);
if (v___x_259_ == 0)
{
lean_object* v___x_260_; 
v___x_260_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10);
v___y_230_ = v___x_260_;
goto v___jp_229_;
}
else
{
lean_object* v___x_261_; 
v___x_261_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11);
v___y_230_ = v___x_261_;
goto v___jp_229_;
}
}
case 3:
{
lean_object* v___x_262_; uint8_t v___x_263_; 
v___x_262_ = lean_unsigned_to_nat(1024u);
v___x_263_ = lean_nat_dec_le(v___x_262_, v_prec_214_);
if (v___x_263_ == 0)
{
lean_object* v___x_264_; 
v___x_264_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10);
v___y_237_ = v___x_264_;
goto v___jp_236_;
}
else
{
lean_object* v___x_265_; 
v___x_265_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11);
v___y_237_ = v___x_265_;
goto v___jp_236_;
}
}
default: 
{
lean_object* v___x_266_; uint8_t v___x_267_; 
v___x_266_ = lean_unsigned_to_nat(1024u);
v___x_267_ = lean_nat_dec_le(v___x_266_, v_prec_214_);
if (v___x_267_ == 0)
{
lean_object* v___x_268_; 
v___x_268_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__10);
v___y_244_ = v___x_268_;
goto v___jp_243_;
}
else
{
lean_object* v___x_269_; 
v___x_269_ = lean_obj_once(&lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11, &lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11_once, _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__11);
v___y_244_ = v___x_269_;
goto v___jp_243_;
}
}
}
v___jp_215_:
{
lean_object* v___x_217_; lean_object* v___x_218_; uint8_t v___x_219_; lean_object* v___x_220_; lean_object* v___x_221_; 
v___x_217_ = ((lean_object*)(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__1));
lean_inc(v___y_216_);
v___x_218_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_218_, 0, v___y_216_);
lean_ctor_set(v___x_218_, 1, v___x_217_);
v___x_219_ = 0;
v___x_220_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_220_, 0, v___x_218_);
lean_ctor_set_uint8(v___x_220_, sizeof(void*)*1, v___x_219_);
v___x_221_ = l_Repr_addAppParen(v___x_220_, v_prec_214_);
return v___x_221_;
}
v___jp_222_:
{
lean_object* v___x_224_; lean_object* v___x_225_; uint8_t v___x_226_; lean_object* v___x_227_; lean_object* v___x_228_; 
v___x_224_ = ((lean_object*)(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__3));
lean_inc(v___y_223_);
v___x_225_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_225_, 0, v___y_223_);
lean_ctor_set(v___x_225_, 1, v___x_224_);
v___x_226_ = 0;
v___x_227_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_227_, 0, v___x_225_);
lean_ctor_set_uint8(v___x_227_, sizeof(void*)*1, v___x_226_);
v___x_228_ = l_Repr_addAppParen(v___x_227_, v_prec_214_);
return v___x_228_;
}
v___jp_229_:
{
lean_object* v___x_231_; lean_object* v___x_232_; uint8_t v___x_233_; lean_object* v___x_234_; lean_object* v___x_235_; 
v___x_231_ = ((lean_object*)(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__5));
lean_inc(v___y_230_);
v___x_232_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_232_, 0, v___y_230_);
lean_ctor_set(v___x_232_, 1, v___x_231_);
v___x_233_ = 0;
v___x_234_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_234_, 0, v___x_232_);
lean_ctor_set_uint8(v___x_234_, sizeof(void*)*1, v___x_233_);
v___x_235_ = l_Repr_addAppParen(v___x_234_, v_prec_214_);
return v___x_235_;
}
v___jp_236_:
{
lean_object* v___x_238_; lean_object* v___x_239_; uint8_t v___x_240_; lean_object* v___x_241_; lean_object* v___x_242_; 
v___x_238_ = ((lean_object*)(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__7));
lean_inc(v___y_237_);
v___x_239_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_239_, 0, v___y_237_);
lean_ctor_set(v___x_239_, 1, v___x_238_);
v___x_240_ = 0;
v___x_241_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_241_, 0, v___x_239_);
lean_ctor_set_uint8(v___x_241_, sizeof(void*)*1, v___x_240_);
v___x_242_ = l_Repr_addAppParen(v___x_241_, v_prec_214_);
return v___x_242_;
}
v___jp_243_:
{
lean_object* v___x_245_; lean_object* v___x_246_; uint8_t v___x_247_; lean_object* v___x_248_; lean_object* v___x_249_; 
v___x_245_ = ((lean_object*)(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___closed__9));
lean_inc(v___y_244_);
v___x_246_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_246_, 0, v___y_244_);
lean_ctor_set(v___x_246_, 1, v___x_245_);
v___x_247_ = 0;
v___x_248_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_248_, 0, v___x_246_);
lean_ctor_set_uint8(v___x_248_, sizeof(void*)*1, v___x_247_);
v___x_249_ = l_Repr_addAppParen(v___x_248_, v_prec_214_);
return v___x_249_;
}
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr___boxed(lean_object* v_x_270_, lean_object* v_prec_271_){
_start:
{
uint8_t v_x_289__boxed_272_; lean_object* v_res_273_; 
v_x_289__boxed_272_ = lean_unbox(v_x_270_);
v_res_273_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_instReprOwner_repr(v_x_289__boxed_272_, v_prec_271_);
lean_dec(v_prec_271_);
return v_res_273_;
}
}
LEAN_EXPORT uint8_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner___redArg(lean_object* v_bad_276_, lean_object* v_tangent_277_, lean_object* v_qCertified_278_, lean_object* v_bcCertified_279_, lean_object* v_00_u03b3_280_){
_start:
{
lean_object* v___x_281_; uint8_t v___x_282_; 
lean_inc(v_00_u03b3_280_);
v___x_281_ = lean_apply_1(v_bad_276_, v_00_u03b3_280_);
v___x_282_ = lean_unbox(v___x_281_);
if (v___x_282_ == 0)
{
uint8_t v___x_283_; 
lean_dec(v_00_u03b3_280_);
lean_dec_ref(v_bcCertified_279_);
lean_dec_ref(v_qCertified_278_);
lean_dec_ref(v_tangent_277_);
v___x_283_ = 4;
return v___x_283_;
}
else
{
lean_object* v___x_284_; uint8_t v___x_285_; 
lean_inc(v_00_u03b3_280_);
v___x_284_ = lean_apply_1(v_tangent_277_, v_00_u03b3_280_);
v___x_285_ = lean_unbox(v___x_284_);
if (v___x_285_ == 0)
{
lean_object* v___x_286_; uint8_t v___x_287_; 
lean_inc(v_00_u03b3_280_);
v___x_286_ = lean_apply_1(v_qCertified_278_, v_00_u03b3_280_);
v___x_287_ = lean_unbox(v___x_286_);
if (v___x_287_ == 0)
{
lean_object* v___x_288_; uint8_t v___x_289_; 
v___x_288_ = lean_apply_1(v_bcCertified_279_, v_00_u03b3_280_);
v___x_289_ = lean_unbox(v___x_288_);
if (v___x_289_ == 0)
{
uint8_t v___x_290_; 
v___x_290_ = 3;
return v___x_290_;
}
else
{
uint8_t v___x_291_; 
v___x_291_ = 2;
return v___x_291_;
}
}
else
{
uint8_t v___x_292_; 
lean_dec(v_00_u03b3_280_);
lean_dec_ref(v_bcCertified_279_);
v___x_292_ = 1;
return v___x_292_;
}
}
else
{
uint8_t v___x_293_; 
lean_dec(v_00_u03b3_280_);
lean_dec_ref(v_bcCertified_279_);
lean_dec_ref(v_qCertified_278_);
v___x_293_ = 0;
return v___x_293_;
}
}
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner___redArg___boxed(lean_object* v_bad_294_, lean_object* v_tangent_295_, lean_object* v_qCertified_296_, lean_object* v_bcCertified_297_, lean_object* v_00_u03b3_298_){
_start:
{
uint8_t v_res_299_; lean_object* v_r_300_; 
v_res_299_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner___redArg(v_bad_294_, v_tangent_295_, v_qCertified_296_, v_bcCertified_297_, v_00_u03b3_298_);
v_r_300_ = lean_box(v_res_299_);
return v_r_300_;
}
}
LEAN_EXPORT uint8_t lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner(lean_object* v_F_301_, lean_object* v_bad_302_, lean_object* v_tangent_303_, lean_object* v_qCertified_304_, lean_object* v_bcCertified_305_, lean_object* v_00_u03b3_306_){
_start:
{
uint8_t v___x_307_; 
v___x_307_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner___redArg(v_bad_302_, v_tangent_303_, v_qCertified_304_, v_bcCertified_305_, v_00_u03b3_306_);
return v___x_307_;
}
}
LEAN_EXPORT lean_object* lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner___boxed(lean_object* v_F_308_, lean_object* v_bad_309_, lean_object* v_tangent_310_, lean_object* v_qCertified_311_, lean_object* v_bcCertified_312_, lean_object* v_00_u03b3_313_){
_start:
{
uint8_t v_res_314_; lean_object* v_r_315_; 
v_res_314_ = lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_firstOwner(v_F_308_, v_bad_309_, v_tangent_310_, v_qCertified_311_, v_bcCertified_312_, v_00_u03b3_313_);
v_r_315_ = lean_box(v_res_314_);
return v_r_315_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Std(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_kbM1SourceBoundBridge_KbM1SourceBoundBridge(uint8_t builtin) {
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
lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_basePrime = _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_basePrime();
lean_mark_persistent(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_basePrime);
lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_extensionDegree = _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_extensionDegree();
lean_mark_persistent(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_extensionDegree);
lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_domainSize = _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_domainSize();
lean_mark_persistent(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_domainSize);
lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_codeDimension = _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_codeDimension();
lean_mark_persistent(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_codeDimension);
lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_agreement = _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_agreement();
lean_mark_persistent(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_agreement);
lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentCharge = _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentCharge();
lean_mark_persistent(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_tangentCharge);
lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_budget = _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_budget();
lean_mark_persistent(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_budget);
lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_remainingBudget = _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_remainingBudget();
lean_mark_persistent(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_remainingBudget);
lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_legacyM1Paid = _init_lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_legacyM1Paid();
lean_mark_persistent(lp_kbM1SourceBoundBridge_KbM1SourceBoundBridge_legacyM1Paid);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
