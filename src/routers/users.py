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
    REGISTER_PATH,
    FINISH_REGISTER_PATH,
)
from validation import (
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
    url = REGISTER_PATH + "/" + version + "/users/register"
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
    url = f"{FINISH_REGISTER_PATH}/{version}/users/{uid}/finish-register"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {**request_model.dict()},
    )
