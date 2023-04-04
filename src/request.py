import aiohttp

from fastapi.encoders import (
    jsonable_encoder,
)
from errors import (
    CustomException,
    ERR_INTERNAL,
)


# a priori podemos dejar los headers que use por default aiohttp
# despues podemos ver si hace falta que reciba headers extras
async def make_request(
    url,
    headers,
    method,
    body,
):
    json_compatible_body = jsonable_encoder(body)
    async with aiohttp.ClientSession() as session:
        try:
            async with session.request(
                method,
                url,
                json=json_compatible_body,
            ) as response:
                response_json = await response.json()
                return response_json
        except Exception:
            raise CustomException(
                status_code=502,
                error_code=ERR_INTERNAL,
                description="Gateway failed to connect to service",
            )
