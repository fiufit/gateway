import os

REGISTER_PATH = os.getenv(
    "REGISTER_PATH",
    "localhost",
)
FINISH_REGISTER_PATH = os.getenv(
    "FINISH_REGISTER_PATH",
    "localhost",
)
APP_HOST = os.getenv("HOST", "localhost")
APP_PORT = int(os.getenv("PORT", "8000"))
FIREBASE_ADMIN = os.getenv(
    "FIREBASE_ADMIN",
    "firebase.json",
)

# Endpoints que necesitan validar jwt y mail verificado
NEEDS_AUTH = ["users/finish-register"]
