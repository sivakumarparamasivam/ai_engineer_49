# ---------------------------
# a) Base Class: Employee
# ---------------------------

class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")


# ---------------------------
# c) Subclass: Manager
# ---------------------------

class Manager(Employee):
    def __init__(self, name, emp_id, department, team_size):
        super().__init__(name, emp_id, department)  # call base constructor
        self.team_size = team_size

    def display_info(self):  # override
        super().display_info()  # reuse parent details
        print(f"Team Size: {self.team_size}")


# ---------------------------
# d) Subclass: Developer
# ---------------------------

class Developer(Employee):
    def __init__(self, name, emp_id, department, programming_language):
        super().__init__(name, emp_id, department)
        self.programming_language = programming_language

    def display_info(self):  # override
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# ---------------------------
# e) Main section
# ---------------------------

if __name__ == "__main__":
    # Create objects
    mgr = Manager("Alice Johnson", "M123", "IT Operations", 8)
    dev = Developer("Bob Smith", "D456", "Software Development", "Python")

    # Display info
    print("=== Manager Details ===")
    mgr.display_info()

    print("\n=== Developer Details ===")
    dev.display_info()
