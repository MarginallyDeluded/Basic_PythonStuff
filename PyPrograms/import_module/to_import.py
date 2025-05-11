
#import sys
#sys.path.append("/home/vboxuser/PyPrograms/import_module")
import module as mod

courses = ['Maths','CompSci','Chem','english']

index = mod.find_index(courses,'CompSci')
print(index)
