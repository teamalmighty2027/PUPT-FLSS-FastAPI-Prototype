from fastapi import APIRouter
from . import handlers

router = APIRouter()

# Scheduling
# 
# Route::get('/populate-schedules', [ScheduleController::class, 'populateSchedules']);
# Route::post('/assign-schedule', [ScheduleController::class, 'assignSchedule']);
# Route::post('/duplicate-course', [ScheduleController::class, 'duplicateCourse']);
# Route::delete('/remove-duplicate-course', [ScheduleController::class, 'removeDuplicateCourse']);
# Route::get('/get-active-faculty', [FacultyController::class, 'getFacultyDetails']);
# Route::get('/get-available-rooms', [RoomController::class, 'getAllRooms']);
# Route::post('/toggle-all-schedule', [ScheduleController::class, 'toggleAllSchedules']);
# Route::post('/toggle-single-schedule', [ScheduleController::class, 'toggleSingleSchedule']);