import logging
import employee

logger = logging.getLogger(__name__) #in main logging channel not root
logger.setLevel(logging.DEBUG) #sets level of logging

formatter = logging.Formatter('%(levelname)s:%(levelno)s:%(message)s')

file_handler = logging.FileHandler('log2.log')
#file_handler.setLevel(logging.ERROR) #In case we only want to write errors or above levels to log file
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

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

logger.info(f'{num1} + {num2} = {add(num1,num2)}')
logger.info(f'{num1} - {num2} = {sub(num1,num2)}')
