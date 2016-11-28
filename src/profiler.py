# -*- coding: utf-8 -*-
'''
'''

import os
import sys
import time
import unittest
import spade
import random
import json
from db.Queries import q01_User, q02_User, q03_User, q04_User, q05_User


HOST = "127.0.0.1"

class Profiler(spade.Agent.Agent):
    ''' '''

    def _setup(self):
        ''''''
        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("inform")
        template.setConversationId("Profiler")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.ProfilerBehav(),mt)

        # Watch for events

        template.setPerformative("inform")
        template.setConversationId("Event")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.EventBehav(),mt)

        print "\n\n*********** Profiler Agent has Started\n\n"


    def sendToCoordinator(self, performative, conversationID, content):
        '''Function that takes as parameter the perfomative, conversation and content to
        be sent back to the coordinator '''
        msg = spade.ACLMessage.ACLMessage()
        msg.setOntology("MaS")
        msg.setPerformative(performative)
        msg.setConversationId(conversationID)
        msg.setContent(content)
        msg.addReceiver(spade.AID.aid("coordinator@"+HOST,["xmpp://coordinator@"+HOST]))
        self.send(msg)

    class ProfilerBehav(spade.Behaviour.Behaviour):

        def _process(self):
            usuarioIngresado = self.ingreso()
            if usuarioIngresado != 0:
            	self.menu(usuarioIngresado)

#---------------------------------------------------> Ingreso preferencias <---------------------------------------------------------#
        def ingresarPreferenciaEmpresa(self,usuario):
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
        	self.menu(usuario)

        def ingresarPreferenciaGiro(self,usuario):
        	correo = usuario
        	print "Giro que te interesa: "
        	print "1) Software"
        	print "2) IT"
        	giro = raw_input("Giro deseado [1,2]: ")
        	giro = int(giro)
        	preferencia = q05_User(correo, giro)
        	if preferencia == 1:
        		print "Preferencia por giro agregada exitosamente."
        	else:
        		print "Preferencia no se pudo agregar. "
        	print " "
        	self.menu(usuario)



#-------------------------------------------------------> Inversiones nuevas <--------------------------------------------------------#
        def crearInversion(self,usuario):
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
        	self.menu(usuario)

#-----------------------------------------> Ingreso o registro <----------------------------------------------------------------#
        def ingreso(self):
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
        def menu(self,usuario):
        	#Opciones
        	print "Menu:"
        	print "1) Crear inversion."
        	print "2) Consultar inversion."
        	print "3) Ingresar preferencia por giro de la empresa."
        	print "4) Ingresar preferencia por nombre de la empresa."
        	opcion = raw_input("Opcion deseada [1,2,3 o 4]: ")
        	print " "
        	if(opcion == "1"):
        		self.crearInversion(usuario)
        	elif (opcion == "2"):
        		self.query(usuario)
        	elif (opcion == "3"):
        		self.ingresarPreferenciaGiro(usuario)
        	elif (opcion == "4"):
        		self.ingresarPreferenciaEmpresa(usuario)
        	else:
        		print "Opcion invalida."

        def query(self,usuario):
            self.myAgent.sendToCoordinator("request", "TechnicalAnalysis", "q01 Apple" )
            self.msg = self._receive(True)
            print self.msg.getContent()
            self.menu(usuario)
#------------------------------------------------------------> Event Behaviour <--------------------------------------------------------------#

    class EventBehav(spade.Behaviour.Behaviour):
        def _process(self):
            self.msg = self._receive(True)
            print self.msg.getContent()



if __name__ == "__main__":
	profiler = Profiler("profiler@"+HOST,"secret")
	profiler.start()
        alive = True
        while alive:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                alive=False
        print "Profiler stopped"
        profiler.stop()
        sys.exit(0)
