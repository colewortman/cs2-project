from PyQt6.QtWidgets import *
from project_gui import *
from formulas import *

class Logic(QMainWindow, Ui_Calculator):
    '''
    Class to handle the logic behind the gui.
    '''
    def __init__(self) -> None:
        '''
        Method to get variables connected to the gui.
        '''
        super().__init__()
        self.setupUi(self)

        self.add_button.clicked.connect(lambda : self.operation(1))
        self.subtract_button.clicked.connect(lambda : self.operation(2))
        self.multiply_button.clicked.connect(lambda : self.operation(3))
        self.divide_button.clicked.connect(lambda : self.operation(4))

        self.clear_button.clicked.connect(lambda : self.clear())
        self.enter_button.clicked.connect(lambda : self.enter())
    
    def operation(self, num: int) -> None:
        '''
        Function to display and track the operation.
        :param num: comparing value.
        '''
        if num == 1:
            self.operation_label.setText('+')
        elif num == 2:
            self.operation_label.setText('-')
        elif num == 3:
            self.operation_label.setText('x')
        elif num == 4:
            self.operation_label.setText('÷')
        else:
            self.operation_label.setText('')
    
    def clear(self) -> None:
        '''
        Function to clear all necessary labels and inputs.
        '''
        self.operation(0)

        self.number_input_one.setText('')
        self.number_input_two.setText('')
        self.answer_label.setText('0')
        self.error_label.setText('')
    
    def enter(self) -> None:
        '''
        Function to handle calculations and errors.
        '''
        try:
            first_num = self.number_input_one.text()
            second_num = self.number_input_two.text()

            if self.operation_label.text() == '+':
                self.answer_label.setText(add(first_num, second_num))
            elif self.operation_label.text() == '-':
                self.answer_label.setText(subtract(first_num, second_num))
            elif self.operation_label.text() == 'x':
                self.answer_label.setText(multiply(first_num, second_num))
            elif self.operation_label.text() == '÷':
                self.answer_label.setText(divide(first_num, second_num))
            else:
                self.error_label.setText("Select An Operation")
        except ValueError:
            self.error_label.setText("Enter Numeric Values")
        except ZeroDivisionError:
            self.error_label.setText("Cannot Divide By Zero")