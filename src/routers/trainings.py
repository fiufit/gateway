from fastapi import (
    APIRouter,
    Request,
    Depends,
)
from config import (
    TRAININGS_SERVICE_URL as TRAININGS_URL,
)
from auth.user_jwt_bearer import (
    UserJWTBearer,
)
from auth.jwt_bearer import JWTBearer
from models.trainings.create_training_request import (
    CreateTrainingRequest,
    CreateExerciseRequest,
)
from models.trainings.get_trainings import (
    GetTrainingsRequest,
)
from models.trainings.update_training import (
    UpdateTrainingRequest,
)
from request import (
    make_request,
)


router = APIRouter()
user_auth_scheme = UserJWTBearer()
auth_scheme = JWTBearer()


@router.post("/{version}/trainings")
async def create_training_plan(
    request: Request,
    request_model: CreateTrainingRequest,
    version,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = TRAININGS_URL + "/" + version + "/trainings"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"trainer_id": uid, **request_model.dict()},
    )


@router.get("/{version}/trainings")
async def get_training_plans(
    request: Request,
    version,
    request_model: GetTrainingsRequest = Depends(),
    _: dict = Depends(auth_scheme),
):
    params = request_model.to_query_string()
    url = f"{TRAININGS_URL}/{version}/trainings?{params}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.patch("/{version}/trainings/{training_id}")
async def update_training_plan(
    request: Request,
    request_model: UpdateTrainingRequest,
    version,
    training_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"trainer_id": uid, **request_model.dict()},
    )


@router.get("/{version}/trainings/{training_id}/exercises/{exercise_id}")
async def get_exercise_by_id(
    request: Request,
    version,
    training_id,
    exercise_id,
    _: dict = Depends(auth_scheme),
):
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/exercises/{exercise_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.post("/{version}/trainings/{training_id}/exercises")
async def create_exercise(
    request: Request,
    request_model: CreateExerciseRequest,
    version,
    training_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/exercises"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"trainer_id": uid, **request_model.dict()},
    )


@router.delete("/{version}/trainings/{training_id}/exercises/{exercise_id}")
async def delete_exercise(
    request: Request,
    version,
    training_id,
    exercise_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/exercises/{exercise_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"trainer_id": uid},
    )


@router.patch("/{version}/trainings/{training_id}/exercises/{exercise_id}")
async def update_exercise(
    request: Request,
    request_model: CreateExerciseRequest,
    version,
    training_id,
    exercise_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/exercises/{exercise_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"trainer_id": uid, **request_model.dict()},
    )
