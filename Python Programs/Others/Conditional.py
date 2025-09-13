age = int(input("Enter age"))
print("may age", age)
if (age <= 25):
    print("1st Bucket - age is", age)
elif (age > 25) and (age <= 50):
    print("2nd Bucket - age is", age)    
else:
    print("3rd  Bucket - age is", age)