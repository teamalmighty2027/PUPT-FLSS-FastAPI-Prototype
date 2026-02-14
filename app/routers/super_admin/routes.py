from fastapi import APIRouter
from . import handlers

# Super Admin Routes
# Routes for super admin related actions
# Requires its own super admin protection

router = APIRouter(
    prefix="/super_admin",
)

router.add_api_route(
    methods=["GET"],
    path="/health",
    endpoint=handlers.health_check,
)

# Route::get('/showAccounts', [AccountController::class, 'index']);
# Route::post('/addAccount', [AccountController::class, 'store']);
# Route::get('/accounts/{user}', [AccountController::class, 'show']);
# Route::put('/updateAccount/{user}', [AccountController::class, 'update']);
# Route::delete('/deleteAccount/{user}', [AccountController::class, 'destroy']);

# Route::get('/getAdmins', [AccountController::class, 'indexAdmins']);
# Route::post('/addAdmins', [AccountController::class, 'storeAdmin']);
# Route::put('/updateAdmins/{admin}', [AccountController::class, 'updateAdmin']);
# Route::delete('/deleteAdmins/{admin}', [AccountController::class, 'destroyAdmin']);