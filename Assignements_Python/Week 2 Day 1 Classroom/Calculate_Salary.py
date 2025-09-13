def calculate_salary(basic, hra, da, bonus=0):
    salary = basic + hra + da + bonus
    return salary

salary_1=calculate_salary(30000, 8000, 5000)
print("Salary with default bonus", salary_1)

salary_2=calculate_salary(30000, 8000, 5000, 2000)
print("Salary with given bonus", salary_2)