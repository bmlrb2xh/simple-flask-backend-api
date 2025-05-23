from app import state
from app.utils import settings
from app.api.app import app

import werkzeug
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    state.engine = create_engine(
        url = f"postgresql+psycopg2://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
        echo = settings.DEBUG
    )
    Session = sessionmaker(bind = state.engine)
    state.session = Session()

    werkzeug.run_simple(
        hostname = settings.HOST,
        port = settings.PORT,
        application = app,
        use_reloader = settings.DEBUG,
        use_debugger = settings.DEBUG
    )
