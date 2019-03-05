
my_list = [0, 1, 2, 3, 4]
and_equal_list = [x for x in range(5)]

multiple_list = [x * 3 for x in range(5)]

print(multiple_list)
print(8 % 3)
print(9 % 2)
print([n for n in range(10) if n % 2 == 0])

people_you_know = ["Rolf", " John", "anna", "GREG"]
NORMALIZED_PEOPLE = [person.strip().lower()  for person in people_you_know]
print(NORMALIZED_PEOPLE)
