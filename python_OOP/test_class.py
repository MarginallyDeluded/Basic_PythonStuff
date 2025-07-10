#test class creation to count number of occurences in a string
#doesnt work for multi-char items, will fix later

class test_string:

    num = 0 # class variable

    def __init__(self,words):
        self.words = words # instance variable
        
        test_string.num += 1

    def count(self,item):
        count = 0
        for char in self.words:
            if char == item:
                count += 1
        return count

print(test_string.num)

# objects/instances
string1 = test_string('Hello there, Hello again there, Hello no longer, how much longer')
string2 = test_string('Doitashimashite')

#print(test_string.__dict__)
#print(string1.__dict__)
#print(string2.__dict__)

# the above attribute will print the number of instances declared in the class
# since the method __init__ is called everytime an instance is declared

#print(string1.count('H'))
