import random

def guess_number():
    secret_number = random.randint(1, 20)
    guess_count = 0
    guess = 0
    
    while guess != secret_number:
        guess = int(input("Guess a number between 1 and 20: "))
        guess_count += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the secret number in" + str(guess_count) + "guesses!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        guess_number()
    else:
        print("Thanks for playing!")
        
guess_number()