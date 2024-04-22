# I added while loops to handle the missuse of some words and ad a little suspense.
#Tester notes:

print("---------------------------------------------------\nThe Old Town Road\nALPHA BUILD 0.1B")
init_value = 1
retry_value = 0
failed_value = 0
retry_entry = ""
failed_entry = ""
print("Game TIP #1: All possible answers are showed in CAPS")
print("Game TIP #2: Be carefull, depending on the question you will had a limited number of atempts")
while init_value == 1:
    if failed_value == 1:
        failed_entry = "Thinking outside the box isn't a good idea, especially against a group of unidentified monsters\nGAME OVER\n"
    if retry_value == 1:
        retry_entry = " again"
    init_a = input (f"" + str(failed_entry) + "Do you want to play the game" + str(retry_entry) +"? (YES/NO)")
    if init_a.lower() == "no":
        print ()
        init_value = 0
    elif init_a.lower() == "yes":
        init_value = 0
        a_value = 1
        b_value = 1
        c_value = 1
        d_value = 1
        allowed_atempts = 3
        retry_value = 1
        failed_value = 0
        print("You are traveling alone in your car in the middle of the night near the deviation to the Old Town.\nWhile you were distracted by the radio, your pickup impacted something; you stopped immediately and saw how the thing you hit flew for a few meters and wondered what was that, you turned on the fog lights and saw that thing isn't a human or an animal.\nYou disembarked the vehicle and looked with horror at that thing in the distance. One part of you thinks that TAKING A CLOSER LOOK will be helpful to kill your curiosity about what you hit, but; another part of you knows that STAYING NEAR THE PICKUP could be less dangerous, and BOARDING THE PICKUP is the safest choice.")
        while a_value == 1:
            main_road_desition_01 = input("What are you going to do?")
            if main_road_desition_01.lower() == "take a closer look" or main_road_desition_01.lower() == "taking a closer look":
                a_value = 0
                init_value = 1
                print("The thing started growling and moving. You panicked and tried to run back to the safety of the pickup, but that thing was not alone in the dark, and it was too late for you to realize that...\n\nGAME OVER")
            elif(main_road_desition_01.lower() == "staying near the pickup" or main_road_desition_01.lower() == "stay near the pickup"):
                a_value = 0
                print ("You see in the distance how that thing started moving again, after a moment you hear a distant scream behind you, there are more and are coming towards the pickup, you have two options RUN INTO TO THE FOREST or RUN TO THE PICKUP. You need to react fast or you are not going to survive")
                while allowed_atempts > 0 and b_value == 1:
                    answer_01_b = input(f"Where are you going to run?\natempts remaining: {allowed_atempts}\n")
                    if answer_01_b.lower() == "to the forest" or answer_01_b.lower() == "the forest" or answer_01_b.lower() == "forest":
                        allowed_atempts = 0
                        b_value = 0
                        init_value = 1
                        print("Like a goat to the slaughterhouse, you run directly to the forest, where other monsters were waiting for you...\nGAME OVER")
                    elif answer_01_b.lower() == "to the pickup" and allowed_atempts == 2 or answer_01_b.lower() == "the pickup" and allowed_atempts == 2 or answer_01_b.lower() == "pickup" and allowed_atempts == 2 or answer_01_b.lower() == "to the pickup" and allowed_atempts == 1 or answer_01_b.lower() == "the pickup" and allowed_atempts == 1 or answer_01_b.lower() == "pickup" and allowed_atempts == 1:
                        allowed_atempts = 0
                        b_value = 0
                        init_value = 1
                        retry_value = 1
                        failed_value = 0
                        print("You tried to run to the pickup, but you don't reacted as fast as those things...\nGAME OVER")
                    elif answer_01_b.lower() == "to the pickup" and allowed_atempts == 3 or answer_01_b.lower() == "the pickup" and allowed_atempts == 3 or answer_01_b.lower() == "pickup" and allowed_atempts == 3:
                        b_value = 0
                        print("You almost got caught by one of these things. Now you are inside the pickup, but the others look even more dreadful; you can FULLY REVERSE the vehicle and try to go back from where you came from or RUN OVER THAT THING and try to make it into the deviation.")
                        allowed_atempts = 2
                        while allowed_atempts > 0 and c_value == 1:
                            answer_02_a = input(f"What are you going to do?\natempts remaining: {allowed_atempts}")
                            if answer_02_a.lower() == "fully reverse" or answer_02_a.lower() == "full reverse" or answer_02_a.lower() == "reverse":
                                c_value = 0
                                allowed_atempts = 0
                                init_value = 1
                                retry_value = 1
                                failed_value = 0
                                print("You tried to escape but there were a lot of these things surrounding your pickup; the last thing you saw was the claws of one of them coming at high speed towards your face.\nGAME OVER")
                            elif answer_02_a.lower() == "run over that thing" and allowed_atempts == 1 or answer_02_a.lower() == "run over" and allowed_atempts == 1 or answer_02_a.lower() == "run over it" and allowed_atempts == 1:
                                c_value = 0
                                allowed_atempts = 0
                                init_value = 1
                                retry_value = 1
                                failed_value = 0
                                print("You tried to run over that thing, but it reacted fast and jumped over the front of the vehicle; the last thing you saw was his open mouth full of fangs.\nGAME OVER")
                            elif answer_02_a.lower() == "run over that thing" and allowed_atempts == 2 or answer_02_a.lower() == "run over" and allowed_atempts == 2 or answer_02_a.lower() == "run over it" and allowed_atempts == 2:
                                c_value = 0
                                print("You run over that thing and shake the others from the tail of your pickup, after an almost never-ending moment you make it to the deviation, and now one part of you wants an answer about the attack if you go TO THE OLD TOWN maybe the habitants can help you to understand what happened; but in the other hand, you can take the exit TO THE HIGHWAY and try to forget everything.")
                                while d_value == 1:
                                    answer_03_a = input("what direction are you going to take?")
                                    if answer_03_a.lower() == "to the old town" or answer_03_a.lower() == "old town":
                                        d_value = 0
                                        init_value = 1
                                        retry_value = 1
                                        failed_value = 0
                                        print("The night started to get darker when you drove to the Old Town. During your drive, you saw other things like the one you left behind on the road, but they are lurking inside the woods, avoiding the open spaces. As soon you get closer to the Old Town, a weird mist involved your vehicle, you don't know what to expect, but you need answers no matter what the risks are.\nGAME OVER")
                                    elif answer_03_a.lower() == "to the highway" or answer_03_a.lower() == "highway":
                                        d_value = 0
                                        init_value = 1
                                        retry_value = 1
                                        failed_value = 0
                                        print("The moon started to shine bright during your high-speed drive on the highway. Sometime after that, some cars pass you by, which helps you to calm down, but the flashbacks of the things you saw aren't leaving your mind. After a while, you stopped at a motel and sleep for the night. Hoping that in the morning you forget everything.\nGAME OVER")
                                    else:
                                        print("Insert a valid answer: ")
                            else:
                                allowed_atempts -= 1
                                failed_value = 1
                                retry_value = 1
                                init_value = 1
                    else:
                        allowed_atempts -= 1
                        failed_value = 1
                        retry_value = 1
                        init_value = 1
            elif(main_road_desition_01.lower() == "get in the pickup" or main_road_desition_01.lower() == "boarding the pickup"):
                print("You got into the pickup as fast as possible, and see how that thing is standing now, after a moment you realize that isn´t alone, you need to think fast, because the others look even more dreadful; you can FULLY REVERSE the vehicle and try to go back from where you came from or RUN OVER THAT THING and try to make it into the deviation.")
                a_value = 0
                while allowed_atempts > 0 and b_value == 1:
                    answer_01_c = input(f"FULL REVERSE or RUN OVER THAT THING\natempts remaining: {allowed_atempts}")
                    if answer_01_c.lower() == "full reverse" or answer_01_c.lower() == "reverse":
                        allowed_atempts = 1
                        b_value = 0
                        print("During the escape attempt, you panicked and hit a tree, now that thing and others are running towards you and the pickup isn't responding, you can LEAVE THE PICKUP and try to run as fast as you can or STAY IN THE PICKUP and try to ignite the engine again.")
                        while allowed_atempts > 0 and c_value == 1:
                            answer_02_b = input(f"What are you going to do?\nYou only have one opportunity.")
                            if answer_02_b.lower() == "leave" or answer_02_b.lower() == "leave the pickup":
                                c_value = 0
                                init_value = 1
                                retry_value = 1
                                failed_value = 0
                                print("After you disembarked the pickup, you noticed something... It wasn't a tree... It was a very huge and dreadful thing that was really hungry...\nGAME OVER")
                            elif answer_02_b.lower() == "stay" or answer_02_b.lower() == "stay in the pickup":
                                c_value = 0
                                init_value = 1
                                retry_value = 1
                                failed_value = 0
                                print("You tried with all your habilities to start the engine again, but unfortunately when the pickup started to move again you weren't alone inside the vehicle...\nGAME OVER")
                            else:
                                allowed_atempts -= 1
                                init_value = 1
                                retry_value = 1
                                failed_value = 1
                    elif answer_01_c.lower() == "run over that thing" or answer_01_c.lower() == "run over":
                        b_value = 0
                        print("You run over that thing and saw trought the mirror how the others started devouring the corpse, after an almost neverending moment you make it to the deviation, and now one part of you wants an answer about the attack if you go TO THE OLD TOWN maybe the habitants can help you to understand what happened; but in the other hand, you can take the exit TO THE HIGHWAY and try to forget everything.")
                        while c_value == 1:
                            answer_03_a = input("what direction are you going to take?")
                            if answer_03_a.lower() == "to the old town" or answer_03_a.lower() == "old town":
                                c_value = 0
                                init_value = 1
                                retry_value = 1
                                failed_value = 0
                                print("The night started to get darker when you drove to the Old Town. During your drive, you saw other things like the one you left behind on the road, but they are lurking inside the woods, avoiding the open spaces. As soon you get closer to the Old Town, a weird mist involved your vehicle, you don't know what to expect, but you need answers no matter what the risks are.\nGAME OVER")
                            elif answer_03_a.lower() == "to the highway" or answer_03_a.lower() == "highway":
                                c_value = 0
                                init_value = 1
                                retry_value = 1
                                failed_value = 0
                                print("The moon started to shine bright during your high-speed drive on the highway. Sometime after that, some cars pass you by, which helps you to calm down, but the flashbacks of the things you saw aren't leaving your mind. After a while, you stopped at a motel and sleep for the night. Hoping that in the morning you forget everything.\nGAME OVER")
                            else:
                                print("Insert a valid answer: ")
                    else:
                        allowed_atempts -= 1
                        init_value = 1
                        retry_value = 1
                        failed_value = 1
            else:
                a_value = 1
                print("Insert a valid answer: ")
    else:
        init_value = 1
        print("Insert a valid answer: ")
print("Goodbye\n---------------------------------------------------")