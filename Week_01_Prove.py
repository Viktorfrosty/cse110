# I added other fillable words, a corresponding capitalization with every word, and a conditional (if/elif/else) at the end.

print("Please add the following: \n")
name1 = input ("Your first name: ")
Time = input("day or night: ")
adjective1 = input ("An adjective: ")
adjective2 = input ("Another adjective: ")
animal = input ("An animal: ")
verb1 = input ("A verb: ")
verb2 = input ("Another verb: ")
exclamation = input ("An exclamation: ")
print()
print (f"Ok! {name1.capitalize()}, your history is the following: \n")
print (f"The other {Time.lower()}, I was really in a {adjective2.lower()} trouble. It all started when I saw a very") 
print (f"{adjective1.lower()} {animal.lower()} {verb1.lower()} down the hallway. {exclamation.capitalize()}! I yelled. But all ") 
print (f"I could think to do was to {verb2} over and over. Miraculously, ")
print (f"that caused it to stop, but not before it tried to {verb1.lower()} ")
print (f"right in front of my family. Incredible isn't it?\n")
Answer = input("Do you believe in the veracity of that history (yes/no): ")
if (Answer == "no"):
    print (f"\n Really {name1.capitalize()}?, come on, you know I'm not lying.\n -------------------------------------------------------")
elif (Answer == "yes"):
    print (f"\n Wow! {name1.capitalize()}, I´m guessing that you have some crazy tales too.\n -------------------------------------------------------")
else:
    print (f"\n {name1.capitalize()}, it was a yes or no question...\n -------------------------------------------------------")