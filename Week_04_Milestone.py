# comment
import random
words_roster=["temple","moroni","mosiah","nimrod","exodus"]
selected_word=random.choice(words_roster)
guess_word=""
attempts_value=1
print(f"Welcome to the word guessing game!\n \nYour hint is: ",end="")
for selected_hidden_letter in selected_word:
    selected_hidden_letter="_ "
    print(selected_hidden_letter, end="")
print()
while guess_word!=selected_word:
    guess_word=input("\nwhat is your guess?\n")
    if guess_word.lower()!=selected_word.lower():
        attempts_value=attempts_value+1
        print("your guess wasn't correct.")
print(f"Game over.\nIt took you {attempts_value} attempts.")