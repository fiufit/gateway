from fastapi import (
    APIRouter,
    Request,
    Depends,
)
from config import (
    USERS_SERVICE_URL,
)
from auth.admin_jwt_bearer import (
    AdminJWTBearer,
)
from register_request import (
    RegisterRequest,
)
from request import (
    make_request,
)


router = APIRouter()
admin_auth_scheme = AdminJWTBearer()


@router.post("/{version}/admin/register")
async def register(
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
async def login(
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
