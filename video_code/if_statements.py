
# should_continue = True
#
# if should_continue == True:
#     print("Hello!")
#
# known_people = ["John", "Anna", "Mary"]
#
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know this person! {}".format(person))
# else:
#     print("Nope!!{}".format(person))


def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas:")  # John,Rolf,Anna,Greg
    people_list = people.split(",")  # John,Rolf,Anna,Greg

    #people_without_spaces = []
    #for person in people_list:
    #    people_without_spaces.append(person.strip())

    people_without_spaces = [person.strip() for person in people_list]

    return people_without_spaces


def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("You know {}!".format(person))

ask_user()








numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def event_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return eve


