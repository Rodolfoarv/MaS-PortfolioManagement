#QUERIES
# -*- coding: utf-8 -*-

#Importa las librerias.
import MySQLdb
import json
import collections

#Datos de la conexion.
db_host = '127.0.0.1'
db_port = 3306
db_usuario = 'root'
db_password = 'passcode'
base_de_datos = 'PortafolioInversiones'

#Q01: Regresa todas las acciones del dia actual.
def q01():
	#Conecta a la base de datos.
	conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	#Crea un cursor.
	cursor = conn.cursor()
	#Query 01: Regresa todas las acciones del dia actual.
	query = "SELECT E.Nombre, A.PrecioApertura, A.PrecioClausura, A.ValorActual, A.Volumen, A.Volatilidad FROM Accion AS A INNER JOIN Empresa AS E ON A.ID_Empresa=E.ID_EMPRESA WHERE fecha = DATE(NOW())"
	#Se ejecuta el query disenado.
	cursor.execute(query)

	#Crea una lista de objetos.
	objects_list = []
	if query.upper().startswith('SELECT'):
		rows = cursor.fetchall()   # Lectura de datos.
		#Crea un diccionario por cada registro devuelto del query.
		for row in rows:
			d = collections.OrderedDict()
			d['Empresa'] = row[0]
			d['PrecioApertura'] = float(row[1])
			d['PrecioClausura'] = float(row[2])
			d['ValorActual'] = float(row[3])
			d['Volumen'] = int(row[4])
			d['Volatilidad'] = int(row[5])
			objects_list.append(d)
		#Convierte a JSON los diccionarios.
		jsonResult = json.dumps(objects_list)

	else:
		#Escritura, modificacion o eliminacion de datos.
		conn.commit()
		rows = None

	#Cierra el cursor.
	cursor.close()
	#Cierra la conexion.
	conn.close()
	#Muestra lo obtenido.
	jsonResult = json.loads(jsonResult)
	return jsonResult

#Q02: Regresa todas las acciones de la empresa indicada del dia actual.
def q02(empresa):
	#Conecta a la base de datos.
	conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	#Crea un cursor.
	cursor = conn.cursor()
	#Query 02: Regresa todas las acciones de la empresa indicada del dia actual.
	#En este caso recupera las de Apple, pero hay que cambiar ese campo cada vez que se quieran buscar acciones de cierta empresa.
	query = "SELECT E.Nombre, A.PrecioApertura, A.PrecioClausura, A.ValorActual, A.Volumen, A.Volatilidad FROM Accion AS A INNER JOIN Empresa AS E ON A.ID_Empresa=E.ID_EMPRESA WHERE fecha = DATE(NOW()) AND E.Nombre = '%s'" %empresa
	#Se ejecuta el query disenado.
	cursor.execute(query)

	#Crea una lista de objetos.
	objects_list = []
	if query.upper().startswith('SELECT'):
		rows = cursor.fetchall()   # Lectura de datos.
		#Crea un diccionario por cada registro devuelto del query.
		for row in rows:
			d = collections.OrderedDict()
			d['Empresa'] = row[0]
			d['PrecioApertura'] = float(row[1])
			d['PrecioClausura'] = float(row[2])
			d['ValorActual'] = float(row[3])
			d['Volumen'] = int(row[4])
			d['Volatilidad'] = int(row[5])
			objects_list.append(d)
		#Convierte a JSON los diccionarios.
		jsonResult = json.dumps(objects_list)

	else:
		#Escritura, modificacion o eliminacion de datos.
		conn.commit()
		rows = None

	#Cierra el cursor.
	cursor.close()
	#Cierra la conexion.
	conn.close()
	#Muestra lo obtenido.
	jsonResult = json.loads(jsonResult)
	return jsonResult

