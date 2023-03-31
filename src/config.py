import os

REGISTER_PATH = os.getenv("REGISTER_PATH")
FINISH_REGISTER_PATH = os.getenv("FINISH_REGISTER_PATH")
APP_HOST = os.getenv("HOST")
APP_PORT = int(os.getenv("PORT"))
FIREBASE_ADMIN = os.getenv("FIREBASE_SDK_JSON_PATH")

#Endpoints que necesitan validar jwt y mail verificado
NEEDS_AUTH = ["/users/finish_register"]
