from fastapi import APIRouter
from . import handlers

router = APIRouter()

# Faculty Notification Routes

# Route::get('/faculty-notifications', [FacultyNotificationController::class, 'getFacultyNotifications']);
# Route::get('/request-notifications', [FacultyNotificationController::class, 'getRequestNotifications']);
# Route::get('/notify-faculty-deadlines-single', [EmailController::class, 'notifyFacultyBeforeDeadlineSingle']);
# Route::post('/test-faculty-notification', [EmailController::class, 'singleDeadlineNotification']);
# Route::get('/notify-global-deadline', [EmailController::class, 'notifyGlobalFacultyDeadline']);