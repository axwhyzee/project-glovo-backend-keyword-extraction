from flask import Flask, request
from flask_cors import CORS
from keywords_extractor import extract_keywords


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def read_root():
    return "Index"

@app.route('/keywords')
def get_keywords():
    r = request.get_json()
    
    try:
        return extract_keywords(r['content'], r['heading'], r['top_n'])
    except KeyError:
        return {'Error': 'Invalid parameter'}
    
        
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)