from fastapi import APIRouter
import handlers

# Super Admin Routes
# Routes for super admin related actions

router = APIRouter()

router.include_router(
    methods=["GET"],
    prefix="/health",
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