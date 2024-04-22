with open("hr_system.txt") as human_resources_list:
    for human_elements in human_resources_list:
        human_elements = human_elements.split(" ")
        person_name = human_elements[0]
        id_number = human_elements[1]
        person_title = human_elements[2]
        salary = float(human_elements[3])
        paycheck = salary/24
        if person_title == "Engineer":
            paycheck += 1000
        print(f"Name: {person_name}; ID: {id_number}; Job title: {person_title}; Paycheck: ${paycheck:.2f}")