# server/controllers/appearance_controller.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db
from models.appearance import Appearance

blueprint = Blueprint('appearances', __name__)

@blueprint.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()
    return jsonify({'message': 'Appearance added'}), 201