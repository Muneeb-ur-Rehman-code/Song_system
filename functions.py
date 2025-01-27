import os
import time
import pyglet
import pygame
from .song import songs
from .history import ListeningHistory
from .mood_map import mood_map
import threading

# Initialize pyglet player
player = pyglet.media.Player()
player.volume = 1.0  # Default volume

# Initialize pygame for event handling
pygame.init()

# Initialize the listening history
listening_history = ListeningHistory()

def clear_screen():
    """Clear the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')
def play_song(user, song_title):
    """
    Play a song for the user and add it to their listening history.
    
    Parameters:
        user (User): The logged-in user.
        song_title (str): The title of the song to be played.
    """
    try:
        found = False

        # Check if the song title exists in the song list
        for song in songs:
            if song.title == song_title:
                found = True
                print(f"Now Playing: {song.title} by {song.artist}")
                print("Press Enter to stop and return to the menu.")

                user.add_to_history(song_title)  # Add to the user's history

                # Check if the file exists
                if os.path.isfile(song.filepath):
                    # Load the song file using pyglet
                    source = pyglet.media.load(song.filepath)
                    player.queue(source)
                    player.play()

                    # Wait for the user to press Enter to stop the song
                    input("Press Enter to stop and return to the menu.")
                    
                    # Stop the song
                    player.pause()
                    print("Stopping the song and returning to the menu...")

                else:
                    print("Song file not found. Playing without audio.")
                break  # Exit the loop after the song is found and played

        if not found:
            print("Song not found.")
            return  # Exit the function if the song wasn't found

    except Exception as e:
        # Handle any exception that occurs
        print(f"An error occurred: {str(e)}")

    # Wait for the user to press Enter before returning to the main menu
    print("Returning to the menu...\n")
    time.sleep(1)  # Optional: sleep for a short time to avoid rapid menu transition
    
def recommend_by_artist(user):
    """
    Recommend songs by a specific artist.

    Parameters:
        user (User): The logged-in user.
    """
    clear_screen()
    displayed_artists = set()
    for song in songs:
        if song.artist not in displayed_artists:
            print(f"- {song.artist}")
            displayed_artists.add(song.artist)

    artist = input("\nEnter an artist to see songs or 'back' to return: ")
    if artist == "back":
        return
    
    found = False
    for song in songs:
        if song.artist.lower() == artist.lower():  # Case-insensitive match
            print(f"- {song.title} [{song.genre}]")
            found = True
    
    if not found:
        print("No songs found by this artist.")

def recommend_by_genre(user):
    """
    Recommend songs by a specific genre.

    Parameters:
        user (User): The logged-in user.
    """
    clear_screen()
    displayed_genres = set()
    for song in songs:
        if song.genre not in displayed_genres:
            print(f"- {song.genre}")
            displayed_genres.add(song.genre)

    genre = input("\nEnter a genre to see songs or 'back' to return: ")
    if genre == "back":
        return
    
    found = False
    for song in songs:
        if song.genre.lower() == genre.lower():  # Case-insensitive match
            print(f"- {song.title} by {song.artist}")
            found = True
    
    if not found:
        print("No songs found in this genre.")

def recommend_by_mood(user):
    """
    Recommend songs based on the user's mood.

    Parameters:
        user (User): The logged-in user.
    """
    clear_screen()
    displayed_moods = set()
    for genre, mood in mood_map.items():
        if mood not in displayed_moods:
            print(f"- {mood}")
            displayed_moods.add(mood)

    mood = input("\nEnter a mood to see songs or 'back' to return: ")
    if mood == "back":
        return

    found = False
    for genre, mood_value in mood_map.items():
        if mood_value.lower() == mood.lower():  # Case-insensitive match
            for song in songs:
                if song.genre == genre:
                    print(f"- {song.title} by {song.artist}")
                    found = True

    if not found:
        print("No songs found for this mood.")

def display_songs():
    """
    Display a list of all available songs.

    """
    clear_screen()
    print("==== List of Songs ====")
    for index, song in enumerate(songs):
        print(f"{index + 1}. {song.title} - {song.artist} [{song.genre}]")
