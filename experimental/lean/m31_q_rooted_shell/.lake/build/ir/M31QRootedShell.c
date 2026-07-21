// Lean compiler output
// Module: M31QRootedShell
// Imports: public import Init public meta import Init public import M31QRootedShell.Envelope public import M31QRootedShell.Deployed public import M31QRootedShell.ToyCounterexample public import M31QRootedShell.MultiplicativeCounterexample public import M31QRootedShell.PaddingBridgeAudit
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
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_m31QRootedShell_M31QRootedShell_Envelope(uint8_t builtin);
lean_object* initialize_m31QRootedShell_M31QRootedShell_Deployed(uint8_t builtin);
lean_object* initialize_m31QRootedShell_M31QRootedShell_ToyCounterexample(uint8_t builtin);
lean_object* initialize_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample(uint8_t builtin);
lean_object* initialize_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_m31QRootedShell_M31QRootedShell(uint8_t builtin) {
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
res = initialize_m31QRootedShell_M31QRootedShell_Deployed(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_m31QRootedShell_M31QRootedShell_ToyCounterexample(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_m31QRootedShell_M31QRootedShell_MultiplicativeCounterexample(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_m31QRootedShell_M31QRootedShell_PaddingBridgeAudit(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
