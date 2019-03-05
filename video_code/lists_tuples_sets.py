
my_variable = "hello"

#A list, a mutible collection can be appended:
list_grades = [77, 80, 90]

#A tuple, an immutable collection:
tuple_grades = (77, 80, 90)

#A set, unique and unordered
set_grades = {77, 80, 90}

print(set_grades)

#adding a few elements to the list_grades collection
list_grades.append(100) #adding 100
print(list_grades)

#Adding a number to the tuple
tuple_grades = tuple_grades + (100,) #comma is needed
tuple_grades = tuple_grades + (105, 107) # no need for additional comma after 2nd
print(tuple_grades)

#changing an element in the list group
list_grades[0] = 60
print(list_grades)

#adding to the set
set_grades.add(60)
print(set_grades)
set_grades.add(60) #this won't have any effect on the printed version as two of the same does not appear
print(set_grades)

#finding a match/matches between the variables in two sets
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_numbers)) #printing the matched numbers between each,
#another set is produced with the matching numbers

print(your_lottery_numbers.union(winning_numbers)) #printing the matched AND other numbers left over, 1 of each variable

#the difference between two sets
print({1, 2, 3, 4}.difference({1, 2}))
