from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
import numpy as np
import uvicorn
from keywords_extractor import extract_keywords


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'], 
    allow_headers=['*'],
)

@app.get('/')
def read_root():
    return "Index"

@app.get('/keywords/')
async def get_keywords(request: Request):
    r = await request.json()

    try:
        return extract_keywords(r['content'], r['heading'], r['top_n'])
    except KeyError:
        return {'Error': 'Invalid parameter'}
    
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=10000, reload=True)