"""importing the module"""
# pylint: disable=import-error
import kewordargs as kb


# only positional arguments
print("Bill 1:", kb.calculate_bill(500, 2))

# with custom tax
print("Bill 2:", kb.calculate_bill(500, 2, tax=0.1 ))

"""with custom discount""" 
print("Bill 3:", kb.calculate_bill(500, 2, discount=50))

""" with custom tax and discount"""
print("Bill 4:", kb.calculate_bill(500, 2, tax=0.08, discount=100))

print(__doc__)


