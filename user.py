import json
from .history import ListeningHistory  # Import ListeningHistory

class User:
    def __init__(self, username, password):
        """
        Initialize a new User instance.
        
        Parameters:
            username (str): The username of the user.
            password (str): The user's password.
        """
        self.username = username
        self.password = password
        self.listening_history = ListeningHistory()  # Initialize a listening history instance

    def add_to_history(self, song_title):
        """
        Add a song to the user's listening history.

        Parameters:
            song_title (str): The title of the song to add.
        """
        try:
            self.listening_history.add_to_history(self.username, song_title)  # Use username as key for history
            self.save_history_to_json()  # Save history after adding a song
        except Exception as e:
            print(f"Error while adding song to history: {e}")

    def save_history_to_json(self):
        """
        Save the listening history to the JSON file after an update.
        """
        users = load_users()  # Load existing users
        if self.username in users:
            users[self.username]["listening_history"] = list(self.listening_history.user_history.get(self.username, []))
            save_users(users)  # Save updated users with history

    def to_dict(self):
        """
        Convert the User instance to a dictionary for saving to JSON.
        
        Returns:
            dict: A dictionary representation of the user.
        """
        try:
            return {
                "username": self.username,
                "password": self.password,
                "listening_history": self.listening_history.user_history.get(self.username, []),
            }
        except Exception as e:
            print(f"Error while converting user data to dictionary: {e}")
            return {}

# Load users from file
def load_users():
    """
    Load users from the JSON file.

    Returns:
        dict: A dictionary of users loaded from the file.
    """
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No users file found. Returning an empty dictionary.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding the users file. Returning an empty dictionary.")
        return {}
    except Exception as e:
        print(f"An error occurred while loading users: {e}")
        return {}

# Save users to file
def save_users(users):
    """
    Save users to the JSON file.

    Parameters:
        users (dict): A dictionary of users to save.
    """
    try:
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving users: {e}")

# Sign-up function
def sign_up():
    """
    Handle the sign-up process for a new user.

    Returns:
        User: The newly created User instance or None if unsuccessful.
    """
    try:
        users = load_users()
        username = input("Enter a username: ")
        if username in users:
            print("Username already exists. Please choose a different username.")
            return None
        password = input("Enter a password: ")
        new_user = User(username, password)
        users[username] = new_user.to_dict()
        save_users(users)
        print("Sign-up successful!")
        return new_user
    except Exception as e:
        print(f"An error occurred during sign-up: {e}")
        return None

# Login function
def login():
    """
    Handle the login process for an existing user.

    Returns:
        User: The logged-in User instance or None if unsuccessful.
    """
    try:
        users = load_users()
        username = input("Enter your username: ")
        if username not in users:
            print("No such user found. Please sign up first.")
            return None
        password = input("Enter your password: ")
        if users[username]["password"] == password:
            print("Login successful!")
            user = User(username, password)
            # Restore listening history for the logged-in user
            history = users[username].get("listening_history", [])
            user.listening_history.user_history[username] = history
            return user
        else:
            print("Incorrect password. Try again.")
            return None
    except Exception as e:
        print(f"An error occurred during login: {e}")
        return None
