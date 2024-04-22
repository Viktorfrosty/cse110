# I used the try and except to avoid an invalid input and adjusted an user input currency symbol
import itertools as it
print("------------------------------------------------------------------------------------------\nWelcome to the Shopping Cart System Ver0.1A")
user_conditional = 0
shopping_list = []
items_values_list = []
item_number_list = range(1,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
total_value = 0
currency_sign = input("Please insert the currency symbol: ")
while user_conditional != 5:
    print("\nPlease select an option using the corrresponding number:\n1 = Add an item.\n2 = View cart.\n3 = Remove item.\n4 = Compute total.\n5 = Quit.")
    user_conditional = (input("option number: "))
    try:
        user_conditional = int(user_conditional)
        if user_conditional == 1:
            list_element = input("Insert an item: ")
            shopping_list.append(list_element)
            items_value = input(f"Please insert the unitary price of {list_element.lower()}: {currency_sign}")
            items_values_list.append(items_value)
            print(f"¨{str(list_element).capitalize()}¨ was added to the cart.")
        elif user_conditional == 2:
            print("the items on the cart are:")
            for number_of_item, list_element, items_value in zip(item_number_list, shopping_list, items_values_list):
                print(f"{number_of_item}: {list_element.capitalize()} unit value: {items_value} {currency_sign}.")
        elif user_conditional == 3:
            items_index = len(shopping_list)
            for number_of_item in range(items_index):
                list_element = shopping_list[number_of_item]
                print(f"{number_of_item+1}: {str(list_element).capitalize()}.")
            remove_item = int(input("Which item would you like to remove? "))
            shopping_list.pop(remove_item-1)
            items_values_list.pop(remove_item-1)
            print("Item removed from the cart.")
        elif user_conditional == 4:
            for items_value in items_values_list:
                total_value = float(total_value) + float(items_value)
            print(f"the total cost is: {total_value:.2f} {currency_sign}")
            total_value = 0
        elif user_conditional == 5:
            print("Goodbye\n------------------------------------------------------------------------------------------")
        else:
            print("Select a valid option.")
    except ValueError:
        print("Input a valid option.")