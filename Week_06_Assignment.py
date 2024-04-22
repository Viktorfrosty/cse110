# with open ("books.txt") as book_name_list:
#     for book_name in book_name_list:
#         book_name = book_name.strip()
#         print(book_name)

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
minor_age = 999
minor_name = ""
for human_beign in people:
    element = human_beign.split()
    human_beign_name = element[0]
    human_beign_age = int(element[1])
    if human_beign_age < minor_age:
        minor_age = human_beign_age
        minor_name = human_beign_name
print(f"The youngest person is: {minor_name}, with {minor_age} years old.")