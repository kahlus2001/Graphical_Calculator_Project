"""Graphical calculator program: the GUI.

Author: Mikolaj Kahl and Joris Wijnands

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit

from math_functions import *

from PyQt5 import QtCore

import random

# define globals
expression = ""
result = ""
check = False


class GraphInputWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        """Initializer of the GraphWindow class.
        """
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Centre Window")
        self.label.setPixmap(QtGui.QPixmap(600, 600))
        layout.addWidget(self.label)

        self.input_function = QLineEdit("Input function", self)
        layout.addWidget(self.input_function)
        self.input_lower = QLineEdit("Input lower bound", self)
        layout.addWidget(self.input_lower)
        self.input_upper = QLineEdit("Input upper bound", self)
        layout.addWidget(self.input_upper)
        self.input_function.setGeometry(0, 80, 250, 40)
        self.input_lower.setGeometry(0, 120, 125, 40)
        self.input_upper.setGeometry(125, 120, 125, 40)

        confirm_button = QtWidgets.QPushButton('Confirm', self)
        layout.addWidget(confirm_button)
        confirm_button.clicked.connect(self.draw_graph)
        confirm_button.setGeometry(65, 200, 120, 60)

    def draw_graph(self) -> None:
        """Draw graph from user input."""
        plot(self.input_function.text(), int(self.input_lower.text()), int(self.input_upper.text()))


class GUI(QtWidgets.QMainWindow):
    """A class where we make our Graphical User Interface based on PyQt
    """

    def __init__(self) -> None:
        """Initializer of the GUI class
        """
        super().__init__()
        main = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        main.setLayout(layout)
        self.setCentralWidget(main)

        # create buttons
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

        # assign buttons
        functions = [self.undo, self.clear_all, self.left_bracket, self.right_bracket, self.graph, self.add7, self.add8,
                     self.add9, self.add_divide, self.add_sqrt, self.add4, self.add5, self.add6, self.add_multiply,
                     self.add_modulo, self.add1, self.add2, self.add3, self.add_minus, self.add_power, self.add0,
                     self.add_dot, self.change_sign, self.add_plus, self.equals]

        for index, function in enumerate(functions):
            button[index].clicked.connect(function)

        # create displays as label
        self.previous = QtWidgets.QLabel('', self)
        layout.addWidget(self.previous, 0, 0, 1, 5)
        self.previous.setFont(QFont('Arial', 20))
        self.previous.setStyleSheet("QLabel { background-color : black; color : white; }")

        self.display = QtWidgets.QLabel('', self)
        layout.addWidget(self.display, 1, 0, 1, 5)
        self.display.setFont(QFont('Arial', 20))
        self.display.setStyleSheet("QLabel { background-color : black; color : white; }")
        self.display.setAlignment(QtCore.Qt.AlignRight)

        # position window on screen, set title, show window.
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
        self.graph = GraphInputWindow()
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

