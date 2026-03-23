from random import random


class Artist:
    def __init__(self, name, DoB, country):
        self.name = name
        self.DoB = DoB
        self.country = country
        self.list_of_albums = []
        self.list_of_songs = []
    def display_artist(self):
        print(f"Artist Name: {self.name}")
        print(f"Date of Birth: {self.DoB}")
        print(f"Country: {self.country}")
        for artist_album in self.list_of_albums:
            print(f"Album: {artist_album.albumTitle}")
        for track in self.list_of_songs:
            print(f"Song: {track}")
    def add_album(self, song_album):
        self.list_of_albums.append(song_album)
    def add_song(self, artist_song):
        self.list_of_songs.append(artist_song)

class Song:
    def __init__(self, song_title, artist_name, year_of_release):
        self.yearOfRelease = year_of_release
        self.artistName = artist_name
        self.songTitle = song_title
    def display_song(self):
        print(f"Song Title: {self.songTitle}")
        print(f"Artist: {self.artistName}")
        print(f"Year of Release: {self.yearOfRelease}\n")

class Album:
    def __init__(self, album_title, artist_name, year_of_release):
        self.albumTitle = album_title
        self.artistName = artist_name
        self.yearOfRelease = year_of_release
        self.listOfSongs = []

    def display_album(self):
        index = 0
        print(f"Album Title: {self.albumTitle}")
        print(f"Artist: {self.artistName}")
        print(f"Year of Release: {self.yearOfRelease}")
        for i in self.listOfSongs:
            print(f"Song: {index} {i.songTitle}")
            index += 1
    def add_song(self, song_title, year_of_release):
        playlist_song = Song(song_title, self.artistName, year_of_release)
        self.listOfSongs.append(playlist_song)
        return playlist_song


class Playlist:
    def __init__(self, playlist_title):
        self.playlistTitle = playlist_title
        self.listOfSongs = []
    def add_song(self, song):
        self.listOfSongs.append(song)
    def print_all_songs(self):
        index = 0
        for song in self.listOfSongs:
            print(f"Song: {index} {song.songTitle}")
            index += 1
    def sort_playlist(self, order='ASC'):
        self.listOfSongs.sort(key=lambda song: song.songTitle, reverse=(order == 'DESC'))
    def shuffle_playlist(self):
        import random
        random.shuffle(self.listOfSongs)

artist = Artist("Rammstein", "1963", "Germany")
album = Album("Rammstein", artist.name, "2019")
album.add_song("Deutschland", "2019")
album.add_song("Radio", "2019")

artist.add_album(album)
artist.add_song(album.listOfSongs[0])
artist.add_song(album.listOfSongs[1])

playlist = Playlist("Rammstein")
for song in album.listOfSongs:
    playlist.add_song(song)
print("Artist Information:")
print(artist.display_artist())
print("\n\nAlbum Information:")
print(album.display_album())
print("\n\nPlaylist Information:")
playlist.print_all_songs()
print("\n\n Sorted Playlist:")
for song in playlist.listOfSongs:
    playlist.sort_playlist("ASC")
    playlist.print_all_songs()
print("\n\nShuffled Playlist:")
for song in playlist.listOfSongs:
    playlist.shuffle_playlist()
    playlist.print_all_songs()