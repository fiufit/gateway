from fastapi import (
    APIRouter,
    Request,
    Depends,
)
from config import (
    METRICS_SERVICE_URL as METRICS_URL,
)

from auth.user_jwt_bearer import (
    UserJWTBearer,
)
from auth.jwt_bearer import JWTBearer
from models.metrics.create_metric import CreateMetricRequest
from models.metrics.get_metrics import GetMetricsRequest

from request import make_request

router = APIRouter()
user_auth_scheme = UserJWTBearer()
auth_scheme = JWTBearer()


@router.post("/{version}/metrics", tags=["metrics"])
async def create_metric(
    request: Request,
    request_model: CreateMetricRequest,
    version,
    _: dict = Depends(auth_scheme),
):
    url = f"{METRICS_URL}/{version}/metrics?"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {**request_model.dict()},
    )


@router.get("/{version}/metrics", tags=["metrics"])
async def get_metrics(
    request: Request,
    version,
    request_model: GetMetricsRequest = Depends(),
    _: dict = Depends(auth_scheme),
):
    params = request_model.to_query_string()
    url = f"{METRICS_URL}/{version}/metrics?{params}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        {**request_model.dict()},
    )
