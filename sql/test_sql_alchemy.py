# need mypysql and sql alchemy
# Add values into environment variables

from os import getenv
from sqlalchemy import create_engine

user = getenv("PHP_MY_ADMIN_USER")
password = getenv("PHP_MY_ADMIN_PASSWORD")
server = getenv("MY_SQL_SERVER")
port = getenv("MY_SQL_PORT")
database = getenv("MY_SQL_DATABASE")
table = getenv("MY_SQL_TABLE")

engine = create_engine(f'mysql+pymysql://{user}:{password}@{server}:{port}/{database}')
print(engine)

with engine.connect() as connection:
    result = connection.execute(f"select date from {table} order by date DESC limit 1")
    for row in result:
        print(row["date"])
