from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from keywords_extractor import extract_keywords
from flask import Flask, request
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    args = request.args
    
    try:
        return extract_keywords(args.get('content'), args.get('heading'), int(args.get('top_n')))
    except KeyError:
        return {'Error': 'Invalid parameter'}
    
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))