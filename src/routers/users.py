from fastapi import (
    APIRouter,
    Request,
    Depends,
)
from config import (
    USERS_SERVICE_URL,
)
from auth.jwt_bearer import (
    JWTBearer,
)
from auth.user_jwt_bearer import UserJWTBearer
from register_request import (
    RegisterRequest,
    FinishRegisterRequest,
)
from request import (
    make_request,
)


router = APIRouter()
user_auth_scheme = UserJWTBearer()
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
    user: dict = Depends(user_auth_scheme),
):
    print(user)
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
    _: dict = Depends(auth_scheme),
):
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
    _: dict = Depends(auth_scheme),
):
    url = f"{USERS_SERVICE_URL}/{version}/users?nickname={nickname}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )
