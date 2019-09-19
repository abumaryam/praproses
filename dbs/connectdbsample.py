# Untuk menggunakannya silahakan rename file ini menjadi connectdb
import mysql.connector

def dbcon():
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="namadatabase"
	)
	return db


