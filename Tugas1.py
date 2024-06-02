import mysql.connector as mysql
import pandas as pd

conn = mysql.connect(
    host='localhost',user='root',password='',database='tbdp2')

cursor = conn.cursor()
cursor.execute("SELECT kelompok.kodeklmpk,departemen.namadept,kelompok.namaklmpk FROM kelompok LEFT JOIN departemen ON departemen.kodedept = kelompok.kodedept")
datas = cursor.fetchall()
df = pd.DataFrame(datas)
print("Sebanyak {} data telah ditemukan".format(cursor.rowcount))
df.columns=["Kode Kelompok","Nama Departemen","Nama Kelompok"]
print(df)

cursor.close()
conn.close()