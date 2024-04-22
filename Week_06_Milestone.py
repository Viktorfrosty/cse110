# It took me a while to deal with that csv first line
import csv
with open("life-expectancy.csv", "r") as list_live_expectancy:
    next(list_live_expectancy)
    min_expectancy_value = 150
    max_expectancy_value = 0
    for elements in list_live_expectancy:
        elements = elements.split(",")
        entity_name = elements[0]
        entity_code = elements[1]
        year = int(elements[2])
        life_expectancy = float(elements[3])
        if life_expectancy < min_expectancy_value:
            min_expectancy_value = life_expectancy
        elif life_expectancy > max_expectancy_value:
            max_expectancy_value = life_expectancy
    print(f"The lowest life expectancy is: {min_expectancy_value:.2f} years.\nThe highest life expectancy is: {max_expectancy_value:.2f} years.")