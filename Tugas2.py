import mysql.connector as mysql
import pandas as pd

conn = mysql.connect(
    host='localhost',user='root',password='',database='tbdp2')

cursor = conn.cursor()
cursor.execute("""SELECT namadept, count(*) as banyak, sum(stok) as stok FROM barang 
                INNER JOIN kelompok ON kelompok.kodeklmpk = barang.kodeklmpk 
                INNER JOIN departemen ON departemen.kodedept = kelompok.kodedept 
                GROUP BY namadept""")
datas = cursor.fetchall()
df = pd.DataFrame(datas)
print("Sebanyak {} data telah ditemukan".format(cursor.rowcount))
df.columns=["0","1","2"]
print(df)

cursor.close()
conn.close()