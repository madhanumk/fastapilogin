from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:PODApoda420@database123.cdgcimsw0ilk.us-east-1.rds.amazonaws.com:3306/mydb")

meta = MetaData()

meta.create_all(engine)
conn = engine.connect()