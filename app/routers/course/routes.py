from fastapi import APIRouter
from . import handlers

router = APIRouter()

# Course Routes

# Route::get('/courses', [CourseController::class, 'index']);
# Route::post('/addCourse', [CourseController::class, 'addCourse']);
# Route::put('/courses/{id}', [CourseController::class, 'updateCourse']);
# Route::delete('/courses/{id}', [CourseController::class, 'deleteCourse']);