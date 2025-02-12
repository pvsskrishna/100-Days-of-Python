import random
import string

lower = list(string.ascii_lowercase)

numbers = []
for num in range(0,10):
    numbers += str(num)

symbols = ['!','#','$','%','&','*','(',')','+']
print(symbols)

print('Welcome to the PyPassword Generator!')
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))

Password = ""
for char in range(1,nr_letters+1):
    Password += random.choice(lower)

for num in range(1,nr_numbers+1):
    Password += random.choice(numbers)

for symbol in range(1,nr_symbols+1):
    Password += random.choice(symbols)

print(Password)

Password_list = []
for char in range(1,nr_letters+1):
    Password_list.append(random.choice(lower))

for num in range(1,nr_numbers+1):
    Password_list.append(random.choice(numbers))

for symbol in range(1,nr_symbols+1):
    Password_list.append(random.choice(symbols))

print(Password_list)
random.shuffle(Password_list)
print(Password_list)

new_password = ""
for shuffle_key in Password_list:
    new_password += shuffle_key
print(new_password)
