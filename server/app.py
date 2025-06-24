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

# Add a simple root route
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to the Late Show API!',
        'status': 'running',
        'version': '1.0'
    }), 200

# Register blueprints
from controllers import guest_controller, episode_controller, appearance_controller, auth_controller
app.register_blueprint(guest_controller.blueprint, url_prefix='/guests')
app.register_blueprint(episode_controller.blueprint, url_prefix='/episodes')
app.register_blueprint(appearance_controller.blueprint, url_prefix='/appearances')
app.register_blueprint(auth_controller.blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)