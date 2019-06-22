import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='0009', db='s3')

cursor = conn.cursor() # conn.cursor.DictCursor) dictionary
x = cursor.execute('select * from classcharger')
print(x)
print(cursor.fetchone())
print(cursor.fetchall())
print(cursor.scroll(-3), mode='relativ') # absolute
print(cursor.fetchmany(3))

conn.commit()
cursor.close()
conn.close()