#Q01_User: Regresa todas las acciones del dia actual relacionadas con cierto usuario.
def q03(usuario):
	#Conecta a la base de datos.
	conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	#Crea un cursor.
	cursor = conn.cursor()
	#Query 01_User: Regresa todas las acciones del dia actual relacionadas con cierto usuario.
	query = "SELECT E.Nombre, A.PrecioApertura, A.PrecioClausura, A.ValorActual, A.Volumen, A.Volatilidad FROM Accion AS A INNER JOIN Empresa AS E ON A.ID_Empresa=E.ID_EMPRESA INNER JOIN PreferenciaEmpresa AS P ON P.ID_EMPRESA=E.ID_EMPRESA WHERE fecha = DATE(NOW()) AND P.Correo = '%s'" %usuario
	#Se ejecuta el query disenado.
	cursor.execute(query)

	#Crea una lista de objetos.
	objects_list = []
	if query.upper().startswith('SELECT'):
		rows = cursor.fetchall()   # Lectura de datos.
		#Crea un diccionario por cada registro devuelto del query.
		for row in rows:
			d = collections.OrderedDict()
			d['Empresa'] = row[0]
			d['PrecioApertura'] = float(row[1])
			d['PrecioClausura'] = float(row[2])
			d['ValorActual'] = float(row[3])
			d['Volumen'] = int(row[4])
			d['Volatilidad'] = int(row[5])
			objects_list.append(d)
		#Convierte a JSON los diccionarios.
		jsonResult = json.dumps(objects_list)

	else:
		#Escritura, modificacion o eliminacion de datos.
		conn.commit()
		rows = None

	#Cierra el cursor.
	cursor.close()
	#Cierra la conexion.
	conn.close()
	#Muestra lo obtenido.
	jsonResult = json.loads(jsonResult)
	return jsonResult

#Q02_User: Regresa todas las acciones del dia actual relacionadas con el giro
def q04(usuario):
	#Conecta a la base de datos.
	conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	#Crea un cursor.
	cursor = conn.cursor()
	#Ingreso del nombre.
	#Query 02_User: Regresa todas las acciones del dia actual relacionadas con cierto usuario.
	query = "SELECT E.Nombre, A.PrecioApertura, A.PrecioClausura, A.ValorActual, A.Volumen, A.Volatilidad FROM Accion AS A INNER JOIN Empresa AS E ON A.ID_Empresa=E.ID_EMPRESA INNER JOIN PreferenciaGiro AS P ON P.ID_Giro=E.ID_Giro WHERE fecha = DATE(NOW()) AND P.Correo = '%s'" %usuario
	#Se ejecuta el query disenado.
	cursor.execute(query)

	#Crea una lista de objetos.
	objects_list = []
	if query.upper().startswith('SELECT'):
		rows = cursor.fetchall()   # Lectura de datos.
		#Crea un diccionario por cada registro devuelto del query.
		for row in rows:
			d = collections.OrderedDict()
			d['Empresa'] = row[0]
			d['PrecioApertura'] = float(row[1])
			d['PrecioClausura'] = float(row[2])
			d['ValorActual'] = float(row[3])
			d['Volumen'] = int(row[4])
			d['Volatilidad'] = int(row[5])
			objects_list.append(d)
		#Convierte a JSON los diccionarios.
		jsonResult = json.dumps(objects_list)

	else:
		#Escritura, modificacion o eliminacion de datos.
		conn.commit()
		rows = None

	#Cierra el cursor.
	cursor.close()
	#Cierra la conexion.
	conn.close()
	#Muestra lo obtenido.
	jsonResult = json.loads(jsonResult)
	return jsonResult

#Q05: Regresa todas las acciones de la empresa indicada dentro de un rango de fechas.
def q05(empresa, inicio, final):
	#Conecta a la base de datos.
	conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	#Crea un cursor.
	cursor = conn.cursor()
	#Query 04: Regresa todas las acciones de la empresa indicada dentro de un rango de fechas.
	#En este caso recupera las de Apple, pero hay que cambiar ese campo cada vez que se quieran buscar acciones de cierta empresa.
	query = "SELECT E.Nombre, A.PrecioApertura, A.PrecioClausura, A.ValorActual, A.Volumen, A.Volatilidad FROM Accion AS A INNER JOIN Empresa AS E ON A.ID_Empresa=E.ID_EMPRESA WHERE fecha BETWEEN '%s' AND '%s' AND E.Nombre = '%s'" %(inicio, final, empresa)
	#Se ejecuta el query disenado.
	print query
	cursor.execute(query)

	#Crea una lista de objetos.
	objects_list = []
	if query.upper().startswith('SELECT'):
		rows = cursor.fetchall()   # Lectura de datos.
		#Crea un diccionario por cada registro devuelto del query.
		for row in rows:
			d = collections.OrderedDict()
			d['Empresa'] = row[0]
			d['PrecioApertura'] = float(row[1])
			d['PrecioClausura'] = float(row[2])
			d['ValorActual'] = float(row[3])
			d['Volumen'] = int(row[4])
			d['Volatilidad'] = int(row[5])
			objects_list.append(d)
		#Convierte a JSON los diccionarios.
		jsonResult = json.dumps(objects_list)

	else:
		#Escritura, modificacion o eliminacion de datos.
		conn.commit()
		rows = None

	#Cierra el cursor.
	cursor.close()
	#Cierra la conexion.
	conn.close()
	#Muestra lo obtenido.
	jsonResult = json.loads(jsonResult)
	return jsonResult

