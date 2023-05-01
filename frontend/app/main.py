import os
import aiohttp
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

http_session: aiohttp.ClientSession = aiohttp.ClientSession()


@asynccontextmanager
async def lifespan(app):
    yield
    await http_session.close()


app: FastAPI = FastAPI(lifespan=lifespan)


@app.get("/")
async def hello():
    async with http_session.get(
        f"http://{os.environ.get('HELLO_BACKEND_SERVICE_HOST')}:{os.environ.get('HELLO_BACKEND_SERVICE_PORT')}/hello"
    ) as response:
        if response.status != 200:
            raise HTTPException(500, "internal server error")
        res_json = await response.json()
        return f"{res_json['message']} from {res_json['pod']}"
