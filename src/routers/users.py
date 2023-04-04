from fastapi import (
    APIRouter,
    Request,
    Depends,
)
from errors import (
    CustomException,
    ERR_AUTHORIZATION,
)
from config import (
    USERS_SERVICE_URL,
)
from auth.jwt_bearer import (
    JWTBearer,
)
from register_request import (
    RegisterRequest,
    FinishRegisterRequest,
)
from request import (
    make_request,
)


router = APIRouter()
auth_scheme = JWTBearer()


@router.post("/{version}/register")
async def register(
    request: Request,
    request_model: RegisterRequest,
    version,
):
    url = USERS_SERVICE_URL + "/" + version + "/register"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {**request_model.dict()},
    )


@router.post("/{version}/users/finish-register")
async def finish_register(
    request: Request,
    request_model: FinishRegisterRequest,
    version,
    user: dict = Depends(auth_scheme),
):
    if user["email_verified"] is False:
        raise CustomException(
            status_code=401,
            error_code=ERR_AUTHORIZATION,
            description="User does not have a verified email",
        )
    uid = user["uid"]
    url = f"{USERS_SERVICE_URL}/{version}/users/{uid}/finish-register"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {**request_model.dict()},
    )
