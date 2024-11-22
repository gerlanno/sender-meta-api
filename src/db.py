import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

CONNECTION = "sqlite:///database.db"
engine = create_engine(CONNECTION, echo=True)   

def create_session():
 
    Session = sessionmaker(bind=engine)

    session = Session()
    
    return session

