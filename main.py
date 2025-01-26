from .menu import display_menu
from .functions import display_songs, play_song, recommend_by_artist, recommend_by_genre, recommend_by_mood
from .user import sign_up, login

def main():
    """
    Main function to handle user interaction with the system.
    Includes login/signup flow and the main menu loop.
    """
    user = None  # Initialize user as None
    
    # Login or Sign-up flow
    while not user:
        try:
            print("1. Sign Up\n2. Login\n3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                user = sign_up()  # Sign up the user
            elif choice == "2":
                user = login()  # Log in the user
            elif choice == "3":
                print("Exiting the system. Goodbye!")
                return
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred during sign-up/login: {e}")

    # Main Menu loop after successful login or sign-up
    while True:
        try:
            choice = display_menu()  # Display the main menu and get the user's choice

            if choice == 1:
                display_songs()
            elif choice == 2:
                song_title = input("Enter song title to play or 'back' to return: ").strip()
                if song_title.lower() != "back":
                    play_song(user, song_title)  # Pass the user to play the selected song
            elif choice == 3:
                recommend_by_artist(user)  # Recommend songs based on artist for the logged-in user
            elif choice == 4:
                recommend_by_genre(user)  # Recommend songs based on genre for the logged-in user
            elif choice == 5:
                recommend_by_mood(user)  # Recommend songs based on mood using user's history
            elif choice == 6:
                user.listening_history.display_history(user)  # Display the listening history for the logged-in user
            elif choice == 7:
                print("Exiting the system. Goodbye!")
                break  # Exit the main menu loop
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
