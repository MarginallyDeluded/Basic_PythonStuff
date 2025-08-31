import logging

logger = logging.getLogger(__name__) #in main logging channel not root
logger.setLevel(logging.INFO) #sets level of logging

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(levelno)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        logger.info('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

logger.info(emp_1.first)
logger.info(emp_1.email)
logger.info(emp_1.fullname)

del emp_1.fullname
