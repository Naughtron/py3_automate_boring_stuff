def spam():
    global eggs
    eggs = 'spam' # this is the global assignment for eggs

def bacon():
    eggs = 'bacon' # this is the local assignment for eggs inside bacon()
    
def ham():
    print(eggs) # this will print the global value
    
eggs = 42 
# call spam
spam()

print(eggs) # this should show spam