number_list=[]
number_value=1
sum_value=0
print("Enter a list of numbers, type 0 when finished.")
while number_value != 0:
    number_value = int(input("Insert a number: "))
    if number_value != 0:
        number_list.append(number_value)
for number_value in number_list:
    sum_value = sum_value + number_value
print(f"the sum of the numbers is: {sum_value}")
avg_value = sum(number_list) / len(number_list)
print(f"The average is: {avg_value}")
print(f"The largest number is: {max(number_list)}")
print(f"The smallest positive number is: {min(number_list)}")
for numbers in number_list:
    print(f"the sorted numbers are: {numbers}", end="\n")