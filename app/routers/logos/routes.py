# Logos Routes

# Route::prefix('logos')->group(function () {
#   Route::get('/', [LogoController::class, 'index']);
#   Route::post('/upload', [LogoController::class, 'upload']);
#   Route::get('/image/{type}', [LogoController::class, 'getImage'])->where('type', 'university|government');
#   Route::get('/details/{type}', [LogoController::class, 'show'])->where('type', 'university|government');
#   Route::delete('/{type}', [LogoController::class, 'delete'])->where('type', 'university|government');
# });