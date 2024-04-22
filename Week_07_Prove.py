#I added random options for the wind chill calculation with a random def, a user selecteced loop for closing the program when desired and some format details.

def temperature_convertion(selected_temperature):
    selected_temperature = (selected_temperature * (9/5)) + 32
    return selected_temperature

def random_number_selection(random_temperature_selection,random_speed_slection):
    import random
    if random_temperature_selection:
        random_number = random.randint(-45,40)
        return random_number
    if random_speed_slection:
        random_number = random.randint(0,61)
        return random_number

def wind_chill_calculation(selected_temperature, wind_speed_data):
    wind_chill = 35.74 + 0.6215 * selected_temperature - 35.75 * wind_speed_data ** 0.16 + 0.4275 * selected_temperature * wind_speed_data ** 0.16
    print(f"At temperature {selected_temperature:.2f} F, and wind speed {wind_speed_data} MPH, the windchill is: {wind_chill:.2f} F")

def temperature_selection():
    while True:
        try:
            temperature_input_selection = int(input("\n1: Especific temperature value.\n2: Random temperature value.\n"))
            if temperature_input_selection == 2:
                user_selected_temperature = random_number_selection(True, False)
                return user_selected_temperature
            elif temperature_input_selection == 1:
                user_selected_temperature = float(input("\nInsert the temperature value: "))
                temperature_type_selection = int(input("the registered temperature was in:\n1: celsius.\n2: Fahrenheit.\n"))
                if temperature_type_selection == 1:
                    user_selected_temperature = temperature_convertion(user_selected_temperature)
                    return user_selected_temperature
                if temperature_type_selection == 2:
                    return user_selected_temperature
                else:
                    print("Select a valid option.")
            else:
                print("Select a valid option.")
        except ValueError:
            print("Insert a valid input.")

def wind_chill_selection(selected_temperature):
    while True:
        try:
            user_wind_chill_display_selection = int(input("\n1: Wind chill single calculation.\n2: Wind chill chart calculation.\n"))
            if user_wind_chill_display_selection == 2:
                wind_speed_table = range(5,61,5)
                print()
                for wind_speed_data in wind_speed_table:
                    wind_chill_calculation(selected_temperature, wind_speed_data)
                break
            elif user_wind_chill_display_selection == 1:
                wind_speed_selection = int(input("\n1: Especific number.\n2: Random Number.\n"))
                if wind_speed_selection == 1:
                    wind_speed_data = float(input("\nInsert the wind speed: "))
                    while wind_speed_data < 0:
                        try:
                            wind_speed_data = float(input("Insert a valid wind speed value: "))
                        except ValueError:
                            print("Insert a valid value")
                    print()
                    wind_chill_calculation(selected_temperature, wind_speed_data)
                elif wind_speed_selection == 2:
                    wind_speed_data = random_number_selection(False, True)
                    print()
                    wind_chill_calculation(selected_temperature, wind_speed_data)
                else:
                    print("Select a valid option")
            break
        except ValueError:
            print("Insert a valid input.")

print("Windchill calculator table (Alpha Build 0.1)")
while True:
    try:
        user_main_selection = int(input("\nPlease, select an option:\n1: Wind chill calculation.\n2: Close the program.\n"))
        if user_main_selection == 2:
            print("\nGoodbye, have a nice day.")
            break
        elif user_main_selection == 1:
            selected_temperature = temperature_selection()
            wind_chill_selection(selected_temperature)
        else:
            print("Select a valid option.")
    except ValueError:
        print("Please insert a valid input.")