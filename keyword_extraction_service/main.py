from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
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

@app.get('/keywords')
def get_keywords(content: str, heading: str, top_n: int):
    
    try:
        return extract_keywords(content, heading, top_n)
    except KeyError:
        return {'Error': 'Invalid parameter'}