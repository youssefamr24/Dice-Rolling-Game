import random

print("Welcome to Dice Rolling World Game")
print("==================================")
counter = 0
while True:
    # User input for how many dice he wants to roll.
    nums_dice = int(input("How many dice do you want to roll? "))

    # Validates that the number of rolling dice is +ve
    if nums_dice == 0 or nums_dice <= 0:
        print("Please enter a postive number.")
        continue

    # User input for rolling the dice or not.
    roll_choice = input("Roll the dice? (y/n): ").strip().lower()

    # Checks if choice is anything except yes or no then it will be invalid choice.
    if (roll_choice != 'y') and (roll_choice != 'n'):
        print('Invalid choice!')

    # Checks if choice is yes then save the random numbers in a list and increment the counter and print the list.
    elif roll_choice == 'y':
        counter += 1
        dice_rolls = [random.randint(1, 6) for _ in range(nums_dice)]
        print(tuple(dice_rolls))
        continue

    else:
        print(f"You have rolled the dice {counter} times. ")
        print("Thanks for playing!")
        print("Exiting the program ...")
        break
