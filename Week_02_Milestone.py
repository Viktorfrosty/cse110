#Milestone Requirements. By midweek, to help make sure you are on track to finish the assignment, you need to complete the following:
#Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
#Ask the user for the number of adults and children and store these values properly into variables as integers.
#Ask the user for the sales tax rate and store the value properly as a floating point number.
#Compute and display the subtotal (don't worry about rounding to two decimals at this point).

print("----------------------------------------------------")
print("Meal price calculator V0.1")
print("----------------------------------------------------")
child_meal_price = float(input("Insert child meal price: "))
adult_meal_price = float(input("Insert adult meal price: "))
n_adults = int(input("Insert the total count of adults: "))
n_childs = int(input("Insert the total count of childrens: "))
tax_rate = float(input("Insert tax rate: "))
print()
childs_cost = child_meal_price * n_childs
adults_cost = adult_meal_price * n_adults
subtotal = childs_cost + adults_cost
print(f"Subtotal: {subtotal}")