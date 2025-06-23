import random

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\n")
target = random.randint(1, 100)

# Loop until a valid difficulty level is selected
while True:
    try:
        level = int(input("Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)\n"))
        match level:
            case 1:
                chances = 10
                break
            case 2:
                chances = 5
                break
            case 3:
                chances = 3
                break
            case _:
                print("Invalid input. Please enter 1, 2, or 3.\n")
    except ValueError:
        print("Please enter a valid number (1, 2, or 3).\n")

print(f"You have {chances} chances to guess the correct number.")



guess_count = 0

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        
        if guess < 1 or guess > 100:
            print("Invalid input. Please enter a number between 1 and 100.\n")
            continue

        guess_count += 1

        if guess > target:
            print(f"Incorrect! The number is less than {guess}")
        elif guess < target:
            print(f"Incorrect! The number is greater than {guess}")
        else:
            print(f"Congratulations! You guessed the correct number in {guess_count} attempt(s).")
            break

        if guess_count == chances:
            print(f"You've used all {chances} chances. The correct number was {target}.")
            break

    except ValueError:
        print("Please enter a valid number (1-100).\n")
