import mysql.connector as mysql

conn = mysql.connect(
    host='localhost',user='root',password='',database='tbdp2')

cursor = conn.cursor()

strQuery = """INSERT INTO departemen(kodedept,namadept)VALUES(%s,%s)"""
val = ('08','FASHION')
cursor.execute(strQuery, val)
conn.commit()
print("Sebanayak {} data telah ditambahkan".format(cursor.rowcount))

cursor.close()
conn.close()