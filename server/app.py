from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to the Late Show API!',
        'status': 'running',
        'version': '1.0'
    }), 200

from controllers import guest_controller, episode_controller, appearance_controller, auth_controller

if __name__ == '__main__':
    app.run(debug=True)