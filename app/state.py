from typing import Optional
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

engine: Optional[Engine] = None
session: Optional[sessionmaker] = None
