lst=["siva","murugan","vinayak","Venkat","petharna","Mari"]
set1={1,2,3,4,5}
set2={6,5,6,7,8}
print('siva')
print(set1^set2)
print(lst[0:3])  # Output: ['siva', 'murugan', 'vinayak']
print(lst[1:4])  # Output: ['murugan', 'vinayak', 'Venkat']
print(lst[5:1:-1])  # Output: ['murugan', 'Venkat', 'Mari']
print(lst[-3:-1])  # Output: ['Venkat', 'petharna']
lst.append("kumar")
del lst[2]
print(lst)
tp=("siva","murugan","vinayak","Venkat","petharna","Mari")

for i in range(5):
    print(i)
else:
    print("Loop completed without break")

tuple_collection = (1, 2, 3, 4, 5)

print(tuple_collection[1:4])  # Output: (2, 3, 4)
print(tuple_collection[0:3])  # Output: (1, 2, 3)
print(tuple_collection[4:1:-1])  # Output: (5, 4, 3)
print(tuple_collection[-3:-1])  # Output: (3, 4)
a=""
def solve(a):
    a=[1,3,5]
    a=[2,4,6]   
    
print(a)
solve(a)
print(a)

print(2**3+(5+6)**(1+1))


print("x"*10)
def thrive(n):
    if n % 15 ==0:
        print("thrive",end=" ")
    elif n % 3 != 0 and n % 5 != 0:
        # print(n)
        print("neither",end=" ")
    elif n % 3 == 0:
        # print(n)
        print("three",end=" ") 
    elif n % 5 == 0:
        # print(n)
        print("five",end=" ")
thrive(35)
thrive(56)
thrive(15)
thrive(39)   

print("x"*10)
def solve(a,b):
    print(a,b)
    return b if a==0 else solve(b%a,a)
print(solve(20,50))

dict_1={'name':None,'age':24,'place':"chennai"}
print(dict_1)

if (a==5) and (b==10):
    print("true")
else:
    print("false")