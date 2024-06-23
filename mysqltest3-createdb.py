from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, text, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
# Connect to MySQL (change user, password, and host as needed)


DATABASE_URI = 'mysql+pymysql://root:Naples727575!!@127.0.0.1'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URI, echo=True)

with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS db2"))
    conn.execute(text("USE db2"))
    # conn.execute(text("USE payroll"))
Base = declarative_base()
engine.dispose()