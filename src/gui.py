
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit

import random

class GUI(QtWidgets.QMainWindow):
    """A class where we make our Graphical User Interface based on PyQT
    """

    def __init__(self) -> None:
        """Initializer of the GUI class
        """
        super().__init__()
        main = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        main.setLayout(layout)
        self.setCentralWidget(main)

        names = ['C', 'AC', 'log', 'graph', '',
                 '7', '8', '9', '/', 'sqrt',
                 '4', '5', '6', '*', '%',
                 '1', '2', '3', '-', '',
                 '0', '.', '+/-', '+', '=']

        positions = [(i, j) for i in range(5) for j in range(5)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtWidgets.QPushButton(name)
            layout.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Graphical Calculator')
        self.show()