#Q06: Regresa los giros de interés para un usuario.
def q06(usuario):
	#Conecta a la base de datos.
	conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	#Crea un cursor.
	cursor = conn.cursor()
	#Ingreso del nombre.
	#Query 03_User: Regresa los giros de interés para un usuario.
	query = "SELECT G.Nombre FROM Giro AS G INNER JOIN PreferenciaGiro AS P ON G.ID_Giro=P.ID_Giro WHERE P.Correo = '%s'" %usuario
	#Se ejecuta el query disenado.
	cursor.execute(query)

	#Crea una lista de objetos.
	objects_list = []
	if query.upper().startswith('SELECT'):
		rows = cursor.fetchall()   # Lectura de datos.
		#Crea un diccionario por cada registro devuelto del query.
		for row in rows:
			d = collections.OrderedDict()
			d['Giro'] = row[0]
			objects_list.append(d)
		#Convierte a JSON los diccionarios.
		jsonResult = json.dumps(objects_list)

	else:
		#Escritura, modificacion o eliminacion de datos.
		conn.commit()
		rows = None

	#Cierra el cursor.
	cursor.close()
	#Cierra la conexion.
	conn.close()
	#Muestra lo obtenido.
	jsonResult = json.loads(jsonResult)
	return jsonResult

#07: Actualiza el volumen de una accion.
def q07(volumen, empresa):
	try:
	    #Conecta a la base de datos.
	    conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	    #Crea un cursor.
	    cursor = conn.cursor()
	    #Query 07: Actualiza el volumen de la accion.
	    query = "UPDATE Accion AS a INNER JOIN Empresa AS e ON a.ID_Empresa = e.ID_EMPRESA SET a.Volumen = %d WHERE fecha = DATE(NOW()) AND e.nombre = '%s'" %(volumen, empresa)
	    #Se ejecuta el query disenado.
	    cursor.execute(query)
	    #Escritura, modificacion o eliminacion de datos.
	    conn.commit()

	finally:
	    #Cierra el cursor.
	    cursor.close()
	    #Cierra la conexion.
	    conn.close()
	    #Muestra lo obtenido.
	    print "Actualizacion del volumen exitosa."

#q08: Actualiza el valor actual de una accion. 
def q08(valorActual, empresa):
	try:
	    #Conecta a la base de datos.
	    conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	    #Crea un cursor.
	    cursor = conn.cursor()
	    #Query 08: Actualiza el valor actual de la accion.
	    query = "UPDATE Accion AS a INNER JOIN Empresa AS e ON a.ID_Empresa = e.ID_EMPRESA SET a.ValorActual = %d WHERE fecha = DATE(NOW()) AND e.nombre = '%s'" %(valorActual, empresa)
	    #Se ejecuta el query disenado.
	    cursor.execute(query)
	    #Escritura, modificacion o eliminacion de datos.
	    conn.commit()

	finally:
	    #Cierra el cursor.
	    cursor.close()
	    #Cierra la conexion.
	    conn.close()
	    #Muestra lo obtenido.
	    print "Actualizacion del valor actual exitosa."

#q09: Regresa el número de estrategia de la inversion para cierta empresa de un usuario 
def q09(empresa,usuario):
	#Conecta a la base de datos.
	conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	#Crea un cursor.
	cursor = conn.cursor()
	#Ingreso del nombre.
	#Query 03_User: Regresa los giros de interés para un usuario.
	query = "SELECT E.Nombre, I.EstrategiaInversion FROM Inversion AS I INNER JOIN Empresa AS E ON I.ID_Empresa = E.ID_EMPRESA WHERE E.Nombre = '%s' AND I.Correo = '%s'" %(empresa,usuario)
	print query
	#Se ejecuta el query disenado.
	cursor.execute(query)

	#Crea una lista de objetos.
	objects_list = []
	if query.upper().startswith('SELECT'):
		rows = cursor.fetchall()   # Lectura de datos.
		#Crea un diccionario por cada registro devuelto del query.
		for row in rows:
			d = collections.OrderedDict()
			d['Empresa'] = row[0]
			d['EstrategiaInversion'] = int(row[1])

			objects_list.append(d)
		#Convierte a JSON los diccionarios.
		jsonResult = json.dumps(objects_list)

	else:
		#Escritura, modificacion o eliminacion de datos.
		conn.commit()
		rows = None

	#Cierra el cursor.
	cursor.close()
	#Cierra la conexion.
	conn.close()
	#Muestra lo obtenido.
	jsonResult = json.loads(jsonResult)
	return jsonResult


#print q05("Apple", "2016-10-09", "2016-10-10")
#print q09("Apple", "aers@gmail.com")