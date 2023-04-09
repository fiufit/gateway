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


@router.post("/{version}/users/register")
async def register(
    request: Request,
    request_model: RegisterRequest,
    version,
):
    url = USERS_SERVICE_URL + "/" + version + "/users/register"
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


@router.get("/{version}/users/{user_id}")
async def get_user_by_uid(
    request: Request,
    version,
    user_id,
    user: dict = Depends(auth_scheme),
):
    if user["email_verified"] is False:
        raise CustomException(
            status_code=401,
            error_code=ERR_AUTHORIZATION,
            description="User does not have a verified email",
        )
    url = f"{USERS_SERVICE_URL}/{version}/users/{user_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )


@router.get("/{version}/users")
async def get_user_by_nickname(
    request: Request,
    version,
    nickname: str,
    user: dict = Depends(auth_scheme),
):
    if user["email_verified"] is False:
        raise CustomException(
            status_code=401,
            error_code=ERR_AUTHORIZATION,
            description="User does not have a verified email",
        )
    url = f"{USERS_SERVICE_URL}/{version}/users?nickname={nickname}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )
