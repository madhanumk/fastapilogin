from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root@localhost:3306/test")

meta = MetaData()

meta.create_all(engine)
conn = engine.connect()