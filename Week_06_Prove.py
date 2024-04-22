# I added various options to select the life expectancy output, an invalid input handler, a range in th selection oy year option to avoid an odd result, and a continuity loop.

with open("life-expectancy.csv", "r") as list_live_expectancy:
    next(list_live_expectancy)
    min_expectancy_value = 150
    max_expectancy_value = 0
    average_expectancy = []
    average_dividend = 0
    general_average_value = 0
    min_expectancy_entity = ""
    min_expectancy_year = 0
    max_expectancy_entity = ""
    max_expectancy_year = 0
    for elements in list_live_expectancy:
        elements = elements.split(",")
        entity_name = elements[0]
        year = int(elements[2])
        life_expectancy = float(elements[3])
        average_expectancy.append(life_expectancy)
        average_dividend += life_expectancy
        if life_expectancy < min_expectancy_value:
            min_expectancy_value = life_expectancy
            min_expectancy_entity = entity_name
            min_expectancy_year = year
        elif life_expectancy > max_expectancy_value:
            max_expectancy_value = life_expectancy
            max_expectancy_entity = entity_name
            max_expectancy_year = year
        average_divisor = len(average_expectancy)
        general_average_value = average_dividend/average_divisor
    print(f"----------------------------------------------------------------------------------------------------------------------------------\n\nWelcome to the life expectancy datasheet analistic program. (Alpha Build 0.62)\n\nThe overall life expectancy in our datasheet is {general_average_value:.2f} years.\nThe Country with the lowest life expectancy was {min_expectancy_entity} in {min_expectancy_year}, with an average of {min_expectancy_value:.2f} years.\nThe Country with the highest life expectancy was {max_expectancy_entity} in {max_expectancy_year}, with an average of {max_expectancy_value:.2f} years.\n\nDo you want an especific information?")

while True:
    try:
        user_selection = int(input("\nPlease select one of the following options:\n1: Country.\n2: Year.\n3: Country and year.\n4: Close the program.\nOption number: "))
        if user_selection == 1:
            selected_country = input("Please insert the country name: ")
            with open("life-expectancy.csv", "r") as list_live_expectancy:
                next(list_live_expectancy)
                min_expectancy_value = 150
                max_expectancy_value = 0
                average_expectancy = []
                average_dividend = 0
                average_value = 0
                for elements in list_live_expectancy:
                    elements = elements.split(",")
                    entity_name = elements[0]
                    year = int(elements[2])
                    life_expectancy = float(elements[3])
                    if selected_country.lower() == entity_name.lower():
                        average_expectancy.append(life_expectancy)
                        average_dividend += life_expectancy
                        if life_expectancy < min_expectancy_value:
                            min_expectancy_value = life_expectancy
                            min_expectancy_year = year
                        elif life_expectancy > max_expectancy_value:
                            max_expectancy_value = life_expectancy
                            max_expectancy_year = year
                        average_divisor = len(average_expectancy)
                        average_value = average_dividend/average_divisor
                if average_value != 0:
                    print(f"\nThe alltime average life expectancy of {selected_country.title()} is {average_value:.2f} years.\nThe minimun life expectancy was {min_expectancy_value:.2f} years in {min_expectancy_year}.\nThe maximun life expectancy was {max_expectancy_value:.2f} years in {max_expectancy_year}.")
                elif average_value == 0:
                    print("Value not found in the datasheet.")
        elif user_selection == 2:
            selected_year = int(input("(Year range goes from 1851 to 2019)\nPlease insert the year: "))
            with open("life-expectancy.csv", "r") as list_live_expectancy:
                next(list_live_expectancy)
                min_expectancy_value = 150
                max_expectancy_value = 0
                average_expectancy = []
                average_dividend = 0
                average_value = 0
                for elements in list_live_expectancy:
                    elements = elements.split(",")
                    entity_name = elements[0]
                    year = int(elements[2])
                    life_expectancy = float(elements[3])
                    if selected_year < 2020 and selected_year > 1850:
                        if selected_year == year:
                            average_expectancy.append(life_expectancy)
                            average_dividend += life_expectancy
                            if life_expectancy < min_expectancy_value:
                                min_expectancy_value = life_expectancy
                                min_expectancy_entity = entity_name
                            elif life_expectancy > max_expectancy_value:
                                max_expectancy_value = life_expectancy
                                max_expectancy_entity = entity_name
                            average_divisor = len(average_expectancy)
                            average_value = average_dividend/average_divisor
                if average_value != 0:
                    print(f"\nThe average life expectancy in {selected_year} was {average_value:.2f} years.\nThe country with the minimun life expectancy was {min_expectancy_entity.title()} with {min_expectancy_value:.2f} years.\nThe country with the maximun life expectancy was {max_expectancy_entity.title()} with {max_expectancy_value:.2f} years.")
                elif average_value == 0:
                    print("Value not found in the datasheet.")
        elif user_selection == 3:
            selected_country = input("Please insert the country name: ")
            selected_year = int(input("(Year range goes from 1851 to 2019)\nPlease insert the year: "))
            with open("life-expectancy.csv", "r") as list_live_expectancy:
                next(list_live_expectancy)
                #
                min_expectancy_value = 150
                max_expectancy_value = 0
                average_expectancy = []
                average_dividend = 0
                average_value = 0
                #
                for elements in list_live_expectancy:
                    elements = elements.split(",")
                    entity_name = elements[0]
                    year = int(elements[2])
                    life_expectancy = float(elements[3])
                    if selected_year < 2020 and selected_year > 1850:
                        if selected_country.lower() == entity_name.lower() and selected_year == year:
                            required_life_expectancy = life_expectancy
                            print(f"\nThe life expectancy of {selected_country.title()} in {selected_year} was {required_life_expectancy:.2f} years.")
                            if required_life_expectancy > general_average_value:
                                print(f"Which is higher than the overall average.\n{selected_country.title()} {required_life_expectancy:.3f} years compared to {general_average_value:.3f} years.(overall average expectancy.)")
                            elif required_life_expectancy < general_average_value:
                                print(f"Which is lower than the overall average.\n{selected_country.title()} {required_life_expectancy:.3f} years compared to {general_average_value:.3f} years.(overall average expectancy.)")
                            elif required_life_expectancy == general_average_value:
                                print(f"Which is equal than the overall average.\n{selected_country.title()} {required_life_expectancy:.3f} years compared to {general_average_value:.3f} years.(overall average expectancy.)")
        elif user_selection == 4:
            print("Goodbye\n----------------------------------------------------------------------------------------------------------------------------------\n")
            break
        else:
            print("Insert a valid option")
    except ValueError:
        print("Inser a valid input")