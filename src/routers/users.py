from fastapi import APIRouter, Request, Depends
from config import REGISTER_PATH, FINISH_REGISTER_PATH
from fastapi.responses import JSONResponse
from validation import JWTBearer
from register_request import RegisterRequest, FinishRegisterRequest
from request import make_request


router = APIRouter()
auth_scheme = JWTBearer()



@router.post("/{version}/users/register")
async def register(request: Request,
                   request_model: RegisterRequest,
                   version):
    url = REGISTER_PATH+"/"+version+"/users/register"
    return await make_request(url, dict(request.headers), request.method, {**request_model.dict()})


@router.post("/{version}/users/finish-register")
async def finish_register(request: Request, 
                          request_model: FinishRegisterRequest,
                          version,
                          user: dict = Depends(auth_scheme)):
    if user["email_verified"] is False: return JSONResponse(status_code=401,content={"error":{"code":"CODIGO_LOCO","description":"User does not have a verified email"}})
    uid = user["uid"]
    url = FINISH_REGISTER_PATH+"/"+version+"/users/"+uid+"/finish-register"
    return await make_request(url, dict(request.headers), request.method, {**request_model.dict()})



