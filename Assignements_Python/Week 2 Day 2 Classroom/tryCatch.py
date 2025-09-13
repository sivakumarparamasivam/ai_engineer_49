
try:
    x = 10
    print(x)
except NameError as err:
    print("Variable x is not defined", err)
except Exception as ex:
    print("Some other error occurred", ex)  
else:
    print("No error occurred, x is:", x)
finally:
    print("Execution completed")