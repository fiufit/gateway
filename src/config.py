import os

USERS_SERVICE_URL = os.getenv(
    "USERS_SERVICE_URL",
    "localhost",
)
APP_HOST = os.getenv("HOST", "localhost")
APP_PORT = int(os.getenv("PORT", "8000"))
FIREBASE_ADMIN = os.getenv(
    "FIREBASE_ADMIN",
    "firebase.json",
)
