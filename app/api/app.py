from app.routers.users import users_router
from app.api.error_handlers import ERROR_HANDLERS

from flask import Flask
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

app.register_blueprint(users_router, url_prefix = '/api')

for error, handler in ERROR_HANDLERS.items():
    app.register_error_handler(error, handler)
