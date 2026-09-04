import os

from flask import Flask
from src.config.data_base import init_db
from src.routes import init_routes
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    required_vars = [
        "SECRET_KEY"
    ]
    
    missing_vars = [var for var in required_vars if not app.config.get(var)]
    if missing_vars:
        raise RuntimeError(f"Missing environment variables: {', '.join(missing_vars)}")

    JWTManager(app)

    init_db(app)
    init_routes(app)
    return app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)