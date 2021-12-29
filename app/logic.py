import sys
import random

sys.path.insert(1, '/lottery/')

user_numbers = []
random_range = [*range(1,49,1)]

print("Welcome in lotto simulator")
print("Please write 6 numbers in range from 1 to 49")

def get_user_numbers(user_numbers,random_range):
    a, b, c, d, e, f = list(map(int, input().split()))
    user_numbers.append(a)
    user_numbers.append(b)
    user_numbers.append(c)
    user_numbers.append(d)
    user_numbers.append(e)
    user_numbers.append(f)

    for element in user_numbers:
        if element not in random_range:
            return False
        else:
            return True

while get_user_numbers(user_numbers, random_range) == True:
    # print(len(user_numbers))
    if len(user_numbers) != 6:
        print("Wrong ammount of numbers ", len(user_numbers), ". You need to write 6 numbers.")
        import main
# else:
#     print("Numbers out of range 1-49.")
#     import main

    else:
        generated_values =[random.randrange(1,49,1)for i in range(6)]
        print(generated_values)
        break
