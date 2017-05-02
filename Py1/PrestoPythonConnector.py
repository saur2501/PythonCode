#from prestodb.dbapi import Connection
import prestodb
conn = prestodb.dbapi.Connection(host="192.168.237.140",port=8081,user="root",catalog="hive",schema="tpcds_text_2")
cur = conn.cursor()
cur.execute('select * from customer limit 5')
rows = cur.fetchall()
#print rows
for x in rows:
    print x
