# Authenticaion routes

# Route::middleware('custom.ratelimit:login')->group(function () {
#     Route::post('login', [AuthController::class, 'login'])->name('login');
# });

# Route::middleware('auth:sanctum')->group(function () {
#     Route::post('logout', [AuthController::class, 'logout'])->name('logout');
#     Route::post('/change-password', [AuthController::class, 'changePassword']);
# });

# Route::post('/password/email', [PasswordResetController::class, 'sendResetLinkEmail']);
# Route::post('/password/reset', [PasswordResetController::class, 'reset']);
# Route::post('/password/verify-token', [PasswordResetController::class, 'verifyToken']);