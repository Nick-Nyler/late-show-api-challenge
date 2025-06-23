from flask import Blueprint, jsonify, abort 
from flask_jwt_extended import jwt_required 
from server.models.episode import Episode 
from server.models.appearance import Appearance 
from server.models import db 

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    """
    Retrieves a list of all episodes.
    Returns episode details in JSON format.
    """
    episodes = Episode.query.all() 
    
    return jsonify([
        {"id": e.id, "date": e.date.isoformat(), "number": e.number} 
        for e in episodes
    ]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    """
    Retrieves details for a specific episode, including its appearances.
    Returns 404 if the episode is not found.
    """
    episode = Episode.query.get_or_404(id)
    
    appearances = [
        {"id": a.id, "rating": a.rating, "guest_id": a.guest_id} 
        for a in episode.appearances
    ]
    return jsonify({
        "id": episode.id, 
        "date": episode.date.isoformat(), 
        "number": episode.number, 
        "appearances": appearances
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required() 
def delete_episode(id):
    """
    Deletes a specific episode and its associated appearances.
    Requires a valid JWT token.
    Returns 404 if the episode is not found.
    """
    episode = Episode.query.get_or_404(id)
    
    db.session.delete(episode)
    db.session.commit() 
    
    return jsonify({"message": "Episode deleted successfully"}), 200

