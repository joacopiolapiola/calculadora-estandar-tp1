#poner botones
#layout = QGridLayout()

#layout.addWidget(, 0, 3)
#layout.addWidget(QPushButton("uno"), 0, 0)
#layout.addWidget(QPushButton("dos"), 0, 1)
#layout.addWidget(QPushButton("tres"), 0, 2)
#layout.addWidget(QPushButton("uno"), 0, 0)
#layout.addWidget(Color("orange"), 2, 2)
#layout.addWidget(Color("blue"), 3, 0)

#hacer lector 
#mostrar = QLabel(lector)
#mostrar.setText(lector))
#lector=lector+""

#calcular

#mas funciones

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("calculadora")
                
        layout = QGridLayout()
        layout.addWidget(QPushButton("uno"), 0, 0)
        layout.addWidget(QPushButton("dos"), 0, 1)
        layout.addWidget(QPushButton("tres"), 0, 2)
        layout.addWidget(QPushButton("uno"), 0, 0)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
