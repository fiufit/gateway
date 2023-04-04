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
)
from auth.validation import (
    initialize_firebase_app,
)
from routers import (
    users,
)
from errors import (
    CustomException,
    handle_validation_error,
    handle_custom_exception,
)

app = FastAPI()

app.include_router(users.router)

app.add_exception_handler(RequestValidationError, handle_validation_error)
app.add_exception_handler(CustomException, handle_custom_exception)


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
