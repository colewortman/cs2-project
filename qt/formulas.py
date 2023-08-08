def add(num1: str, num2: str) -> str:
    '''
    Function to add 2 numbers.
    :param num1: first number.
    :param num2: second number.
    :return: sum of 2 numbers.
    '''
    answer = float(num1) + float(num2)
    return str(round(answer, 5))

def subtract(num1: str, num2: str) -> str:
    '''
    Function to subtract 2 numbers.
    :param num1: first number.
    :param num2: second number.
    :return: difference of 2 numbers.
    '''
    answer = float(num1) - float(num2)
    return str(round(answer, 5))

def multiply(num1: str, num2: str) -> str:
    '''
    Function to multiply 2 numbers.
    :param num1: first number.
    :param num2: second number.
    :return: product of 2 numbers.
    '''
    answer = float(num1) * float(num2)
    if float(num1) == 0 or float(num2) == 0:
        answer = 0.0
    return str(round(answer, 5))

def divide(num1: str, num2: str) -> str:
    '''
    Function to divide 2 numbers.
    :param num1: first number.
    :param num2: second number.
    :return: quotient of 2 numbers.
    '''
    if float(num2) == 0:
        raise ZeroDivisionError
    else:
        answer = float(num1) / float(num2)
        if float(num1) == 0:
            answer = 0.0
        return str(round(answer, 5))

