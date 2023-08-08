import unittest
from formulas import *

class MyTestCase(unittest.TestCase):

    DELTA_VALUE = 0.001
    
    def test_add(self):
        #string input
        self.assertRaises(ValueError, add, '0', 'x')
        self.assertRaises(ValueError, add, '0', '1 2 3')
        self.assertRaises(ValueError, add, 'y', '1 2 3')
        #negative input
        self.assertAlmostEqual(add('1', '-2'), '-1.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(add('-1', '-5'), '-6.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(add('-1', '5'), '4.0', delta=MyTestCase.DELTA_VALUE)
        #positive/zero input
        self.assertAlmostEqual(add('0', '0'), '0.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(add('2', '0'), '2.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(add('0', '4'), '4.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(add('5', '6'), '11.0', delta=MyTestCase.DELTA_VALUE)
        

    def test_subtract(self):
        #string input
        self.assertRaises(ValueError, subtract, '0', 'x')
        self.assertRaises(ValueError, subtract, '0', '1 2 3')
        self.assertRaises(ValueError, subtract, 'y', '1 2 3')
        #negative input
        self.assertAlmostEqual(subtract('1', '-2'), '3.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('2', '-1'), '3.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('-1', '-5'), '4.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('-1', '5'), '-6.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('-5', '1'), '-6.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('-5', '5'), '-10.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('5', '-5'), '10.0', delta=MyTestCase.DELTA_VALUE)
        #positive/zero input
        self.assertAlmostEqual(subtract('5', '0'), '5.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('-5', '0'), '-5.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('0', '-5'), '5.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('0', '5'), '-5.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('0', '0'), '0.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('10', '-1'), '11.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(subtract('1', '10'), '-9.0', delta=MyTestCase.DELTA_VALUE)

    def test_multiply(self):
        #string input
        self.assertRaises(ValueError, multiply, '0', 'x')
        self.assertRaises(ValueError, multiply, '0', '1 2 3')
        self.assertRaises(ValueError, multiply, 'y', '1 2 3')
        #negative input
        self.assertAlmostEqual(multiply('5', '-5'), '-25.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(multiply('-5', '5'), '-25.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(multiply('-5', '-5'), '25.0', delta=MyTestCase.DELTA_VALUE)
        #positive/zero input
        self.assertAlmostEqual(multiply('5', '0'), '0.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(multiply('0', '-5'), '0.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(multiply('0', '0'), '0.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(multiply('0', '1'), '0.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(multiply('5', '5'), '25.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(multiply('1', '5'), '5.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(multiply('1', '1'), '1.0', delta=MyTestCase.DELTA_VALUE)

    def test_divide(self):
        #string input
        self.assertRaises(ValueError, divide, '0', 'x')
        self.assertRaises(ValueError, divide, '0', '1 2 3')
        self.assertRaises(ValueError, divide, 'y', '1 2 3')
        #negative input
        self.assertAlmostEqual(divide('5', '-10'), '-0.5', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(divide('12', '-10'), '-1.2', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(divide('-10', '5'), '-2.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(divide('-10', '12'), '-0.83333', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(divide('-5', '-10'), '0.5', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(divide('-10', '-5'), '2.0', delta=MyTestCase.DELTA_VALUE)
        #zero input
        self.assertRaises(ZeroDivisionError, divide, '0', '0')
        self.assertRaises(ZeroDivisionError, divide, '2', '0')
        self.assertAlmostEqual(divide('0', '2'), '0.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(divide('0', '-2'), '0.0', delta=MyTestCase.DELTA_VALUE)
        #positive input
        self.assertAlmostEqual(divide('20', '1'), '20.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(divide('1', '20'), '0.05', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(divide('6', '6'), '1.0', delta=MyTestCase.DELTA_VALUE)
        self.assertAlmostEqual(divide('10', '11'), '0.90909', delta=MyTestCase.DELTA_VALUE)

if __name__ == '__main__':
    unittest.main()