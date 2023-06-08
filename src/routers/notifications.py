from fastapi import (
    APIRouter,
    Request,
    Depends,
)
from config import (
    NOTIFICATIONS_SERVICE_URL as NOTIFICATIONS_URL,
)

from auth.user_jwt_bearer import (
    UserJWTBearer,
)
from auth.jwt_bearer import JWTBearer
from models.notifications.create_push import CreateNotificationRequest
from models.notifications.create_subscriber import CreateSubscriberRequest
from models.notifications.update_subscriber import UpdateSubscriberRequest

from request import make_request

router = APIRouter()
user_auth_scheme = UserJWTBearer()
auth_scheme = JWTBearer()


@router.post("/{version}/notifications/push", tags=["notifications"])
async def create_push_notification(
    request: Request,
    request_model: CreateNotificationRequest,
    version,
    _: dict = Depends(auth_scheme),
):
    url = NOTIFICATIONS_URL + "/api/" + version + "/notifications/push"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {**request_model.dict()},
    )


@router.post("/{version}/notifications/subscribers", tags=["notifications"])
async def create_subscriber(
    request: Request,
    request_model: CreateSubscriberRequest,
    version,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = NOTIFICATIONS_URL + "/api/" + version + "/subscribers"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid, **request_model.dict()},
    )


@router.patch("/{version}/notifications/subscribers/{id}", tags=["notifications"])
async def update_subscriber(
    request: Request,
    request_model: UpdateSubscriberRequest,
    version,
    id,
    user: dict = Depends(user_auth_scheme),
):
    uid = user["uid"]
    url = NOTIFICATIONS_URL + "/api/" + version + "/subscribers/" + id
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {"user_id": uid, **request_model.dict()},
    )
