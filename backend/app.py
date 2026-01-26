from flask import Flask
from config import Config
from models import db
from routes import bp
# from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # CORS(app)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(bp, url_prefix='/api')
    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # create tables
    app.run(debug=True, port=5000)