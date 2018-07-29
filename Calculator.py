
import time 
import pyforms

from   pyforms          import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from pyforms import settings as formSettings

class Calculator(BaseWidget):
    def __init__(self):
        super(Calculator,self).__init__('Calculator')
        self.formset = ['_box1', ('_clear', '_pcent', '_divide'), 
                ('_n7', '_n8', '_n9', '_multiply'),('_n4', '_n5', '_n6', '_subtract'), 
                ('_n1', '_n2', '_n3', '_add'), ('_pN', '_n0', '_dot', '_result')]

        #Define the text area
        self._box1 = ControlText('')
        
        #Define the number buttons
        self._n0 = ControlButton('0')
        self._n1 = ControlButton('1')
        self._n2 = ControlButton('2')
        self._n3 = ControlButton('3')
        self._n4 = ControlButton('4')
        self._n5 = ControlButton('5')
        self._n6 = ControlButton('6')
        self._n7 = ControlButton('7')
        self._n8 = ControlButton('8')
        self._n9 = ControlButton('9')

        #Define the operator buttons
        self._add = ControlButton('+')
        self._subtract = ControlButton('-')
        self._multiply = ControlButton('*')
        self._divide = ControlButton('/')

        self._pcent = ControlButton('%')
        self._dot = ControlButton('.')
        self._pN = ControlButton('+/-')
        self._clear = ControlButton('C')
        self._result = ControlButton('=')

        #Define the number actions
        self._n0.value = self.__n0
        self._n1.value = self.__n1
        self._n2.value = self.__n2
        self._n3.value = self.__n3
        self._n4.value = self.__n4
        self._n5.value = self.__n5
        self._n6.value = self.__n6
        self._n7.value = self.__n7
        self._n8.value = self.__n8
        self._n9.value = self.__n9

        #Define the operator actions
        self._add.value = self.__add
        self._subtract.value = self.__subtract
        self._multiply.value = self.__multiply
        self._divide.value = self.__divide

        self._pcent.value = self.__pcent
        self._dot.value = self.__dot
        self._pN.value = self.__pN
        self._clear.value = self.__clear
        self._result.value = self.__result

    def __n0(self):
        self._box1.value += "0"    
    def __n1(self):
        self._box1.value += "1"
    def __n2(self):
        self._box1.value += "2"
    def __n3(self):
        self._box1.value += "3"
    def __n4(self):
        self._box1.value += "4"
    def __n5(self):
        self._box1.value += "5"
    def __n6(self):
        self._box1.value += "6"
    def __n7(self):
        self._box1.value += "7"
    def __n8(self):
        self._box1.value += "8"
    def __n9(self):
        self._box1.value += "9"
        
    def __add(self):
        self._box1.value += "+"
    def __subtract(self):
        self._box1.value += "-"
    def __multiply(self):
        self._box1.value += "*"
    def __divide(self):
        self._box1.value += "/"

    def __pcent(self):
        try:
            self._box1.value = str(float(self._box1.value)/100)
        except ValueError:
            self._box1.value = ""
    def __dot(self):
        self._box1.value += "."
    def __pN(self):
        self._box1.value = str(float(self._box1.value)*-1)
    def __clear(self):
        self._box1.value = ""
    def __result(self):
        try:
            self._box1.value = str(eval(self._box1.value))
        except ZeroDivisionError:
            self._box1.value = "Can't divide by zero"
            time.sleep(2)
            self._box1.value = ""
        except SyntaxError:
            self._box1.value = ""
        except ValueError:
            self._box1.value = ""
        
    
#Execute the application
if __name__ == "__main__":
    pyforms.start_app(Calculator, geometry=(200, 200, 400, 300))
