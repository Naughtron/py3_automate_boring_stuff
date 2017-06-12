# create a init list
dogNames = []
# always run 
while True:
    print('Enter the name of a dog' + str(len(dogNames) + 1) +
          '(or enter nothing to stop)')
    
    # break out if the user enters an empty string
    name = input()
    if name == '':
        break
    
    dogNames = dogNames + [name] # this adds to the list

print('The dog names are:')
for name in dogNames:
    print('' + name)