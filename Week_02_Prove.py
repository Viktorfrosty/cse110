# I wrote a discount variable, a tip variable, and some conditionals (if/elif/else) to the code, also I added a short receipt model at the end when the option "do you want a detailed receipt (yes/no): yes" is selected.

print("----------------------------------------------------")
print("Meal price calculator V0.1A")
print("----------------------------------------------------")
child_meal_price = float(input("Insert child meal price: $"))
adult_meal_price = float(input("Insert adult meal price: $"))
n_adults = int(input("Insert the total count of adults: "))
n_childs = int(input("Insert the total count of childrens: "))
discount_rate = float(input("Insert discount rate: %"))
tax_rate = float(input("Insert tax rate: %"))
childs_cost = child_meal_price * n_childs
adults_cost = adult_meal_price * n_adults
subtotal = childs_cost + adults_cost
print(f"\n----------------------------------------------------\nSubtotal: ${subtotal:.2f}")
discount_value = (subtotal * discount_rate) / 100
print(f"discount {discount_rate:.2f}%: ${discount_value:.2f}")
discounted_subtotal = (subtotal - discount_value)
tax_value = (discounted_subtotal * tax_rate) / 100
print(f"tax {tax_rate:.2f}%: ${tax_value:.2f}")
taxed_discounted_subtotal = (discounted_subtotal + tax_value)
print(f"Total: {taxed_discounted_subtotal:.2f}")
tip_value = float(input("Insert tip: $"))
total_value = discounted_subtotal + tax_value + tip_value
print(f"Total amount to pay: ${total_value:.2f}\n----------------------------------------------------")
payment_value = float(input("Insert payment amount: $"))
change_value = payment_value - total_value
print(f"Change: ${change_value:.2f}\n----------------------------------------------------")
Answer = input("Do you want a detailed receipt? (yes/no): ")
if (Answer == "yes"):
    print(f"\n-------------------------------------------------\nDetailed Receipt")
    if (n_adults > 0):
        print(f"\nAdult meal\n{n_adults} x ${adult_meal_price:.2f}" + f"${adults_cost:.2f}".rjust(26))
    if (n_childs > 0):
        print(f"Children meal\n{n_childs} x ${child_meal_price:.2f}" + f"${childs_cost:.2f}".rjust(26))
    print(f"Subtotal:" + f"${subtotal:.2f}".rjust(26))
    print(f"discount " + f"{discount_rate:.2f}%:" + f"-${discount_value:.2f}".rjust(20))
    print(f"tax " + f"{tax_rate:.2f}%:" + f"${tax_value:.2f}".rjust(25))
    print(f"tip:" + f"${tip_value:.2f}".rjust(31))
    print(f"-------------------------------------------------\nTotal:" + f"${total_value:.2f}".rjust(29))
    print(f"Cash:" + f"${payment_value:.2f}".rjust(30))
    print(f"Change:" + f"${change_value:.2f}".rjust(28) + "\n-------------------------------------------------")
elif (Answer == "no"):
    print(f"have a good day")
    print(f"\n-------------------------------------------------")
else:
    print(f"Wrong Input")
    print(f"\n-------------------------------------------------")
