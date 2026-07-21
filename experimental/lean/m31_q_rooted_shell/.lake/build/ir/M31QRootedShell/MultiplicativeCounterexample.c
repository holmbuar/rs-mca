// Lean compiler output
// Module: M31QRootedShell.MultiplicativeCounterexample
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
lean_object* lean_nat_add(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
lean_object* lean_nat_mod(lean_object*, lean_object*);
lean_object* l_List_range(lean_object*);
uint8_t l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(lean_object*, lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_mul(lean_object*, lean_object*);
lean_object* l_List_lengthTR___redArg(lean_object*);
uint8_t lean_nat_dec_lt(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_p;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_n;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_m;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_w;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generator;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices___closed__0;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domain(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domain___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_powMod(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_powMod___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sumNat(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sumNat___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_pairSum(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_pairSum___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_prefix1_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_prefix1(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_prefix2(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicates(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicates___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_beq___at___00List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_beq___at___00List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0_spec__0___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_sameSupport_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_sameSupport_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_rotateSupport_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_rotateSupport_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotateSupport(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotateSupport___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_reflectSupport_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_reflectSupport_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectSupport(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectSupport___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotationFixes(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotationFixes___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectionFixes(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectionFixes___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__1(lean_object*, uint8_t, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__1___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__0___boxed(lean_object*, lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__1___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_interCard_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_interCard_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_interCard(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_interCard___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_exchangeDistance(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_exchangeDistance___boxed(lean_object*, lean_object*);
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(18) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__0 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__0_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__1 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__1_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__1_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__2 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__2_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__2_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__3 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__3_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__3_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__4 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__4_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__4_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__5 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__5_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__5_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__6 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__6_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__6_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__7 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__7_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__7_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__8 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__8_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__8_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__9 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__9_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(19) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__10 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__10_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(17) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__10_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__11 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__11_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__11_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__12 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__12_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__12_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__13 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__13_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__14_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__13_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__14 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__14_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__15_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__14_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__15 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__15_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__16_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__15_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__16 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__16_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__17_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__16_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__17 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__17_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__18_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__17_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__18 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__18_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__19_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__18_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__19 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__19_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__20_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(17) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__20 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__20_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__21_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(16) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__20_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__21 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__21_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__22_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__21_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__22 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__22_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__23_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__22_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__23 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__23_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__24_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(10) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__23_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__24 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__24_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__25_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__24_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__25 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__25_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__26_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__25_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__26 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__26_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__27_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__26_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__27 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__27_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__28_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__27_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__28 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__28_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__29_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__28_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__29 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__29_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__30_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(18) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__10_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__30 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__30_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__31_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__30_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__31 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__31_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__32_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__31_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__32 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__32_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__33_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__32_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__33 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__33_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__34_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__33_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__34 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__34_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__35_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__34_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__35 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__35_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__36_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__35_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__36 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__36_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__37_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__36_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__37 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__37_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__38_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__37_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__38 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__38_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__39_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(16) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__39 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__39_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__40_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__39_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__40 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__40_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__41_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__40_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__41 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__41_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__42_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(10) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__41_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__42 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__42_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__43_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__42_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__43 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__43_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__44_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__43_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__44 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__44_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__45_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__44_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__45 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__45_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__46_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__45_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__46 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__46_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__47_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__46_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__47 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__47_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__48_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__10_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__48 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__48_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__49_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(14) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__48_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__49 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__49_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__50_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__49_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__50 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__50_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__51_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__50_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__51 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__51_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__52_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__51_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__52 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__52_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__53_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__52_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__53 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__53_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__54_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__53_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__54 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__54_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__55_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__54_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__55 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__55_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__56_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__55_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__56 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__56_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__57_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(16) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__10_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__57 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__57_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__58_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__57_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__58 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__58_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__59_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(14) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__58_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__59 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__59_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__60_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(10) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__59_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__60 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__60_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__61_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__60_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__61 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__61_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__62_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__61_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__62 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__62_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__63_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__62_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__63 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__63_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__64_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__63_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__64 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__64_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__65_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__64_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__65 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__65_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__66_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(17) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__30_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__66 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__66_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__67_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__66_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__67 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__67_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__68_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__67_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__68 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__68_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__69_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__68_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__69 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__69_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__70_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__69_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__70 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__70_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__71_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__70_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__71 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__71_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__72_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__71_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__72 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__72_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__73_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__72_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__73 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__73_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__74_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(16) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__74 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__74_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__75_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__74_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__75 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__75_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__76_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__75_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__76 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__76_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__77_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__76_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__77 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__77_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__78_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__77_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__78 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__78_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__79_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__78_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__79 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__79_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__80_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__79_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__80 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__80_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__81_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__80_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__81 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__81_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__82_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__81_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__82 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__82_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__83_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__82_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__83 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__83_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__84_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__21_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__84 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__84_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__85_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__84_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__85 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__85_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__86_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__85_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__86 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__86_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__87_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__86_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__87 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__87_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__88_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__87_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__88 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__88_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__89_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__88_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__89 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__89_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__90_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__89_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__90 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__90_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__91_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__90_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__91 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__91_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__92_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__39_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__92 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__92_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__93_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__92_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__93 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__93_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__94_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__93_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__94 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__94_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__95_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__94_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__95 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__95_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__96_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__95_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__96 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__96_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__97_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__96_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__97 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__97_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__98_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__97_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__98 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__98_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__99_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__98_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__99 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__99_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__100_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(14) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__74_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__100 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__100_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__101_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__100_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__101 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__101_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__102_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__101_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__102 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__102_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__103_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__102_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__103 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__103_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__104_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__103_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__104 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__104_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__105_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__104_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__105 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__105_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__106_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__105_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__106 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__106_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__107_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__106_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__107 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__107_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__108_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__107_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__108 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__108_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__109_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(16) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__11_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__109 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__109_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__110_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__109_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__110 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__110_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__111_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__110_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__111 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__111_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__112_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__111_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__112 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__112_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__113_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__112_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__113 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__113_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__114_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__113_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__114 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__114_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__115_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__114_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__115 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__115_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__116_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__115_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__116 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__116_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__117_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(17) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__117 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__117_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__118_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(16) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__117_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__118 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__118_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__119_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__118_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__119 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__119_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__120_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__119_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__120 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__120_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__121_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__120_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__121 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__121_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__122_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__121_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__122 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__122_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__123_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__122_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__123 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__123_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__124_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__123_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__124 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__124_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__125_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__124_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__125 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__125_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__126_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(14) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__109_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__126 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__126_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__127_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__126_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__127 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__127_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__128_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__127_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__128 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__128_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__129_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__128_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__129 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__129_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__130_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__129_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__130 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__130_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__131_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__130_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__131 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__131_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__132_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__131_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__132 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__132_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__133_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(16) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__30_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__133 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__133_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__134_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(14) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__133_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__134 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__134_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__135_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__134_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__135 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__135_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__136_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__135_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__136 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__136_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__137_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__136_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__137 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__137_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__138_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__137_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__138 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__138_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__139_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__138_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__139 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__139_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__140_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__139_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__140 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__140_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__141_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(14) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__66_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__141 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__141_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__142_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__141_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__142 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__142_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__143_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__142_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__143 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__143_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__144_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(10) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__143_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__144 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__144_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__145_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__144_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__145 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__145_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__146_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__145_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__146 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__146_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__147_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__146_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__147 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__147_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__148_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__147_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__148 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__148_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__149_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__140_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__148_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__149 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__149_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__150_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__132_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__149_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__150 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__150_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__151_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__125_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__150_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__151 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__151_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__152_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__116_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__151_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__152 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__152_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__153_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__108_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__152_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__153 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__153_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__154_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__99_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__153_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__154 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__154_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__155_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__91_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__154_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__155 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__155_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__156_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__83_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__155_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__156 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__156_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__157_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__73_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__156_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__157 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__157_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__158_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__65_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__157_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__158 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__158_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__159_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__56_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__158_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__159 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__159_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__160_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__47_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__159_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__160 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__160_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__161_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__38_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__160_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__161 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__161_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__162_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__29_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__161_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__162 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__162_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__163_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__19_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__162_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__163 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__163_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__164_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__9_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__163_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__164 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__164_value;
LEAN_EXPORT const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__164_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__140_value),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected___closed__0 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected___closed__0_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__29_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected___closed__1 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected___closed__1_value;
LEAN_EXPORT const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected___closed__1_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__132_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__148_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__0 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__0_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__125_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__0_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__1 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__1_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__116_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__1_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__2 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__2_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__108_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__2_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__3 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__3_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__99_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__3_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__4 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__4_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__91_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__4_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__5 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__5_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__83_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__5_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__6 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__6_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__73_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__6_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__7 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__7_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__65_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__7_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__8 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__8_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__56_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__8_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__9 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__9_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__47_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__9_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__10 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__10_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__38_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__10_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__11 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__11_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__19_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__11_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__12 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__12_value;
static const lean_ctor_object lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__9_value),((lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__12_value)}};
static const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__13 = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__13_value;
LEAN_EXPORT const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected___closed__13_value;
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_residual_spec__0(lean_object*, lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual___closed__0;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual;
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_deleted_spec__0(lean_object*, lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted___closed__0;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted;
LEAN_EXPORT const lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchor = (const lean_object*)&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog___closed__147_value;
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_neighborsAt_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_neighborsAt_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_neighborsAt(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_neighborsAt___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rootedDegree(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rootedDegree___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__0___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__1(lean_object*, lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore___closed__0;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore;
static lean_once_cell_t lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0___closed__0;
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0(lean_object*, lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore___closed__0;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck;
static lean_once_cell_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__0;
static lean_once_cell_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__1;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__0;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__1;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__0___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__1(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__1___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__0;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__1;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck;
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck_spec__0___boxed(lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck___closed__0;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__0;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__1;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__2_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__2;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__4_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__4;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__5_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__5;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__6_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__6;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__7_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__7;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__8_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__8;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__9_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__9;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__10_once = LEAN_ONCE_CELL_INITIALIZER;
static uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__10;
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_q;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_choose(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_choose___boxed(lean_object*, lean_object*);
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__0;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__1;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__0;
static lean_once_cell_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__1;
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows;
LEAN_EXPORT lean_object* lp_m31QRootedShell___private_M31QRootedShell_MultiplicativeCounterexample_0__M31QRootedShell_degreeSum_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_m31QRootedShell___private_M31QRootedShell_MultiplicativeCounterexample_0__M31QRootedShell_degreeSum_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*);
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_p(void){
_start:
{
lean_object* v___x_1_; 
v___x_1_ = lean_unsigned_to_nat(241u);
return v___x_1_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_n(void){
_start:
{
lean_object* v___x_2_; 
v___x_2_ = lean_unsigned_to_nat(20u);
return v___x_2_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_m(void){
_start:
{
lean_object* v___x_3_; 
v___x_3_ = lean_unsigned_to_nat(10u);
return v___x_3_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_w(void){
_start:
{
lean_object* v___x_4_; 
v___x_4_ = lean_unsigned_to_nat(2u);
return v___x_4_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generator(void){
_start:
{
lean_object* v___x_5_; 
v___x_5_ = lean_unsigned_to_nat(235u);
return v___x_5_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices___closed__0(void){
_start:
{
lean_object* v___x_6_; lean_object* v___x_7_; 
v___x_6_ = lean_unsigned_to_nat(20u);
v___x_7_ = l_List_range(v___x_6_);
return v___x_7_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices(void){
_start:
{
lean_object* v___x_8_; 
v___x_8_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices___closed__0);
return v___x_8_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domain(lean_object* v_x_9_){
_start:
{
lean_object* v___x_10_; uint8_t v___x_11_; 
v___x_10_ = lean_unsigned_to_nat(0u);
v___x_11_ = lean_nat_dec_eq(v_x_9_, v___x_10_);
if (v___x_11_ == 0)
{
lean_object* v___x_12_; uint8_t v___x_13_; 
v___x_12_ = lean_unsigned_to_nat(1u);
v___x_13_ = lean_nat_dec_eq(v_x_9_, v___x_12_);
if (v___x_13_ == 0)
{
lean_object* v___x_14_; uint8_t v___x_15_; 
v___x_14_ = lean_unsigned_to_nat(2u);
v___x_15_ = lean_nat_dec_eq(v_x_9_, v___x_14_);
if (v___x_15_ == 0)
{
lean_object* v___x_16_; uint8_t v___x_17_; 
v___x_16_ = lean_unsigned_to_nat(3u);
v___x_17_ = lean_nat_dec_eq(v_x_9_, v___x_16_);
if (v___x_17_ == 0)
{
lean_object* v___x_18_; uint8_t v___x_19_; 
v___x_18_ = lean_unsigned_to_nat(4u);
v___x_19_ = lean_nat_dec_eq(v_x_9_, v___x_18_);
if (v___x_19_ == 0)
{
lean_object* v___x_20_; uint8_t v___x_21_; 
v___x_20_ = lean_unsigned_to_nat(5u);
v___x_21_ = lean_nat_dec_eq(v_x_9_, v___x_20_);
if (v___x_21_ == 0)
{
lean_object* v___x_22_; uint8_t v___x_23_; 
v___x_22_ = lean_unsigned_to_nat(6u);
v___x_23_ = lean_nat_dec_eq(v_x_9_, v___x_22_);
if (v___x_23_ == 0)
{
lean_object* v___x_24_; uint8_t v___x_25_; 
v___x_24_ = lean_unsigned_to_nat(7u);
v___x_25_ = lean_nat_dec_eq(v_x_9_, v___x_24_);
if (v___x_25_ == 0)
{
lean_object* v___x_26_; uint8_t v___x_27_; 
v___x_26_ = lean_unsigned_to_nat(8u);
v___x_27_ = lean_nat_dec_eq(v_x_9_, v___x_26_);
if (v___x_27_ == 0)
{
lean_object* v___x_28_; uint8_t v___x_29_; 
v___x_28_ = lean_unsigned_to_nat(9u);
v___x_29_ = lean_nat_dec_eq(v_x_9_, v___x_28_);
if (v___x_29_ == 0)
{
lean_object* v___x_30_; uint8_t v___x_31_; 
v___x_30_ = lean_unsigned_to_nat(10u);
v___x_31_ = lean_nat_dec_eq(v_x_9_, v___x_30_);
if (v___x_31_ == 0)
{
lean_object* v___x_32_; uint8_t v___x_33_; 
v___x_32_ = lean_unsigned_to_nat(11u);
v___x_33_ = lean_nat_dec_eq(v_x_9_, v___x_32_);
if (v___x_33_ == 0)
{
lean_object* v___x_34_; uint8_t v___x_35_; 
v___x_34_ = lean_unsigned_to_nat(12u);
v___x_35_ = lean_nat_dec_eq(v_x_9_, v___x_34_);
if (v___x_35_ == 0)
{
lean_object* v___x_36_; uint8_t v___x_37_; 
v___x_36_ = lean_unsigned_to_nat(13u);
v___x_37_ = lean_nat_dec_eq(v_x_9_, v___x_36_);
if (v___x_37_ == 0)
{
lean_object* v___x_38_; uint8_t v___x_39_; 
v___x_38_ = lean_unsigned_to_nat(14u);
v___x_39_ = lean_nat_dec_eq(v_x_9_, v___x_38_);
if (v___x_39_ == 0)
{
lean_object* v___x_40_; uint8_t v___x_41_; 
v___x_40_ = lean_unsigned_to_nat(15u);
v___x_41_ = lean_nat_dec_eq(v_x_9_, v___x_40_);
if (v___x_41_ == 0)
{
lean_object* v___x_42_; uint8_t v___x_43_; 
v___x_42_ = lean_unsigned_to_nat(16u);
v___x_43_ = lean_nat_dec_eq(v_x_9_, v___x_42_);
if (v___x_43_ == 0)
{
lean_object* v___x_44_; uint8_t v___x_45_; 
v___x_44_ = lean_unsigned_to_nat(17u);
v___x_45_ = lean_nat_dec_eq(v_x_9_, v___x_44_);
if (v___x_45_ == 0)
{
lean_object* v___x_46_; uint8_t v___x_47_; 
v___x_46_ = lean_unsigned_to_nat(18u);
v___x_47_ = lean_nat_dec_eq(v_x_9_, v___x_46_);
if (v___x_47_ == 0)
{
lean_object* v___x_48_; uint8_t v___x_49_; 
v___x_48_ = lean_unsigned_to_nat(19u);
v___x_49_ = lean_nat_dec_eq(v_x_9_, v___x_48_);
if (v___x_49_ == 0)
{
return v___x_10_;
}
else
{
lean_object* v___x_50_; 
v___x_50_ = lean_unsigned_to_nat(40u);
return v___x_50_;
}
}
else
{
lean_object* v___x_51_; 
v___x_51_ = lean_unsigned_to_nat(154u);
return v___x_51_;
}
}
else
{
lean_object* v___x_52_; 
v___x_52_ = lean_unsigned_to_nat(135u);
return v___x_52_;
}
}
else
{
lean_object* v___x_53_; 
v___x_53_ = lean_unsigned_to_nat(98u);
return v___x_53_;
}
}
else
{
lean_object* v___x_54_; 
v___x_54_ = lean_unsigned_to_nat(64u);
return v___x_54_;
}
}
else
{
lean_object* v___x_55_; 
v___x_55_ = lean_unsigned_to_nat(150u);
return v___x_55_;
}
}
else
{
lean_object* v___x_56_; 
v___x_56_ = lean_unsigned_to_nat(216u);
return v___x_56_;
}
}
else
{
lean_object* v___x_57_; 
v___x_57_ = lean_unsigned_to_nat(205u);
return v___x_57_;
}
}
else
{
return v___x_22_;
}
}
else
{
lean_object* v___x_58_; 
v___x_58_ = lean_unsigned_to_nat(240u);
return v___x_58_;
}
}
else
{
lean_object* v___x_59_; 
v___x_59_ = lean_unsigned_to_nat(201u);
return v___x_59_;
}
}
else
{
lean_object* v___x_60_; 
v___x_60_ = lean_unsigned_to_nat(87u);
return v___x_60_;
}
}
else
{
lean_object* v___x_61_; 
v___x_61_ = lean_unsigned_to_nat(106u);
return v___x_61_;
}
}
else
{
lean_object* v___x_62_; 
v___x_62_ = lean_unsigned_to_nat(143u);
return v___x_62_;
}
}
else
{
lean_object* v___x_63_; 
v___x_63_ = lean_unsigned_to_nat(177u);
return v___x_63_;
}
}
else
{
lean_object* v___x_64_; 
v___x_64_ = lean_unsigned_to_nat(91u);
return v___x_64_;
}
}
else
{
lean_object* v___x_65_; 
v___x_65_ = lean_unsigned_to_nat(25u);
return v___x_65_;
}
}
else
{
lean_object* v___x_66_; 
v___x_66_ = lean_unsigned_to_nat(36u);
return v___x_66_;
}
}
else
{
lean_object* v___x_67_; 
v___x_67_ = lean_unsigned_to_nat(235u);
return v___x_67_;
}
}
else
{
lean_object* v___x_68_; 
v___x_68_ = lean_unsigned_to_nat(1u);
return v___x_68_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domain___boxed(lean_object* v_x_69_){
_start:
{
lean_object* v_res_70_; 
v_res_70_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domain(v_x_69_);
lean_dec(v_x_69_);
return v_res_70_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_powMod(lean_object* v_a_71_, lean_object* v_x_72_){
_start:
{
lean_object* v_zero_73_; uint8_t v_isZero_74_; 
v_zero_73_ = lean_unsigned_to_nat(0u);
v_isZero_74_ = lean_nat_dec_eq(v_x_72_, v_zero_73_);
if (v_isZero_74_ == 1)
{
lean_object* v___x_75_; 
v___x_75_ = lean_unsigned_to_nat(1u);
return v___x_75_;
}
else
{
lean_object* v_one_76_; lean_object* v_n_77_; lean_object* v___x_78_; lean_object* v___x_79_; lean_object* v___x_80_; lean_object* v___x_81_; 
v_one_76_ = lean_unsigned_to_nat(1u);
v_n_77_ = lean_nat_sub(v_x_72_, v_one_76_);
v___x_78_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_powMod(v_a_71_, v_n_77_);
lean_dec(v_n_77_);
v___x_79_ = lean_nat_mul(v___x_78_, v_a_71_);
lean_dec(v___x_78_);
v___x_80_ = lean_unsigned_to_nat(241u);
v___x_81_ = lean_nat_mod(v___x_79_, v___x_80_);
lean_dec(v___x_79_);
return v___x_81_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_powMod___boxed(lean_object* v_a_82_, lean_object* v_x_83_){
_start:
{
lean_object* v_res_84_; 
v_res_84_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_powMod(v_a_82_, v_x_83_);
lean_dec(v_x_83_);
lean_dec(v_a_82_);
return v_res_84_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sumNat(lean_object* v_x_85_){
_start:
{
if (lean_obj_tag(v_x_85_) == 0)
{
lean_object* v___x_86_; 
v___x_86_ = lean_unsigned_to_nat(0u);
return v___x_86_;
}
else
{
lean_object* v_head_87_; lean_object* v_tail_88_; lean_object* v___x_89_; lean_object* v___x_90_; 
v_head_87_ = lean_ctor_get(v_x_85_, 0);
v_tail_88_ = lean_ctor_get(v_x_85_, 1);
v___x_89_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sumNat(v_tail_88_);
v___x_90_ = lean_nat_add(v_head_87_, v___x_89_);
lean_dec(v___x_89_);
return v___x_90_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sumNat___boxed(lean_object* v_x_91_){
_start:
{
lean_object* v_res_92_; 
v_res_92_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sumNat(v_x_91_);
lean_dec(v_x_91_);
return v_res_92_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_pairSum(lean_object* v_x_93_){
_start:
{
if (lean_obj_tag(v_x_93_) == 0)
{
lean_object* v___x_94_; 
v___x_94_ = lean_unsigned_to_nat(0u);
return v___x_94_;
}
else
{
lean_object* v_head_95_; lean_object* v_tail_96_; lean_object* v___x_97_; lean_object* v___x_98_; lean_object* v___x_99_; lean_object* v___x_100_; 
v_head_95_ = lean_ctor_get(v_x_93_, 0);
v_tail_96_ = lean_ctor_get(v_x_93_, 1);
v___x_97_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sumNat(v_tail_96_);
v___x_98_ = lean_nat_mul(v_head_95_, v___x_97_);
lean_dec(v___x_97_);
v___x_99_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_pairSum(v_tail_96_);
v___x_100_ = lean_nat_add(v___x_98_, v___x_99_);
lean_dec(v___x_99_);
lean_dec(v___x_98_);
return v___x_100_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_pairSum___boxed(lean_object* v_x_101_){
_start:
{
lean_object* v_res_102_; 
v_res_102_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_pairSum(v_x_101_);
lean_dec(v_x_101_);
return v_res_102_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_prefix1_spec__0(lean_object* v_a_103_, lean_object* v_a_104_){
_start:
{
if (lean_obj_tag(v_a_103_) == 0)
{
lean_object* v___x_105_; 
v___x_105_ = l_List_reverse___redArg(v_a_104_);
return v___x_105_;
}
else
{
lean_object* v_head_106_; lean_object* v_tail_107_; lean_object* v___x_109_; uint8_t v_isShared_110_; uint8_t v_isSharedCheck_116_; 
v_head_106_ = lean_ctor_get(v_a_103_, 0);
v_tail_107_ = lean_ctor_get(v_a_103_, 1);
v_isSharedCheck_116_ = !lean_is_exclusive(v_a_103_);
if (v_isSharedCheck_116_ == 0)
{
v___x_109_ = v_a_103_;
v_isShared_110_ = v_isSharedCheck_116_;
goto v_resetjp_108_;
}
else
{
lean_inc(v_tail_107_);
lean_inc(v_head_106_);
lean_dec(v_a_103_);
v___x_109_ = lean_box(0);
v_isShared_110_ = v_isSharedCheck_116_;
goto v_resetjp_108_;
}
v_resetjp_108_:
{
lean_object* v___x_111_; lean_object* v___x_113_; 
v___x_111_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domain(v_head_106_);
lean_dec(v_head_106_);
if (v_isShared_110_ == 0)
{
lean_ctor_set(v___x_109_, 1, v_a_104_);
lean_ctor_set(v___x_109_, 0, v___x_111_);
v___x_113_ = v___x_109_;
goto v_reusejp_112_;
}
else
{
lean_object* v_reuseFailAlloc_115_; 
v_reuseFailAlloc_115_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_115_, 0, v___x_111_);
lean_ctor_set(v_reuseFailAlloc_115_, 1, v_a_104_);
v___x_113_ = v_reuseFailAlloc_115_;
goto v_reusejp_112_;
}
v_reusejp_112_:
{
v_a_103_ = v_tail_107_;
v_a_104_ = v___x_113_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_prefix1(lean_object* v_S_117_){
_start:
{
lean_object* v___x_118_; lean_object* v___x_119_; lean_object* v___x_120_; lean_object* v___x_121_; lean_object* v___x_122_; 
v___x_118_ = lean_box(0);
v___x_119_ = lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_prefix1_spec__0(v_S_117_, v___x_118_);
v___x_120_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sumNat(v___x_119_);
lean_dec(v___x_119_);
v___x_121_ = lean_unsigned_to_nat(241u);
v___x_122_ = lean_nat_mod(v___x_120_, v___x_121_);
lean_dec(v___x_120_);
return v___x_122_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_prefix2(lean_object* v_S_123_){
_start:
{
lean_object* v___x_124_; lean_object* v___x_125_; lean_object* v___x_126_; lean_object* v___x_127_; lean_object* v___x_128_; 
v___x_124_ = lean_box(0);
v___x_125_ = lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_prefix1_spec__0(v_S_123_, v___x_124_);
v___x_126_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_pairSum(v___x_125_);
lean_dec(v___x_125_);
v___x_127_ = lean_unsigned_to_nat(241u);
v___x_128_ = lean_nat_mod(v___x_126_, v___x_127_);
lean_dec(v___x_126_);
return v___x_128_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicates(lean_object* v_x_129_){
_start:
{
if (lean_obj_tag(v_x_129_) == 0)
{
uint8_t v___x_130_; 
v___x_130_ = 1;
return v___x_130_;
}
else
{
lean_object* v_head_131_; lean_object* v_tail_132_; uint8_t v___x_133_; 
v_head_131_ = lean_ctor_get(v_x_129_, 0);
v_tail_132_ = lean_ctor_get(v_x_129_, 1);
v___x_133_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_131_, v_tail_132_);
if (v___x_133_ == 0)
{
v_x_129_ = v_tail_132_;
goto _start;
}
else
{
uint8_t v___x_135_; 
v___x_135_ = 0;
return v___x_135_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicates___boxed(lean_object* v_x_136_){
_start:
{
uint8_t v_res_137_; lean_object* v_r_138_; 
v_res_137_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicates(v_x_136_);
lean_dec(v_x_136_);
v_r_138_ = lean_box(v_res_137_);
return v_r_138_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_beq___at___00List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0_spec__0(lean_object* v_x_139_, lean_object* v_x_140_){
_start:
{
if (lean_obj_tag(v_x_139_) == 0)
{
if (lean_obj_tag(v_x_140_) == 0)
{
uint8_t v___x_141_; 
v___x_141_ = 1;
return v___x_141_;
}
else
{
uint8_t v___x_142_; 
v___x_142_ = 0;
return v___x_142_;
}
}
else
{
if (lean_obj_tag(v_x_140_) == 0)
{
uint8_t v___x_143_; 
v___x_143_ = 0;
return v___x_143_;
}
else
{
lean_object* v_head_144_; lean_object* v_tail_145_; lean_object* v_head_146_; lean_object* v_tail_147_; uint8_t v___x_148_; 
v_head_144_ = lean_ctor_get(v_x_139_, 0);
v_tail_145_ = lean_ctor_get(v_x_139_, 1);
v_head_146_ = lean_ctor_get(v_x_140_, 0);
v_tail_147_ = lean_ctor_get(v_x_140_, 1);
v___x_148_ = lean_nat_dec_eq(v_head_144_, v_head_146_);
if (v___x_148_ == 0)
{
return v___x_148_;
}
else
{
v_x_139_ = v_tail_145_;
v_x_140_ = v_tail_147_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_beq___at___00List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0_spec__0___boxed(lean_object* v_x_150_, lean_object* v_x_151_){
_start:
{
uint8_t v_res_152_; lean_object* v_r_153_; 
v_res_152_ = lp_m31QRootedShell_List_beq___at___00List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0_spec__0(v_x_150_, v_x_151_);
lean_dec(v_x_151_);
lean_dec(v_x_150_);
v_r_153_ = lean_box(v_res_152_);
return v_r_153_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0(lean_object* v_a_154_, lean_object* v_x_155_){
_start:
{
if (lean_obj_tag(v_x_155_) == 0)
{
uint8_t v___x_156_; 
v___x_156_ = 0;
return v___x_156_;
}
else
{
lean_object* v_head_157_; lean_object* v_tail_158_; uint8_t v___x_159_; 
v_head_157_ = lean_ctor_get(v_x_155_, 0);
v_tail_158_ = lean_ctor_get(v_x_155_, 1);
v___x_159_ = lp_m31QRootedShell_List_beq___at___00List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0_spec__0(v_a_154_, v_head_157_);
if (v___x_159_ == 0)
{
v_x_155_ = v_tail_158_;
goto _start;
}
else
{
return v___x_159_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0___boxed(lean_object* v_a_161_, lean_object* v_x_162_){
_start:
{
uint8_t v_res_163_; lean_object* v_r_164_; 
v_res_163_ = lp_m31QRootedShell_List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0(v_a_161_, v_x_162_);
lean_dec(v_x_162_);
lean_dec(v_a_161_);
v_r_164_ = lean_box(v_res_163_);
return v_r_164_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports(lean_object* v_x_165_){
_start:
{
if (lean_obj_tag(v_x_165_) == 0)
{
uint8_t v___x_166_; 
v___x_166_ = 1;
return v___x_166_;
}
else
{
lean_object* v_head_167_; lean_object* v_tail_168_; uint8_t v___x_169_; 
v_head_167_ = lean_ctor_get(v_x_165_, 0);
v_tail_168_ = lean_ctor_get(v_x_165_, 1);
v___x_169_ = lp_m31QRootedShell_List_elem___at___00M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports_spec__0(v_head_167_, v_tail_168_);
if (v___x_169_ == 0)
{
v_x_165_ = v_tail_168_;
goto _start;
}
else
{
uint8_t v___x_171_; 
v___x_171_ = 0;
return v___x_171_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports___boxed(lean_object* v_x_172_){
_start:
{
uint8_t v_res_173_; lean_object* v_r_174_; 
v_res_173_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports(v_x_172_);
lean_dec(v_x_172_);
v_r_174_ = lean_box(v_res_173_);
return v_r_174_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_sameSupport_spec__0(lean_object* v_A_175_, lean_object* v_B_176_, lean_object* v_x_177_){
_start:
{
if (lean_obj_tag(v_x_177_) == 0)
{
uint8_t v___x_178_; 
v___x_178_ = 1;
return v___x_178_;
}
else
{
lean_object* v_head_179_; lean_object* v_tail_180_; uint8_t v___y_182_; uint8_t v___x_184_; uint8_t v___x_185_; 
v_head_179_ = lean_ctor_get(v_x_177_, 0);
v_tail_180_ = lean_ctor_get(v_x_177_, 1);
v___x_184_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_179_, v_A_175_);
v___x_185_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_179_, v_B_176_);
if (v___x_184_ == 0)
{
if (v___x_185_ == 0)
{
v_x_177_ = v_tail_180_;
goto _start;
}
else
{
v___y_182_ = v___x_184_;
goto v___jp_181_;
}
}
else
{
v___y_182_ = v___x_185_;
goto v___jp_181_;
}
v___jp_181_:
{
if (v___y_182_ == 0)
{
return v___y_182_;
}
else
{
v_x_177_ = v_tail_180_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_sameSupport_spec__0___boxed(lean_object* v_A_187_, lean_object* v_B_188_, lean_object* v_x_189_){
_start:
{
uint8_t v_res_190_; lean_object* v_r_191_; 
v_res_190_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_sameSupport_spec__0(v_A_187_, v_B_188_, v_x_189_);
lean_dec(v_x_189_);
lean_dec(v_B_188_);
lean_dec(v_A_187_);
v_r_191_ = lean_box(v_res_190_);
return v_r_191_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport(lean_object* v_A_192_, lean_object* v_B_193_){
_start:
{
lean_object* v___x_194_; uint8_t v___x_195_; 
v___x_194_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices;
v___x_195_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_sameSupport_spec__0(v_A_192_, v_B_193_, v___x_194_);
return v___x_195_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport___boxed(lean_object* v_A_196_, lean_object* v_B_197_){
_start:
{
uint8_t v_res_198_; lean_object* v_r_199_; 
v_res_198_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport(v_A_196_, v_B_197_);
lean_dec(v_B_197_);
lean_dec(v_A_196_);
v_r_199_ = lean_box(v_res_198_);
return v_r_199_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_rotateSupport_spec__0(lean_object* v_shift_200_, lean_object* v_a_201_, lean_object* v_a_202_){
_start:
{
if (lean_obj_tag(v_a_201_) == 0)
{
lean_object* v___x_203_; 
v___x_203_ = l_List_reverse___redArg(v_a_202_);
return v___x_203_;
}
else
{
lean_object* v_head_204_; lean_object* v_tail_205_; lean_object* v___x_207_; uint8_t v_isShared_208_; uint8_t v_isSharedCheck_216_; 
v_head_204_ = lean_ctor_get(v_a_201_, 0);
v_tail_205_ = lean_ctor_get(v_a_201_, 1);
v_isSharedCheck_216_ = !lean_is_exclusive(v_a_201_);
if (v_isSharedCheck_216_ == 0)
{
v___x_207_ = v_a_201_;
v_isShared_208_ = v_isSharedCheck_216_;
goto v_resetjp_206_;
}
else
{
lean_inc(v_tail_205_);
lean_inc(v_head_204_);
lean_dec(v_a_201_);
v___x_207_ = lean_box(0);
v_isShared_208_ = v_isSharedCheck_216_;
goto v_resetjp_206_;
}
v_resetjp_206_:
{
lean_object* v___x_209_; lean_object* v___x_210_; lean_object* v___x_211_; lean_object* v___x_213_; 
v___x_209_ = lean_nat_add(v_head_204_, v_shift_200_);
lean_dec(v_head_204_);
v___x_210_ = lean_unsigned_to_nat(20u);
v___x_211_ = lean_nat_mod(v___x_209_, v___x_210_);
lean_dec(v___x_209_);
if (v_isShared_208_ == 0)
{
lean_ctor_set(v___x_207_, 1, v_a_202_);
lean_ctor_set(v___x_207_, 0, v___x_211_);
v___x_213_ = v___x_207_;
goto v_reusejp_212_;
}
else
{
lean_object* v_reuseFailAlloc_215_; 
v_reuseFailAlloc_215_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_215_, 0, v___x_211_);
lean_ctor_set(v_reuseFailAlloc_215_, 1, v_a_202_);
v___x_213_ = v_reuseFailAlloc_215_;
goto v_reusejp_212_;
}
v_reusejp_212_:
{
v_a_201_ = v_tail_205_;
v_a_202_ = v___x_213_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_rotateSupport_spec__0___boxed(lean_object* v_shift_217_, lean_object* v_a_218_, lean_object* v_a_219_){
_start:
{
lean_object* v_res_220_; 
v_res_220_ = lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_rotateSupport_spec__0(v_shift_217_, v_a_218_, v_a_219_);
lean_dec(v_shift_217_);
return v_res_220_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotateSupport(lean_object* v_shift_221_, lean_object* v_S_222_){
_start:
{
lean_object* v___x_223_; lean_object* v___x_224_; 
v___x_223_ = lean_box(0);
v___x_224_ = lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_rotateSupport_spec__0(v_shift_221_, v_S_222_, v___x_223_);
return v___x_224_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotateSupport___boxed(lean_object* v_shift_225_, lean_object* v_S_226_){
_start:
{
lean_object* v_res_227_; 
v_res_227_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotateSupport(v_shift_225_, v_S_226_);
lean_dec(v_shift_225_);
return v_res_227_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_reflectSupport_spec__0(lean_object* v_axis_228_, lean_object* v_a_229_, lean_object* v_a_230_){
_start:
{
if (lean_obj_tag(v_a_229_) == 0)
{
lean_object* v___x_231_; 
v___x_231_ = l_List_reverse___redArg(v_a_230_);
return v___x_231_;
}
else
{
lean_object* v_head_232_; lean_object* v_tail_233_; lean_object* v___x_235_; uint8_t v_isShared_236_; uint8_t v_isSharedCheck_245_; 
v_head_232_ = lean_ctor_get(v_a_229_, 0);
v_tail_233_ = lean_ctor_get(v_a_229_, 1);
v_isSharedCheck_245_ = !lean_is_exclusive(v_a_229_);
if (v_isSharedCheck_245_ == 0)
{
v___x_235_ = v_a_229_;
v_isShared_236_ = v_isSharedCheck_245_;
goto v_resetjp_234_;
}
else
{
lean_inc(v_tail_233_);
lean_inc(v_head_232_);
lean_dec(v_a_229_);
v___x_235_ = lean_box(0);
v_isShared_236_ = v_isSharedCheck_245_;
goto v_resetjp_234_;
}
v_resetjp_234_:
{
lean_object* v___x_237_; lean_object* v___x_238_; lean_object* v___x_239_; lean_object* v___x_240_; lean_object* v___x_242_; 
v___x_237_ = lean_unsigned_to_nat(20u);
v___x_238_ = lean_nat_add(v_axis_228_, v___x_237_);
v___x_239_ = lean_nat_sub(v___x_238_, v_head_232_);
lean_dec(v_head_232_);
lean_dec(v___x_238_);
v___x_240_ = lean_nat_mod(v___x_239_, v___x_237_);
lean_dec(v___x_239_);
if (v_isShared_236_ == 0)
{
lean_ctor_set(v___x_235_, 1, v_a_230_);
lean_ctor_set(v___x_235_, 0, v___x_240_);
v___x_242_ = v___x_235_;
goto v_reusejp_241_;
}
else
{
lean_object* v_reuseFailAlloc_244_; 
v_reuseFailAlloc_244_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_244_, 0, v___x_240_);
lean_ctor_set(v_reuseFailAlloc_244_, 1, v_a_230_);
v___x_242_ = v_reuseFailAlloc_244_;
goto v_reusejp_241_;
}
v_reusejp_241_:
{
v_a_229_ = v_tail_233_;
v_a_230_ = v___x_242_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_reflectSupport_spec__0___boxed(lean_object* v_axis_246_, lean_object* v_a_247_, lean_object* v_a_248_){
_start:
{
lean_object* v_res_249_; 
v_res_249_ = lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_reflectSupport_spec__0(v_axis_246_, v_a_247_, v_a_248_);
lean_dec(v_axis_246_);
return v_res_249_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectSupport(lean_object* v_axis_250_, lean_object* v_S_251_){
_start:
{
lean_object* v___x_252_; lean_object* v___x_253_; 
v___x_252_ = lean_box(0);
v___x_253_ = lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_reflectSupport_spec__0(v_axis_250_, v_S_251_, v___x_252_);
return v___x_253_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectSupport___boxed(lean_object* v_axis_254_, lean_object* v_S_255_){
_start:
{
lean_object* v_res_256_; 
v_res_256_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectSupport(v_axis_254_, v_S_255_);
lean_dec(v_axis_254_);
return v_res_256_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotationFixes(lean_object* v_S_257_, lean_object* v_shift_258_){
_start:
{
lean_object* v___x_259_; uint8_t v___x_260_; 
lean_inc(v_S_257_);
v___x_259_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotateSupport(v_shift_258_, v_S_257_);
v___x_260_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport(v_S_257_, v___x_259_);
lean_dec(v___x_259_);
lean_dec(v_S_257_);
return v___x_260_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotationFixes___boxed(lean_object* v_S_261_, lean_object* v_shift_262_){
_start:
{
uint8_t v_res_263_; lean_object* v_r_264_; 
v_res_263_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotationFixes(v_S_261_, v_shift_262_);
lean_dec(v_shift_262_);
v_r_264_ = lean_box(v_res_263_);
return v_r_264_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectionFixes(lean_object* v_S_265_, lean_object* v_axis_266_){
_start:
{
lean_object* v___x_267_; uint8_t v___x_268_; 
lean_inc(v_S_265_);
v___x_267_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectSupport(v_axis_266_, v_S_265_);
v___x_268_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport(v_S_265_, v___x_267_);
lean_dec(v___x_267_);
lean_dec(v_S_265_);
return v___x_268_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectionFixes___boxed(lean_object* v_S_269_, lean_object* v_axis_270_){
_start:
{
uint8_t v_res_271_; lean_object* v_r_272_; 
v_res_271_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectionFixes(v_S_269_, v_axis_270_);
lean_dec(v_axis_270_);
v_r_272_ = lean_box(v_res_271_);
return v_r_272_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__1(lean_object* v_S_273_, uint8_t v___x_274_, lean_object* v_x_275_){
_start:
{
if (lean_obj_tag(v_x_275_) == 0)
{
uint8_t v___x_276_; 
lean_dec(v_S_273_);
v___x_276_ = 1;
return v___x_276_;
}
else
{
lean_object* v_head_277_; lean_object* v_tail_278_; uint8_t v___x_279_; 
v_head_277_ = lean_ctor_get(v_x_275_, 0);
v_tail_278_ = lean_ctor_get(v_x_275_, 1);
lean_inc(v_S_273_);
v___x_279_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectionFixes(v_S_273_, v_head_277_);
if (v___x_279_ == 0)
{
if (v___x_274_ == 0)
{
lean_dec(v_S_273_);
return v___x_274_;
}
else
{
v_x_275_ = v_tail_278_;
goto _start;
}
}
else
{
uint8_t v___x_281_; 
lean_dec(v_S_273_);
v___x_281_ = 0;
return v___x_281_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__1___boxed(lean_object* v_S_282_, lean_object* v___x_283_, lean_object* v_x_284_){
_start:
{
uint8_t v___x_120__boxed_285_; uint8_t v_res_286_; lean_object* v_r_287_; 
v___x_120__boxed_285_ = lean_unbox(v___x_283_);
v_res_286_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__1(v_S_282_, v___x_120__boxed_285_, v_x_284_);
lean_dec(v_x_284_);
v_r_287_ = lean_box(v_res_286_);
return v_r_287_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__0(lean_object* v_S_288_, lean_object* v_x_289_){
_start:
{
if (lean_obj_tag(v_x_289_) == 0)
{
uint8_t v___x_290_; 
lean_dec(v_S_288_);
v___x_290_ = 1;
return v___x_290_;
}
else
{
lean_object* v_head_291_; lean_object* v_tail_292_; lean_object* v___x_293_; lean_object* v___x_294_; uint8_t v___x_295_; 
v_head_291_ = lean_ctor_get(v_x_289_, 0);
v_tail_292_ = lean_ctor_get(v_x_289_, 1);
v___x_293_ = lean_unsigned_to_nat(1u);
v___x_294_ = lean_nat_add(v_head_291_, v___x_293_);
lean_inc(v_S_288_);
v___x_295_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotationFixes(v_S_288_, v___x_294_);
lean_dec(v___x_294_);
if (v___x_295_ == 0)
{
v_x_289_ = v_tail_292_;
goto _start;
}
else
{
uint8_t v___x_297_; 
lean_dec(v_S_288_);
v___x_297_ = 0;
return v___x_297_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__0___boxed(lean_object* v_S_298_, lean_object* v_x_299_){
_start:
{
uint8_t v_res_300_; lean_object* v_r_301_; 
v_res_300_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__0(v_S_298_, v_x_299_);
lean_dec(v_x_299_);
v_r_301_ = lean_box(v_res_300_);
return v_r_301_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___closed__0(void){
_start:
{
lean_object* v___x_302_; lean_object* v___x_303_; 
v___x_302_ = lean_unsigned_to_nat(19u);
v___x_303_ = l_List_range(v___x_302_);
return v___x_303_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric(lean_object* v_S_304_){
_start:
{
lean_object* v___x_305_; uint8_t v___x_306_; 
v___x_305_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___closed__0);
lean_inc(v_S_304_);
v___x_306_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__0(v_S_304_, v___x_305_);
if (v___x_306_ == 0)
{
lean_dec(v_S_304_);
return v___x_306_;
}
else
{
lean_object* v___x_307_; uint8_t v___x_308_; 
v___x_307_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices;
v___x_308_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric_spec__1(v_S_304_, v___x_306_, v___x_307_);
return v___x_308_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___boxed(lean_object* v_S_309_){
_start:
{
uint8_t v_res_310_; lean_object* v_r_311_; 
v_res_310_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric(v_S_309_);
v_r_311_ = lean_box(v_res_310_);
return v_r_311_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__0(lean_object* v_A_312_, lean_object* v_B_313_, lean_object* v_x_314_){
_start:
{
if (lean_obj_tag(v_x_314_) == 0)
{
uint8_t v___x_315_; 
lean_dec(v_A_312_);
v___x_315_ = 0;
return v___x_315_;
}
else
{
lean_object* v_head_316_; lean_object* v_tail_317_; lean_object* v___x_318_; uint8_t v___x_319_; 
v_head_316_ = lean_ctor_get(v_x_314_, 0);
v_tail_317_ = lean_ctor_get(v_x_314_, 1);
lean_inc(v_A_312_);
v___x_318_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rotateSupport(v_head_316_, v_A_312_);
v___x_319_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport(v___x_318_, v_B_313_);
lean_dec(v___x_318_);
if (v___x_319_ == 0)
{
v_x_314_ = v_tail_317_;
goto _start;
}
else
{
lean_dec(v_A_312_);
return v___x_319_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__0___boxed(lean_object* v_A_321_, lean_object* v_B_322_, lean_object* v_x_323_){
_start:
{
uint8_t v_res_324_; lean_object* v_r_325_; 
v_res_324_ = lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__0(v_A_321_, v_B_322_, v_x_323_);
lean_dec(v_x_323_);
lean_dec(v_B_322_);
v_r_325_ = lean_box(v_res_324_);
return v_r_325_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__1(lean_object* v_A_326_, lean_object* v_B_327_, lean_object* v_x_328_){
_start:
{
if (lean_obj_tag(v_x_328_) == 0)
{
uint8_t v___x_329_; 
lean_dec(v_A_326_);
v___x_329_ = 0;
return v___x_329_;
}
else
{
lean_object* v_head_330_; lean_object* v_tail_331_; lean_object* v___x_332_; uint8_t v___x_333_; 
v_head_330_ = lean_ctor_get(v_x_328_, 0);
v_tail_331_ = lean_ctor_get(v_x_328_, 1);
lean_inc(v_A_326_);
v___x_332_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectSupport(v_head_330_, v_A_326_);
v___x_333_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport(v___x_332_, v_B_327_);
lean_dec(v___x_332_);
if (v___x_333_ == 0)
{
v_x_328_ = v_tail_331_;
goto _start;
}
else
{
lean_dec(v_A_326_);
return v___x_333_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__1___boxed(lean_object* v_A_335_, lean_object* v_B_336_, lean_object* v_x_337_){
_start:
{
uint8_t v_res_338_; lean_object* v_r_339_; 
v_res_338_ = lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__1(v_A_335_, v_B_336_, v_x_337_);
lean_dec(v_x_337_);
lean_dec(v_B_336_);
v_r_339_ = lean_box(v_res_338_);
return v_r_339_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit(lean_object* v_A_340_, lean_object* v_B_341_){
_start:
{
lean_object* v___x_342_; uint8_t v___x_343_; 
v___x_342_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices;
lean_inc(v_A_340_);
v___x_343_ = lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__0(v_A_340_, v_B_341_, v___x_342_);
if (v___x_343_ == 0)
{
uint8_t v___x_344_; 
v___x_344_ = lp_m31QRootedShell_List_any___at___00M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit_spec__1(v_A_340_, v_B_341_, v___x_342_);
return v___x_344_;
}
else
{
lean_dec(v_A_340_);
return v___x_343_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit___boxed(lean_object* v_A_345_, lean_object* v_B_346_){
_start:
{
uint8_t v_res_347_; lean_object* v_r_348_; 
v_res_347_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit(v_A_345_, v_B_346_);
lean_dec(v_B_346_);
v_r_348_ = lean_box(v_res_347_);
return v_r_348_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_interCard_spec__0(lean_object* v_B_349_, lean_object* v_a_350_, lean_object* v_a_351_){
_start:
{
if (lean_obj_tag(v_a_350_) == 0)
{
lean_object* v___x_352_; 
v___x_352_ = l_List_reverse___redArg(v_a_351_);
return v___x_352_;
}
else
{
lean_object* v_head_353_; lean_object* v_tail_354_; lean_object* v___x_356_; uint8_t v_isShared_357_; uint8_t v_isSharedCheck_364_; 
v_head_353_ = lean_ctor_get(v_a_350_, 0);
v_tail_354_ = lean_ctor_get(v_a_350_, 1);
v_isSharedCheck_364_ = !lean_is_exclusive(v_a_350_);
if (v_isSharedCheck_364_ == 0)
{
v___x_356_ = v_a_350_;
v_isShared_357_ = v_isSharedCheck_364_;
goto v_resetjp_355_;
}
else
{
lean_inc(v_tail_354_);
lean_inc(v_head_353_);
lean_dec(v_a_350_);
v___x_356_ = lean_box(0);
v_isShared_357_ = v_isSharedCheck_364_;
goto v_resetjp_355_;
}
v_resetjp_355_:
{
uint8_t v___x_358_; 
v___x_358_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_head_353_, v_B_349_);
if (v___x_358_ == 0)
{
lean_del_object(v___x_356_);
lean_dec(v_head_353_);
v_a_350_ = v_tail_354_;
goto _start;
}
else
{
lean_object* v___x_361_; 
if (v_isShared_357_ == 0)
{
lean_ctor_set(v___x_356_, 1, v_a_351_);
v___x_361_ = v___x_356_;
goto v_reusejp_360_;
}
else
{
lean_object* v_reuseFailAlloc_363_; 
v_reuseFailAlloc_363_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_363_, 0, v_head_353_);
lean_ctor_set(v_reuseFailAlloc_363_, 1, v_a_351_);
v___x_361_ = v_reuseFailAlloc_363_;
goto v_reusejp_360_;
}
v_reusejp_360_:
{
v_a_350_ = v_tail_354_;
v_a_351_ = v___x_361_;
goto _start;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_interCard_spec__0___boxed(lean_object* v_B_365_, lean_object* v_a_366_, lean_object* v_a_367_){
_start:
{
lean_object* v_res_368_; 
v_res_368_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_interCard_spec__0(v_B_365_, v_a_366_, v_a_367_);
lean_dec(v_B_365_);
return v_res_368_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_interCard(lean_object* v_A_369_, lean_object* v_B_370_){
_start:
{
lean_object* v___x_371_; lean_object* v___x_372_; lean_object* v___x_373_; 
v___x_371_ = lean_box(0);
v___x_372_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_interCard_spec__0(v_B_370_, v_A_369_, v___x_371_);
v___x_373_ = l_List_lengthTR___redArg(v___x_372_);
lean_dec(v___x_372_);
return v___x_373_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_interCard___boxed(lean_object* v_A_374_, lean_object* v_B_375_){
_start:
{
lean_object* v_res_376_; 
v_res_376_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_interCard(v_A_374_, v_B_375_);
lean_dec(v_B_375_);
return v_res_376_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_exchangeDistance(lean_object* v_A_377_, lean_object* v_B_378_){
_start:
{
lean_object* v___x_379_; lean_object* v___x_380_; lean_object* v___x_381_; 
v___x_379_ = l_List_lengthTR___redArg(v_A_377_);
v___x_380_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_interCard(v_A_377_, v_B_378_);
v___x_381_ = lean_nat_sub(v___x_379_, v___x_380_);
lean_dec(v___x_380_);
lean_dec(v___x_379_);
return v___x_381_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_exchangeDistance___boxed(lean_object* v_A_382_, lean_object* v_B_383_){
_start:
{
lean_object* v_res_384_; 
v_res_384_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_exchangeDistance(v_A_382_, v_B_383_);
lean_dec(v_B_383_);
return v_res_384_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_residual_spec__0(lean_object* v_a_931_, lean_object* v_a_932_){
_start:
{
if (lean_obj_tag(v_a_931_) == 0)
{
lean_object* v___x_933_; 
v___x_933_ = l_List_reverse___redArg(v_a_932_);
return v___x_933_;
}
else
{
lean_object* v_head_934_; lean_object* v_tail_935_; lean_object* v___x_937_; uint8_t v_isShared_938_; uint8_t v_isSharedCheck_945_; 
v_head_934_ = lean_ctor_get(v_a_931_, 0);
v_tail_935_ = lean_ctor_get(v_a_931_, 1);
v_isSharedCheck_945_ = !lean_is_exclusive(v_a_931_);
if (v_isSharedCheck_945_ == 0)
{
v___x_937_ = v_a_931_;
v_isShared_938_ = v_isSharedCheck_945_;
goto v_resetjp_936_;
}
else
{
lean_inc(v_tail_935_);
lean_inc(v_head_934_);
lean_dec(v_a_931_);
v___x_937_ = lean_box(0);
v_isShared_938_ = v_isSharedCheck_945_;
goto v_resetjp_936_;
}
v_resetjp_936_:
{
uint8_t v___x_939_; 
lean_inc(v_head_934_);
v___x_939_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric(v_head_934_);
if (v___x_939_ == 0)
{
lean_del_object(v___x_937_);
lean_dec(v_head_934_);
v_a_931_ = v_tail_935_;
goto _start;
}
else
{
lean_object* v___x_942_; 
if (v_isShared_938_ == 0)
{
lean_ctor_set(v___x_937_, 1, v_a_932_);
v___x_942_ = v___x_937_;
goto v_reusejp_941_;
}
else
{
lean_object* v_reuseFailAlloc_944_; 
v_reuseFailAlloc_944_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_944_, 0, v_head_934_);
lean_ctor_set(v_reuseFailAlloc_944_, 1, v_a_932_);
v___x_942_ = v_reuseFailAlloc_944_;
goto v_reusejp_941_;
}
v_reusejp_941_:
{
v_a_931_ = v_tail_935_;
v_a_932_ = v___x_942_;
goto _start;
}
}
}
}
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual___closed__0(void){
_start:
{
lean_object* v___x_946_; lean_object* v___x_947_; lean_object* v___x_948_; 
v___x_946_ = lean_box(0);
v___x_947_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog));
v___x_948_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_residual_spec__0(v___x_947_, v___x_946_);
return v___x_948_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual(void){
_start:
{
lean_object* v___x_949_; 
v___x_949_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual___closed__0);
return v___x_949_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_deleted_spec__0(lean_object* v_a_950_, lean_object* v_a_951_){
_start:
{
if (lean_obj_tag(v_a_950_) == 0)
{
lean_object* v___x_952_; 
v___x_952_ = l_List_reverse___redArg(v_a_951_);
return v___x_952_;
}
else
{
lean_object* v_head_953_; lean_object* v_tail_954_; lean_object* v___x_956_; uint8_t v_isShared_957_; uint8_t v_isSharedCheck_964_; 
v_head_953_ = lean_ctor_get(v_a_950_, 0);
v_tail_954_ = lean_ctor_get(v_a_950_, 1);
v_isSharedCheck_964_ = !lean_is_exclusive(v_a_950_);
if (v_isSharedCheck_964_ == 0)
{
v___x_956_ = v_a_950_;
v_isShared_957_ = v_isSharedCheck_964_;
goto v_resetjp_955_;
}
else
{
lean_inc(v_tail_954_);
lean_inc(v_head_953_);
lean_dec(v_a_950_);
v___x_956_ = lean_box(0);
v_isShared_957_ = v_isSharedCheck_964_;
goto v_resetjp_955_;
}
v_resetjp_955_:
{
uint8_t v___x_958_; 
lean_inc(v_head_953_);
v___x_958_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric(v_head_953_);
if (v___x_958_ == 0)
{
lean_object* v___x_960_; 
if (v_isShared_957_ == 0)
{
lean_ctor_set(v___x_956_, 1, v_a_951_);
v___x_960_ = v___x_956_;
goto v_reusejp_959_;
}
else
{
lean_object* v_reuseFailAlloc_962_; 
v_reuseFailAlloc_962_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_962_, 0, v_head_953_);
lean_ctor_set(v_reuseFailAlloc_962_, 1, v_a_951_);
v___x_960_ = v_reuseFailAlloc_962_;
goto v_reusejp_959_;
}
v_reusejp_959_:
{
v_a_950_ = v_tail_954_;
v_a_951_ = v___x_960_;
goto _start;
}
}
else
{
lean_del_object(v___x_956_);
lean_dec(v_head_953_);
v_a_950_ = v_tail_954_;
goto _start;
}
}
}
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted___closed__0(void){
_start:
{
lean_object* v___x_965_; lean_object* v___x_966_; lean_object* v___x_967_; 
v___x_965_ = lean_box(0);
v___x_966_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog));
v___x_967_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_deleted_spec__0(v___x_966_, v___x_965_);
return v___x_967_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted(void){
_start:
{
lean_object* v___x_968_; 
v___x_968_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted___closed__0);
return v___x_968_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_neighborsAt_spec__0(lean_object* v_e_970_, lean_object* v_a_971_, lean_object* v_a_972_){
_start:
{
if (lean_obj_tag(v_a_971_) == 0)
{
lean_object* v___x_973_; 
v___x_973_ = l_List_reverse___redArg(v_a_972_);
return v___x_973_;
}
else
{
lean_object* v_head_974_; lean_object* v_tail_975_; lean_object* v___x_977_; uint8_t v_isShared_978_; uint8_t v_isSharedCheck_989_; 
v_head_974_ = lean_ctor_get(v_a_971_, 0);
v_tail_975_ = lean_ctor_get(v_a_971_, 1);
v_isSharedCheck_989_ = !lean_is_exclusive(v_a_971_);
if (v_isSharedCheck_989_ == 0)
{
v___x_977_ = v_a_971_;
v_isShared_978_ = v_isSharedCheck_989_;
goto v_resetjp_976_;
}
else
{
lean_inc(v_tail_975_);
lean_inc(v_head_974_);
lean_dec(v_a_971_);
v___x_977_ = lean_box(0);
v_isShared_978_ = v_isSharedCheck_989_;
goto v_resetjp_976_;
}
v_resetjp_976_:
{
lean_object* v___x_979_; uint8_t v___x_980_; 
v___x_979_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchor));
v___x_980_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameSupport(v_head_974_, v___x_979_);
if (v___x_980_ == 0)
{
lean_object* v___x_981_; uint8_t v___x_982_; 
v___x_981_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_exchangeDistance(v___x_979_, v_head_974_);
v___x_982_ = lean_nat_dec_eq(v___x_981_, v_e_970_);
lean_dec(v___x_981_);
if (v___x_982_ == 0)
{
lean_del_object(v___x_977_);
lean_dec(v_head_974_);
v_a_971_ = v_tail_975_;
goto _start;
}
else
{
lean_object* v___x_985_; 
if (v_isShared_978_ == 0)
{
lean_ctor_set(v___x_977_, 1, v_a_972_);
v___x_985_ = v___x_977_;
goto v_reusejp_984_;
}
else
{
lean_object* v_reuseFailAlloc_987_; 
v_reuseFailAlloc_987_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_987_, 0, v_head_974_);
lean_ctor_set(v_reuseFailAlloc_987_, 1, v_a_972_);
v___x_985_ = v_reuseFailAlloc_987_;
goto v_reusejp_984_;
}
v_reusejp_984_:
{
v_a_971_ = v_tail_975_;
v_a_972_ = v___x_985_;
goto _start;
}
}
}
else
{
lean_del_object(v___x_977_);
lean_dec(v_head_974_);
v_a_971_ = v_tail_975_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_neighborsAt_spec__0___boxed(lean_object* v_e_990_, lean_object* v_a_991_, lean_object* v_a_992_){
_start:
{
lean_object* v_res_993_; 
v_res_993_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_neighborsAt_spec__0(v_e_990_, v_a_991_, v_a_992_);
lean_dec(v_e_990_);
return v_res_993_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_neighborsAt(lean_object* v_e_994_){
_start:
{
lean_object* v___x_995_; lean_object* v___x_996_; lean_object* v___x_997_; 
v___x_995_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected));
v___x_996_ = lean_box(0);
v___x_997_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_neighborsAt_spec__0(v_e_994_, v___x_995_, v___x_996_);
return v___x_997_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_neighborsAt___boxed(lean_object* v_e_998_){
_start:
{
lean_object* v_res_999_; 
v_res_999_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_neighborsAt(v_e_998_);
lean_dec(v_e_998_);
return v_res_999_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rootedDegree(lean_object* v_e_1000_){
_start:
{
lean_object* v___x_1001_; lean_object* v___x_1002_; 
v___x_1001_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_neighborsAt(v_e_1000_);
v___x_1002_ = l_List_lengthTR___redArg(v___x_1001_);
lean_dec(v___x_1001_);
return v___x_1002_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rootedDegree___boxed(lean_object* v_e_1003_){
_start:
{
lean_object* v_res_1004_; 
v_res_1004_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rootedDegree(v_e_1003_);
lean_dec(v_e_1003_);
return v_res_1004_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__0(lean_object* v_x_1005_, lean_object* v_x_1006_){
_start:
{
if (lean_obj_tag(v_x_1006_) == 0)
{
uint8_t v___x_1007_; 
v___x_1007_ = 1;
return v___x_1007_;
}
else
{
lean_object* v_head_1008_; lean_object* v_tail_1009_; uint8_t v___x_1010_; 
v_head_1008_ = lean_ctor_get(v_x_1006_, 0);
v_tail_1009_ = lean_ctor_get(v_x_1006_, 1);
v___x_1010_ = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(v_x_1005_, v_head_1008_);
if (v___x_1010_ == 0)
{
return v___x_1010_;
}
else
{
v_x_1006_ = v_tail_1009_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__0___boxed(lean_object* v_x_1012_, lean_object* v_x_1013_){
_start:
{
uint8_t v_res_1014_; lean_object* v_r_1015_; 
v_res_1014_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__0(v_x_1012_, v_x_1013_);
lean_dec(v_x_1013_);
lean_dec(v_x_1012_);
v_r_1015_ = lean_box(v_res_1014_);
return v_r_1015_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__1(lean_object* v_a_1016_, lean_object* v_a_1017_){
_start:
{
if (lean_obj_tag(v_a_1016_) == 0)
{
lean_object* v___x_1018_; 
v___x_1018_ = l_List_reverse___redArg(v_a_1017_);
return v___x_1018_;
}
else
{
lean_object* v_head_1019_; lean_object* v_tail_1020_; lean_object* v___x_1022_; uint8_t v_isShared_1023_; uint8_t v_isSharedCheck_1031_; 
v_head_1019_ = lean_ctor_get(v_a_1016_, 0);
v_tail_1020_ = lean_ctor_get(v_a_1016_, 1);
v_isSharedCheck_1031_ = !lean_is_exclusive(v_a_1016_);
if (v_isSharedCheck_1031_ == 0)
{
v___x_1022_ = v_a_1016_;
v_isShared_1023_ = v_isSharedCheck_1031_;
goto v_resetjp_1021_;
}
else
{
lean_inc(v_tail_1020_);
lean_inc(v_head_1019_);
lean_dec(v_a_1016_);
v___x_1022_ = lean_box(0);
v_isShared_1023_ = v_isSharedCheck_1031_;
goto v_resetjp_1021_;
}
v_resetjp_1021_:
{
lean_object* v___x_1024_; uint8_t v___x_1025_; 
v___x_1024_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected));
v___x_1025_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__0(v_head_1019_, v___x_1024_);
if (v___x_1025_ == 0)
{
lean_del_object(v___x_1022_);
lean_dec(v_head_1019_);
v_a_1016_ = v_tail_1020_;
goto _start;
}
else
{
lean_object* v___x_1028_; 
if (v_isShared_1023_ == 0)
{
lean_ctor_set(v___x_1022_, 1, v_a_1017_);
v___x_1028_ = v___x_1022_;
goto v_reusejp_1027_;
}
else
{
lean_object* v_reuseFailAlloc_1030_; 
v_reuseFailAlloc_1030_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_1030_, 0, v_head_1019_);
lean_ctor_set(v_reuseFailAlloc_1030_, 1, v_a_1017_);
v___x_1028_ = v_reuseFailAlloc_1030_;
goto v_reusejp_1027_;
}
v_reusejp_1027_:
{
v_a_1016_ = v_tail_1020_;
v_a_1017_ = v___x_1028_;
goto _start;
}
}
}
}
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore___closed__0(void){
_start:
{
lean_object* v___x_1032_; lean_object* v___x_1033_; lean_object* v___x_1034_; 
v___x_1032_ = lean_box(0);
v___x_1033_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchor));
v___x_1034_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__1(v___x_1033_, v___x_1032_);
return v___x_1034_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore(void){
_start:
{
lean_object* v___x_1035_; 
v___x_1035_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore___closed__0);
return v___x_1035_;
}
}
static lean_object* _init_lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0___closed__0(void){
_start:
{
lean_object* v___x_1036_; lean_object* v___x_1037_; 
v___x_1036_ = lean_unsigned_to_nat(6u);
v___x_1037_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_neighborsAt(v___x_1036_);
return v___x_1037_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0(lean_object* v_a_1038_, lean_object* v_a_1039_){
_start:
{
if (lean_obj_tag(v_a_1038_) == 0)
{
lean_object* v___x_1040_; 
v___x_1040_ = l_List_reverse___redArg(v_a_1039_);
return v___x_1040_;
}
else
{
lean_object* v_head_1041_; lean_object* v_tail_1042_; lean_object* v___x_1044_; uint8_t v_isShared_1045_; uint8_t v_isSharedCheck_1053_; 
v_head_1041_ = lean_ctor_get(v_a_1038_, 0);
v_tail_1042_ = lean_ctor_get(v_a_1038_, 1);
v_isSharedCheck_1053_ = !lean_is_exclusive(v_a_1038_);
if (v_isSharedCheck_1053_ == 0)
{
v___x_1044_ = v_a_1038_;
v_isShared_1045_ = v_isSharedCheck_1053_;
goto v_resetjp_1043_;
}
else
{
lean_inc(v_tail_1042_);
lean_inc(v_head_1041_);
lean_dec(v_a_1038_);
v___x_1044_ = lean_box(0);
v_isShared_1045_ = v_isSharedCheck_1053_;
goto v_resetjp_1043_;
}
v_resetjp_1043_:
{
lean_object* v___x_1046_; uint8_t v___x_1047_; 
v___x_1046_ = lean_obj_once(&lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0___closed__0, &lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0___closed__0_once, _init_lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0___closed__0);
v___x_1047_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualCommonCore_spec__0(v_head_1041_, v___x_1046_);
if (v___x_1047_ == 0)
{
lean_del_object(v___x_1044_);
lean_dec(v_head_1041_);
v_a_1038_ = v_tail_1042_;
goto _start;
}
else
{
lean_object* v___x_1050_; 
if (v_isShared_1045_ == 0)
{
lean_ctor_set(v___x_1044_, 1, v_a_1039_);
v___x_1050_ = v___x_1044_;
goto v_reusejp_1049_;
}
else
{
lean_object* v_reuseFailAlloc_1052_; 
v_reuseFailAlloc_1052_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v_reuseFailAlloc_1052_, 0, v_head_1041_);
lean_ctor_set(v_reuseFailAlloc_1052_, 1, v_a_1039_);
v___x_1050_ = v_reuseFailAlloc_1052_;
goto v_reusejp_1049_;
}
v_reusejp_1049_:
{
v_a_1038_ = v_tail_1042_;
v_a_1039_ = v___x_1050_;
goto _start;
}
}
}
}
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore___closed__0(void){
_start:
{
lean_object* v___x_1054_; lean_object* v___x_1055_; lean_object* v___x_1056_; 
v___x_1054_ = lean_box(0);
v___x_1055_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchor));
v___x_1056_ = lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0(v___x_1055_, v___x_1054_);
return v___x_1056_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore(void){
_start:
{
lean_object* v___x_1057_; 
v___x_1057_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore___closed__0);
return v___x_1057_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck_spec__0(lean_object* v_x_1058_){
_start:
{
if (lean_obj_tag(v_x_1058_) == 0)
{
uint8_t v___x_1059_; 
v___x_1059_ = 1;
return v___x_1059_;
}
else
{
lean_object* v_head_1060_; lean_object* v_tail_1061_; lean_object* v___x_1062_; lean_object* v___x_1063_; lean_object* v___x_1064_; uint8_t v___x_1065_; 
v_head_1060_ = lean_ctor_get(v_x_1058_, 0);
v_tail_1061_ = lean_ctor_get(v_x_1058_, 1);
v___x_1062_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domain(v_head_1060_);
v___x_1063_ = lean_unsigned_to_nat(235u);
v___x_1064_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_powMod(v___x_1063_, v_head_1060_);
v___x_1065_ = lean_nat_dec_eq(v___x_1062_, v___x_1064_);
lean_dec(v___x_1064_);
lean_dec(v___x_1062_);
if (v___x_1065_ == 0)
{
return v___x_1065_;
}
else
{
v_x_1058_ = v_tail_1061_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck_spec__0___boxed(lean_object* v_x_1067_){
_start:
{
uint8_t v_res_1068_; lean_object* v_r_1069_; 
v_res_1068_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck_spec__0(v_x_1067_);
lean_dec(v_x_1067_);
v_r_1069_ = lean_box(v_res_1068_);
return v_r_1069_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck___closed__0(void){
_start:
{
lean_object* v___x_1070_; uint8_t v___x_1071_; 
v___x_1070_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices;
v___x_1071_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck_spec__0(v___x_1070_);
return v___x_1071_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck(void){
_start:
{
uint8_t v___x_1072_; 
v___x_1072_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck___closed__0);
return v___x_1072_;
}
}
static lean_object* _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__0(void){
_start:
{
lean_object* v___x_1073_; lean_object* v___x_1074_; lean_object* v___x_1075_; 
v___x_1073_ = lean_unsigned_to_nat(20u);
v___x_1074_ = lean_unsigned_to_nat(235u);
v___x_1075_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_powMod(v___x_1074_, v___x_1073_);
return v___x_1075_;
}
}
static uint8_t _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__1(void){
_start:
{
lean_object* v___x_1076_; lean_object* v___x_1077_; uint8_t v___x_1078_; 
v___x_1076_ = lean_unsigned_to_nat(1u);
v___x_1077_ = lean_obj_once(&lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__0, &lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__0_once, _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__0);
v___x_1078_ = lean_nat_dec_eq(v___x_1077_, v___x_1076_);
return v___x_1078_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0(lean_object* v_x_1079_){
_start:
{
if (lean_obj_tag(v_x_1079_) == 0)
{
uint8_t v___x_1080_; 
v___x_1080_ = 1;
return v___x_1080_;
}
else
{
lean_object* v_head_1081_; lean_object* v_tail_1082_; lean_object* v___x_1083_; lean_object* v___x_1084_; lean_object* v___x_1085_; lean_object* v___x_1086_; uint8_t v___x_1087_; 
v_head_1081_ = lean_ctor_get(v_x_1079_, 0);
v_tail_1082_ = lean_ctor_get(v_x_1079_, 1);
v___x_1083_ = lean_unsigned_to_nat(1u);
v___x_1084_ = lean_unsigned_to_nat(235u);
v___x_1085_ = lean_nat_add(v_head_1081_, v___x_1083_);
v___x_1086_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_powMod(v___x_1084_, v___x_1085_);
lean_dec(v___x_1085_);
v___x_1087_ = lean_nat_dec_eq(v___x_1086_, v___x_1083_);
lean_dec(v___x_1086_);
if (v___x_1087_ == 0)
{
uint8_t v___x_1088_; 
v___x_1088_ = lean_uint8_once(&lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__1, &lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__1_once, _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__1);
if (v___x_1088_ == 0)
{
return v___x_1088_;
}
else
{
v_x_1079_ = v_tail_1082_;
goto _start;
}
}
else
{
uint8_t v___x_1090_; 
v___x_1090_ = 0;
return v___x_1090_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___boxed(lean_object* v_x_1091_){
_start:
{
uint8_t v_res_1092_; lean_object* v_r_1093_; 
v_res_1092_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0(v_x_1091_);
lean_dec(v_x_1091_);
v_r_1093_ = lean_box(v_res_1092_);
return v_r_1093_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck___closed__0(void){
_start:
{
lean_object* v___x_1094_; uint8_t v___x_1095_; 
v___x_1094_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric___closed__0);
v___x_1095_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0(v___x_1094_);
return v___x_1095_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck(void){
_start:
{
uint8_t v___x_1096_; 
v___x_1096_ = lean_uint8_once(&lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__1, &lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__1_once, _init_lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck_spec__0___closed__1);
if (v___x_1096_ == 0)
{
return v___x_1096_;
}
else
{
uint8_t v___x_1097_; 
v___x_1097_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck___closed__0);
return v___x_1097_;
}
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__0(void){
_start:
{
lean_object* v___x_1098_; lean_object* v___x_1099_; lean_object* v___x_1100_; 
v___x_1098_ = lean_box(0);
v___x_1099_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices;
v___x_1100_ = lp_m31QRootedShell_List_mapTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_prefix1_spec__0(v___x_1099_, v___x_1098_);
return v___x_1100_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__1(void){
_start:
{
lean_object* v___x_1101_; uint8_t v___x_1102_; 
v___x_1101_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__0);
v___x_1102_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicates(v___x_1101_);
return v___x_1102_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck(void){
_start:
{
uint8_t v___x_1103_; 
v___x_1103_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__1, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__1_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck___closed__1);
return v___x_1103_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__0(lean_object* v_x_1104_){
_start:
{
if (lean_obj_tag(v_x_1104_) == 0)
{
uint8_t v___x_1105_; 
v___x_1105_ = 1;
return v___x_1105_;
}
else
{
lean_object* v_head_1106_; lean_object* v_tail_1107_; lean_object* v___x_1108_; uint8_t v___x_1109_; 
v_head_1106_ = lean_ctor_get(v_x_1104_, 0);
v_tail_1107_ = lean_ctor_get(v_x_1104_, 1);
v___x_1108_ = lean_unsigned_to_nat(20u);
v___x_1109_ = lean_nat_dec_lt(v_head_1106_, v___x_1108_);
if (v___x_1109_ == 0)
{
return v___x_1109_;
}
else
{
v_x_1104_ = v_tail_1107_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__0___boxed(lean_object* v_x_1111_){
_start:
{
uint8_t v_res_1112_; lean_object* v_r_1113_; 
v_res_1112_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__0(v_x_1111_);
lean_dec(v_x_1111_);
v_r_1113_ = lean_box(v_res_1112_);
return v_r_1113_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__1(lean_object* v_x_1114_){
_start:
{
if (lean_obj_tag(v_x_1114_) == 0)
{
uint8_t v___x_1115_; 
v___x_1115_ = 1;
return v___x_1115_;
}
else
{
lean_object* v_head_1116_; lean_object* v_tail_1117_; uint8_t v___y_1119_; lean_object* v___x_1122_; lean_object* v___x_1123_; uint8_t v___x_1124_; 
v_head_1116_ = lean_ctor_get(v_x_1114_, 0);
v_tail_1117_ = lean_ctor_get(v_x_1114_, 1);
v___x_1122_ = l_List_lengthTR___redArg(v_head_1116_);
v___x_1123_ = lean_unsigned_to_nat(10u);
v___x_1124_ = lean_nat_dec_eq(v___x_1122_, v___x_1123_);
lean_dec(v___x_1122_);
if (v___x_1124_ == 0)
{
v___y_1119_ = v___x_1124_;
goto v___jp_1118_;
}
else
{
uint8_t v___x_1125_; 
v___x_1125_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicates(v_head_1116_);
v___y_1119_ = v___x_1125_;
goto v___jp_1118_;
}
v___jp_1118_:
{
if (v___y_1119_ == 0)
{
return v___y_1119_;
}
else
{
uint8_t v___x_1120_; 
v___x_1120_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__0(v_head_1116_);
if (v___x_1120_ == 0)
{
return v___x_1120_;
}
else
{
v_x_1114_ = v_tail_1117_;
goto _start;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__1___boxed(lean_object* v_x_1126_){
_start:
{
uint8_t v_res_1127_; lean_object* v_r_1128_; 
v_res_1127_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__1(v_x_1126_);
lean_dec(v_x_1126_);
v_r_1128_ = lean_box(v_res_1127_);
return v_r_1128_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__0(void){
_start:
{
lean_object* v___x_1129_; uint8_t v___x_1130_; 
v___x_1129_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog));
v___x_1130_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_noDuplicateSupports(v___x_1129_);
return v___x_1130_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__1(void){
_start:
{
lean_object* v___x_1131_; uint8_t v___x_1132_; 
v___x_1131_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog));
v___x_1132_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck_spec__1(v___x_1131_);
return v___x_1132_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck(void){
_start:
{
uint8_t v___x_1133_; 
v___x_1133_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__0);
if (v___x_1133_ == 0)
{
return v___x_1133_;
}
else
{
uint8_t v___x_1134_; 
v___x_1134_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__1, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__1_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck___closed__1);
return v___x_1134_;
}
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck_spec__0(lean_object* v_x_1135_){
_start:
{
if (lean_obj_tag(v_x_1135_) == 0)
{
uint8_t v___x_1136_; 
v___x_1136_ = 1;
return v___x_1136_;
}
else
{
lean_object* v_head_1137_; lean_object* v_tail_1138_; uint8_t v___y_1140_; lean_object* v___x_1142_; lean_object* v___x_1143_; uint8_t v___x_1144_; 
v_head_1137_ = lean_ctor_get(v_x_1135_, 0);
lean_inc_n(v_head_1137_, 2);
v_tail_1138_ = lean_ctor_get(v_x_1135_, 1);
lean_inc(v_tail_1138_);
lean_dec_ref_known(v_x_1135_, 2);
v___x_1142_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_prefix1(v_head_1137_);
v___x_1143_ = lean_unsigned_to_nat(92u);
v___x_1144_ = lean_nat_dec_eq(v___x_1142_, v___x_1143_);
lean_dec(v___x_1142_);
if (v___x_1144_ == 0)
{
lean_dec(v_head_1137_);
v___y_1140_ = v___x_1144_;
goto v___jp_1139_;
}
else
{
lean_object* v___x_1145_; lean_object* v___x_1146_; uint8_t v___x_1147_; 
v___x_1145_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_prefix2(v_head_1137_);
v___x_1146_ = lean_unsigned_to_nat(135u);
v___x_1147_ = lean_nat_dec_eq(v___x_1145_, v___x_1146_);
lean_dec(v___x_1145_);
v___y_1140_ = v___x_1147_;
goto v___jp_1139_;
}
v___jp_1139_:
{
if (v___y_1140_ == 0)
{
lean_dec(v_tail_1138_);
return v___y_1140_;
}
else
{
v_x_1135_ = v_tail_1138_;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck_spec__0___boxed(lean_object* v_x_1148_){
_start:
{
uint8_t v_res_1149_; lean_object* v_r_1150_; 
v_res_1149_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck_spec__0(v_x_1148_);
v_r_1150_ = lean_box(v_res_1149_);
return v_r_1150_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck___closed__0(void){
_start:
{
lean_object* v___x_1151_; uint8_t v___x_1152_; 
v___x_1151_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawCatalog));
v___x_1152_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck_spec__0(v___x_1151_);
return v___x_1152_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck(void){
_start:
{
uint8_t v___x_1153_; 
v___x_1153_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck___closed__0);
return v___x_1153_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck_spec__0(lean_object* v_x_1154_){
_start:
{
if (lean_obj_tag(v_x_1154_) == 0)
{
uint8_t v___x_1155_; 
v___x_1155_ = 1;
return v___x_1155_;
}
else
{
lean_object* v_head_1156_; lean_object* v_tail_1157_; uint8_t v___x_1158_; 
v_head_1156_ = lean_ctor_get(v_x_1154_, 0);
lean_inc(v_head_1156_);
v_tail_1157_ = lean_ctor_get(v_x_1154_, 1);
lean_inc(v_tail_1157_);
lean_dec_ref_known(v_x_1154_, 2);
v___x_1158_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_dihedralGeneric(v_head_1156_);
if (v___x_1158_ == 0)
{
lean_dec(v_tail_1157_);
return v___x_1158_;
}
else
{
v_x_1154_ = v_tail_1157_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck_spec__0___boxed(lean_object* v_x_1160_){
_start:
{
uint8_t v_res_1161_; lean_object* v_r_1162_; 
v_res_1161_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck_spec__0(v_x_1160_);
v_r_1162_ = lean_box(v_res_1161_);
return v_r_1162_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck___closed__0(void){
_start:
{
lean_object* v___x_1163_; uint8_t v___x_1164_; 
v___x_1163_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected));
v___x_1164_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck_spec__0(v___x_1163_);
return v___x_1164_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck(void){
_start:
{
uint8_t v___x_1165_; 
v___x_1165_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck___closed__0);
return v___x_1165_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck_spec__0(lean_object* v_x_1166_){
_start:
{
if (lean_obj_tag(v_x_1166_) == 0)
{
uint8_t v___x_1167_; 
v___x_1167_ = 1;
return v___x_1167_;
}
else
{
lean_object* v_head_1168_; lean_object* v_tail_1169_; lean_object* v___x_1170_; uint8_t v___x_1171_; 
v_head_1168_ = lean_ctor_get(v_x_1166_, 0);
lean_inc(v_head_1168_);
v_tail_1169_ = lean_ctor_get(v_x_1166_, 1);
lean_inc(v_tail_1169_);
lean_dec_ref_known(v_x_1166_, 2);
v___x_1170_ = lean_unsigned_to_nat(17u);
v___x_1171_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_reflectionFixes(v_head_1168_, v___x_1170_);
if (v___x_1171_ == 0)
{
lean_dec(v_tail_1169_);
return v___x_1171_;
}
else
{
v_x_1166_ = v_tail_1169_;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck_spec__0___boxed(lean_object* v_x_1173_){
_start:
{
uint8_t v_res_1174_; lean_object* v_r_1175_; 
v_res_1174_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck_spec__0(v_x_1173_);
v_r_1175_ = lean_box(v_res_1174_);
return v_r_1175_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck___closed__0(void){
_start:
{
lean_object* v___x_1176_; uint8_t v___x_1177_; 
v___x_1176_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedExpected));
v___x_1177_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck_spec__0(v___x_1176_);
return v___x_1177_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck(void){
_start:
{
uint8_t v___x_1178_; 
v___x_1178_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck___closed__0);
return v___x_1178_;
}
}
LEAN_EXPORT uint8_t lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck_spec__0(lean_object* v_x_1179_){
_start:
{
if (lean_obj_tag(v_x_1179_) == 0)
{
uint8_t v___x_1180_; 
v___x_1180_ = 1;
return v___x_1180_;
}
else
{
lean_object* v_head_1181_; lean_object* v_tail_1182_; lean_object* v___x_1183_; uint8_t v___x_1184_; 
v_head_1181_ = lean_ctor_get(v_x_1179_, 0);
v_tail_1182_ = lean_ctor_get(v_x_1179_, 1);
v___x_1183_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchor));
v___x_1184_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_sameDihedralOrbit(v___x_1183_, v_head_1181_);
if (v___x_1184_ == 0)
{
v_x_1179_ = v_tail_1182_;
goto _start;
}
else
{
uint8_t v___x_1186_; 
v___x_1186_ = 0;
return v___x_1186_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck_spec__0___boxed(lean_object* v_x_1187_){
_start:
{
uint8_t v_res_1188_; lean_object* v_r_1189_; 
v_res_1188_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck_spec__0(v_x_1187_);
lean_dec(v_x_1187_);
v_r_1189_ = lean_box(v_res_1188_);
return v_r_1189_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck___closed__0(void){
_start:
{
lean_object* v___x_1190_; uint8_t v___x_1191_; 
v___x_1190_ = lean_obj_once(&lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0___closed__0, &lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0___closed__0_once, _init_lp_m31QRootedShell_List_filterTR_loop___at___00M31QRootedShell_MultiplicativeCounterexample_starCommonCore_spec__0___closed__0);
v___x_1191_ = lp_m31QRootedShell_List_all___at___00M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck_spec__0(v___x_1190_);
return v___x_1191_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck(void){
_start:
{
uint8_t v___x_1192_; 
v___x_1192_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck___closed__0);
return v___x_1192_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__0(void){
_start:
{
lean_object* v___x_1193_; lean_object* v___x_1194_; 
v___x_1193_ = lean_unsigned_to_nat(7u);
v___x_1194_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rootedDegree(v___x_1193_);
return v___x_1194_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__1(void){
_start:
{
lean_object* v___x_1195_; lean_object* v___x_1196_; uint8_t v___x_1197_; 
v___x_1195_ = lean_unsigned_to_nat(3u);
v___x_1196_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__0);
v___x_1197_ = lean_nat_dec_eq(v___x_1196_, v___x_1195_);
return v___x_1197_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__2(void){
_start:
{
lean_object* v___x_1198_; lean_object* v___x_1199_; 
v___x_1198_ = lean_unsigned_to_nat(5u);
v___x_1199_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rootedDegree(v___x_1198_);
return v___x_1199_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3(void){
_start:
{
lean_object* v___x_1200_; lean_object* v___x_1201_; 
v___x_1200_ = lean_unsigned_to_nat(6u);
v___x_1201_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rootedDegree(v___x_1200_);
return v___x_1201_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__4(void){
_start:
{
lean_object* v___x_1202_; lean_object* v___x_1203_; lean_object* v___x_1204_; 
v___x_1202_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3);
v___x_1203_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__2, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__2_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__2);
v___x_1204_ = lean_nat_add(v___x_1203_, v___x_1202_);
return v___x_1204_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__5(void){
_start:
{
lean_object* v___x_1205_; lean_object* v___x_1206_; lean_object* v___x_1207_; 
v___x_1205_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__0);
v___x_1206_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__4, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__4_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__4);
v___x_1207_ = lean_nat_add(v___x_1206_, v___x_1205_);
return v___x_1207_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__6(void){
_start:
{
lean_object* v___x_1208_; lean_object* v___x_1209_; 
v___x_1208_ = ((lean_object*)(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualExpected));
v___x_1209_ = l_List_lengthTR___redArg(v___x_1208_);
return v___x_1209_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__7(void){
_start:
{
lean_object* v___x_1210_; lean_object* v___x_1211_; lean_object* v___x_1212_; 
v___x_1210_ = lean_unsigned_to_nat(1u);
v___x_1211_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__6, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__6_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__6);
v___x_1212_ = lean_nat_sub(v___x_1211_, v___x_1210_);
return v___x_1212_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__8(void){
_start:
{
lean_object* v___x_1213_; lean_object* v___x_1214_; uint8_t v___x_1215_; 
v___x_1213_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__7, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__7_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__7);
v___x_1214_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__5, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__5_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__5);
v___x_1215_ = lean_nat_dec_eq(v___x_1214_, v___x_1213_);
return v___x_1215_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__9(void){
_start:
{
lean_object* v___x_1216_; lean_object* v___x_1217_; uint8_t v___x_1218_; 
v___x_1216_ = lean_unsigned_to_nat(1u);
v___x_1217_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__2, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__2_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__2);
v___x_1218_ = lean_nat_dec_eq(v___x_1217_, v___x_1216_);
return v___x_1218_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__10(void){
_start:
{
lean_object* v___x_1219_; lean_object* v___x_1220_; uint8_t v___x_1221_; 
v___x_1219_ = lean_unsigned_to_nat(10u);
v___x_1220_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3);
v___x_1221_ = lean_nat_dec_eq(v___x_1220_, v___x_1219_);
return v___x_1221_;
}
}
static uint8_t _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck(void){
_start:
{
uint8_t v___y_1223_; uint8_t v___x_1226_; 
v___x_1226_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__9, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__9_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__9);
if (v___x_1226_ == 0)
{
v___y_1223_ = v___x_1226_;
goto v___jp_1222_;
}
else
{
uint8_t v___x_1227_; 
v___x_1227_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__10, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__10_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__10);
v___y_1223_ = v___x_1227_;
goto v___jp_1222_;
}
v___jp_1222_:
{
if (v___y_1223_ == 0)
{
return v___y_1223_;
}
else
{
uint8_t v___x_1224_; 
v___x_1224_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__1, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__1_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__1);
if (v___x_1224_ == 0)
{
return v___x_1224_;
}
else
{
uint8_t v___x_1225_; 
v___x_1225_ = lean_uint8_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__8, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__8_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__8);
return v___x_1225_;
}
}
}
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_q(void){
_start:
{
lean_object* v___x_1228_; 
v___x_1228_ = lean_unsigned_to_nat(58081u);
return v___x_1228_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_choose(lean_object* v_x_1229_, lean_object* v_x_1230_){
_start:
{
lean_object* v_zero_1231_; uint8_t v_isZero_1232_; 
v_zero_1231_ = lean_unsigned_to_nat(0u);
v_isZero_1232_ = lean_nat_dec_eq(v_x_1230_, v_zero_1231_);
if (v_isZero_1232_ == 1)
{
lean_object* v___x_1233_; 
v___x_1233_ = lean_unsigned_to_nat(1u);
return v___x_1233_;
}
else
{
uint8_t v_isZero_1234_; 
v_isZero_1234_ = lean_nat_dec_eq(v_x_1229_, v_zero_1231_);
if (v_isZero_1234_ == 1)
{
return v_zero_1231_;
}
else
{
lean_object* v_one_1235_; lean_object* v_n_1236_; lean_object* v_n_1237_; lean_object* v___x_1238_; lean_object* v___x_1239_; lean_object* v___x_1240_; lean_object* v___x_1241_; 
v_one_1235_ = lean_unsigned_to_nat(1u);
v_n_1236_ = lean_nat_sub(v_x_1230_, v_one_1235_);
v_n_1237_ = lean_nat_sub(v_x_1229_, v_one_1235_);
v___x_1238_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_choose(v_n_1237_, v_n_1236_);
v___x_1239_ = lean_nat_add(v_n_1236_, v_one_1235_);
lean_dec(v_n_1236_);
v___x_1240_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_choose(v_n_1237_, v___x_1239_);
lean_dec(v___x_1239_);
lean_dec(v_n_1237_);
v___x_1241_ = lean_nat_add(v___x_1238_, v___x_1240_);
lean_dec(v___x_1240_);
lean_dec(v___x_1238_);
return v___x_1241_;
}
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_choose___boxed(lean_object* v_x_1242_, lean_object* v_x_1243_){
_start:
{
lean_object* v_res_1244_; 
v_res_1244_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_choose(v_x_1242_, v_x_1243_);
lean_dec(v_x_1243_);
lean_dec(v_x_1242_);
return v_res_1244_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__0(void){
_start:
{
lean_object* v___x_1245_; lean_object* v___x_1246_; lean_object* v___x_1247_; 
v___x_1245_ = lean_unsigned_to_nat(6u);
v___x_1246_ = lean_unsigned_to_nat(10u);
v___x_1247_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_choose(v___x_1246_, v___x_1245_);
return v___x_1247_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__1(void){
_start:
{
lean_object* v___x_1248_; lean_object* v___x_1249_; 
v___x_1248_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__0);
v___x_1249_ = lean_nat_mul(v___x_1248_, v___x_1248_);
return v___x_1249_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6(void){
_start:
{
lean_object* v___x_1250_; 
v___x_1250_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__1, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__1_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6___closed__1);
return v___x_1250_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__0(void){
_start:
{
lean_object* v___x_1251_; lean_object* v___x_1252_; lean_object* v___x_1253_; 
v___x_1251_ = lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6;
v___x_1252_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck___closed__3);
v___x_1253_ = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(v___x_1253_, 0, v___x_1252_);
lean_ctor_set(v___x_1253_, 1, v___x_1251_);
return v___x_1253_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__1(void){
_start:
{
lean_object* v___x_1254_; lean_object* v___x_1255_; lean_object* v___x_1256_; 
v___x_1254_ = lean_box(0);
v___x_1255_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__0, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__0_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__0);
v___x_1256_ = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(v___x_1256_, 0, v___x_1255_);
lean_ctor_set(v___x_1256_, 1, v___x_1254_);
return v___x_1256_;
}
}
static lean_object* _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows(void){
_start:
{
lean_object* v___x_1257_; 
v___x_1257_ = lean_obj_once(&lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__1, &lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__1_once, _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows___closed__1);
return v___x_1257_;
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell___private_M31QRootedShell_MultiplicativeCounterexample_0__M31QRootedShell_degreeSum_match__1_splitter___redArg(lean_object* v_x_1258_, lean_object* v_h__1_1259_, lean_object* v_h__2_1260_){
_start:
{
if (lean_obj_tag(v_x_1258_) == 0)
{
lean_object* v___x_1261_; lean_object* v___x_1262_; 
lean_dec(v_h__2_1260_);
v___x_1261_ = lean_box(0);
v___x_1262_ = lean_apply_1(v_h__1_1259_, v___x_1261_);
return v___x_1262_;
}
else
{
lean_object* v_head_1263_; lean_object* v_tail_1264_; lean_object* v___x_1265_; 
lean_dec(v_h__1_1259_);
v_head_1263_ = lean_ctor_get(v_x_1258_, 0);
lean_inc(v_head_1263_);
v_tail_1264_ = lean_ctor_get(v_x_1258_, 1);
lean_inc(v_tail_1264_);
lean_dec_ref_known(v_x_1258_, 2);
v___x_1265_ = lean_apply_2(v_h__2_1260_, v_head_1263_, v_tail_1264_);
return v___x_1265_;
}
}
}
LEAN_EXPORT lean_object* lp_m31QRootedShell___private_M31QRootedShell_MultiplicativeCounterexample_0__M31QRootedShell_degreeSum_match__1_splitter(lean_object* v_motive_1266_, lean_object* v_x_1267_, lean_object* v_h__1_1268_, lean_object* v_h__2_1269_){
_start:
{
if (lean_obj_tag(v_x_1267_) == 0)
{
lean_object* v___x_1270_; lean_object* v___x_1271_; 
lean_dec(v_h__2_1269_);
v___x_1270_ = lean_box(0);
v___x_1271_ = lean_apply_1(v_h__1_1268_, v___x_1270_);
return v___x_1271_;
}
else
{
lean_object* v_head_1272_; lean_object* v_tail_1273_; lean_object* v___x_1274_; 
lean_dec(v_h__1_1268_);
v_head_1272_ = lean_ctor_get(v_x_1267_, 0);
lean_inc(v_head_1272_);
v_tail_1273_ = lean_ctor_get(v_x_1267_, 1);
lean_inc(v_tail_1273_);
lean_dec_ref_known(v_x_1267_, 2);
v___x_1274_ = lean_apply_2(v_h__2_1269_, v_head_1272_, v_tail_1273_);
return v___x_1274_;
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_m31QRootedShell_M31QRootedShell_Envelope(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample(uint8_t builtin) {
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
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_p = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_p();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_p);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_n = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_n();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_n);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_m = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_m();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_m);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_w = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_w();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_w);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generator = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generator();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generator);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_indices);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residual);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deleted);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualCommonCore);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_starCommonCore);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainPowerCheck();
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_generatorExactOrderCheck();
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_domainDistinctCheck();
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_supportShapeCheck();
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_rawPrefixCheck();
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_residualGenericCheck();
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_deletedReflectionCheck();
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_anchorNeighborOrbitCheck();
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_distanceHistogramCheck();
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_q = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_q();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_q);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6 = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_ambientShell6);
lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows = _init_lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows();
lean_mark_persistent(lp_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample_counterexampleRows);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
