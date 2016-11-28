import spade
from db.Queries import q01_User, q02_User, q03_User, q04_User, q05_User

#---------------------------------------------------> Ingreso preferencias <---------------------------------------------------------#
def ingresarPreferenciaEmpresa(usuario):
	correo = usuario
	print "Empresa que te interesa: "
	print "1) Microsoft"
	print "2) Apple"
	print "3) Alphabet"
	print "4) IBM"
	empresa = raw_input("Empresa deseada [1,2,3 o 4]: ")
	empresa = int(empresa)
	preferencia = q04_User(correo, empresa)
	if preferencia == 1:
		print "Preferencia por empresa agregada exitosamente."
	else:
		print "Preferencia no se pudo agregar. "
	print " "
	menu(usuario)



#-------------------------------------------------------> Inversiones nuevas <--------------------------------------------------------#
def crearInversion(usuario):
	correo = usuario
	fecha = raw_input("Fecha de hoy[AAAA-MM-AA]: ")
	print "Empresa en la que quieres invertir: "
	print "1) Microsoft"
	print "2) Apple"
	print "3) Alphabet"
	print "4) IBM"
	empresa = raw_input("Empresa deseada [1,2,3 o 4]: ")
	empresa = int(empresa)
	capital = raw_input("Capital destinado a esta inversion: ")
	capital = float(capital)
	riesgo = raw_input("Tolerancia al riesgo [0 < Valor < 1]: ")
	riesgo = float(riesgo)
	print "Estrategia que quieres usar para la inversion: "
	print "1) Si el valor de mis acciones sube continuamente [+ de 2 veces], VENDER."
	print "2) Si el valor de mis acciones decrementa continuamente [+ de 5 veces], VENDER."
	print "3) Si el volumen de mis acciones sube abruptamente, COMPRAR."
	print "4) Si el volumen de mis acciones baja abruptamente, VENDER."
	estrategia = raw_input("Estrategia deseada [1,2,3 o 4]: ")
	estrategia = int(estrategia)
	inversion = q03_User(correo, fecha, empresa, capital, riesgo, estrategia)
	if inversion == 1:
		print "Inversion creada exitosamente."
	else:
		print "Inversion no se pudo crear."
	print " "
	menu(usuario)

#-----------------------------------------> Ingreso o registro <----------------------------------------------------------------#
def ingreso():
	print "Bienvenido, por favor escoje una opcion para empezar: "
	print "1) Entrar"
	print "2) Crear nuevo perfil"
	opcion = raw_input("Opcion deseada [1 o 2]: ")
	print " "
	#Entrar.
	if(opcion == "1"):
		print "Escogiste la opcion 1."
		correo = raw_input("Correo: ")
		passwd = raw_input("Password: ")
		usuario = q01_User(correo, passwd)
		if usuario != 0:
			print " "
			print "Bienvenido %s" %usuario
		else:
			print "Error en el correo o contrasena"
		print " "
	#Registrarse.
	else:
		print "Escogiste la opcion 2."
		correo = raw_input("Correo: ")
		passwd = raw_input("Password: ")
		nombre = raw_input("Nombre: ")
		apellidoM = raw_input("Apellido Materno: ")
		apellidoP = raw_input("Apellido Paterno: ")
		fechaNac = raw_input("Fecha de nacimiento [AAAA-MM-DD]: ")
		capital = raw_input("Capital inicial: ")
		capitalN = float(capital)
		usuario = q02_User(correo, nombre, apellidoM, apellidoP, fechaNac,passwd, capitalN)
		if usuario != 0:
			print " "
			print "Bienvenido %s" %usuario
			print " "
		else:
			print "Error en el correo o contrasena"
			print " "
	return usuario

#------------------------------------------------------------> Menu inicial <--------------------------------------------------------------#
def menu(usuario):
	#Opciones
	print "Menu:"
	print "1) Crear inversion."
	print "2) Consultar inversion."
	print "3) Ingresar preferencia por giro de la empresa."
	print "4) Ingresar preferencia por nombre de la empresa."
	opcion = raw_input("Opcion deseada [1,2,3 o 4]: ")
	print " "
	if(opcion == "1"):
		crearInversion(usuario)
	elif (opcion == "2"):
		print "2"
	elif (opcion == "3"):
		ingresarPreferenciaGiro(usuario)
	elif (opcion == "4"):
		ingresarPreferenciaEmpresa(usuario)
	else:
		print "Opcion invalida."

#------------------------------------------------------------------> Main <--------------------------------------------------------------#
usuarioIngresado = ingreso()
if usuarioIngresado != 0:
	menu(usuarioIngresado)
