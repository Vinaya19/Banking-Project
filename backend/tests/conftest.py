import pytest
import sys
sys.path.append('../backend/')
from models import db
from flask import Flask

@pytest.fixture()
def app():
    app = Flask(__name__)

    # Using in-memory SQLite for testing
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["Testing"] = True

    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def session(app):
    """Provide a clean database session for each test."""
    with app.app_context():
        yield db.session