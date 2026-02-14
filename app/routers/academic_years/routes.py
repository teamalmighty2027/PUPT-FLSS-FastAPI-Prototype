from fastapi import APIRouter
from . import handlers

router = APIRouter()

# Academic Year Routes

# Route::get('/get-academic-years', [AcademicYearController::class, 'getAcademicYears']);
# Route::post('/add-academic-year', [AcademicYearController::class, 'addAcademicYear']);
# Route::delete('/delete-academic-year', [AcademicYearController::class, 'deleteAcademicYear']);
# Route::get('/get-active-year-semester', [AcademicYearController::class, 'getActiveAcademicYearAndSemester']);
# Route::post('/set-active-year-semester', [AcademicYearController::class, 'setActiveAcademicYearAndSemester']);
# Route::post('/fetch-ay-prog-details', [AcademicYearController::class, 'getProgramDetailsByAcademicYear']);
# Route::get('/active-year-levels-curricula', [AcademicYearController::class, 'getActiveYearLevelsCurricula']);
# Route::post('/update-yr-lvl-curricula', [AcademicYearController::class, 'updateYearLevelCurricula']);
# Route::post('/update-sections', [AcademicYearController::class, 'updateSections']);
# Route::delete('/remove-program', [AcademicYearController::class, 'removeProgramFromAcademicYear']);
# Route::get('/offered-courses-sem', [AcademicYearController::class, 'getOfferedCoursesBySem']);