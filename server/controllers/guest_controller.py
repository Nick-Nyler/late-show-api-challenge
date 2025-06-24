# server/controllers/guest_controller.py
from flask import Blueprint, request, jsonify
from models import db
from models.guest import Guest

blueprint = Blueprint('guests', __name__)

@blueprint.route('/', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{'id': g.id, 'name': g.name, 'occupation': g.occupation} for g in guests]), 200