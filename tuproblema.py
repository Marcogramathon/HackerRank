from sqlite3 import Cursor
import psycopg2
conn = psycopg2.connect(
    database="Marco",
    user="postgres",
    password="password",
    host="database.ccngzbdiikxi.us-east-2.rds.amazonaws.com",
    port=5432
)
with open('Marco.csv') as f:
    data=f.readlines()
    data1= [(float(e.strip().split(',')[0]),float(e.strip().split(',')[1])) for e in data]
#print (data1)
query="""
    CREATE TABLE coordenadas(lat float8,lon float8)
"""
cur=conn.cursor()
# cur.execute(query)
# for i in data1:
#     cur.execute(f"INSERT INTO coordenadas (lat,lon) VALUES {i}")
# cur.execute("DELETE FROM coordenadas ")
# conn.commit()
cur.execute("SELECT * FROM coordenadas")
filas=cur.fetchall()
for i in filas:
    print (i)
