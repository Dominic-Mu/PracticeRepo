my_goal = "Learn Data Science and Programming"
class_goal = "Make the world a better place"
print(f"I would like to {my_goal}, so that I can {class_goal}!", end=" ")
print("It feels so cool to be able to do this!!", end="\n")

animal_names = ['Albatross', 'Baboon', 'Camel', 'Donkey', 'Eagle']
for x in animal_names:
    print(x)

student_grades = [45, 57, 77, 85]
for y in student_grades:
    if y <= 60 and y > 50:
        print('Average')
    elif y > 60:
        print('Excellent')
    else:
        print('Below Average')