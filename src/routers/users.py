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
from auth.validation import validate_deleter
from auth.user_jwt_bearer import UserJWTBearer
from auth.admin_jwt_bearer import AdminJWTBearer
from models.register_request import (
    RegisterRequest,
    FinishRegisterRequest,
)
from models.update_request import UpdateUserRequest
from request import (
    make_request,
)


router = APIRouter()
user_auth_scheme = UserJWTBearer()
admin_auth_scheme = AdminJWTBearer()
auth_scheme = JWTBearer()


@router.post("/{version}/users/register")
async def user_register(
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
async def user_finish_register(
    request: Request,
    request_model: FinishRegisterRequest,
    version,
    user: dict = Depends(user_auth_scheme),
):
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


@router.post("/{version}/admin/register")
async def admin_register(
    request: Request,
    request_model: RegisterRequest,
    version,
    _: dict = Depends(admin_auth_scheme),
):
    url = USERS_SERVICE_URL + "/" + version + "/admin/register"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {**request_model.dict()},
    )


@router.post("/{version}/admin/login")
async def admin_login(
    request: Request,
    request_model: RegisterRequest,
    version,
):
    url = USERS_SERVICE_URL + "/" + version + "/admin/login"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {**request_model.dict()},
    )


@router.patch("/{version}/users")
async def update_user(
    request: Request,
    request_model: UpdateUserRequest,
    version,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = f"{USERS_SERVICE_URL}/{version}/users/{uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {**request_model.dict()},
    )


@router.delete("/{version}/users/{user_id}")
async def delete_user(
    request: Request,
    version,
    user_id,
    user: dict = Depends(auth_scheme),
):
    validate_deleter(user, user_id)
    url = f"{USERS_SERVICE_URL}/{version}/users/{user_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {},
    )
