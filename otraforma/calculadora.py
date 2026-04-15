import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")

        # widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # layout 
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        #mostramos los digitos los resultados y eso en la pantalla
        self.pantalla = QLabel("0")
        main_layout.addWidget(self.pantalla)

        
        layout = QGridLayout()
        main_layout.addLayout(layout)

        botones = ["1", "2", "3","4", "5", "6","7", "8", "9","0", "-", "*","/", "+", "="]

        self.botones = {}

        row = 0
        col = 0

        for b in botones:

            boton = QPushButton(b)
            layout.addWidget(boton, row, col)
            self.botones[b] = boton

            # nunca me dijieron que checked existe mal ahi
            boton.clicked.connect(lambda checked, t=b: self.presionado(t))

            col += 1
            if col == 3:
                col = 0
                row += 1

        self.expresion = "" #despues de presionar un boton se reinicia

    def presionado(self, b):
        if b == "=":
            try:
                resultado = str(eval(self.expresion))
                self.pantalla.setText(resultado)
                self.expresion = resultado
            except:
                self.pantalla.setText("Error")
                self.expresion = ""
        else:
            self.expresion += b
            self.pantalla.setText(self.expresion)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
