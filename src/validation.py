import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from fastapi import HTTPException
from .config import NEEDS_AUTH, FIREBASE_ADMIN


cred = credentials.Certificate(FIREBASE_ADMIN)
firebase_admin.initialize_app(cred)


async def validate_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token, check_revoked=True)
        return decoded_token
    except:
        raise HTTPException(status_code=401, detail="Invalid authorization token")


async def get_validated_user(auth, path):
    if path not in NEEDS_AUTH: return None
    if not auth: raise HTTPException(status_code=401, detail="Authorization header is missing")
    try:
        scheme, token = auth.split()
    except: raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    if scheme.lower() != "bearer": raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    user = await validate_token(token)
    if not user['email_verified']: raise HTTPException(status_code=401, detail="User does not have a verified email")
    return user