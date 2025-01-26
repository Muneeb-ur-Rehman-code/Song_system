import json
from collections import deque

class ListeningHistory:
    def __init__(self, max_size=5, filename="history.json"):
        """
        Initialize the ListeningHistory class with a user-specific song history.
        Each user's history is loaded from a JSON file and stored as a deque with a maximum size.
        
        Parameters:
            max_size (int): The maximum number of songs to keep in the history for each user.
            filename (str): The path to the JSON file to store and retrieve the history.
        """
        self.max_size = max_size
        self.filename = filename
        self.user_history = self.load_history()

    def load_history(self):
        """
        Load the history from the JSON file.
        
        Returns:
            dict: A dictionary where each key is a username and the value is the deque of song history.
        """
        try:
            with open(self.filename, 'r') as file:
                history_data = json.load(file)
                # Convert lists to deques
                for user, songs in history_data.items():
                    history_data[user] = deque(songs, maxlen=self.max_size)
                return history_data
        except FileNotFoundError:
            return {}  # If the file doesn't exist, return an empty history
        except json.JSONDecodeError:
            return {}  # If the file is empty or corrupt, return an empty history

    def save_history(self):
        """
        Save the history to the JSON file.
        """
        try:
            with open(self.filename, 'w') as file:
                # Convert deques back to lists for saving to JSON
                history_data = {user: list(songs) for user, songs in self.user_history.items()}
                json.dump(history_data, file, indent=4)
        except Exception as e:
            print(f"Error saving history to file: {e}")

    def add_to_history(self, user, song_title):
        """
        Add a song to the user's listening history.
        
        Parameters:
            user (str or User): The user object or username string.
            song_title (str): The title of the song to add.
        """
        username = getattr(user, "username", user)  # Handle both User objects and plain usernames
        if username not in self.user_history:
            self.user_history[username] = deque(maxlen=self.max_size)
        
        self.user_history[username].append(song_title)
        self.save_history()  # Save the history after each update

    def display_history(self, user):
        """
        Display the recent songs played by the user.
        
        Parameters:
            user (str or User): The user object or username string.
        """
        username = getattr(user, "username", user)  # Handle both User objects and plain usernames
        if username not in self.user_history or not self.user_history[username]:
            print(f"No recent songs played for user {username}.")
        else:
            print(f"Recent songs for {username}:")
            for song in self.user_history[username]:
                print(f"- {song}")
        
        # Wait for user to press Enter to exit and return to the menu
        input("Press Enter to exit and return to the menu.")

    def get_history(self, user):
        """
        Retrieve the user's listening history as a list.
        
        Parameters:
            user (str or User): The user object or username string.
            
        Returns:
            list: The listening history for the user.
        """
        username = getattr(user, "username", user)  # Handle both User objects and plain usernames
        return list(self.user_history.get(username, []))
