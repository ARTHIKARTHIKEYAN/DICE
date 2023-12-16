import random

def roll_dice(num_dice, num_sides):
    results = []
    for _ in range(num_dice):
        roll_result = random.randint(1, num_sides)
        results.append(roll_result)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        try:
            num_dice = int(input("Enter the number of dice: "))
            num_sides = int(input("Enter the number of sides on each die: "))
            
            if num_dice <= 0 or num_sides <= 0:
                raise ValueError("Please enter positive values for the number of dice and sides.")
            
            dice_results = roll_dice(num_dice, num_sides)
            
            print(f"\nResults of rolling {num_dice} dice with {num_sides} sides:")
            print(dice_results)
        
        except ValueError as ve:
            print(f"Error: {ve}")
        
        play_again = input("\nDo you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for using the Dice Rolling Simulator. THANKS FOR PLAYING WITH ME!")
            break

if __name__ == "__main__":
    main()
