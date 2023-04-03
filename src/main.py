from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import uvicorn

from config import APP_HOST, APP_PORT
from validation import initialize_firebase_app
from routers import users
from errors import CustomException, ERR_BAD_REQUEST

app = FastAPI() 
app.include_router(users.router)

'''
Handler for exceptions raised due to validations errors in the request
'''
@app.exception_handler(RequestValidationError)
def handle_validation_error(request, exc) -> JSONResponse:
    error_messages = []
    for error in exc.errors():
        field_name = error['loc']
        error_messages.append(f"{field_name}: {error['msg']}")
    message = ", ".join(error_messages)
    return JSONResponse(status_code=400,
                        content={"error":{"code":ERR_BAD_REQUEST,
                                          "description":f"Request validation error - {message}"}})
    


@app.exception_handler(CustomException)
def handle_exception(request, exc) -> JSONResponse:
    return exc.create_json_response()



if __name__ == '__main__':
    try:
        initialize_firebase_app()
    except:
        raise Exception("Could not initialize firebase")
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)