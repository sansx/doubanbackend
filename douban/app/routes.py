from flask import jsonify
from app import app
from app.models import dbmovie

@app.route('/')
@app.route('/index')
def index():
    return jsonify(dbmovie.query.get(2).to_dict())