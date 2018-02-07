def spam():
    global eggs
    eggs = "spam" # this is the global var

def bacon():
    eggs = "bacon" # this is a local var

def ham():
    print(eggs) # this is the global var

eggs = 42 # this is the global var
spam()
print(eggs)
