import random

print('Password Generator')

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"£$%^&*()'

number = int(input('Number Of Passwords To Generate: '))
length = int(input('What is the length of the Password: '))

passwords = []

print('\nHere are your Options:')
for i in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(f'{i+1}: {password}')
    passwords.append(password)

choice = int(input('\nSelect the number corresponding to the password you want to save: '))

if choice < 1 or choice > number:
    print('Invalid selection')
else:
    selected_password = passwords[choice - 1]
    filename = "userpasses.txt"
    with open(filename, 'w') as file:
        file.write(selected_password)
        print(f'Password saved to {filename} successfully.')
