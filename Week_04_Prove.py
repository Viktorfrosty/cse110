#I added various word list, random word variables, a difficulty selector, allowed attempts and diferent game modes.
import random
print("---------------------------------------------------\nThe Word Guessing Game\nALPHA BUILD 0.1A\n")
play_time="yes"
retry_value=0
retry_entry=""
while play_time=="yes":
    if retry_value==1:
        retry_entry="again"
    play_time=input(F"Do you want to play the game {retry_entry}? (yes/no)\n")
    if play_time.lower()=="yes":
        print("Choose a difficulty level: (easy/normal/hard)")
        difficulty_level=""
        while difficulty_level=="":
            difficulty_level=input("")
            if difficulty_level.lower()=="easy":
                words_roster=["temple","moroni","mosiah","exodus"]
                selected_word=random.choice(words_roster)
                guess_word=""
                attempts_value=1
                print(f"\nHead's up!\nYour hint is: ",end="")
                for selected_hidden_letter in selected_word:
                    selected_hidden_letter="_ "
                    print(selected_hidden_letter, end="")
                print()
                while guess_word!=selected_word:
                    hint_prompt=""
                    guess_word=input("\nwhat is your guess?\n")
                    if len(guess_word)!=len(selected_word):
                        attempts_value=attempts_value+1
                        print("Sorry, the guess must have the same number of letters as the secret word.")
                    elif guess_word!=selected_word:
                        for letter_position, letter in enumerate(selected_word):
                            if letter_position<len(guess_word) and letter.lower()==(guess_word)[letter_position]:
                                hint_prompt+=letter.upper()
                            elif letter.lower() in guess_word:
                                hint_prompt+=letter.lower()
                            else:
                                hint_prompt+="_ "
                        print(f'Your hint is: {hint_prompt}')
                        attempts_value=attempts_value+1
                    elif guess_word.lower()==selected_word.lower():
                        print(f"Game over.\nIt took you {attempts_value} attempts.")
                retry_value=1
            elif difficulty_level.lower()=="normal":
                words_roster=["car","napolitan","word","catatonic","exodus"]
                selected_word=random.choice(words_roster)
                guess_word=""
                attempts_value=1
                allowed_attempts_value=5
                print(f"Head's up!\n \nYour hint is: ",end="")
                for selected_hidden_letter in selected_word:
                    selected_hidden_letter="_ "
                    print(selected_hidden_letter, end="")
                print()
                while guess_word!=selected_word and allowed_attempts_value>0:
                    hint_prompt=""
                    guess_word=input("\nwhat is your guess?\n")
                    if len(guess_word)!=len(selected_word):
                        attempts_value=attempts_value+1
                        allowed_attempts_value=allowed_attempts_value-1
                        print(f"Sorry, the guess must have the same number of letters as the secret word.\nattempts remaining: {allowed_attempts_value}")
                    elif guess_word!=selected_word:
                        for letter_position, letter in enumerate(selected_word):
                            if letter_position<len(guess_word) and letter.lower()==(guess_word)[letter_position]:
                                hint_prompt+=letter.upper()
                            elif letter.lower() in guess_word:
                                hint_prompt+=letter.lower()
                            else:
                                hint_prompt+="_ "
                        attempts_value=attempts_value+1
                        allowed_attempts_value=allowed_attempts_value-1
                        print(f"Your hint is: {hint_prompt}\nattempts remaining: {allowed_attempts_value}")
                    elif guess_word.lower()==selected_word.lower():
                        print(f"Game over.\nIt took you {attempts_value} attempts.")
                if allowed_attempts_value==0:
                    print("Game over.")
                retry_value=1
            elif difficulty_level.lower()=="hard":
                words_roster=["temple","moroni","mosiah","israel","exodus"]
                selected_word=random.choice(words_roster)
                guess_word=""
                attempts_value=1
                allowed_attempts_value=5
                for selected_hidden_letter in selected_word:
                    selected_hidden_letter="_ "
                    print(selected_hidden_letter, end="")
                print()
                while guess_word!=selected_word and allowed_attempts_value>0:
                    guess_word=input("\nwhat is your guess?\n")
                    if len(guess_word)!=len(selected_word):
                        attempts_value=attempts_value+1
                        allowed_attempts_value=allowed_attempts_value-1
                        print(f"Sorry, the guess must have the same number of letters as the secret word.\nattempts remaining: {allowed_attempts_value}")
                    elif guess_word.lower()!=selected_word.lower():
                        attempts_value=attempts_value+1
                        allowed_attempts_value=allowed_attempts_value-1
                        print(f"your guess wasn't correct.\nattempts remaining: {allowed_attempts_value}")
                    elif guess_word.lower()==selected_word.lower():
                        retry_value=1
                        print(f"Game over.\nIt took you {attempts_value} attempts.")
                if allowed_attempts_value==0:
                    retry_value=1
                    print(f"Game over.")
            else:
                difficulty_level=""
                print("Insert a valid difficulty level: ")
    elif play_time.lower()=="no":
        print("\nGoodbye\n---------------------------------------------------")
    else:
        play_time="yes"
        print("Insert a valid answer")