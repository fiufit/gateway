from fastapi import (
    APIRouter,
    Request,
    Depends,
)
from config import (
    TRAININGS_SERVICE_URL,
)
from auth.user_jwt_bearer import (
    UserJWTBearer,
)
from auth.jwt_bearer import JWTBearer
from models.trainings.create_training_request import (
    CreateTrainingRequest,
)
from models.trainings.get_trainings import (
    GetTrainingsRequest,
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
    url = TRAININGS_SERVICE_URL + "/" + version + "/trainings"
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
    url = f"{TRAININGS_SERVICE_URL}/{version}/trainings?{params}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )
