print('Welcome to TestLeaf')

age = int(input("Enter age : "))
print("may age -> ", age)
it_exp=int(input("Enter IT experience : "))
print("my it experience -> ", it_exp)
if (age >= 22) and (it_exp >= 2):
    print("Access Granted", age, it_exp)
else:
    print("Access Denied", age, it_exp)
