from dbs.connectdb import connect as db
import mysql.connector
import logging as Log

Log.basicConfig(filename='dbs/db.log', filemode='a+', format='%(asctime)s %(name)s - %(levelname)s - %(message)s')

def select(query):
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def insert(sql,val):
    cursor = db.cursor()
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

def update(sql,val):
    # print("{} record telah diperbaharui".format(cursor.rowcount))
    try:
        cursor = db.cursor()
        cursor.execute(sql,val)
        db.commit()
        Log.warning('Mysql: {} record telah diperbaharui'.format(cursor.rowcount))
        result = True
    except mysql.connector.Error as e:
        Log.error(('ErrorMysql:', e))
        result = False

    return result 

