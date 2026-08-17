import random

print("Welcome to Dice Rolling World Game")
print("==================================")

while True:
    roll_choice = input("Roll the dice? (y/n): ").strip().lower()

    if (roll_choice != 'y') and (roll_choice != 'n'):
        print('Invalid choice!')

    elif roll_choice == 'y':
        rand_num1 = random.randint(1, 6)
        rand_num2 = random.randint(1, 6)
        print(f"({rand_num1}, {rand_num2})")
        continue

    else:
        print("Thanks for playing!")
        print("Exiting the program ...")
        break


    






