# server/controllers/episode_controller.py
from flask import Blueprint, request, jsonify
from models import db
from models.episode import Episode

blueprint = Blueprint('episodes', __name__)

@blueprint.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': e.id, 'date': e.date.isoformat(), 'number': e.number} for e in episodes]), 200

@blueprint.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number
    }), 200

@blueprint.route('/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted'}), 200