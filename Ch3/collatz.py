# define function with number param
def collatz(num):
    if num % 2 == 0: # even number
        print(num // 2)
        return num // 2

    elif num % 2 == 1: # odd number
        result = 3 * num + 1
        print(result)
        return result

# request number from user
user_input = input("Please enter a number: ")
try:
    # keep looping through until number is 1
    while user_input != 1:
        user_input = collatz(int(user_input))
except ValueError:
    print("Please enter an integer")
