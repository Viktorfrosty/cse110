# #notes
print("------------------------------------------------------------------------------------------\nWelcome to the Shopping Cart System Ver0.1A")
user_conditional = 0
shopping_list=[]
list_element=""
while user_conditional != 5:
    print("\nPlease select an option using the corrresponding number:\n1 = Add an item.\n2 = View cart.\n3 = Remove item.\n4 = Compute total.\n5 = Quit.")
    user_conditional = int(input("option number: "))
    if user_conditional == 1:
        list_element = input("Insert an item: ")
        shopping_list.append(list_element)
        print(f"¨{str(list_element).capitalize()}¨ was added to the cart.")
    elif user_conditional == 2:
        print("the items on the cart are:")
        for list_element in shopping_list:
            print(f"{str(list_element).capitalize()}.")
    elif user_conditional == 3:
        print("work in progress")
    elif user_conditional == 4:
        print("work in progress")
    elif user_conditional == 5:
        print("Goodbye\n------------------------------------------------------------------------------------------")
    else:
        print("insert a valid option")