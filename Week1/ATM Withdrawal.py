amt = int(input("Enter the amount to withdraw: "))
if (amt%100!= 0):
    print("Please enter the amount in multiples of 100.")
    print("Invalid Amount")
else:
    print(f"Dispensing {amt}...")
    print("Please collect your cash.")
    print("Transaction Successful") 
    
