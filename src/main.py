from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.security import HTTPBearer
from fastapi.responses import JSONResponse
import uvicorn

from config import APP_HOST, APP_PORT, REGISTER_PATH, FINISH_REGISTER_PATH

from request import make_request

from register_request import RegisterRequest, FinishRegisterRequest

from validation import get_validated_user, initialize_firebase_app


app = FastAPI() 

@app.exception_handler(RequestValidationError)
def handle_validation_error(request, exc) -> JSONResponse:
    error_messages = []
    for error in exc.errors():
        field_name = error['loc']
        error_messages.append(f"{field_name}: {error['msg']}")
    message = ", ".join(error_messages)
    return JSONResponse(status_code=400,content={"error":{"code":"CODIGO_LOCO","description":f"Request validation error - {message}"}})
    

        
@app.middleware("http")
async def api_gateway(request: Request, call_next):
    authorization: str = request.headers.get("Authorization")
    try:
        path = "/".join(request.url.path.split("/")[2::])
    except:
        return JSONResponse(status_code=400, content={"error":{"code:":"CODIGO_LOCO", "description":"Could not parse path"}})
    try:
        user = await get_validated_user(authorization, path)
    except HTTPException as er:
        return JSONResponse(status_code=401, content={"error":{"code":"CODIGO_LOCO","description":er.detail}})
    if user: request.state.verified_user = user
    return await call_next(request)
    # si es necesario agregar algo ademas de lo que responde el back puedo aca


@app.post("/{version}/users/register")
async def register(request: Request,
                   request_model: RegisterRequest,
                   version):
    url = REGISTER_PATH+"/"+version+"/users/register"
    return await make_request(url, dict(request.headers), request.method, {**request_model.dict()})


@app.post("/{version}/users/finish-register")
async def finish_register(request: Request, 
                          request_model: FinishRegisterRequest,
                          version):
    uid = request.state.verified_user["uid"]
    url = FINISH_REGISTER_PATH+"/"+version+"/users/"+uid+"/finish-register"
    return await make_request(url, dict(request.headers), request.method, {**request_model.dict()})


if __name__ == '__main__':
    try:
        initialize_firebase_app()
    except:
        raise Exception("Could not initialize firebase")
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)