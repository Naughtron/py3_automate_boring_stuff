def spam():
    eggs = 'spam local'
    print(eggs) # this will print the local var from spam()
def bacon():
    eggs = 'bacon local' 
    print(eggs) # this will print the local var from bacon()
    # now call spam
    spam()
    print(eggs) # this will now print spam()s version of eggs

eggs = 'global'
bacon()
print(eggs) # this will print global 