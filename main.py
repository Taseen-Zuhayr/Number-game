import random
computerguess = random.randint(1,10)
print("I have my number.")

while True:
    userguess = int(input("Enter your guess here : "))
    if userguess==computerguess:
        print("Congrats! You guessed the same number.")
    else:
        print("The computer made the guess ",computerguess)
        print("Try again!")