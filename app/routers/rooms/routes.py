from fastapi import APIRouter
from . import handlers

router = APIRouter()

# Rooms Routes

# Route::get('/rooms', [RoomController::class, 'getRooms']);
# Route::post('/addRoom', [RoomController::class, 'addRoom']);
# Route::put('/rooms/{room_id}', [RoomController::class, 'updateRoom']);
# Route::delete('/rooms/{room_id}', [RoomController::class, 'deleteRoom']);