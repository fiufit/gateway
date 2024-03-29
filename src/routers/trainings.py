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
from auth.admin_jwt_bearer import AdminJWTBearer
from auth.jwt_bearer import JWTBearer
from models.trainings.create_training_request import (
    CreateTrainingRequest,
    CreateExerciseRequest,
)
from models.trainings.create_review import CreateReviewRequest
from models.trainings.get_reviews import GetReviewsRequest
from models.trainings.get_trainings import (
    GetTrainingsRequest,
)
from models.trainings.update_training import UpdateTrainingRequest
from models.trainings.create_training_session import CreateTrainingSessionRequest
from models.trainings.get_training_sessions import GetTrainingSessionsRequest
from models.trainings.update_training_session import UpdateTrainingSessionRequest
from models.trainings.create_goal import CreateGoalRequest
from models.trainings.update_goals import UpdateGoalRequest
from models.trainings.get_goals import GetGoalsRequest
from models.pagination import Pagination
from request import (
    make_request,
)


router = APIRouter()
user_auth_scheme = UserJWTBearer()
admin_auth_scheme = AdminJWTBearer()
auth_scheme = JWTBearer()


@router.post("/{version}/trainings", tags=["trainings"])
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


@router.get("/{version}/trainings", tags=["trainings"])
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


@router.put("/{version}/trainings/{training_id}", tags=["trainings"])
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


@router.delete("/{version}/trainings/{training_id}", tags=["trainings"])
async def delete_training_plan(
    request: Request,
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
        {"trainer_id": uid},
    )


@router.get(
    "/{version}/trainings/{training_id}/exercises/{exercise_id}", tags=["trainings"]
)
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


@router.post("/{version}/trainings/{training_id}/exercises", tags=["trainings"])
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


@router.delete(
    "/{version}/trainings/{training_id}/exercises/{exercise_id}", tags=["trainings"]
)
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


@router.patch(
    "/{version}/trainings/{training_id}/exercises/{exercise_id}", tags=["trainings"]
)
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


@router.post("/{version}/trainings/{training_id}/reviews", tags=["trainings"])
async def create_review(
    request: Request,
    request_model: CreateReviewRequest,
    version,
    training_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/reviews"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid, **request_model.dict()},
    )


@router.get("/{version}/trainings/{training_id}/reviews", tags=["trainings"])
async def get_reviews(
    request: Request,
    version,
    training_id,
    request_model: GetReviewsRequest = Depends(),
    _: dict = Depends(auth_scheme),
):
    params = request_model.to_query_string()
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/reviews?{params}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.get("/{version}/trainings/{training_id}/reviews/{review_id}", tags=["trainings"])
async def get_review_by_id(
    request: Request, version, training_id, review_id, _: dict = Depends(auth_scheme)
):
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/reviews/{review_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.patch(
    "/{version}/trainings/{training_id}/reviews/{review_id}", tags=["trainings"]
)
async def update_review(
    request: Request,
    request_model: CreateReviewRequest,
    version,
    training_id,
    review_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/reviews/{review_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid, **request_model.dict()},
    )


@router.delete(
    "/{version}/trainings/{training_id}/reviews/{review_id}", tags=["trainings"]
)
async def delete_review(
    request: Request,
    version,
    training_id,
    review_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/reviews/{review_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid},
    )


@router.post("/{version}/training_sessions", tags=["trainings"])
async def create_training_session(
    request: Request,
    version,
    request_model: CreateTrainingSessionRequest = Depends(),
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    params = request_model.to_query_string()
    url = f"{TRAININGS_URL}/{version}/training_sessions?{params}&user_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.get("/{version}/training_sessions", tags=["trainings"])
async def get_training_sessions(
    request: Request,
    version,
    request_model: GetTrainingSessionsRequest = Depends(),
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    params = request_model.to_query_string()
    url = f"{TRAININGS_URL}/{version}/training_sessions?{params}&user_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.get("/{version}/training_sessions/{session_id}", tags=["trainings"])
async def get_training_session_by_id(
    request: Request, version, session_id, user: dict = Depends(user_auth_scheme)
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/training_sessions/{session_id}?requester_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.put("/{version}/training_sessions/{session_id}", tags=["trainings"])
async def update_training_session(
    request: Request,
    request_model: UpdateTrainingSessionRequest,
    version,
    session_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/training_sessions/{session_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"requester_id": uid, **request_model.dict()},
    )


@router.post("/{version}/goals", tags=["trainings"])
async def create_goal(
    request: Request,
    request_model: CreateGoalRequest,
    version,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/goals?"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid, **request_model.dict()},
    )


@router.get("/{version}/goals", tags=["trainings"])
async def get_goals(
    request: Request,
    version,
    model: GetGoalsRequest = Depends(),
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    params = model.to_query_string()
    url = f"{TRAININGS_URL}/{version}/goals?{params}&user_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.get("/{version}/goals/{goal_id}", tags=["trainings"])
async def get_goal_by_id(
    request: Request, version, goal_id, _: dict = Depends(user_auth_scheme)
):
    url = f"{TRAININGS_URL}/{version}/goals/{goal_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.patch("/{version}/goals/{goal_id}", tags=["trainings"])
async def update_goal(
    request: Request,
    request_model: UpdateGoalRequest,
    version,
    goal_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/goals/{goal_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid, **request_model.dict()},
    )


@router.delete("/{version}/goals/{goal_id}", tags=["trainings"])
async def delete_goal(
    request: Request, version, goal_id, user: dict = Depends(user_auth_scheme)
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/goals/{goal_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid},
    )


@router.get("/{version}/trainings/favorites", tags=["trainings"])
async def get_favorite_trainings(
    request: Request,
    version,
    model: Pagination = Depends(),
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    params = model.to_query_string()
    url = f"{TRAININGS_URL}/{version}/trainings/favorites?{params}&user_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.post("/{version}/trainings/{training_id}/favorites", tags=["trainings"])
async def add_favorite_training(
    request: Request,
    version,
    training_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/favorites"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid},
    )


@router.delete("/{version}/trainings/{training_id}/favorites", tags=["trainings"])
async def remove_favorite_training(
    request: Request,
    version,
    training_id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/favorites"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid},
    )


@router.post("/{version}/trainings/{training_id}/enable", tags=["trainings"])
async def enable_training_plan(
    request: Request,
    version,
    training_id,
    _: dict = Depends(admin_auth_scheme),
):
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/enable"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.delete("/{version}/trainings/{training_id}/disable", tags=["trainings"])
async def disable_training_plan(
    request: Request,
    version,
    training_id,
    _: dict = Depends(admin_auth_scheme),
):
    url = f"{TRAININGS_URL}/{version}/trainings/{training_id}/disable"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )
