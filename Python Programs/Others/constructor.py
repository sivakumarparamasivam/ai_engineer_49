class A:

    def __init__(self):
        print("Constructor of A with name:")

    def __init__(self, *args):
     print("Constructor of A")
     print(len(args))

     def test(self):
         print("Test method of A")

     @classmethod
     def hallo(cls):
         print("Hallo method of A")  

    @staticmethod
    def welcome():
         print("Welcome method of A")      

a = A("Siva")
a.test()
A.hallo()
A.welcome()


