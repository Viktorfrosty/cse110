import random
#core requirement:
# magic_number=random.randint(1,100)
# numeric_answer=0
# while numeric_answer!=magic_number:
#     numeric_answer=int(input("\nCan you guess the magic number? "))
#     if numeric_answer==magic_number:
#         print(f"Congratulations! You guess it\n")
#     elif numeric_answer>magic_number:
#         print("Guess a lower number\n")
#     elif numeric_answer<magic_number:
#         print("Guess a higher number\n")

#stetch challenge:
# play_answer="yes"
# while play_answer.lower()!="no":
#     play_answer=input("Do you want to play the game? (yes/no)")
#     if play_answer.lower()=="yes":
#         magic_number=random.randint(1,100)
#         numeric_answer=0
#         attempts_value=1
#         while numeric_answer!=magic_number:
#             numeric_answer=int(input("\nCan you guess the magic number? "))
#             if numeric_answer==magic_number:
#                 print(f"Congratulations! You guess it\nIt took you {attempts_value} attempts to guess it.\n")
#                 play_answer=input("Do you want to play the game? (yes/no)")
#             elif numeric_answer>magic_number:
#                 attempts_value=attempts_value+1
#                 print("Guess a lower number\n")
#             elif numeric_answer<magic_number:
#                 attempts_value=attempts_value+1
#                 print("Guess a higher number\n")
#     elif play_answer.lower()=="no":
#         print()
#     else:
#         play_answer="yes"
#         print("Insert a valid answer")
# print("Goodbye")
