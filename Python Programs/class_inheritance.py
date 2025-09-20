#Multi Level Inheritance
# A Sample class with init method
class Person:
    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def invite(self):
        print('Person :: Welcome', self.name)

class Profession(Person):
    # init method or constructor
    def __init__(self, name, professionalType):
        super().__init__(name)
        self.professionalType = professionalType

    # Sample Method
    def professionDisplay(self):
        print('My profession is', self.professionalType)
"""        
    def invite(self):
        print('Profession :: Welcome', self.name)
"""
class Experience(Profession):
    # init method or constructor
    def __init__(self, name, professionalType, Experience_Years):
        super().__init__(name, professionalType)
        self.Experience_Years = Experience_Years
    # Sample Method
    def experienceShow(self):
        print('My Experience is', self.Experience_Years)
    """
    def invite(self):
        print('Experience :: Welcome', self.name)
    """
# Creating different objects
p1 = Experience('Mani','Director',25)
p2 = Experience('Ram','Sr Lead',10)

#Calling P1 instance Methods
p1.invite()  # Method of Person
p1.professionDisplay()  # Method of Profession Class
p1.experienceShow()  #Method of Experience Class

#With instance created for grandchild class, we can access methods of Parent and Grandparents methods

#Calling P2 instance Methods
p2.invite()
p2.professionDisplay()
p2.experienceShow()


"""
#object creation and initialistion        
p1 = Person('Ram')
p2 = Person('Sita')

p1.invite()
p2.invite()
"""