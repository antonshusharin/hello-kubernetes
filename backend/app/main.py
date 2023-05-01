import os
from fastapi import FastAPI

os.environ.setdefault("POD_ID", "UNKNOWN")
app = FastAPI()

@app.get('/hello')
async def hello():
    return {'message': 'Hello', 'pod': os.environ.get('POD_ID')}