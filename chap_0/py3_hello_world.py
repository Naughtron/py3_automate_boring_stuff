# python 3 hello world!

print('Hello World!')
print('What is your name? ')
usr_name = input()

print('Hey duder, its good to meet you, ' + usr_name)
name_len = len(usr_name)
print('Did you know that the length of your name is: ' + str(name_len))

print("If you don't mind me asking, what is your age? ")
usr_age = input()

print('You will be ' + str(int(usr_age) + 1) + ' in a year.')
