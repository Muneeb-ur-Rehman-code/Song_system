from .functions import clear_screen

def display_menu():
    clear_screen()
    print("=======================")
    print("   Music Recommendation   ")
    print("=======================\n")
    print("1. Display All Songs")
    print("2. Play a Song by Title")
    print("3. Recommend Songs by Artist")
    print("4. Recommend Songs by Genre")
    print("5. Recommend Songs by Mood")
    print("6. Recently Played Recommendations")
    print("7. Exit")
    
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
