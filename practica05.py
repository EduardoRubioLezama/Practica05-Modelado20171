# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
from PyQt4 import QtGui, QtCore
from datetime import datetime, date

class Window(QtGui.QMainWindow):

	def __init__(self):
		super (Window,self).__init__()
		self.setGeometry(50,50,500,500)
		self.setWindowTitle(" ¡Viva Mexico!")
		self.setWindowIcon(QtGui.QIcon('banderaMexico.png'))
		self.label()
		self.creaBoton()
		self.setVisible(True)

	def creaBoton(self):
		texto = "Oprimeme"
		self.boton = Boton (texto,10,150,self)
		

	def label(self):
		label = QtGui.QLabel("Jose Maria Morelos y Pavon",self)	
		label.move(0,40)
		label.resize(200,40)
		label.show()
		label2 = QtGui.QLabel("Miguel Hidalgo y Costilla",self)
		label2.move(0,20)
		label2.resize(200,40)
		label2.show()
		label3 = QtGui.QLabel("Juan Aldama Gonzalez",self)
		label3.move(0,0)
		label3.resize(200,40)

		label3.show()

class Boton(QtGui.QPushButton):

    def __init__(self, texto, ancho, alto, padre):
        QtGui.QPushButton.__init__(self, texto, padre)
        self.move(ancho, alto)
        self.clicked.connect(self.apretar)

    def apretar(self):
        texto = "Faltan " + calculaDias() + " para el 15 de septiembre"
        self.setText(texto)
        self.resize(300,100)


def calculaDias():
    hoy = datetime.now()#Se obtiene la fecha de hoy
    diasFaltantes = ''

    if hoy.month == 9: 
        if hoy.day < 15: 
            diasFaltantes = datetime(hoy.year, 9, 15) - hoy
        elif hoy.day == 15:
            diasFaltantes = "0"
        else: 
            diasFaltantes = datetime(hoy.year + 1, 9, 15) - hoy

    elif hoy.month < 9: 
        diasFaltantes = datetime(hoy.year, 9, 15) - hoy

    else: 
        diasFaltantes = datetime(hoy.year + 1, 9, 15) - hoy

    return str(diasFaltantes) 
	


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window ()
	sys.exit(app.exec_())

run()	