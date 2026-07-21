// Lean compiler output
// Module: M31QRootedShell.ToyCounterexample
// Imports: public import Init public meta import Init public import M31QRootedShell.Envelope
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
lean_object* l_List_lengthTR___redArg(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* l_List_range(lean_object*);
lean_object* lean_nat_mul(lean_object*, lean_object*);
lean_object* lean_nat_add(lean_object*, lean_object*);
lean_object* lean_nat_mod(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices___closed__0;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partner(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partner___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2___boxed(lean_object*);
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(14) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__0 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__0_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__1 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__1_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__1_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__2 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__2_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__2_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__3 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__3_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__3_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__4 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__4_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__4_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__5 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__5_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__5_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__6 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__6_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__6_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__7 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__7_value;
LEAN_EXPORT const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__7_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__0 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__0_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__1 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__1_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__1_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__2 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__2_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(10) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__2_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__3 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__3_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__3_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__4 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__4_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__4_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__5 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__5_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__5_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__6 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__6_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__6_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__7 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__7_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__3_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__8 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__8_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__8_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__9 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__9_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__9_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__10 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__10_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__10_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__11 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__11_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__12 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__12_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(10) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__12_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__13 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__13_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__14_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__13_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__14 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__14_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__15_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__14_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__15 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__15_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__16_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__15_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__16 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__16_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__17_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__16_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__17 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__17_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__18_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__17_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__18 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__18_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__19_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__19 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__19_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__20_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__19_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__20 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__20_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__21_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(10) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__20_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__21 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__21_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__22_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__21_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__22 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__22_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__23_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__22_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__23 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__23_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__24_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__23_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__24 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__24_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__25_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__24_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__25 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__25_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__26_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__26 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__26_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__27_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__26_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__27 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__27_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__28_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(10) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__27_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__28 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__28_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__29_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__28_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__29 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__29_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__30_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__29_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__30 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__30_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__31_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__30_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__31 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__31_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__32_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__31_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__32 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__32_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__33_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__8_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__33 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__33_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__34_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__33_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__34 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__34_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__35_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__34_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__35 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__35_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__36_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__35_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__36 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__36_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__37_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__32_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__36_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__37 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__37_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__38_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__25_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__37_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__38 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__38_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__39_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__18_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__38_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__39 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__39_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__40_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__11_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__39_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__40 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__40_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__41_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__7_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__40_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__41 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__41_value;
LEAN_EXPORT const lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors___closed__41_value;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_sumNat(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_sumNat___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_ToyCounterexample_prefix1_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_prefix1(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_interCard_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_interCard_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_interCard(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_interCard___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_exchangeDistance(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_exchangeDistance___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_negationClosed_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_negationClosed_spec__0___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_negationClosed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_negationClosed___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonCore_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonCore_spec__0___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_commonCore_spec__1(lean_object*, lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore___closed__0;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore;
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_rootedDegree_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_rootedDegree_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_rootedDegree(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_rootedDegree___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_ambientShell7;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_noDuplicates(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_noDuplicates___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_supportShapeCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_supportShapeCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__0;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__1;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__2_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__2;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__3_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__3;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck;
static lean_once_cell_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_distanceSevenCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_distanceSevenCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck;
static lean_once_cell_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_partnerNegationCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_partnerNegationCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__0___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__1(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__1___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck;
static lean_once_cell_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__0;
static lean_once_cell_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__1;
static lean_once_cell_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__2_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__2;
static lean_once_cell_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__3_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__3;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck;
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices___closed__0(void){
_start:
{
lean_object* v___x_1_; lean_object* v___x_2_; 
v___x_1_ = lean_unsigned_to_nat(16u);
v___x_2_ = l_List_range(v___x_1_);
return v___x_2_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices(void){
_start:
{
lean_object* v___x_3_; 
v___x_3_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices___closed__0, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices___closed__0);
return v___x_3_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(lean_object* v_x_4_){
_start:
{
lean_object* v___x_5_; uint8_t v___x_6_; 
v___x_5_ = lean_unsigned_to_nat(0u);
v___x_6_ = lean_nat_dec_eq(v_x_4_, v___x_5_);
if (v___x_6_ == 0)
{
lean_object* v___x_7_; uint8_t v___x_8_; 
v___x_7_ = lean_unsigned_to_nat(1u);
v___x_8_ = lean_nat_dec_eq(v_x_4_, v___x_7_);
if (v___x_8_ == 0)
{
lean_object* v___x_9_; uint8_t v___x_10_; 
v___x_9_ = lean_unsigned_to_nat(2u);
v___x_10_ = lean_nat_dec_eq(v_x_4_, v___x_9_);
if (v___x_10_ == 0)
{
lean_object* v___x_11_; uint8_t v___x_12_; 
v___x_11_ = lean_unsigned_to_nat(3u);
v___x_12_ = lean_nat_dec_eq(v_x_4_, v___x_11_);
if (v___x_12_ == 0)
{
lean_object* v___x_13_; uint8_t v___x_14_; 
v___x_13_ = lean_unsigned_to_nat(4u);
v___x_14_ = lean_nat_dec_eq(v_x_4_, v___x_13_);
if (v___x_14_ == 0)
{
lean_object* v___x_15_; uint8_t v___x_16_; 
v___x_15_ = lean_unsigned_to_nat(5u);
v___x_16_ = lean_nat_dec_eq(v_x_4_, v___x_15_);
if (v___x_16_ == 0)
{
lean_object* v___x_17_; uint8_t v___x_18_; 
v___x_17_ = lean_unsigned_to_nat(6u);
v___x_18_ = lean_nat_dec_eq(v_x_4_, v___x_17_);
if (v___x_18_ == 0)
{
lean_object* v___x_19_; uint8_t v___x_20_; 
v___x_19_ = lean_unsigned_to_nat(7u);
v___x_20_ = lean_nat_dec_eq(v_x_4_, v___x_19_);
if (v___x_20_ == 0)
{
lean_object* v___x_21_; uint8_t v___x_22_; 
v___x_21_ = lean_unsigned_to_nat(8u);
v___x_22_ = lean_nat_dec_eq(v_x_4_, v___x_21_);
if (v___x_22_ == 0)
{
lean_object* v___x_23_; uint8_t v___x_24_; 
v___x_23_ = lean_unsigned_to_nat(9u);
v___x_24_ = lean_nat_dec_eq(v_x_4_, v___x_23_);
if (v___x_24_ == 0)
{
lean_object* v___x_25_; uint8_t v___x_26_; 
v___x_25_ = lean_unsigned_to_nat(10u);
v___x_26_ = lean_nat_dec_eq(v_x_4_, v___x_25_);
if (v___x_26_ == 0)
{
lean_object* v___x_27_; uint8_t v___x_28_; 
v___x_27_ = lean_unsigned_to_nat(11u);
v___x_28_ = lean_nat_dec_eq(v_x_4_, v___x_27_);
if (v___x_28_ == 0)
{
lean_object* v___x_29_; uint8_t v___x_30_; 
v___x_29_ = lean_unsigned_to_nat(12u);
v___x_30_ = lean_nat_dec_eq(v_x_4_, v___x_29_);
if (v___x_30_ == 0)
{
lean_object* v___x_31_; uint8_t v___x_32_; 
v___x_31_ = lean_unsigned_to_nat(13u);
v___x_32_ = lean_nat_dec_eq(v_x_4_, v___x_31_);
if (v___x_32_ == 0)
{
lean_object* v___x_33_; uint8_t v___x_34_; 
v___x_33_ = lean_unsigned_to_nat(14u);
v___x_34_ = lean_nat_dec_eq(v_x_4_, v___x_33_);
if (v___x_34_ == 0)
{
lean_object* v___x_35_; uint8_t v___x_36_; 
v___x_35_ = lean_unsigned_to_nat(15u);
v___x_36_ = lean_nat_dec_eq(v_x_4_, v___x_35_);
if (v___x_36_ == 0)
{
return v___x_5_;
}
else
{
lean_object* v___x_37_; 
v___x_37_ = lean_unsigned_to_nat(74u);
return v___x_37_;
}
}
else
{
lean_object* v___x_38_; 
v___x_38_ = lean_unsigned_to_nat(118u);
return v___x_38_;
}
}
else
{
return v___x_9_;
}
}
else
{
lean_object* v___x_39_; 
v___x_39_ = lean_unsigned_to_nat(105u);
return v___x_39_;
}
}
else
{
lean_object* v___x_40_; 
v___x_40_ = lean_unsigned_to_nat(85u);
return v___x_40_;
}
}
else
{
lean_object* v___x_41_; 
v___x_41_ = lean_unsigned_to_nat(38u);
return v___x_41_;
}
}
else
{
lean_object* v___x_42_; 
v___x_42_ = lean_unsigned_to_nat(88u);
return v___x_42_;
}
}
else
{
lean_object* v___x_43_; 
v___x_43_ = lean_unsigned_to_nat(122u);
return v___x_43_;
}
}
else
{
lean_object* v___x_44_; 
v___x_44_ = lean_unsigned_to_nat(53u);
return v___x_44_;
}
}
else
{
lean_object* v___x_45_; 
v___x_45_ = lean_unsigned_to_nat(9u);
return v___x_45_;
}
}
else
{
lean_object* v___x_46_; 
v___x_46_ = lean_unsigned_to_nat(125u);
return v___x_46_;
}
}
else
{
lean_object* v___x_47_; 
v___x_47_ = lean_unsigned_to_nat(22u);
return v___x_47_;
}
}
else
{
lean_object* v___x_48_; 
v___x_48_ = lean_unsigned_to_nat(42u);
return v___x_48_;
}
}
else
{
lean_object* v___x_49_; 
v___x_49_ = lean_unsigned_to_nat(89u);
return v___x_49_;
}
}
else
{
lean_object* v___x_50_; 
v___x_50_ = lean_unsigned_to_nat(39u);
return v___x_50_;
}
}
else
{
lean_object* v___x_51_; 
v___x_51_ = lean_unsigned_to_nat(5u);
return v___x_51_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain___boxed(lean_object* v_x_52_){
_start:
{
lean_object* v_res_53_; 
v_res_53_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(v_x_52_);
lean_dec(v_x_52_);
return v_res_53_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partner(lean_object* v_x_54_){
_start:
{
lean_object* v___x_55_; uint8_t v___x_56_; 
v___x_55_ = lean_unsigned_to_nat(0u);
v___x_56_ = lean_nat_dec_eq(v_x_54_, v___x_55_);
if (v___x_56_ == 0)
{
lean_object* v___x_57_; uint8_t v___x_58_; 
v___x_57_ = lean_unsigned_to_nat(1u);
v___x_58_ = lean_nat_dec_eq(v_x_54_, v___x_57_);
if (v___x_58_ == 0)
{
lean_object* v___x_59_; uint8_t v___x_60_; 
v___x_59_ = lean_unsigned_to_nat(2u);
v___x_60_ = lean_nat_dec_eq(v_x_54_, v___x_59_);
if (v___x_60_ == 0)
{
lean_object* v___x_61_; uint8_t v___x_62_; 
v___x_61_ = lean_unsigned_to_nat(3u);
v___x_62_ = lean_nat_dec_eq(v_x_54_, v___x_61_);
if (v___x_62_ == 0)
{
lean_object* v___x_63_; uint8_t v___x_64_; 
v___x_63_ = lean_unsigned_to_nat(4u);
v___x_64_ = lean_nat_dec_eq(v_x_54_, v___x_63_);
if (v___x_64_ == 0)
{
lean_object* v___x_65_; uint8_t v___x_66_; 
v___x_65_ = lean_unsigned_to_nat(5u);
v___x_66_ = lean_nat_dec_eq(v_x_54_, v___x_65_);
if (v___x_66_ == 0)
{
lean_object* v___x_67_; uint8_t v___x_68_; 
v___x_67_ = lean_unsigned_to_nat(6u);
v___x_68_ = lean_nat_dec_eq(v_x_54_, v___x_67_);
if (v___x_68_ == 0)
{
lean_object* v___x_69_; uint8_t v___x_70_; 
v___x_69_ = lean_unsigned_to_nat(7u);
v___x_70_ = lean_nat_dec_eq(v_x_54_, v___x_69_);
if (v___x_70_ == 0)
{
lean_object* v___x_71_; uint8_t v___x_72_; 
v___x_71_ = lean_unsigned_to_nat(8u);
v___x_72_ = lean_nat_dec_eq(v_x_54_, v___x_71_);
if (v___x_72_ == 0)
{
lean_object* v___x_73_; uint8_t v___x_74_; 
v___x_73_ = lean_unsigned_to_nat(9u);
v___x_74_ = lean_nat_dec_eq(v_x_54_, v___x_73_);
if (v___x_74_ == 0)
{
lean_object* v___x_75_; uint8_t v___x_76_; 
v___x_75_ = lean_unsigned_to_nat(10u);
v___x_76_ = lean_nat_dec_eq(v_x_54_, v___x_75_);
if (v___x_76_ == 0)
{
lean_object* v___x_77_; uint8_t v___x_78_; 
v___x_77_ = lean_unsigned_to_nat(11u);
v___x_78_ = lean_nat_dec_eq(v_x_54_, v___x_77_);
if (v___x_78_ == 0)
{
lean_object* v___x_79_; uint8_t v___x_80_; 
v___x_79_ = lean_unsigned_to_nat(12u);
v___x_80_ = lean_nat_dec_eq(v_x_54_, v___x_79_);
if (v___x_80_ == 0)
{
lean_object* v___x_81_; uint8_t v___x_82_; 
v___x_81_ = lean_unsigned_to_nat(13u);
v___x_82_ = lean_nat_dec_eq(v_x_54_, v___x_81_);
if (v___x_82_ == 0)
{
lean_object* v___x_83_; uint8_t v___x_84_; 
v___x_83_ = lean_unsigned_to_nat(14u);
v___x_84_ = lean_nat_dec_eq(v_x_54_, v___x_83_);
if (v___x_84_ == 0)
{
lean_object* v___x_85_; uint8_t v___x_86_; 
v___x_85_ = lean_unsigned_to_nat(15u);
v___x_86_ = lean_nat_dec_eq(v_x_54_, v___x_85_);
if (v___x_86_ == 0)
{
return v___x_55_;
}
else
{
return v___x_69_;
}
}
else
{
return v___x_67_;
}
}
else
{
return v___x_65_;
}
}
else
{
return v___x_63_;
}
}
else
{
return v___x_61_;
}
}
else
{
return v___x_59_;
}
}
else
{
return v___x_57_;
}
}
else
{
return v___x_55_;
}
}
else
{
lean_object* v___x_87_; 
v___x_87_ = lean_unsigned_to_nat(15u);
return v___x_87_;
}
}
else
{
lean_object* v___x_88_; 
v___x_88_ = lean_unsigned_to_nat(14u);
return v___x_88_;
}
}
else
{
lean_object* v___x_89_; 
v___x_89_ = lean_unsigned_to_nat(13u);
return v___x_89_;
}
}
else
{
lean_object* v___x_90_; 
v___x_90_ = lean_unsigned_to_nat(12u);
return v___x_90_;
}
}
else
{
lean_object* v___x_91_; 
v___x_91_ = lean_unsigned_to_nat(11u);
return v___x_91_;
}
}
else
{
lean_object* v___x_92_; 
v___x_92_ = lean_unsigned_to_nat(10u);
return v___x_92_;
}
}
else
{
lean_object* v___x_93_; 
v___x_93_ = lean_unsigned_to_nat(9u);
return v___x_93_;
}
}
else
{
lean_object* v___x_94_; 
v___x_94_ = lean_unsigned_to_nat(8u);
return v___x_94_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partner___boxed(lean_object* v_x_95_){
_start:
{
lean_object* v_res_96_; 
v_res_96_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partner(v_x_95_);
lean_dec(v_x_95_);
return v_res_96_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2(lean_object* v_x_97_){
_start:
{
lean_object* v___x_98_; lean_object* v___x_99_; lean_object* v___x_100_; lean_object* v___x_101_; lean_object* v___x_102_; lean_object* v___x_103_; lean_object* v___x_104_; 
v___x_98_ = lean_unsigned_to_nat(2u);
v___x_99_ = lean_nat_mul(v___x_98_, v_x_97_);
v___x_100_ = lean_nat_mul(v___x_99_, v_x_97_);
lean_dec(v___x_99_);
v___x_101_ = lean_unsigned_to_nat(126u);
v___x_102_ = lean_nat_add(v___x_100_, v___x_101_);
lean_dec(v___x_100_);
v___x_103_ = lean_unsigned_to_nat(127u);
v___x_104_ = lean_nat_mod(v___x_102_, v___x_103_);
lean_dec(v___x_102_);
return v___x_104_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2___boxed(lean_object* v_x_105_){
_start:
{
lean_object* v_res_106_; 
v_res_106_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2(v_x_105_);
lean_dec(v_x_105_);
return v_res_106_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_sumNat(lean_object* v_x_259_){
_start:
{
if (lean_obj_tag(v_x_259_) == 0)
{
lean_object* v___x_260_; 
v___x_260_ = lean_unsigned_to_nat(0u);
return v___x_260_;
}
else
{
lean_object* v_head_261_; lean_object* v_tail_262_; lean_object* v___x_263_; lean_object* v___x_264_; 
v_head_261_ = lean_ctor_get(v_x_259_, 0);
v_tail_262_ = lean_ctor_get(v_x_259_, 1);
v___x_263_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_sumNat(v_tail_262_);
v___x_264_ = lean_nat_add(v_head_261_, v___x_263_);
lean_dec(v___x_263_);
return v___x_264_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_sumNat___boxed(lean_object* v_x_265_){
_start:
{
lean_object* v_res_266_; 
v_res_266_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_sumNat(v_x_265_);
lean_dec(v_x_265_);
return v_res_266_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_ToyCounterexample_prefix1_spec__0(lean_object* v_a_267_, lean_object* v_a_268_){
_start:
{
if (lean_obj_tag(v_a_267_) == 0)
{
lean_object* v___x_269_; 
v___x_269_ = l_List_reverse___redArg(v_a_268_);
return v___x_269_;
}
else
{
lean_object* v_head_270_; lean_object* v_tail_271_; lean_object* v___x_273_; uint8_t v_isShared_274_; uint8_t v_isSharedCheck_280_; 
v_head_270_ = lean_ctor_get(v_a_267_, 0);
v_tail_271_ = lean_ctor_get(v_a_267_, 1);
v_isSharedCheck_280_ = !lean_is_exclusive(v_a_267_);
if (v_isSharedCheck_280_ == 0)
{
v___x_273_ = v_a_267_;
v_isShared_274_ = v_isSharedCheck_280_;
goto v_resetjp_272_;
}
else
{
lean_inc(v_tail_271_);
lean_inc(v_head_270_);
lean_dec(v_a_267_);
v___x_273_ = lean_box(0);
v_isShared_274_ = v_isSharedCheck_280_;
goto v_resetjp_272_;
}
v_resetjp_272_:
{
lean_object* v___x_275_; lean_object* v___x_277_; 
v___x_275_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(v_head_270_);
lean_dec(v_head_270_);
if (v_isShared_274_ == 0)
{
lean_ctor_set(v___x_273_, 1, v_a_268_);
lean_ctor_set(v___x_273_, 0, v___x_275_);
v___x_277_ = v___x_273_;
goto v_reusejp_276_;
}
else
{
lean_object* v_reuseFailAlloc_279_; 
v_reuseFailAlloc_279_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_279_, 0, v___x_275_);
lean_ctor_set(v_reuseFailAlloc_279_, 1, v_a_268_);
v___x_277_ = v_reuseFailAlloc_279_;
goto v_reusejp_276_;
}
v_reusejp_276_:
{
v_a_267_ = v_tail_271_;
v_a_268_ = v___x_277_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_prefix1(lean_object* v_S_281_){
_start:
{
lean_object* v___x_282_; lean_object* v___x_283_; lean_object* v___x_284_; lean_object* v___x_285_; lean_object* v___x_286_; 
v___x_282_ = lean_box(0);
v___x_283_ = lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_ToyCounterexample_prefix1_spec__0(v_S_281_, v___x_282_);
v___x_284_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_sumNat(v___x_283_);
lean_dec(v___x_283_);
v___x_285_ = lean_unsigned_to_nat(127u);
v___x_286_ = lean_nat_mod(v___x_284_, v___x_285_);
lean_dec(v___x_284_);
return v___x_286_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_interCard_spec__0(lean_object* v_B_287_, lean_object* v_a_288_, lean_object* v_a_289_){
_start:
{
if (lean_obj_tag(v_a_288_) == 0)
{
lean_object* v___x_290_; 
v___x_290_ = l_List_reverse___redArg(v_a_289_);
return v___x_290_;
}
else
{
lean_object* v_head_291_; lean_object* v_tail_292_; lean_object* v___x_294_; uint8_t v_isShared_295_; uint8_t v_isSharedCheck_302_; 
v_head_291_ = lean_ctor_get(v_a_288_, 0);
v_tail_292_ = lean_ctor_get(v_a_288_, 1);
v_isSharedCheck_302_ = !lean_is_exclusive(v_a_288_);
if (v_isSharedCheck_302_ == 0)
{
v___x_294_ = v_a_288_;
v_isShared_295_ = v_isSharedCheck_302_;
goto v_resetjp_293_;
}
else
{
lean_inc(v_tail_292_);
lean_inc(v_head_291_);
lean_dec(v_a_288_);
v___x_294_ = lean_box(0);
v_isShared_295_ = v_isSharedCheck_302_;
goto v_resetjp_293_;
}
v_resetjp_293_:
{
uint8_t v___x_296_; 
v___x_296_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_291_, v_B_287_);
if (v___x_296_ == 0)
{
lean_del_object(v___x_294_);
lean_dec(v_head_291_);
v_a_288_ = v_tail_292_;
goto _start;
}
else
{
lean_object* v___x_299_; 
if (v_isShared_295_ == 0)
{
lean_ctor_set(v___x_294_, 1, v_a_289_);
v___x_299_ = v___x_294_;
goto v_reusejp_298_;
}
else
{
lean_object* v_reuseFailAlloc_301_; 
v_reuseFailAlloc_301_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_301_, 0, v_head_291_);
lean_ctor_set(v_reuseFailAlloc_301_, 1, v_a_289_);
v___x_299_ = v_reuseFailAlloc_301_;
goto v_reusejp_298_;
}
v_reusejp_298_:
{
v_a_288_ = v_tail_292_;
v_a_289_ = v___x_299_;
goto _start;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_interCard_spec__0___boxed(lean_object* v_B_303_, lean_object* v_a_304_, lean_object* v_a_305_){
_start:
{
lean_object* v_res_306_; 
v_res_306_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_interCard_spec__0(v_B_303_, v_a_304_, v_a_305_);
lean_dec(v_B_303_);
return v_res_306_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_interCard(lean_object* v_A_307_, lean_object* v_B_308_){
_start:
{
lean_object* v___x_309_; lean_object* v___x_310_; lean_object* v___x_311_; 
v___x_309_ = lean_box(0);
v___x_310_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_interCard_spec__0(v_B_308_, v_A_307_, v___x_309_);
v___x_311_ = l_List_lengthTR___redArg(v___x_310_);
lean_dec(v___x_310_);
return v___x_311_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_interCard___boxed(lean_object* v_A_312_, lean_object* v_B_313_){
_start:
{
lean_object* v_res_314_; 
v_res_314_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_interCard(v_A_312_, v_B_313_);
lean_dec(v_B_313_);
return v_res_314_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_exchangeDistance(lean_object* v_A_315_, lean_object* v_B_316_){
_start:
{
lean_object* v___x_317_; lean_object* v___x_318_; lean_object* v___x_319_; 
v___x_317_ = l_List_lengthTR___redArg(v_A_315_);
v___x_318_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_interCard(v_A_315_, v_B_316_);
v___x_319_ = lean_nat_sub(v___x_317_, v___x_318_);
lean_dec(v___x_318_);
lean_dec(v___x_317_);
return v___x_319_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_exchangeDistance___boxed(lean_object* v_A_320_, lean_object* v_B_321_){
_start:
{
lean_object* v_res_322_; 
v_res_322_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_exchangeDistance(v_A_320_, v_B_321_);
lean_dec(v_B_321_);
return v_res_322_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_negationClosed_spec__0(lean_object* v_S_323_, lean_object* v_x_324_){
_start:
{
if (lean_obj_tag(v_x_324_) == 0)
{
uint8_t v___x_325_; 
v___x_325_ = 1;
return v___x_325_;
}
else
{
lean_object* v_head_326_; lean_object* v_tail_327_; lean_object* v___x_328_; uint8_t v___x_329_; 
v_head_326_ = lean_ctor_get(v_x_324_, 0);
v_tail_327_ = lean_ctor_get(v_x_324_, 1);
v___x_328_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partner(v_head_326_);
v___x_329_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v___x_328_, v_S_323_);
lean_dec(v___x_328_);
if (v___x_329_ == 0)
{
return v___x_329_;
}
else
{
v_x_324_ = v_tail_327_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_negationClosed_spec__0___boxed(lean_object* v_S_331_, lean_object* v_x_332_){
_start:
{
uint8_t v_res_333_; lean_object* v_r_334_; 
v_res_333_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_negationClosed_spec__0(v_S_331_, v_x_332_);
lean_dec(v_x_332_);
lean_dec(v_S_331_);
v_r_334_ = lean_box(v_res_333_);
return v_r_334_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_negationClosed(lean_object* v_S_335_){
_start:
{
uint8_t v___x_336_; 
v___x_336_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_negationClosed_spec__0(v_S_335_, v_S_335_);
return v___x_336_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_negationClosed___boxed(lean_object* v_S_337_){
_start:
{
uint8_t v_res_338_; lean_object* v_r_339_; 
v_res_338_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_negationClosed(v_S_337_);
lean_dec(v_S_337_);
v_r_339_ = lean_box(v_res_338_);
return v_r_339_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonCore_spec__0(lean_object* v_x_340_, lean_object* v_x_341_){
_start:
{
if (lean_obj_tag(v_x_341_) == 0)
{
uint8_t v___x_342_; 
v___x_342_ = 1;
return v___x_342_;
}
else
{
lean_object* v_head_343_; lean_object* v_tail_344_; uint8_t v___x_345_; 
v_head_343_ = lean_ctor_get(v_x_341_, 0);
v_tail_344_ = lean_ctor_get(v_x_341_, 1);
v___x_345_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_x_340_, v_head_343_);
if (v___x_345_ == 0)
{
return v___x_345_;
}
else
{
v_x_341_ = v_tail_344_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonCore_spec__0___boxed(lean_object* v_x_347_, lean_object* v_x_348_){
_start:
{
uint8_t v_res_349_; lean_object* v_r_350_; 
v_res_349_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonCore_spec__0(v_x_347_, v_x_348_);
lean_dec(v_x_348_);
lean_dec(v_x_347_);
v_r_350_ = lean_box(v_res_349_);
return v_r_350_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_commonCore_spec__1(lean_object* v_a_351_, lean_object* v_a_352_){
_start:
{
if (lean_obj_tag(v_a_351_) == 0)
{
lean_object* v___x_353_; 
v___x_353_ = l_List_reverse___redArg(v_a_352_);
return v___x_353_;
}
else
{
lean_object* v_head_354_; lean_object* v_tail_355_; lean_object* v___x_357_; uint8_t v_isShared_358_; uint8_t v_isSharedCheck_366_; 
v_head_354_ = lean_ctor_get(v_a_351_, 0);
v_tail_355_ = lean_ctor_get(v_a_351_, 1);
v_isSharedCheck_366_ = !lean_is_exclusive(v_a_351_);
if (v_isSharedCheck_366_ == 0)
{
v___x_357_ = v_a_351_;
v_isShared_358_ = v_isSharedCheck_366_;
goto v_resetjp_356_;
}
else
{
lean_inc(v_tail_355_);
lean_inc(v_head_354_);
lean_dec(v_a_351_);
v___x_357_ = lean_box(0);
v_isShared_358_ = v_isSharedCheck_366_;
goto v_resetjp_356_;
}
v_resetjp_356_:
{
lean_object* v___x_359_; uint8_t v___x_360_; 
v___x_359_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors));
v___x_360_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonCore_spec__0(v_head_354_, v___x_359_);
if (v___x_360_ == 0)
{
lean_del_object(v___x_357_);
lean_dec(v_head_354_);
v_a_351_ = v_tail_355_;
goto _start;
}
else
{
lean_object* v___x_363_; 
if (v_isShared_358_ == 0)
{
lean_ctor_set(v___x_357_, 1, v_a_352_);
v___x_363_ = v___x_357_;
goto v_reusejp_362_;
}
else
{
lean_object* v_reuseFailAlloc_365_; 
v_reuseFailAlloc_365_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_365_, 0, v_head_354_);
lean_ctor_set(v_reuseFailAlloc_365_, 1, v_a_352_);
v___x_363_ = v_reuseFailAlloc_365_;
goto v_reusejp_362_;
}
v_reusejp_362_:
{
v_a_351_ = v_tail_355_;
v_a_352_ = v___x_363_;
goto _start;
}
}
}
}
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore___closed__0(void){
_start:
{
lean_object* v___x_367_; lean_object* v___x_368_; lean_object* v___x_369_; 
v___x_367_ = lean_box(0);
v___x_368_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor));
v___x_369_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_commonCore_spec__1(v___x_368_, v___x_367_);
return v___x_369_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore(void){
_start:
{
lean_object* v___x_370_; 
v___x_370_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore___closed__0, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore___closed__0);
return v___x_370_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_rootedDegree_spec__0(lean_object* v_e_371_, lean_object* v_a_372_, lean_object* v_a_373_){
_start:
{
if (lean_obj_tag(v_a_372_) == 0)
{
lean_object* v___x_374_; 
v___x_374_ = l_List_reverse___redArg(v_a_373_);
return v___x_374_;
}
else
{
lean_object* v_head_375_; lean_object* v_tail_376_; lean_object* v___x_378_; uint8_t v_isShared_379_; uint8_t v_isSharedCheck_388_; 
v_head_375_ = lean_ctor_get(v_a_372_, 0);
v_tail_376_ = lean_ctor_get(v_a_372_, 1);
v_isSharedCheck_388_ = !lean_is_exclusive(v_a_372_);
if (v_isSharedCheck_388_ == 0)
{
v___x_378_ = v_a_372_;
v_isShared_379_ = v_isSharedCheck_388_;
goto v_resetjp_377_;
}
else
{
lean_inc(v_tail_376_);
lean_inc(v_head_375_);
lean_dec(v_a_372_);
v___x_378_ = lean_box(0);
v_isShared_379_ = v_isSharedCheck_388_;
goto v_resetjp_377_;
}
v_resetjp_377_:
{
lean_object* v___x_380_; lean_object* v___x_381_; uint8_t v___x_382_; 
v___x_380_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor));
v___x_381_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_exchangeDistance(v___x_380_, v_head_375_);
v___x_382_ = lean_nat_dec_eq(v___x_381_, v_e_371_);
lean_dec(v___x_381_);
if (v___x_382_ == 0)
{
lean_del_object(v___x_378_);
lean_dec(v_head_375_);
v_a_372_ = v_tail_376_;
goto _start;
}
else
{
lean_object* v___x_385_; 
if (v_isShared_379_ == 0)
{
lean_ctor_set(v___x_378_, 1, v_a_373_);
v___x_385_ = v___x_378_;
goto v_reusejp_384_;
}
else
{
lean_object* v_reuseFailAlloc_387_; 
v_reuseFailAlloc_387_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_387_, 0, v_head_375_);
lean_ctor_set(v_reuseFailAlloc_387_, 1, v_a_373_);
v___x_385_ = v_reuseFailAlloc_387_;
goto v_reusejp_384_;
}
v_reusejp_384_:
{
v_a_372_ = v_tail_376_;
v_a_373_ = v___x_385_;
goto _start;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_rootedDegree_spec__0___boxed(lean_object* v_e_389_, lean_object* v_a_390_, lean_object* v_a_391_){
_start:
{
lean_object* v_res_392_; 
v_res_392_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_rootedDegree_spec__0(v_e_389_, v_a_390_, v_a_391_);
lean_dec(v_e_389_);
return v_res_392_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_rootedDegree(lean_object* v_e_393_){
_start:
{
lean_object* v___x_394_; lean_object* v___x_395_; lean_object* v___x_396_; lean_object* v___x_397_; 
v___x_394_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors));
v___x_395_ = lean_box(0);
v___x_396_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_ToyCounterexample_rootedDegree_spec__0(v_e_393_, v___x_394_, v___x_395_);
v___x_397_ = l_List_lengthTR___redArg(v___x_396_);
lean_dec(v___x_396_);
return v___x_397_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_rootedDegree___boxed(lean_object* v_e_398_){
_start:
{
lean_object* v_res_399_; 
v_res_399_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_rootedDegree(v_e_398_);
lean_dec(v_e_398_);
return v_res_399_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_ambientShell7(void){
_start:
{
lean_object* v___x_400_; 
v___x_400_ = lean_unsigned_to_nat(64u);
return v___x_400_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_noDuplicates(lean_object* v_x_401_){
_start:
{
if (lean_obj_tag(v_x_401_) == 0)
{
uint8_t v___x_402_; 
v___x_402_ = 1;
return v___x_402_;
}
else
{
lean_object* v_head_403_; lean_object* v_tail_404_; uint8_t v___x_405_; 
v_head_403_ = lean_ctor_get(v_x_401_, 0);
v_tail_404_ = lean_ctor_get(v_x_401_, 1);
v___x_405_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_403_, v_tail_404_);
if (v___x_405_ == 0)
{
v_x_401_ = v_tail_404_;
goto _start;
}
else
{
uint8_t v___x_407_; 
v___x_407_ = 0;
return v___x_407_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_noDuplicates___boxed(lean_object* v_x_408_){
_start:
{
uint8_t v_res_409_; lean_object* v_r_410_; 
v_res_409_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_noDuplicates(v_x_408_);
lean_dec(v_x_408_);
v_r_410_ = lean_box(v_res_409_);
return v_r_410_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_supportShapeCheck_spec__0(lean_object* v_x_411_){
_start:
{
if (lean_obj_tag(v_x_411_) == 0)
{
uint8_t v___x_412_; 
v___x_412_ = 1;
return v___x_412_;
}
else
{
lean_object* v_head_413_; lean_object* v_tail_414_; uint8_t v___y_416_; lean_object* v___x_418_; lean_object* v___x_419_; uint8_t v___x_420_; 
v_head_413_ = lean_ctor_get(v_x_411_, 0);
v_tail_414_ = lean_ctor_get(v_x_411_, 1);
v___x_418_ = l_List_lengthTR___redArg(v_head_413_);
v___x_419_ = lean_unsigned_to_nat(8u);
v___x_420_ = lean_nat_dec_eq(v___x_418_, v___x_419_);
lean_dec(v___x_418_);
if (v___x_420_ == 0)
{
v___y_416_ = v___x_420_;
goto v___jp_415_;
}
else
{
uint8_t v___x_421_; 
v___x_421_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_noDuplicates(v_head_413_);
v___y_416_ = v___x_421_;
goto v___jp_415_;
}
v___jp_415_:
{
if (v___y_416_ == 0)
{
return v___y_416_;
}
else
{
v_x_411_ = v_tail_414_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_supportShapeCheck_spec__0___boxed(lean_object* v_x_422_){
_start:
{
uint8_t v_res_423_; lean_object* v_r_424_; 
v_res_423_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_supportShapeCheck_spec__0(v_x_422_);
lean_dec(v_x_422_);
v_r_424_ = lean_box(v_res_423_);
return v_r_424_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__0(void){
_start:
{
lean_object* v___x_425_; uint8_t v___x_426_; 
v___x_425_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors));
v___x_426_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_supportShapeCheck_spec__0(v___x_425_);
return v___x_426_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__1(void){
_start:
{
lean_object* v___x_427_; lean_object* v___x_428_; 
v___x_427_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor));
v___x_428_ = l_List_lengthTR___redArg(v___x_427_);
return v___x_428_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__2(void){
_start:
{
lean_object* v___x_429_; lean_object* v___x_430_; uint8_t v___x_431_; 
v___x_429_ = lean_unsigned_to_nat(8u);
v___x_430_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__1, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__1_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__1);
v___x_431_ = lean_nat_dec_eq(v___x_430_, v___x_429_);
return v___x_431_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__3(void){
_start:
{
lean_object* v___x_432_; uint8_t v___x_433_; 
v___x_432_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor));
v___x_433_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_noDuplicates(v___x_432_);
return v___x_433_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck(void){
_start:
{
uint8_t v___y_435_; uint8_t v___x_437_; 
v___x_437_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__2, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__2_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__2);
if (v___x_437_ == 0)
{
v___y_435_ = v___x_437_;
goto v___jp_434_;
}
else
{
uint8_t v___x_438_; 
v___x_438_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__3, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__3_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__3);
v___y_435_ = v___x_438_;
goto v___jp_434_;
}
v___jp_434_:
{
if (v___y_435_ == 0)
{
return v___y_435_;
}
else
{
uint8_t v___x_436_; 
v___x_436_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck___closed__0);
return v___x_436_;
}
}
}
}
static lean_object* _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0___closed__0(void){
_start:
{
lean_object* v___x_439_; lean_object* v___x_440_; 
v___x_439_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor));
v___x_440_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_prefix1(v___x_439_);
return v___x_440_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0(lean_object* v_x_441_){
_start:
{
if (lean_obj_tag(v_x_441_) == 0)
{
uint8_t v___x_442_; 
v___x_442_ = 1;
return v___x_442_;
}
else
{
lean_object* v_head_443_; lean_object* v_tail_444_; lean_object* v___x_445_; lean_object* v___x_446_; uint8_t v___x_447_; 
v_head_443_ = lean_ctor_get(v_x_441_, 0);
lean_inc(v_head_443_);
v_tail_444_ = lean_ctor_get(v_x_441_, 1);
lean_inc(v_tail_444_);
lean_dec_ref_known(v_x_441_, 2);
v___x_445_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_prefix1(v_head_443_);
v___x_446_ = lean_obj_once(&lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0___closed__0, &lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0___closed__0_once, _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0___closed__0);
v___x_447_ = lean_nat_dec_eq(v___x_445_, v___x_446_);
lean_dec(v___x_445_);
if (v___x_447_ == 0)
{
lean_dec(v_tail_444_);
return v___x_447_;
}
else
{
v_x_441_ = v_tail_444_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0___boxed(lean_object* v_x_449_){
_start:
{
uint8_t v_res_450_; lean_object* v_r_451_; 
v_res_450_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0(v_x_449_);
v_r_451_ = lean_box(v_res_450_);
return v_r_451_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck___closed__0(void){
_start:
{
lean_object* v___x_452_; uint8_t v___x_453_; 
v___x_452_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors));
v___x_453_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_commonPrefixCheck_spec__0(v___x_452_);
return v___x_453_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck(void){
_start:
{
uint8_t v___x_454_; 
v___x_454_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck___closed__0);
return v___x_454_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_distanceSevenCheck_spec__0(lean_object* v_x_455_){
_start:
{
if (lean_obj_tag(v_x_455_) == 0)
{
uint8_t v___x_456_; 
v___x_456_ = 1;
return v___x_456_;
}
else
{
lean_object* v_head_457_; lean_object* v_tail_458_; lean_object* v___x_459_; lean_object* v___x_460_; lean_object* v___x_461_; uint8_t v___x_462_; 
v_head_457_ = lean_ctor_get(v_x_455_, 0);
v_tail_458_ = lean_ctor_get(v_x_455_, 1);
v___x_459_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor));
v___x_460_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_exchangeDistance(v___x_459_, v_head_457_);
v___x_461_ = lean_unsigned_to_nat(7u);
v___x_462_ = lean_nat_dec_eq(v___x_460_, v___x_461_);
lean_dec(v___x_460_);
if (v___x_462_ == 0)
{
return v___x_462_;
}
else
{
v_x_455_ = v_tail_458_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_distanceSevenCheck_spec__0___boxed(lean_object* v_x_464_){
_start:
{
uint8_t v_res_465_; lean_object* v_r_466_; 
v_res_465_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_distanceSevenCheck_spec__0(v_x_464_);
lean_dec(v_x_464_);
v_r_466_ = lean_box(v_res_465_);
return v_r_466_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck___closed__0(void){
_start:
{
lean_object* v___x_467_; uint8_t v___x_468_; 
v___x_467_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors));
v___x_468_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_distanceSevenCheck_spec__0(v___x_467_);
return v___x_468_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck(void){
_start:
{
uint8_t v___x_469_; 
v___x_469_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck___closed__0);
return v___x_469_;
}
}
static uint8_t _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___closed__0(void){
_start:
{
lean_object* v___x_470_; uint8_t v___x_471_; 
v___x_470_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_anchor));
v___x_471_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_negationClosed_spec__0(v___x_470_, v___x_470_);
return v___x_471_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0(lean_object* v_x_472_){
_start:
{
if (lean_obj_tag(v_x_472_) == 0)
{
uint8_t v___x_473_; 
v___x_473_ = 1;
return v___x_473_;
}
else
{
lean_object* v_head_474_; lean_object* v_tail_475_; uint8_t v___x_476_; 
v_head_474_ = lean_ctor_get(v_x_472_, 0);
v_tail_475_ = lean_ctor_get(v_x_472_, 1);
v___x_476_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_negationClosed_spec__0(v_head_474_, v_head_474_);
if (v___x_476_ == 0)
{
v_x_472_ = v_tail_475_;
goto _start;
}
else
{
uint8_t v___x_478_; 
v___x_478_ = lean_uint8_once(&lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___closed__0, &lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___closed__0_once, _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___closed__0);
if (v___x_478_ == 0)
{
return v___x_478_;
}
else
{
v_x_472_ = v_tail_475_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___boxed(lean_object* v_x_480_){
_start:
{
uint8_t v_res_481_; lean_object* v_r_482_; 
v_res_481_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0(v_x_480_);
lean_dec(v_x_480_);
v_r_482_ = lean_box(v_res_481_);
return v_r_482_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck___closed__0(void){
_start:
{
lean_object* v___x_483_; uint8_t v___x_484_; 
v___x_483_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_neighbors));
v___x_484_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0(v___x_483_);
return v___x_484_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck(void){
_start:
{
uint8_t v___x_485_; 
v___x_485_ = lean_uint8_once(&lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___closed__0, &lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___closed__0_once, _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_quotientPruningCheck_spec__0___closed__0);
if (v___x_485_ == 0)
{
uint8_t v___x_486_; 
v___x_486_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck___closed__0);
return v___x_486_;
}
else
{
uint8_t v___x_487_; 
v___x_487_ = 0;
return v___x_487_;
}
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_partnerNegationCheck_spec__0(lean_object* v_x_488_){
_start:
{
if (lean_obj_tag(v_x_488_) == 0)
{
uint8_t v___x_489_; 
v___x_489_ = 1;
return v___x_489_;
}
else
{
lean_object* v_head_490_; lean_object* v_tail_491_; lean_object* v___x_492_; lean_object* v___x_493_; lean_object* v___x_494_; lean_object* v___x_495_; lean_object* v___x_496_; lean_object* v___x_497_; lean_object* v___x_498_; uint8_t v___x_499_; 
v_head_490_ = lean_ctor_get(v_x_488_, 0);
v_tail_491_ = lean_ctor_get(v_x_488_, 1);
v___x_492_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(v_head_490_);
v___x_493_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partner(v_head_490_);
v___x_494_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(v___x_493_);
lean_dec(v___x_493_);
v___x_495_ = lean_nat_add(v___x_492_, v___x_494_);
lean_dec(v___x_494_);
lean_dec(v___x_492_);
v___x_496_ = lean_unsigned_to_nat(127u);
v___x_497_ = lean_nat_mod(v___x_495_, v___x_496_);
lean_dec(v___x_495_);
v___x_498_ = lean_unsigned_to_nat(0u);
v___x_499_ = lean_nat_dec_eq(v___x_497_, v___x_498_);
lean_dec(v___x_497_);
if (v___x_499_ == 0)
{
return v___x_499_;
}
else
{
v_x_488_ = v_tail_491_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_partnerNegationCheck_spec__0___boxed(lean_object* v_x_501_){
_start:
{
uint8_t v_res_502_; lean_object* v_r_503_; 
v_res_502_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_partnerNegationCheck_spec__0(v_x_501_);
lean_dec(v_x_501_);
v_r_503_ = lean_box(v_res_502_);
return v_r_503_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck___closed__0(void){
_start:
{
lean_object* v___x_504_; uint8_t v___x_505_; 
v___x_504_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices;
v___x_505_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_partnerNegationCheck_spec__0(v___x_504_);
return v___x_505_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck(void){
_start:
{
uint8_t v___x_506_; 
v___x_506_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck___closed__0);
return v___x_506_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__0(lean_object* v_i_507_, lean_object* v_x_508_){
_start:
{
if (lean_obj_tag(v_x_508_) == 0)
{
uint8_t v___x_509_; 
v___x_509_ = 1;
return v___x_509_;
}
else
{
lean_object* v_head_510_; lean_object* v_tail_511_; uint8_t v___y_513_; lean_object* v___x_515_; lean_object* v___x_516_; lean_object* v___x_517_; lean_object* v___x_518_; uint8_t v___x_519_; uint8_t v___y_521_; uint8_t v___x_523_; 
v_head_510_ = lean_ctor_get(v_x_508_, 0);
v_tail_511_ = lean_ctor_get(v_x_508_, 1);
v___x_515_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(v_i_507_);
v___x_516_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2(v___x_515_);
lean_dec(v___x_515_);
v___x_517_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(v_head_510_);
v___x_518_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2(v___x_517_);
lean_dec(v___x_517_);
v___x_519_ = lean_nat_dec_eq(v___x_516_, v___x_518_);
lean_dec(v___x_518_);
lean_dec(v___x_516_);
v___x_523_ = lean_nat_dec_eq(v_head_510_, v_i_507_);
if (v___x_523_ == 0)
{
lean_object* v___x_524_; uint8_t v___x_525_; 
v___x_524_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partner(v_i_507_);
v___x_525_ = lean_nat_dec_eq(v_head_510_, v___x_524_);
lean_dec(v___x_524_);
v___y_521_ = v___x_525_;
goto v___jp_520_;
}
else
{
v___y_521_ = v___x_523_;
goto v___jp_520_;
}
v___jp_512_:
{
if (v___y_513_ == 0)
{
return v___y_513_;
}
else
{
v_x_508_ = v_tail_511_;
goto _start;
}
}
v___jp_520_:
{
if (v___x_519_ == 0)
{
if (v___y_521_ == 0)
{
v_x_508_ = v_tail_511_;
goto _start;
}
else
{
v___y_513_ = v___x_519_;
goto v___jp_512_;
}
}
else
{
v___y_513_ = v___y_521_;
goto v___jp_512_;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__0___boxed(lean_object* v_i_526_, lean_object* v_x_527_){
_start:
{
uint8_t v_res_528_; lean_object* v_r_529_; 
v_res_528_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__0(v_i_526_, v_x_527_);
lean_dec(v_x_527_);
lean_dec(v_i_526_);
v_r_529_ = lean_box(v_res_528_);
return v_r_529_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__1(lean_object* v_x_530_){
_start:
{
if (lean_obj_tag(v_x_530_) == 0)
{
uint8_t v___x_531_; 
v___x_531_ = 1;
return v___x_531_;
}
else
{
lean_object* v_head_532_; lean_object* v_tail_533_; lean_object* v___x_534_; uint8_t v___x_535_; 
v_head_532_ = lean_ctor_get(v_x_530_, 0);
v_tail_533_ = lean_ctor_get(v_x_530_, 1);
v___x_534_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices;
v___x_535_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__0(v_head_532_, v___x_534_);
if (v___x_535_ == 0)
{
return v___x_535_;
}
else
{
v_x_530_ = v_tail_533_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__1___boxed(lean_object* v_x_537_){
_start:
{
uint8_t v_res_538_; lean_object* v_r_539_; 
v_res_538_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__1(v_x_537_);
lean_dec(v_x_537_);
v_r_539_ = lean_box(v_res_538_);
return v_r_539_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck___closed__0(void){
_start:
{
lean_object* v___x_540_; uint8_t v___x_541_; 
v___x_540_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices;
v___x_541_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_ToyCounterexample_t2FiberCheck_spec__1(v___x_540_);
return v___x_541_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck(void){
_start:
{
uint8_t v___x_542_; 
v___x_542_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck___closed__0);
return v___x_542_;
}
}
static lean_object* _init_lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__0(void){
_start:
{
lean_object* v___x_543_; lean_object* v___x_544_; 
v___x_543_ = lean_unsigned_to_nat(0u);
v___x_544_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(v___x_543_);
return v___x_544_;
}
}
static lean_object* _init_lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__1(void){
_start:
{
lean_object* v___x_545_; lean_object* v___x_546_; 
v___x_545_ = lean_unsigned_to_nat(1u);
v___x_546_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(v___x_545_);
return v___x_546_;
}
}
static lean_object* _init_lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__2(void){
_start:
{
lean_object* v___x_547_; lean_object* v___x_548_; lean_object* v___x_549_; 
v___x_547_ = lean_obj_once(&lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__1, &lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__1_once, _init_lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__1);
v___x_548_ = lean_obj_once(&lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__0, &lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__0_once, _init_lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__0);
v___x_549_ = lean_nat_mul(v___x_548_, v___x_547_);
return v___x_549_;
}
}
static lean_object* _init_lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__3(void){
_start:
{
lean_object* v___x_550_; lean_object* v___x_551_; lean_object* v___x_552_; 
v___x_550_ = lean_unsigned_to_nat(127u);
v___x_551_ = lean_obj_once(&lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__2, &lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__2_once, _init_lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__2);
v___x_552_ = lean_nat_mod(v___x_551_, v___x_550_);
return v___x_552_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0(lean_object* v_x_553_){
_start:
{
if (lean_obj_tag(v_x_553_) == 0)
{
uint8_t v___x_554_; 
v___x_554_ = 0;
return v___x_554_;
}
else
{
lean_object* v_head_555_; lean_object* v_tail_556_; lean_object* v___x_557_; lean_object* v___x_558_; uint8_t v___x_559_; 
v_head_555_ = lean_ctor_get(v_x_553_, 0);
v_tail_556_ = lean_ctor_get(v_x_553_, 1);
v___x_557_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_domain(v_head_555_);
v___x_558_ = lean_obj_once(&lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__3, &lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__3_once, _init_lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___closed__3);
v___x_559_ = lean_nat_dec_eq(v___x_557_, v___x_558_);
lean_dec(v___x_557_);
if (v___x_559_ == 0)
{
v_x_553_ = v_tail_556_;
goto _start;
}
else
{
return v___x_559_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0___boxed(lean_object* v_x_561_){
_start:
{
uint8_t v_res_562_; lean_object* v_r_563_; 
v_res_562_ = lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0(v_x_561_);
lean_dec(v_x_561_);
v_r_563_ = lean_box(v_res_562_);
return v_r_563_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck___closed__0(void){
_start:
{
lean_object* v___x_564_; uint8_t v___x_565_; 
v___x_564_ = lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices;
v___x_565_ = lp_m31QRootedShell_List_any___at___00M31QRootedShell_ToyCounterexample_notProductClosedCheck_spec__0(v___x_564_);
return v___x_565_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck(void){
_start:
{
uint8_t v___x_566_; 
v___x_566_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck___closed__0);
if (v___x_566_ == 0)
{
uint8_t v___x_567_; 
v___x_567_ = 1;
return v___x_567_;
}
else
{
uint8_t v___x_568_; 
v___x_568_ = 0;
return v___x_568_;
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_m31QRootedShell_M31QRootedShell_Envelope(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_m31QRootedShell_M31QRootedShell_ToyCounterexample(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_m31QRootedShell_M31QRootedShell_Envelope(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_indices);
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonCore);
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_ambientShell7 = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_ambientShell7();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_ambientShell7);
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_supportShapeCheck();
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_commonPrefixCheck();
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_distanceSevenCheck();
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_quotientPruningCheck();
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_partnerNegationCheck();
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_t2FiberCheck();
lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck = _init_lp_m31QRootedShell_M31QRootedShell_ToyCounterexample_notProductClosedCheck();
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
