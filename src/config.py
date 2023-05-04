import os

USERS_SERVICE_URL = os.getenv(
    "USERS_SERVICE_URL",
    "localhost",
)
TRAININGS_SERVICE_URL = os.getenv(
    "TRAININGS_SERVICE_URL",
    "localhost",
)
APP_HOST = os.getenv("HOST", "localhost")
APP_PORT = int(os.getenv("PORT", "8000"))
FIREBASE_ADMIN = os.getenv(
    "FIREBASE_ADMIN",
    "firebase.json",
)
USERS_JWT_KEY = os.getenv(
    "USERS_JWT_PUBLIC_KEY",
)
ALLOWED_ORIGINS = [
    os.getenv("BACKOFFICE_DOMAIN"),
    os.getenv("ANDROID_APP_DOMAIN"),
]
