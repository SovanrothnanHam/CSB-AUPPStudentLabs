"""Which data structure model(s) would you choose to implement the music library and playlist features? 
Explain your choices, considering the characteristics of each data structure and the specific requirements of the application.
"""
"""The data structure model(s) that I choose to implement the music library and playlist features are dictionary and list. 
    . In Music Library Class, I use Dictionary: The self.songs attribute is implemented as a dictionary where song titles serve as keys, 
    and the corresponding Song objects are the values. This allows for fast retrieval of songs by title using constant time complexity
    The use of a dictionary in the music library class is efficient for quick lookups by title, supporting functionalities like getting 
    songs by artist, album, genre, or title.
    . In Playlist Class, I usee List: The self.songs attribute is a list, representing the ordered collection of songs in the playlist. 
    Lists are suitable for maintaining an ordered sequence of elements, making it convenient for operations like adding, removing, and 
    reordering songs. A list in the playlist class is appropriate as it preserves the order of songs, crucial for maintaining the desired 
    sequence of tracks. The reorder_songs function leverages list operations to rearrange songs based on the provided order.
"""
class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length
class MusicLibrary:
    def __init__(self):
        self.songs = {}
    
    def add_song(self, song):
        if song.title not in self.songs:
            self.songs[song.title] = song

    def get_songs_by_artist(self, artist):
        return [song for song in self.songs.values() if song.artist == artist]
       
    def get_songs_by_album(self, album):
        return [song for song in self.songs.values() if song.album == album]

    def get_songs_by_genre(self, genre):
        return [song for song in self.songs.values() if song.genre == genre]

    def get_songs_by_title(self, title):
        return self.songs.get(title, None)
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def reorder_songs(self, new_order):
        self.songs = [self.songs[i] for i in new_order]

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for i, song in enumerate(self.songs, start=1):
            print(f"{i}. {song.title} - {song.artist}")
    

# Example Usage
print("Welcome to Mfun music streaming app")
song1 = Song("song 1", "Artist 1", "Album 1", "Genre 1", 3.5)
song2 = Song("song 2", "Artist 2", "Album 2", "Genre 2", 4.0)

music_library = MusicLibrary()
music_library.add_song(song1)
music_library.add_song(song2)
songs_by_artist1 = music_library.get_songs_by_artist("Artist 1")

playlist1 = Playlist("My Playlist 1")
playlist1.add_song(song1)
playlist1.add_song(song2)
# playlist1.remove_song(song1)

playlist1.display_playlist()

print(f"\nSongs by Artist 1:")
for song in songs_by_artist1:
    print(f"{song.title} - {song.album}")
# output 
# Welcome to Mfun music streaming app
# Playlist: My Playlist 1
# 1. song 1 - Artist 1
# 2. song 2 - Artist 2

# Songs by Artist 1:
# song 1 - Album 1


# Reorder the playlist
# print("Welcome to Mfun music streaming app")
# song1 = Song("Title 1", "Artist 1", "Album 1", "Genre 1", 3.5)
# song2 = Song("Title 2", "Artist 2", "Album 2", "Genre 2", 4.0)
# song3 = Song("Title 3", "Artist 3", "Album 3", "Genre 3", 5.2)

# music_library = MusicLibrary()
# music_library.add_song(song1)
# music_library.add_song(song2)
# music_library.add_song(song3)
# songs_by_artist1 = music_library.get_songs_by_artist("Artist 1")
# # Add songs to the playlist
# playlist1 = Playlist("My Playlist 1")
# playlist1.add_song(song1)
# playlist1.add_song(song2)
# playlist1.add_song(song3)
# # Display the original playlist
# print("Original Playlist:")
# playlist1.display_playlist()
# # Define a new order for the songs
# new_order = [2, 1, 0]

# # Reorder the songs in the playlist
# playlist1.reorder_songs(new_order)

# # Display the reordered playlist
# print("\nReordered Playlist:")
# playlist1.display_playlist()
# # output
# # Welcome to Mfun music streaming app
# # Original Playlist:
# # Playlist: My Playlist 1
# # 1. Title 1 - Artist 1
# # 2. Title 2 - Artist 2
# # 3. Title 3 - Artist 3

# # Reordered Playlist:
# # Playlist: My Playlist 1
# # 1. Title 3 - Artist 3
# # 2. Title 2 - Artist 2
# # 3. Title 1 - Artist 1





