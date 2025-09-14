class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


class Tester(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    def run_tests(self):  
        print(f"{self.name} / {self.employee_id} is running automation tests")


if __name__ == "__main__":
    obj1 = Tester("Sivakumar", 456)   
    obj2 = Tester("Ramkumar", 786)
    obj1.run_tests()
    obj2.run_tests()
