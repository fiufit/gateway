from fastapi import (
    FastAPI,
)
from fastapi.exceptions import (
    RequestValidationError,
)

import uvicorn

from config import (
    APP_HOST,
    APP_PORT,
    ALLOWED_ORIGINS,
)
from auth.validation import (
    initialize_firebase_app,
)
from routers import (
    users,
    trainings,
)
from errors import (
    CustomException,
    handle_validation_error,
    handle_custom_exception,
)

from fastapi.middleware.cors import CORSMiddleware

from middlewares.cors import get_origin_list
from docs import tags_metadata

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(users.router)
app.include_router(trainings.router)

app.add_exception_handler(RequestValidationError, handle_validation_error)
app.add_exception_handler(CustomException, handle_custom_exception)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_origin_list(ALLOWED_ORIGINS),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    try:
        initialize_firebase_app()
    except ValueError:
        raise Exception("Could not initialize firebase")
    uvicorn.run(
        app,
        host=APP_HOST,
        port=APP_PORT,
    )
