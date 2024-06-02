import mysql.connector as mysql

conn = mysql.connect(host='localhost',user='root',password='',database='tbdp2')

if conn.is_connected():
    print("Berhasil Koneksi")
    conn.close()