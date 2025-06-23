from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app import db
from models.episode import Episode
from models.appearance import Appearance

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number
    } for episode in episodes])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': [{
            'id': app.id,
            'rating': app.rating,
            'guest_id': app.guest_id
        } for app in appearances]
    })

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted successfully'})