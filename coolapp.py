# printing using python format
my_goal = "Learn Data Science and Programming"
class_goal = "Make the world a better place"
print(f"I would like to {my_goal}, so that I can {class_goal}!", end=" ")
print("It feels so cool to be able to do this!!", end="\n")

# simple for loop iterating through a list
animal_names = ['Albatross', 'Baboon', 'Camel', 'Donkey', 'Eagle']
for x in animal_names:
    print(x)

# a simple for loop and control flows' grading system
student_grades = [45, 57, 77, 85]
for y in student_grades:
    if y <= 60 and y > 50:
        print('Average')
    elif y > 60:
        print('Excellent')
    else:
        print('Below Average')

# a function to find a substring from a string
def search(text, word):
    if text.find(word) != -1:
        return "Found it"
    else:
        return "Not Found"

text = input("Enter text: ")
word = input("Enter word to search: ")

print(search(text, word))


# keys function to iterate through a dictionary
x = {"First Name": "Dominic", "Last Name": "Muli"}
for key in x.keys():
    print(f"{key}: {x[key]}")

# items function to iterate through a dictionary
x = {"First Name": "Dominic", "Last Name": "Muli"}
for key, value in x.items():
    print(f"{key}: {value}")

# values function to iterate through a dictionary
x = {"First Name": "Dominic", "Last Name": "Muli"}
for value in x.values():
    print(f"{value}")

# python code to get prime numbers of a number
def prime_factors():
    n = int(input("Enter a number: "))
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors())

# python code to calculate greatest common divisor of two numbers
def gcd():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    i = 1
    while(i <= num1 and i <= num2):
        if(num1 % i == 0 and num2 % i == 0):
            gcd = i
        i += 1
    return gcd

print(gcd())

# python code to calculate least common multiple of two numbers
def lcm():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if(num1 > num2):
        greater = num1
    else:
        greater = num2
    while(True):
        if((greater % num1 == 0) and (greater % num2 == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

print(lcm())