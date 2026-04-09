
#hacer lector 

#calcular

#mas funciones

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout

lector="0"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("calculadora")

        # widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)



        # layout
        layout = QGridLayout()
        central_widget.setLayout(layout)

        botones = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","+","-","/","*","="]
        
        for b in botones:
            var=0
            if(botones.index(b) % 3 == 0 ):
                var=var+1
            b=layout.addWidget(QPushButton(b), botones.index(b),var)

        
        # uno=layout.addWidget(QPushButton("uno"), 0, 0)
        # dos=layout.addWidget(QPushButton("dos"), 0, 1)
        # tres=layout.addWidget(QPushButton("tres"), 0, 2)
        # cuatro=layout.addWidget(QPushButton("cuatro"), 1, 0)
        # cinco=layout.addWidget(QPushButton("cinco"), 1, 1)
        # seis=layout.addWidget(QPushButton("seis"), 1, 2)
        # siete=layout.addWidget(QPushButton("siete"), 2, 0)
        # ocho=layout.addWidget(QPushButton("ocho"), 2, 1)
        # nueve=layout.addWidget(QPushButton("nueve"), 2, 2)
        # mas=layout.addWidget(QPushButton("+"), 0, 3)
        # menos=layout.addWidget(QPushButton("-"), 1, 3)
        # multi=layout.addWidget(QPushButton("X"), 2, 3)
        # dividir=layout.addWidget(QPushButton("/"), 3, 3)
        # igual=layout.addWidget(QPushButton("="), 3, 4)

        #conectar numeros y pantalla
        #uno.clicked.connect(lector=lector+"1")     




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
