# testers Notes
print("Welcome... (all the choices answers are in caps)")
init_value = 1
while (init_value > 0):
    answer_main_menu = input("Do you want to play the game?")
    if(answer_main_menu.lower() == "no"):
        init_value = 0
    elif(answer_main_menu.lower() == "yes"):
        init_value = 0
        print("You are traveling alone in your car in the middle of the night near the deviation to the old town on old Route 13...\nWhile you were distracted by the radio, your pickup impacted something; you stopped immediately and saw how the thing you hit flew for a few meters and wondered what was that, you turned on the fog lights and saw that thing isn't a human or an animal. You disembarked the vehicle and looked with horror at that thing in the distance. One part of you thinks that TAKING A CLOSER LOOK will be helpful to kill your curiosity about what you hit, but; another part of you knows that STAYING NEAR THE PICKUP and BOARDING THE PICKUP are the safest choice.")
        main_road_desition_01 = input("What are you going to do?")
        if(main_road_desition_01.lower() == "take a closer look" or main_road_desition_01.lower() == "taking a closer look"):
            print("The thing started growling and moving. You panicked and began running back towards the pickup but... -test entry-")
            main_road_desition_02A = input("GAME OVER")
            if(main_road_desition_02A.lower() == "game over"):
                print("-test entry-")
                init_value = 1
            else:
                print(f"Thinking outside the box isn't a good idea, especially against a group of unidentified monsters\nGAME OVER")
            init_value = 1
        if(main_road_desition_01.lower() == "get in the pickup" or main_road_desition_01.lower() == "boarding the pickup"):
            print("-test entry-")
            main_road_desition_02B = input("RUN OVER IT / FULL REVERSE")
            if(main_road_desition_02B.lower() == "run over it"):
                print("you killed it...")
                init_value = 1
            elif(main_road_desition_02B.lower() == "full reverse"):
                print("You panicked and hit a tree, now that thing and others monsters are running towards you and the pickup isn't responding... The end is near...\n-test entry-")
                init_value = 1
            else:
                print(f"Thinking outside the box isn't a good idea, especially against a group of unidentified monsters\nGAME OVER")
            init_value = 1
        if(main_road_desition_01.lower() == "staying near the pickup" or main_road_desition_01.lower() == "stay near the pickup"):
            print("-test entry-")
            main_road_desition_02C = input("RUN TO THE TREES / RUN TO THE ROAD")
            if(main_road_desition_02C.lower() == "run to the trees"):
                print("-test entry-")
                init_value = 1
            elif(main_road_desition_02C.lower() == "run to the road"):
                print("-test entry-...\nGAME OVER")
                init_value = 1
            else:
                print(f"Thinking outside the box isn't a good idea, especially against a group of unidentified monsters\nGAME OVER")
            init_value = 1
        else:
            print(f"Thinking outside the box isn't a good idea, especially against a group of unidentified monsters\nGAME OVER")
            init_value = 1
    else:
        print("Insert a valid answer")
        init_value = 1
print()