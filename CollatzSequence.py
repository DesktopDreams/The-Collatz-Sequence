# The Collatz Sequence Tool
#This function performs the CST.
def collatz(): 
    global number 
    #Determines if user input is even or odd, which then performs a specific operation on it.
    if number % 2 == 0: 
        number = number // 2
        print(number)
    elif number % 2 == 1:
        number = number * 3 + 1
        print(number)

print('Welcome to Collatz Sequence')
#Program to make sure user input are in valid intergers.
while True:
    try:
        print('Please enter a valid digits')
        number = int(input()) #Converts user input to intergers
    except ValueError: #Filters the error messages
        print('Sorry, valid digits only!')
        continue
    if number <= 1: #Preventing negatives, 0, and 1.
        print('Sorry, no invalid numbers!')
        continue
    else:
        break

#Program to keep calling collatz() until it reaches 1
while True:
    if number == 1:
        print('With TCS, numbers will always end up as 1!')
        break
    else:
        collatz()
