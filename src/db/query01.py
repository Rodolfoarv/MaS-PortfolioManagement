#Importa las librerias.
import MySQLdb
import json
import collections

def q1():
	#Datos de la conexion.
	db_host = '127.0.0.1'
	db_port = 3306
	db_usuario = 'root'
	db_password = '1'
	base_de_datos = 'PortafolioInversiones'

	#Conecta a la base de datos.
	conn = MySQLdb.Connect(host = db_host, port = db_port, user = db_usuario, passwd = db_password, db = base_de_datos)
	#Crea un cursor.
	cursor = conn.cursor()
	#Query 01: Regresa todas las acciones del dia actual.
	query = 'SELECT Empresa.Nombre, Accion.PrecioApertura, Accion.PrecioClausura, Accion.Pico, Accion.Depresion, Accion.Volumen FROM Accion LEFT JOIN Empresa ON Accion.ID_Empresa=Empresa.ID_EMPRESA WHERE fecha = DATE(NOW())'
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
			d['Pico'] = float(row[3])
			d['Depresion'] = float(row[4])
			d['Volumen'] = int(row[5])
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
	return jsonResult

print q1()
