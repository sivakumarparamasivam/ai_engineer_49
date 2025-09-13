class GrandParent:
    def a(self):
        return "Method from GrandParent"
class ParentParentB:
    def b(self):
        print("#"*20)
        return "Method from ParentB"    


class A(GrandParent):
    def c(self):
        return "Method from class A"
class B(ParentParentB):
    def d(self):
        return "Method from class B"
class C(A,B):
    def c(self):
        print("#"*20)
        return "Method from class C"
obj=C()
print(obj.b())    
print(C.__mro__)  # Method Resolution Order