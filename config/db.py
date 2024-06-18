from sqlalchemy import create_engine,MetaData, select
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:admin@localhost:3306/fast_api")
##DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/fast_api"

engine = create_engine(DATABASE_URL)

metaData = MetaData()


