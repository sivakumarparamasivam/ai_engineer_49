"""Module to calculate bill amount with tax and discount"""
def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
    total_bill = (item_cost * quantity)+ (item_cost * quantity * tax) - discount
    return total_bill

print(calculate_bill(500, 2))
print(__doc__)
if __name__ == "__main__":
    print("Running from main context")
else:
    print("Running from import context")    
