from flask import jsonify, request
from app import app
from app.models import dbmovie

@app.route('/')
@app.route('/movies', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = dbmovie.to_collection_dict(dbmovie.query, page, per_page, 'api.get_users')
    return jsonify(data)