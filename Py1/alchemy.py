from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
engine = create_engine('presto://192.168.237.140:8081/hive/tpcds_text_2')
logs = Table('customer', MetaData(bind=engine), autoload=True)
print select([func.count('*')], from_obj=logs).scalar()
