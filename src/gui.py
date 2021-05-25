"""Graphical calculator program: the GUI.

Author: Mikolaj Kahl and Joris Wijnands

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QLabel
from math_functions import *
import sys

import random

#define globals
expression = ""
result = ""
check = False

class GraphWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Centre Window")
        self.label.setPixmap(QtGui.QPixmap(600, 600))
        layout.addWidget(self.label)



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

        #create buttons
        names = ['C', 'AC', '(', ')', 'graph',
                 '7', '8', '9', '/', 'sqrt',
                 '4', '5', '6', '*', 'mod',
                 '1', '2', '3', '-', '^',
                 '0', '.', '+/-', '+', '=']

        positions = [(i, j) for i in range(2,7) for j in range(5)]

        button = []
        count = 0
        for position, name in zip(positions, names):

            if name == '':
                continue
            button.append(name)
            button[count] = QtWidgets.QPushButton(name, self)
            layout.addWidget(button[count], *position)
            count += 1

        #assign buttons
        button[0].clicked.connect(self.undo)
        button[1].clicked.connect(self.clear_all)
        button[2].clicked.connect(self.left_bracket)
        button[3].clicked.connect(self.right_bracket)
        button[4].clicked.connect(self.graph)
        button[5].clicked.connect(self.add7)
        button[6].clicked.connect(self.add8)
        button[7].clicked.connect(self.add9)
        button[8].clicked.connect(self.add_divide)
        button[9].clicked.connect(self.add_sqrt)
        button[10].clicked.connect(self.add4)
        button[11].clicked.connect(self.add5)
        button[12].clicked.connect(self.add6)
        button[13].clicked.connect(self.add_multiply)
        button[14].clicked.connect(self.add_modulo)
        button[15].clicked.connect(self.add1)
        button[16].clicked.connect(self.add2)
        button[17].clicked.connect(self.add3)
        button[18].clicked.connect(self.add_minus)
        button[19].clicked.connect(self.add_power)
        button[20].clicked.connect(self.add0)
        button[21].clicked.connect(self.add_dot)
        button[22].clicked.connect(self.change_sign)
        button[23].clicked.connect(self.add_plus)
        button[24].clicked.connect(self.equals)

        #create displays as label
        self.previous = QtWidgets.QLabel('', self)
        layout.addWidget(self.previous, 0, 0, 1, 5)
        self.previous.setFont(QFont('Arial', 20))
        self.previous.setStyleSheet("QLabel { background-color : black; color : white; }")

        self.display = QtWidgets.QLabel('', self)
        layout.addWidget(self.display, 1, 0, 1, 5)
        self.display.setFont(QFont('Arial', 20))
        self.display.setStyleSheet("QLabel { background-color : black; color : white; }")

        #position window on screen, set title, show window.
        self.move(300, 150)
        self.setWindowTitle('Graphical Calculator')
        self.show()


    def update(self) -> None:
        """Update display of calculator."""
        global expression, result, check
        self.previous.setText(expression)
        self.display.setText(result)
        if check == True:
            expression = result
            check = False
        if result == "Invalid Input":
            result, expression = '', ''

    def graph(self) -> None:
        self.graph = GraphWindow()
        self.graph.show()



    def add0(self) -> None:
        """"When button '0' is clicked, concatenate 0 to expression."""
        global expression
        expression = expression + '0'
        print(expression)
        self.update()

    def add1(self) -> None:
        """"When button '1' is clicked, concatenate 1 to expression."""
        global expression
        expression = expression + '1'
        print(expression)
        self.update()

    def add2(self) -> None:
        """"When button '2' is clicked, concatenate 2 to expression."""
        global expression
        expression = expression + '2'
        print(expression)
        self.update()

    def add3(self) -> None:
        """"When button '3' is clicked, concatenate 3 to expression."""
        global expression
        expression = expression + '3'
        print(expression)
        self.update()

    def add4(self) -> None:
        """"When button '4' is clicked, concatenate 4 to expression."""
        global expression
        expression = expression + '4'
        print(expression)
        self.update()

    def add5(self) -> None:
        """"When button '5' is clicked, concatenate 5 to expression."""
        global expression
        expression = expression + '5'
        print(expression)
        self.update()

    def add6(self) -> None:
        """"When button '6' is clicked, concatenate 6 to expression."""
        global expression
        expression = expression + '6'
        print(expression)
        self.update()

    def add7(self) -> None:
        """"When button '7' is clicked, concatenate 7 to expression."""
        global expression
        expression = expression + '7'
        print(expression)
        self.update()

    def add8(self) -> None:
        """"When button '8' is clicked, concatenate 8 to expression."""
        global expression
        expression = expression + '8'
        print(expression)
        self.update()

    def add9(self) -> None:
        """"When button '9' is clicked, concatenate 9 to expression."""
        global expression
        expression = expression + '9'
        print(expression)
        self.update()

    def add_multiply(self) -> None:
        """"When button '*' is clicked, concatenate * to expression."""
        global expression
        expression = expression + '*'
        print(expression)
        self.update()

    def add_divide(self) -> None:
        """"When button '1/' is clicked, concatenate / to expression."""
        global expression
        expression = expression + '/'
        print(expression)
        self.update()

    def add_minus(self) -> None:
        """"When button '-' is clicked, concatenate - to expression."""
        global expression
        expression = expression + '-'
        print(expression)
        self.update()

    def add_plus(self) -> None:
        """"When button '+' is clicked, concatenate + to expression."""
        global expression
        expression = expression + '+'
        print(expression)
        self.update()

    def add_dot(self) -> None:
        """"When button '.' is clicked, concatenate . to expression."""
        global expression
        expression = expression + '.'
        print(expression)
        self.update()

    def add_modulo(self) -> None:
        """"When button '%' is clicked, concatenate % to expression."""
        global expression
        expression = expression + '%'
        print(expression)
        self.update()

    def add_power(self) -> None:
        """"When button '^' is clicked, concatenate ** to expression."""
        global expression
        expression = expression + '**'
        print(expression)
        self.update()

    def change_sign(self) -> None:
        """"When button '+/-' is clicked, concatenate -( to expression."""
        global expression
        expression = expression + '-('
        print(expression)
        self.update()

    def left_bracket(self) -> None:
        """"When button '(' is clicked, concatenate ( to expression."""
        global expression
        expression = expression + '('
        print(expression)
        self.update()

    def right_bracket(self) -> None:
        """"When button ')' is clicked, concatenate ) to expression."""
        global expression
        expression = expression + ')'
        print(expression)
        self.update()

    def add_sqrt(self) -> None:
        """"When button 'sqrt' is clicked, concatenate **0.5 to expression."""
        global expression
        expression = expression + '**0.5'
        print(expression)
        self.update()

    def equals(self) -> None:
        global expression, result, check
        new_expression = evaluate(expression, result)
        if new_expression == 'invalid input':
            expression = ''
        else:
            result = str(new_expression)
            check = True
            self.update()

    def clear_all(self) -> None:
        global expression, result
        expression = ''
        result = ''
        print(expression,'cleared')
        self.update()

    def undo(self) -> None:
        global expression
        expression = expression[:-1]
        print(expression)
        self.update()

