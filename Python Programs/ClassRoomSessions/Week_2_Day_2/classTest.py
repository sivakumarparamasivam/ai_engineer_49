class Person:
    def __init__(self, name):
        """Initialize the person's name."""
        self.name = name
        
    def invite(self):
        """Print a welcome message."""
        print("Welcome", self.name )

p1=Person("Ram") 
p2=Person("Sita") 
p1.invite()     
p2.invite() 