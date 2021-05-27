"""Graphical calculator program: the GUI.

Author: Mikolaj Kahl and Joris Wijnands

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""
from PyQt5 import QtWidgets

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit
from math_functions import *
from PyQt5 import QtCore

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
        """Initializer of the GraphWindow class."""
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        self.status_label = QtWidgets.QLabel("Graph status", self)
        layout.addWidget(self.status_label)
        self.status_label.setGeometry(10, 20, 390, 40)
        self.status_label.setFont(QFont('Arial', 10))
        self.status_label.setStyleSheet("QLabel { background-color : black; color : white; }")

        self.input_label = QtWidgets.QLabel("y = ", self)
        layout.addWidget(self.input_label)
        self.input_label.setGeometry(10, 70, 50, 40)
        self.input_function = QLineEdit("Input function, use numpy notation", self)
        layout.addWidget(self.input_function)
        self.input_lower = QLineEdit("Input lower x-bound", self)
        layout.addWidget(self.input_lower)
        self.input_upper = QLineEdit("Input upper x-bound", self)
        layout.addWidget(self.input_upper)

        # input geometry
        self.input_function.setGeometry(40, 70, 220, 40)
        self.input_lower.setGeometry(10, 110, 125, 40)
        self.input_upper.setGeometry(135, 110, 125, 40)

        # input confirm button
        confirm_button = QtWidgets.QPushButton('Confirm', self)
        layout.addWidget(confirm_button)
        confirm_button.clicked.connect(self.draw_graph)
        confirm_button.setGeometry(280, 80, 120, 60)

        self.setWindowTitle('Function Plotter')

    def draw_graph(self) -> None:
        """Draw graph from user input."""
        try:
            message = plot(self.input_function.text(), float(self.input_lower.text()), float(self.input_upper.text()))
            self.status_label.setText(message)
        except Exception:
            self.status_label.setText('Cannot plot function. Invalid input. Please try again.')


class QuadraticWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        """Initializer of the QuadraticWindow class."""
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        self.roots_label = QtWidgets.QLabel("Solve quadratic equation in the form 0=a*x^2+b*x+c:", self)
        layout.addWidget(self.roots_label)
        self.roots_label.setGeometry(5, 10, 400, 30)
        self.roots_label.setFont(QFont('Arial', 10))
        self.roots_label.setStyleSheet("QLabel { background-color : black; color : white; }")

        self.zero = QtWidgets.QLabel("0 = ", self)
        layout.addWidget(self.zero)
        self.a = QLineEdit("a", self)
        layout.addWidget(self.a)
        self.xSquared = QtWidgets.QLabel("x^2+ ", self)
        layout.addWidget(self.xSquared)
        self.b = QLineEdit("b", self)
        layout.addWidget(self.b)
        self.x = QtWidgets.QLabel("x+ ", self)
        layout.addWidget(self.x)
        self.c = QLineEdit("c", self)
        layout.addWidget(self.c)

        # input geometry
        self.zero.setGeometry(100, 50, 20, 20)
        self.a.setGeometry(120, 50, 50, 20)
        self.xSquared.setGeometry(175, 50, 30, 20)
        self.b.setGeometry(210, 50, 50, 20)
        self.x.setGeometry(265, 50, 20, 20)
        self.c.setGeometry(285, 50, 50, 20)

        # confirm button
        solve_button = QtWidgets.QPushButton('Solve equation', self)
        layout.addWidget(solve_button)
        solve_button.clicked.connect(self.solve)
        solve_button.setGeometry(160, 80, 90, 25)

        self.setWindowTitle('Solve Quadratic Equation')

    def solve(self) -> None:
        """Call find_roots function."""
        try:
            roots = find_roots(float(self.a.text()), float(self.b.text()), float(self.c.text()))
            self.roots_label.setText(roots)
        except Exception:
            self.roots_label.setText(' Invalid input. Cannot solve. Try again.')


class GUI(QtWidgets.QMainWindow):
    """A class where we make our Graphical User Interface based on PyQt."""

    def __init__(self) -> None:
        """Initializer of the GUI class"""
        super().__init__()
        main = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        main.setLayout(layout)
        self.setCentralWidget(main)

        # create buttons
        names = ['C', 'AC', '(', ')', 'graph',
                 '7', '8', '9', '/', 'solve_quad',
                 '4', '5', '6', '*', 'mod',
                 '1', '2', '3', '^', 'sqrt',
                 '0', '.', '-', '+', '=']

        positions = [(i, j) for i in range(2, 7) for j in range(5)]

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
                     self.add9, self.add_divide, self.solve_quad, self.add4, self.add5, self.add6, self.add_multiply,
                     self.add_modulo, self.add1, self.add2, self.add3, self.add_power, self.add_sqrt, self.add0,
                     self.add_dot, self.add_minus, self.add_plus, self.equals]

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
        if check:
            expression = result
            check = False
        if result == "Invalid Input":
            result, expression = '', ''

    def graph(self) -> None:
        """Initialize graph window."""
        self.graph = GraphInputWindow()
        self.graph.show()

    def solve_quad(self) -> None:
        self.solve_quad = QuadraticWindow()
        self.solve_quad.show()

    def add0(self) -> None:
        """"When button '0' is clicked, concatenate 0 to expression."""
        global expression
        expression = expression + '0'
        self.update()

    def add1(self) -> None:
        """"When button '1' is clicked, concatenate 1 to expression."""
        global expression
        expression = expression + '1'
        self.update()

    def add2(self) -> None:
        """"When button '2' is clicked, concatenate 2 to expression."""
        global expression
        expression = expression + '2'
        self.update()

    def add3(self) -> None:
        """"When button '3' is clicked, concatenate 3 to expression."""
        global expression
        expression = expression + '3'
        self.update()

    def add4(self) -> None:
        """"When button '4' is clicked, concatenate 4 to expression."""
        global expression
        expression = expression + '4'
        self.update()

    def add5(self) -> None:
        """"When button '5' is clicked, concatenate 5 to expression."""
        global expression
        expression = expression + '5'
        self.update()

    def add6(self) -> None:
        """"When button '6' is clicked, concatenate 6 to expression."""
        global expression
        expression = expression + '6'
        self.update()

    def add7(self) -> None:
        """"When button '7' is clicked, concatenate 7 to expression."""
        global expression
        expression = expression + '7'
        self.update()

    def add8(self) -> None:
        """"When button '8' is clicked, concatenate 8 to expression."""
        global expression
        expression = expression + '8'
        self.update()

    def add9(self) -> None:
        """"When button '9' is clicked, concatenate 9 to expression."""
        global expression
        expression = expression + '9'
        self.update()

    def add_multiply(self) -> None:
        """"When button '*' is clicked, concatenate * to expression."""
        global expression
        expression = expression + '*'
        self.update()

    def add_divide(self) -> None:
        """"When button '1/' is clicked, concatenate / to expression."""
        global expression
        expression = expression + '/'
        self.update()

    def add_minus(self) -> None:
        """"When button '-' is clicked, concatenate - to expression."""
        global expression
        expression = expression + '-'
        self.update()

    def add_plus(self) -> None:
        """"When button '+' is clicked, concatenate + to expression."""
        global expression
        expression = expression + '+'
        self.update()

    def add_dot(self) -> None:
        """"When button '.' is clicked, concatenate . to expression."""
        global expression
        expression = expression + '.'
        self.update()

    def add_modulo(self) -> None:
        """"When button '%' is clicked, concatenate % to expression."""
        global expression
        expression = expression + '%'
        self.update()

    def add_power(self) -> None:
        """"When button '^' is clicked, concatenate ** to expression."""
        global expression
        expression = expression + '**'
        self.update()

    def left_bracket(self) -> None:
        """"When button '(' is clicked, concatenate ( to expression."""
        global expression
        expression = expression + '('
        self.update()

    def right_bracket(self) -> None:
        """"When button ')' is clicked, concatenate ) to expression."""
        global expression
        expression = expression + ')'
        self.update()

    def add_sqrt(self) -> None:
        """"When button 'sqrt' is clicked, concatenate **0.5 to expression."""
        global expression
        expression = expression + '**0.5'
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
        self.update()

    def undo(self) -> None:
        global expression
        expression = expression[:-1]
        self.update()
