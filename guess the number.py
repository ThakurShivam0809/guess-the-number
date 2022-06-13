import random

def game(x,y):
    random_number = random.randint(x, y)
    guess = 0
    while guess != random_number:
        guess = int(input("Enter your random guess: "))
        if guess < random_number:
            print("Incorrect! Think of a greater umber.")
        elif guess > random_number:
            print("Incorrect! Think of a smaller number")
    print(" Correct! You have guessed the correct number.")

def compgame(l,u):
    print("If the guessed number is correct, enter 'c'\nIf the guessed number is greater than your number, enter 'ig'\
\nIf the guessed number is lower than your number, enter 'il' ")
    cond = 'i'
    while cond != 'c':
        rn = random.randint(l,u)
        print(rn)
        cond = input()
        if cond == 'ig':
            u = rn - 1
        elif cond == 'il':
            l = rn + 1    
        else: 
            print(" oops! incorrect input")    

    print("The computer guessed correctly")
      
a = int(input("enter the lower limit: "))
b = int(input("enter the upper limit: "))
compgame(a,b)                 