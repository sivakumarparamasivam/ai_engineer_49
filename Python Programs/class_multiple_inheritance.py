# Multiple Inheritance
# A Sample class with init method
class Person:
    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def invite(self):
        print('Person::Welcome', self.name)

class Profession:
    # init method or constructor
    def __init__(self, professionalType,name):
        self.professionalType = professionalType
        self.name = name

    # Sample Method
    def professionDisplay(self):
        print('My profession is', self.professionalType)
    
        # Sample Method
    def invite(self):
        print('Profession::Welcome', self.name)
        
class Experience(Person, Profession):
    # init method or constructor
    def __init__(self, name, professionalType, Experience_Years):
        Person.__init__(self,name)
        Profession.__init__(self,professionalType,name)
        self.Experience_Years = Experience_Years
    # Sample Method
    """
    def invite(self):
        print('Experience::Welcome', self.name)
    """       
    def experienceShow(self):
        print('My Experience is', self.Experience_Years)

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