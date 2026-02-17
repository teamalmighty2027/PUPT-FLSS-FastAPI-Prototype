from fastapi import APIRouter
from . import handlers

router = APIRouter()

# Curriculum & Curriculum Details Routes

# Route::get('/curricula', [CurriculumController::class, 'index']);
# Route::get('/curricula/{id}', [CurriculumController::class, 'show']);
# Route::post('/addCurriculum', [CurriculumController::class, 'addCurriculum']);
# Route::post('/deleteCurriculum', [CurriculumController::class, 'deleteCurriculum']);
# Route::post('/copyCurriculum', [CurriculumController::class, 'copyCurriculum']);
# Route::put('/updateCurriculum/{id}', [CurriculumController::class, 'update']);

# Route::post('/removeProgramFromCurriculum', [CurriculumController::class, 'removeProgramFromCurriculum']);
# Route::get('/programs-by-curriculum-year/{curriculumYear}', [CurriculumController::class, 'getProgramsByCurriculumYear']);
# Route::post('/addProgramToCurriculum', [CurriculumController::class, 'addProgramToCurriculum']);

# Route::get('/curricula-details/{curriculumYear}/', [CurriculumDetailsController::class, 'getCurriculumDetails']);