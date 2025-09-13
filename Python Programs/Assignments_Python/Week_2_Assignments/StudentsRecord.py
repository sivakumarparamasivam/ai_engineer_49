class Student:
    def __init__(self, name, grade, department):
        self.name = name
        self.grade = grade
        self.department = department

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Department: {self.department}")
        print("-" * 20)

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade updated to {self.grade}")


if __name__ == "__main__":
    
    student1 = Student("Siva", "P", "Computer Science")
    student2 = Student("Params", "R", "Mechanical Engineering")
    student3 = Student("Thiyas", "S", "Electrical Engineering")


    students = [student1, student2, student3]

 
    print("Initial Student Records:")
    for student in students:
        student.print_info()

  
    student2.update_grade("A+")

    
    print("Updated Student Records:")
    for student in students:
        student.print_info()
