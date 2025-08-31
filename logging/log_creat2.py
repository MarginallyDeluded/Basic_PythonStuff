import logging

logging.basicConfig(filename='log1.log',level=logging.DEBUG) #different from logging.debug() method.
                                         #this DEBUG is an integer, DEBUG = 10
def add(*args):

    sum = 0
    for item in args:
        sum += item
    return sum

def sub(num1,num2):

    diff = num1 - num2
    return diff

num1 = 30
num2 = 50

logging.debug(f'{num1} + {num2} = {add(num1,num2)}')
logging.debug(f'{num1} - {num2} = {sub(num1,num2)}')

