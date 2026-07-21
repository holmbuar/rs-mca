// Lean compiler output
// Module: M31QRootedShell.PaddingBridgeAudit
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
uint8_t l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(lean_object*, lean_object*);
uint8_t lean_nat_dec_lt(lean_object*, lean_object*);
lean_object* l_List_range(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* l_List_drop___redArg(lean_object*, lean_object*);
lean_object* lean_nat_mul(lean_object*, lean_object*);
lean_object* lean_nat_add(lean_object*, lean_object*);
lean_object* lean_nat_mod(lean_object*, lean_object*);
lean_object* l_List_lengthTR___redArg(lean_object*);
lean_object* lean_mk_empty_array_with_capacity(lean_object*);
lean_object* l___private_Init_Data_List_Impl_0__List_takeTR_go___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_prime;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder___closed__0;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__0 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__0_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__1 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__1_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__1_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__2 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__2_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__2_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__3 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__3_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__3_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__4 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__4_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__4_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__5 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__5_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__5_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__6 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__6_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__6_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__7 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__7_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__7_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__8 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__8_value;
LEAN_EXPORT const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_commonPaddingOrder___closed__8_value;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_noDuplicates(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_noDuplicates___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_validOrder_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_validOrder_spec__0___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_validOrder(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_validOrder___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_evalMod11(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_evalMod11___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_zeroCodeword(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_zeroCodeword___boxed(lean_object*);
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__0 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__0_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__1 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__1_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__1_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__2 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__2_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__2_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__3 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__3_value;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_received(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_received___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_agreementThreshold;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_radius;
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_agreements_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_agreements(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_errors_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_errors(lean_object*, lean_object*);
static const lean_array_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_selected___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_array_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 246}, .m_size = 0, .m_capacity = 0, .m_data = {}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_selected___closed__0 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_selected___closed__0_value;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_selected(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_padding(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_paddedRoots_spec__0(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedRoots(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_inter_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_inter_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_inter(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_inter___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___lam__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___lam__0___boxed(lean_object*);
static const lean_closure_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___lam__0___boxed, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__0 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__0_value;
static const lean_closure_object lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___boxed, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__1 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__1_value;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedCommonRoots(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualPairIndex(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedPairIndex(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__1(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__1___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__0___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31Radius;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstIndexCap;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeIndexCap;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstBlockedWeightMax;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeBlockedWeightMax;
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_prime(void){
_start:
{
lean_object* v___x_1_; 
v___x_1_ = lean_unsigned_to_nat(11u);
return v___x_1_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder___closed__0(void){
_start:
{
lean_object* v___x_2_; lean_object* v___x_3_; 
v___x_2_ = lean_unsigned_to_nat(9u);
v___x_3_ = l_List_range(v___x_2_);
return v___x_3_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder(void){
_start:
{
lean_object* v___x_4_; 
v___x_4_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder___closed__0, &lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder___closed__0);
return v___x_4_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_noDuplicates(lean_object* v_x_33_){
_start:
{
if (lean_obj_tag(v_x_33_) == 0)
{
uint8_t v___x_34_; 
v___x_34_ = 1;
return v___x_34_;
}
else
{
lean_object* v_head_35_; lean_object* v_tail_36_; uint8_t v___x_37_; 
v_head_35_ = lean_ctor_get(v_x_33_, 0);
v_tail_36_ = lean_ctor_get(v_x_33_, 1);
v___x_37_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_35_, v_tail_36_);
if (v___x_37_ == 0)
{
v_x_33_ = v_tail_36_;
goto _start;
}
else
{
uint8_t v___x_39_; 
v___x_39_ = 0;
return v___x_39_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_noDuplicates___boxed(lean_object* v_x_40_){
_start:
{
uint8_t v_res_41_; lean_object* v_r_42_; 
v_res_41_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_noDuplicates(v_x_40_);
lean_dec(v_x_40_);
v_r_42_ = lean_box(v_res_41_);
return v_r_42_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_validOrder_spec__0(lean_object* v_x_43_){
_start:
{
if (lean_obj_tag(v_x_43_) == 0)
{
uint8_t v___x_44_; 
v___x_44_ = 1;
return v___x_44_;
}
else
{
lean_object* v_head_45_; lean_object* v_tail_46_; lean_object* v___x_47_; uint8_t v___x_48_; 
v_head_45_ = lean_ctor_get(v_x_43_, 0);
v_tail_46_ = lean_ctor_get(v_x_43_, 1);
v___x_47_ = lean_unsigned_to_nat(11u);
v___x_48_ = lean_nat_dec_lt(v_head_45_, v___x_47_);
if (v___x_48_ == 0)
{
return v___x_48_;
}
else
{
v_x_43_ = v_tail_46_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_validOrder_spec__0___boxed(lean_object* v_x_50_){
_start:
{
uint8_t v_res_51_; lean_object* v_r_52_; 
v_res_51_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_validOrder_spec__0(v_x_50_);
lean_dec(v_x_50_);
v_r_52_ = lean_box(v_res_51_);
return v_r_52_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_validOrder(lean_object* v_order_53_){
_start:
{
uint8_t v___y_55_; lean_object* v___x_57_; lean_object* v___x_58_; uint8_t v___x_59_; 
v___x_57_ = l_List_lengthTR___redArg(v_order_53_);
v___x_58_ = lean_unsigned_to_nat(9u);
v___x_59_ = lean_nat_dec_eq(v___x_57_, v___x_58_);
lean_dec(v___x_57_);
if (v___x_59_ == 0)
{
v___y_55_ = v___x_59_;
goto v___jp_54_;
}
else
{
uint8_t v___x_60_; 
v___x_60_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_noDuplicates(v_order_53_);
v___y_55_ = v___x_60_;
goto v___jp_54_;
}
v___jp_54_:
{
if (v___y_55_ == 0)
{
return v___y_55_;
}
else
{
uint8_t v___x_56_; 
v___x_56_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_validOrder_spec__0(v_order_53_);
return v___x_56_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_validOrder___boxed(lean_object* v_order_61_){
_start:
{
uint8_t v_res_62_; lean_object* v_r_63_; 
v_res_62_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_validOrder(v_order_61_);
lean_dec(v_order_61_);
v_r_63_ = lean_box(v_res_62_);
return v_r_63_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_evalMod11(lean_object* v_x_64_, lean_object* v_x_65_){
_start:
{
if (lean_obj_tag(v_x_64_) == 0)
{
lean_object* v___x_66_; 
v___x_66_ = lean_unsigned_to_nat(0u);
return v___x_66_;
}
else
{
lean_object* v_head_67_; lean_object* v_tail_68_; lean_object* v___x_69_; lean_object* v___x_70_; lean_object* v___x_71_; lean_object* v___x_72_; lean_object* v___x_73_; 
v_head_67_ = lean_ctor_get(v_x_64_, 0);
v_tail_68_ = lean_ctor_get(v_x_64_, 1);
v___x_69_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_evalMod11(v_tail_68_, v_x_65_);
v___x_70_ = lean_nat_mul(v_x_65_, v___x_69_);
lean_dec(v___x_69_);
v___x_71_ = lean_nat_add(v_head_67_, v___x_70_);
lean_dec(v___x_70_);
v___x_72_ = lean_unsigned_to_nat(11u);
v___x_73_ = lean_nat_mod(v___x_71_, v___x_72_);
lean_dec(v___x_71_);
return v___x_73_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_evalMod11___boxed(lean_object* v_x_74_, lean_object* v_x_75_){
_start:
{
lean_object* v_res_76_; 
v_res_76_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_evalMod11(v_x_74_, v_x_75_);
lean_dec(v_x_75_);
lean_dec(v_x_74_);
return v_res_76_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_zeroCodeword(lean_object* v_x_77_){
_start:
{
lean_object* v___x_78_; 
v___x_78_ = lean_unsigned_to_nat(0u);
return v___x_78_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_zeroCodeword___boxed(lean_object* v_x_79_){
_start:
{
lean_object* v_res_80_; 
v_res_80_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_zeroCodeword(v_x_79_);
lean_dec(v_x_79_);
return v_res_80_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword(lean_object* v_x_93_){
_start:
{
lean_object* v___x_94_; lean_object* v___x_95_; 
v___x_94_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___closed__3));
v___x_95_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_evalMod11(v___x_94_, v_x_93_);
return v___x_95_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword___boxed(lean_object* v_x_96_){
_start:
{
lean_object* v_res_97_; 
v_res_97_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_cubicCodeword(v_x_96_);
lean_dec(v_x_96_);
return v_res_97_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_received(lean_object* v_x_98_){
_start:
{
lean_object* v___x_99_; uint8_t v___x_100_; 
v___x_99_ = lean_unsigned_to_nat(0u);
v___x_100_ = lean_nat_dec_eq(v_x_98_, v___x_99_);
if (v___x_100_ == 0)
{
lean_object* v___x_101_; uint8_t v___x_102_; 
v___x_101_ = lean_unsigned_to_nat(1u);
v___x_102_ = lean_nat_dec_eq(v_x_98_, v___x_101_);
if (v___x_102_ == 0)
{
lean_object* v___x_103_; uint8_t v___x_104_; 
v___x_103_ = lean_unsigned_to_nat(2u);
v___x_104_ = lean_nat_dec_eq(v_x_98_, v___x_103_);
if (v___x_104_ == 0)
{
lean_object* v___x_105_; uint8_t v___x_106_; 
v___x_105_ = lean_unsigned_to_nat(3u);
v___x_106_ = lean_nat_dec_eq(v_x_98_, v___x_105_);
if (v___x_106_ == 0)
{
lean_object* v___x_107_; uint8_t v___x_108_; 
v___x_107_ = lean_unsigned_to_nat(4u);
v___x_108_ = lean_nat_dec_eq(v_x_98_, v___x_107_);
if (v___x_108_ == 0)
{
lean_object* v___x_109_; uint8_t v___x_110_; 
v___x_109_ = lean_unsigned_to_nat(5u);
v___x_110_ = lean_nat_dec_eq(v_x_98_, v___x_109_);
if (v___x_110_ == 0)
{
lean_object* v___x_111_; uint8_t v___x_112_; 
v___x_111_ = lean_unsigned_to_nat(6u);
v___x_112_ = lean_nat_dec_eq(v_x_98_, v___x_111_);
if (v___x_112_ == 0)
{
lean_object* v___x_113_; uint8_t v___x_114_; 
v___x_113_ = lean_unsigned_to_nat(7u);
v___x_114_ = lean_nat_dec_eq(v_x_98_, v___x_113_);
if (v___x_114_ == 0)
{
lean_object* v___x_115_; uint8_t v___x_116_; 
v___x_115_ = lean_unsigned_to_nat(8u);
v___x_116_ = lean_nat_dec_eq(v_x_98_, v___x_115_);
if (v___x_116_ == 0)
{
return v___x_99_;
}
else
{
return v___x_111_;
}
}
else
{
return v___x_101_;
}
}
else
{
lean_object* v___x_117_; 
v___x_117_ = lean_unsigned_to_nat(10u);
return v___x_117_;
}
}
else
{
return v___x_99_;
}
}
else
{
return v___x_99_;
}
}
else
{
return v___x_99_;
}
}
else
{
return v___x_99_;
}
}
else
{
return v___x_99_;
}
}
else
{
return v___x_99_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_received___boxed(lean_object* v_x_118_){
_start:
{
lean_object* v_res_119_; 
v_res_119_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_received(v_x_118_);
lean_dec(v_x_118_);
return v_res_119_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_agreementThreshold(void){
_start:
{
lean_object* v___x_120_; 
v___x_120_ = lean_unsigned_to_nat(5u);
return v___x_120_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_radius(void){
_start:
{
lean_object* v___x_121_; 
v___x_121_ = lean_unsigned_to_nat(4u);
return v___x_121_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_agreements_spec__0(lean_object* v_c_122_, lean_object* v_a_123_, lean_object* v_a_124_){
_start:
{
if (lean_obj_tag(v_a_123_) == 0)
{
lean_object* v___x_125_; 
lean_dec_ref(v_c_122_);
v___x_125_ = l_List_reverse___redArg(v_a_124_);
return v___x_125_;
}
else
{
lean_object* v_head_126_; lean_object* v_tail_127_; lean_object* v___x_129_; uint8_t v_isShared_130_; uint8_t v_isSharedCheck_139_; 
v_head_126_ = lean_ctor_get(v_a_123_, 0);
v_tail_127_ = lean_ctor_get(v_a_123_, 1);
v_isSharedCheck_139_ = !lean_is_exclusive(v_a_123_);
if (v_isSharedCheck_139_ == 0)
{
v___x_129_ = v_a_123_;
v_isShared_130_ = v_isSharedCheck_139_;
goto v_resetjp_128_;
}
else
{
lean_inc(v_tail_127_);
lean_inc(v_head_126_);
lean_dec(v_a_123_);
v___x_129_ = lean_box(0);
v_isShared_130_ = v_isSharedCheck_139_;
goto v_resetjp_128_;
}
v_resetjp_128_:
{
lean_object* v___x_131_; lean_object* v___x_132_; uint8_t v___x_133_; 
v___x_131_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_received(v_head_126_);
lean_inc_ref(v_c_122_);
lean_inc(v_head_126_);
v___x_132_ = lean_apply_1(v_c_122_, v_head_126_);
v___x_133_ = lean_nat_dec_eq(v___x_131_, v___x_132_);
lean_dec(v___x_132_);
lean_dec(v___x_131_);
if (v___x_133_ == 0)
{
lean_del_object(v___x_129_);
lean_dec(v_head_126_);
v_a_123_ = v_tail_127_;
goto _start;
}
else
{
lean_object* v___x_136_; 
if (v_isShared_130_ == 0)
{
lean_ctor_set(v___x_129_, 1, v_a_124_);
v___x_136_ = v___x_129_;
goto v_reusejp_135_;
}
else
{
lean_object* v_reuseFailAlloc_138_; 
v_reuseFailAlloc_138_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_138_, 0, v_head_126_);
lean_ctor_set(v_reuseFailAlloc_138_, 1, v_a_124_);
v___x_136_ = v_reuseFailAlloc_138_;
goto v_reusejp_135_;
}
v_reusejp_135_:
{
v_a_123_ = v_tail_127_;
v_a_124_ = v___x_136_;
goto _start;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_agreements(lean_object* v_order_140_, lean_object* v_c_141_){
_start:
{
lean_object* v___x_142_; lean_object* v___x_143_; 
v___x_142_ = lean_box(0);
v___x_143_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_agreements_spec__0(v_c_141_, v_order_140_, v___x_142_);
return v___x_143_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_errors_spec__0(lean_object* v_c_144_, lean_object* v_a_145_, lean_object* v_a_146_){
_start:
{
if (lean_obj_tag(v_a_145_) == 0)
{
lean_object* v___x_147_; 
lean_dec_ref(v_c_144_);
v___x_147_ = l_List_reverse___redArg(v_a_146_);
return v___x_147_;
}
else
{
lean_object* v_head_148_; lean_object* v_tail_149_; lean_object* v___x_151_; uint8_t v_isShared_152_; uint8_t v_isSharedCheck_161_; 
v_head_148_ = lean_ctor_get(v_a_145_, 0);
v_tail_149_ = lean_ctor_get(v_a_145_, 1);
v_isSharedCheck_161_ = !lean_is_exclusive(v_a_145_);
if (v_isSharedCheck_161_ == 0)
{
v___x_151_ = v_a_145_;
v_isShared_152_ = v_isSharedCheck_161_;
goto v_resetjp_150_;
}
else
{
lean_inc(v_tail_149_);
lean_inc(v_head_148_);
lean_dec(v_a_145_);
v___x_151_ = lean_box(0);
v_isShared_152_ = v_isSharedCheck_161_;
goto v_resetjp_150_;
}
v_resetjp_150_:
{
lean_object* v___x_153_; lean_object* v___x_154_; uint8_t v___x_155_; 
v___x_153_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_received(v_head_148_);
lean_inc_ref(v_c_144_);
lean_inc(v_head_148_);
v___x_154_ = lean_apply_1(v_c_144_, v_head_148_);
v___x_155_ = lean_nat_dec_eq(v___x_153_, v___x_154_);
lean_dec(v___x_154_);
lean_dec(v___x_153_);
if (v___x_155_ == 0)
{
lean_object* v___x_157_; 
if (v_isShared_152_ == 0)
{
lean_ctor_set(v___x_151_, 1, v_a_146_);
v___x_157_ = v___x_151_;
goto v_reusejp_156_;
}
else
{
lean_object* v_reuseFailAlloc_159_; 
v_reuseFailAlloc_159_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_159_, 0, v_head_148_);
lean_ctor_set(v_reuseFailAlloc_159_, 1, v_a_146_);
v___x_157_ = v_reuseFailAlloc_159_;
goto v_reusejp_156_;
}
v_reusejp_156_:
{
v_a_145_ = v_tail_149_;
v_a_146_ = v___x_157_;
goto _start;
}
}
else
{
lean_del_object(v___x_151_);
lean_dec(v_head_148_);
v_a_145_ = v_tail_149_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_errors(lean_object* v_order_162_, lean_object* v_c_163_){
_start:
{
lean_object* v___x_164_; lean_object* v___x_165_; 
v___x_164_ = lean_box(0);
v___x_165_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_errors_spec__0(v_c_163_, v_order_162_, v___x_164_);
return v___x_165_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_selected(lean_object* v_order_168_, lean_object* v_c_169_){
_start:
{
lean_object* v___x_170_; lean_object* v___x_171_; lean_object* v___x_172_; lean_object* v___x_173_; 
v___x_170_ = lean_unsigned_to_nat(5u);
v___x_171_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_agreements(v_order_168_, v_c_169_);
v___x_172_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_selected___closed__0));
lean_inc(v___x_171_);
v___x_173_ = l___private_Init_Data_List_Impl_0__List_takeTR_go___redArg(v___x_171_, v___x_171_, v___x_170_, v___x_172_);
lean_dec(v___x_171_);
return v___x_173_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_padding(lean_object* v_order_174_, lean_object* v_c_175_){
_start:
{
lean_object* v___x_176_; lean_object* v___x_177_; lean_object* v___x_178_; 
v___x_176_ = lean_unsigned_to_nat(5u);
v___x_177_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_agreements(v_order_174_, v_c_175_);
v___x_178_ = l_List_drop___redArg(v___x_176_, v___x_177_);
lean_dec(v___x_177_);
return v___x_178_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_paddedRoots_spec__0(lean_object* v_order_179_, lean_object* v_c_180_, lean_object* v_a_181_, lean_object* v_a_182_){
_start:
{
if (lean_obj_tag(v_a_181_) == 0)
{
lean_object* v___x_183_; 
lean_dec_ref(v_c_180_);
lean_dec(v_order_179_);
v___x_183_ = l_List_reverse___redArg(v_a_182_);
return v___x_183_;
}
else
{
lean_object* v_head_184_; lean_object* v_tail_185_; lean_object* v___x_187_; uint8_t v_isShared_188_; uint8_t v_isSharedCheck_196_; 
v_head_184_ = lean_ctor_get(v_a_181_, 0);
v_tail_185_ = lean_ctor_get(v_a_181_, 1);
v_isSharedCheck_196_ = !lean_is_exclusive(v_a_181_);
if (v_isSharedCheck_196_ == 0)
{
v___x_187_ = v_a_181_;
v_isShared_188_ = v_isSharedCheck_196_;
goto v_resetjp_186_;
}
else
{
lean_inc(v_tail_185_);
lean_inc(v_head_184_);
lean_dec(v_a_181_);
v___x_187_ = lean_box(0);
v_isShared_188_ = v_isSharedCheck_196_;
goto v_resetjp_186_;
}
v_resetjp_186_:
{
lean_object* v___x_189_; uint8_t v___x_190_; 
lean_inc_ref(v_c_180_);
lean_inc(v_order_179_);
v___x_189_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_selected(v_order_179_, v_c_180_);
v___x_190_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_184_, v___x_189_);
lean_dec(v___x_189_);
if (v___x_190_ == 0)
{
lean_object* v___x_192_; 
if (v_isShared_188_ == 0)
{
lean_ctor_set(v___x_187_, 1, v_a_182_);
v___x_192_ = v___x_187_;
goto v_reusejp_191_;
}
else
{
lean_object* v_reuseFailAlloc_194_; 
v_reuseFailAlloc_194_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_194_, 0, v_head_184_);
lean_ctor_set(v_reuseFailAlloc_194_, 1, v_a_182_);
v___x_192_ = v_reuseFailAlloc_194_;
goto v_reusejp_191_;
}
v_reusejp_191_:
{
v_a_181_ = v_tail_185_;
v_a_182_ = v___x_192_;
goto _start;
}
}
else
{
lean_del_object(v___x_187_);
lean_dec(v_head_184_);
v_a_181_ = v_tail_185_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedRoots(lean_object* v_order_197_, lean_object* v_c_198_){
_start:
{
lean_object* v___x_199_; lean_object* v___x_200_; 
v___x_199_ = lean_box(0);
lean_inc(v_order_197_);
v___x_200_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_paddedRoots_spec__0(v_order_197_, v_c_198_, v_order_197_, v___x_199_);
return v___x_200_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_inter_spec__0(lean_object* v_ys_201_, lean_object* v_a_202_, lean_object* v_a_203_){
_start:
{
if (lean_obj_tag(v_a_202_) == 0)
{
lean_object* v___x_204_; 
v___x_204_ = l_List_reverse___redArg(v_a_203_);
return v___x_204_;
}
else
{
lean_object* v_head_205_; lean_object* v_tail_206_; lean_object* v___x_208_; uint8_t v_isShared_209_; uint8_t v_isSharedCheck_216_; 
v_head_205_ = lean_ctor_get(v_a_202_, 0);
v_tail_206_ = lean_ctor_get(v_a_202_, 1);
v_isSharedCheck_216_ = !lean_is_exclusive(v_a_202_);
if (v_isSharedCheck_216_ == 0)
{
v___x_208_ = v_a_202_;
v_isShared_209_ = v_isSharedCheck_216_;
goto v_resetjp_207_;
}
else
{
lean_inc(v_tail_206_);
lean_inc(v_head_205_);
lean_dec(v_a_202_);
v___x_208_ = lean_box(0);
v_isShared_209_ = v_isSharedCheck_216_;
goto v_resetjp_207_;
}
v_resetjp_207_:
{
uint8_t v___x_210_; 
v___x_210_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_205_, v_ys_201_);
if (v___x_210_ == 0)
{
lean_del_object(v___x_208_);
lean_dec(v_head_205_);
v_a_202_ = v_tail_206_;
goto _start;
}
else
{
lean_object* v___x_213_; 
if (v_isShared_209_ == 0)
{
lean_ctor_set(v___x_208_, 1, v_a_203_);
v___x_213_ = v___x_208_;
goto v_reusejp_212_;
}
else
{
lean_object* v_reuseFailAlloc_215_; 
v_reuseFailAlloc_215_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_215_, 0, v_head_205_);
lean_ctor_set(v_reuseFailAlloc_215_, 1, v_a_203_);
v___x_213_ = v_reuseFailAlloc_215_;
goto v_reusejp_212_;
}
v_reusejp_212_:
{
v_a_202_ = v_tail_206_;
v_a_203_ = v___x_213_;
goto _start;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_inter_spec__0___boxed(lean_object* v_ys_217_, lean_object* v_a_218_, lean_object* v_a_219_){
_start:
{
lean_object* v_res_220_; 
v_res_220_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_inter_spec__0(v_ys_217_, v_a_218_, v_a_219_);
lean_dec(v_ys_217_);
return v_res_220_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_inter(lean_object* v_xs_221_, lean_object* v_ys_222_){
_start:
{
lean_object* v___x_223_; lean_object* v___x_224_; 
v___x_223_ = lean_box(0);
v___x_224_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_PaddingBridgeAudit_inter_spec__0(v_ys_222_, v_xs_221_, v___x_223_);
return v___x_224_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_inter___boxed(lean_object* v_xs_225_, lean_object* v_ys_226_){
_start:
{
lean_object* v_res_227_; 
v_res_227_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_inter(v_xs_225_, v_ys_226_);
lean_dec(v_ys_226_);
return v_res_227_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___lam__0(lean_object* v___y_228_){
_start:
{
lean_object* v___x_229_; 
v___x_229_ = lean_unsigned_to_nat(0u);
return v___x_229_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___lam__0___boxed(lean_object* v___y_230_){
_start:
{
lean_object* v_res_231_; 
v_res_231_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___lam__0(v___y_230_);
lean_dec(v___y_230_);
return v_res_231_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots(lean_object* v_order_234_){
_start:
{
lean_object* v___f_235_; lean_object* v___x_236_; lean_object* v___x_237_; lean_object* v___x_238_; lean_object* v___x_239_; 
v___f_235_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__0));
lean_inc(v_order_234_);
v___x_236_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_errors(v_order_234_, v___f_235_);
v___x_237_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__1));
v___x_238_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_errors(v_order_234_, v___x_237_);
v___x_239_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_inter(v___x_236_, v___x_238_);
lean_dec(v___x_238_);
return v___x_239_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedCommonRoots(lean_object* v_order_240_){
_start:
{
lean_object* v___f_241_; lean_object* v___x_242_; lean_object* v___x_243_; lean_object* v___x_244_; lean_object* v___x_245_; 
v___f_241_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__0));
lean_inc(v_order_240_);
v___x_242_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedRoots(v_order_240_, v___f_241_);
v___x_243_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__1));
v___x_244_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedRoots(v_order_240_, v___x_243_);
v___x_245_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_inter(v___x_242_, v___x_244_);
lean_dec(v___x_244_);
return v___x_245_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualPairIndex(lean_object* v_order_246_){
_start:
{
lean_object* v___f_247_; lean_object* v___x_248_; lean_object* v___x_249_; lean_object* v___x_250_; lean_object* v___x_251_; lean_object* v___x_252_; 
v___f_247_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__0));
lean_inc(v_order_246_);
v___x_248_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_errors(v_order_246_, v___f_247_);
v___x_249_ = l_List_lengthTR___redArg(v___x_248_);
lean_dec(v___x_248_);
v___x_250_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots(v_order_246_);
v___x_251_ = l_List_lengthTR___redArg(v___x_250_);
lean_dec(v___x_250_);
v___x_252_ = lean_nat_sub(v___x_249_, v___x_251_);
lean_dec(v___x_251_);
lean_dec(v___x_249_);
return v___x_252_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedPairIndex(lean_object* v_order_253_){
_start:
{
lean_object* v___f_254_; lean_object* v___x_255_; lean_object* v___x_256_; lean_object* v___x_257_; lean_object* v___x_258_; lean_object* v___x_259_; 
v___f_254_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__0));
lean_inc(v_order_253_);
v___x_255_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedRoots(v_order_253_, v___f_254_);
v___x_256_ = l_List_lengthTR___redArg(v___x_255_);
lean_dec(v___x_255_);
v___x_257_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_paddedCommonRoots(v_order_253_);
v___x_258_ = l_List_lengthTR___redArg(v___x_257_);
lean_dec(v___x_257_);
v___x_259_ = lean_nat_sub(v___x_256_, v___x_258_);
lean_dec(v___x_258_);
lean_dec(v___x_256_);
return v___x_259_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__1(lean_object* v_order_260_, lean_object* v_x_261_){
_start:
{
if (lean_obj_tag(v_x_261_) == 0)
{
uint8_t v___x_262_; 
lean_dec(v_order_260_);
v___x_262_ = 1;
return v___x_262_;
}
else
{
lean_object* v_head_263_; lean_object* v_tail_264_; lean_object* v___f_265_; lean_object* v___x_266_; uint8_t v___x_267_; 
v_head_263_ = lean_ctor_get(v_x_261_, 0);
v_tail_264_ = lean_ctor_get(v_x_261_, 1);
v___f_265_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__0));
lean_inc(v_order_260_);
v___x_266_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_errors(v_order_260_, v___f_265_);
v___x_267_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_263_, v___x_266_);
lean_dec(v___x_266_);
if (v___x_267_ == 0)
{
lean_dec(v_order_260_);
return v___x_267_;
}
else
{
v_x_261_ = v_tail_264_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__1___boxed(lean_object* v_order_269_, lean_object* v_x_270_){
_start:
{
uint8_t v_res_271_; lean_object* v_r_272_; 
v_res_271_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__1(v_order_269_, v_x_270_);
lean_dec(v_x_270_);
v_r_272_ = lean_box(v_res_271_);
return v_r_272_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__0(lean_object* v_order_273_, lean_object* v_x_274_){
_start:
{
if (lean_obj_tag(v_x_274_) == 0)
{
uint8_t v___x_275_; 
lean_dec(v_order_273_);
v___x_275_ = 1;
return v___x_275_;
}
else
{
lean_object* v_head_276_; lean_object* v_tail_277_; lean_object* v___x_278_; lean_object* v___x_279_; uint8_t v___x_280_; 
v_head_276_ = lean_ctor_get(v_x_274_, 0);
v_tail_277_ = lean_ctor_get(v_x_274_, 1);
v___x_278_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__1));
lean_inc(v_order_273_);
v___x_279_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_errors(v_order_273_, v___x_278_);
v___x_280_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_276_, v___x_279_);
lean_dec(v___x_279_);
if (v___x_280_ == 0)
{
lean_dec(v_order_273_);
return v___x_280_;
}
else
{
v_x_274_ = v_tail_277_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__0___boxed(lean_object* v_order_282_, lean_object* v_x_283_){
_start:
{
uint8_t v_res_284_; lean_object* v_r_285_; 
v_res_284_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__0(v_order_282_, v_x_283_);
lean_dec(v_x_283_);
v_r_285_ = lean_box(v_res_284_);
return v_r_285_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable(lean_object* v_order_286_){
_start:
{
lean_object* v___f_287_; lean_object* v___x_288_; uint8_t v___x_289_; 
v___f_287_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__0));
lean_inc_n(v_order_286_, 2);
v___x_288_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_padding(v_order_286_, v___f_287_);
v___x_289_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__0(v_order_286_, v___x_288_);
lean_dec(v___x_288_);
if (v___x_289_ == 0)
{
lean_dec(v_order_286_);
return v___x_289_;
}
else
{
lean_object* v___x_290_; lean_object* v___x_291_; uint8_t v___x_292_; 
v___x_290_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_actualCommonRoots___closed__1));
lean_inc(v_order_286_);
v___x_291_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_padding(v_order_286_, v___x_290_);
v___x_292_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable_spec__1(v_order_286_, v___x_291_);
lean_dec(v___x_291_);
return v___x_292_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable___boxed(lean_object* v_order_293_){
_start:
{
uint8_t v_res_294_; lean_object* v_r_295_; 
v_res_294_ = lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_minimalPairTransportable(v_order_293_);
v_r_295_ = lean_box(v_res_294_);
return v_r_295_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31Radius(void){
_start:
{
lean_object* v___x_296_; 
v___x_296_ = lean_unsigned_to_nat(981129u);
return v___x_296_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstIndexCap(void){
_start:
{
lean_object* v___x_297_; 
v___x_297_ = lean_unsigned_to_nat(20765u);
return v___x_297_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeIndexCap(void){
_start:
{
lean_object* v___x_298_; 
v___x_298_ = lean_unsigned_to_nat(62295u);
return v___x_298_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstBlockedWeightMax(void){
_start:
{
lean_object* v___x_299_; 
v___x_299_ = lean_unsigned_to_nat(960363u);
return v___x_299_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeBlockedWeightMax(void){
_start:
{
lean_object* v___x_300_; 
v___x_300_ = lean_unsigned_to_nat(918833u);
return v___x_300_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Std(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit(uint8_t builtin) {
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
lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_prime = _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_prime();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_prime);
lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder = _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_naturalOrder);
lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_agreementThreshold = _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_agreementThreshold();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_agreementThreshold);
lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_radius = _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_radius();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_radius);
lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31Radius = _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31Radius();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31Radius);
lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstIndexCap = _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstIndexCap();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstIndexCap);
lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeIndexCap = _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeIndexCap();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeIndexCap);
lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstBlockedWeightMax = _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstBlockedWeightMax();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31FirstBlockedWeightMax);
lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeBlockedWeightMax = _init_lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeBlockedWeightMax();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit_m31ThreeBlockedWeightMax);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
