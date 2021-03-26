from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.constants import DATABASE_URL, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME


SQLALCHEMY_DATABASE_URL = F"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_URL}/{DATABASE_NAME}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Create a new session for interact with database
    :param: None
    :action: return session to connect to database everytime this function is called
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
