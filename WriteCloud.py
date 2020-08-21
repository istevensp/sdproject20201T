#!/usr/bin/env python

import serial
import json
import MySQLdb as mariadb

arduino = serial.Serial('/dev/ttyACM0',9600)
print arduino.readline()
print arduino.readline()
while True:
	character = arduino.readline()
	MyJson = character
	try: 
		db = mariadb.connect("mdbp-1.cun4wfkxlev9.us-west-2.rds.amazonaws.com","admin","stevendayana","proyectotest1")
		#print("Conexion Exitosa a la base de datos")
	except: 
        	print("Can't connect to database") 
        	arduino.close()
	if character != '\n':
		try:
			data=json.loads(character)
			print data
			print data['temperature']
			cursor = db.cursor()
			cursor.execute("INSERT INTO temps(fecha,temp,hum)values(now(),"+str(data['temperature'])+","+str(data['humidity'])+")")
			db.commit()
		except ValueError:
			print "Error al escribir "
arduino.close()
