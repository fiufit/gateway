import aiohttp
from fastapi import Response
from fastapi.encoders import jsonable_encoder
import json

# a priori podemos dejar los headers que use por default aiohttp
# despues podemos ver si hace falta que reciba headers extras
async def make_request(url, headers, method, body):
    json_compatible_body = jsonable_encoder(body)
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, json=body) as response:
            res = Response(content=await response.read())
            res.status_code = response.status
            res.headers.update(response.headers)
            return res