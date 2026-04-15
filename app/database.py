#import Dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
#load config
from .config import settings
#create engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)
#session factory 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
#base class 
Base = declarative_base()