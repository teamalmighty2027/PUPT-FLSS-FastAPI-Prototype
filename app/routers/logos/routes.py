from fastapi import APIRouter
from . import handlers

router = APIRouter(
    prefix="/logos",
)

# Logos Routes

#   Route::get('/', [LogoController::class, 'index']);
#   Route::post('/upload', [LogoController::class, 'upload']);
#   Route::get('/image/{type}', [LogoController::class, 'getImage'])->where('type', 'university|government');
#   Route::get('/details/{type}', [LogoController::class, 'show'])->where('type', 'university|government');
#   Route::delete('/{type}', [LogoController::class, 'delete'])->where('type', 'university|government');