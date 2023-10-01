from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
import os

password = os.getenv('PASSWORD')

engine = create_engine("postgresql://postgres:12345@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()
