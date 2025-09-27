class Employee:
    def __init__(self, name):
        self.name = name

    # def execute_tests(self):
    #     print(f"From Automation Skills: {self.name} is executing automated tests")     


class AutomationSkills:
    
    def write_script(self):
        print("Writing Selenium scripts")

    def execute_tests(self):
        print(f"From Automation Skills: {self.name} is executing automated tests")    


class AutomationTester(Employee, AutomationSkills):
    def before_test(self):
        print("Before Test")
        
    # def execute_tests(self):
    #     print(f"From Automation Tester: {self.name} is executing automated tests")


tester = AutomationTester("Siva")


print(f"Employee Name: {tester.name}")
tester.write_script()     
tester.execute_tests()      
