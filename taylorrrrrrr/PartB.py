import unittest
from PartA import Album, Artist, Song, Playlist

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Rammstein", "1995", "Germany")
        self.song = Song("Liebe Ist Fur ALle Da", "Rammstein", 2009)
        self.album = Album("Liebe Ist Fur Alle Da", "Rammstein", 2009)
        self.playlist = Playlist("Rammstein songs")
    def test_artist_instance(self):
        self.assertTrue(isinstance(self.artist, Artist))
    def test_song_instance(self):
        self.assertTrue(isinstance(self.song, Song))
    def test_album_instance(self):
        self.assertTrue(isinstance(self.album, Album))
    def test_playlist_instance(self):
        self.assertTrue(isinstance(self.playlist, Playlist))
    def test_artist_not_song(self):
        self.assertNotIsInstance(self.artist, Song)
    def test_song_not_artist(self):
        self.assertNotIsInstance(self.song, Artist)
    def test_album_not_playlist(self):
        self.assertNotIsInstance(self.album, Playlist)
    def test_playlist_not_album(self):
        self.assertNotIsInstance(self.playlist, Album)

    def test_identical_song(self):
        song1 = Song("Liebe Ist Fur Alle Da", "Rammstein", 2009)
        song2 = song1
        self.assertEqual(song1, song2)
    def test_similar_song(self):
        song1 = Song("Du Hast", "Rammstein", 1998)
        song2 = Song("Du Hast", "Rammstein", 1998)
        self.assertNotEqual(song1, song2)

    #Method tests
    def test_artist_add_song(self):
        self.artist.add_song(self.song)
        self.assertIn(self.song, self.artist.list_of_songs)
    def test_artist_add_album(self):
        self.artist.add_album(self.album)
        self.assertIn(self.album, self.artist.list_of_albums)
    def test_album_add_song(self):
        self.album.add_song("Liebe Ist Fur Alle Da", 2009)
        self.assertEqual(len(self.album.listOfSongs), 1)
    def test_playlist_add_song(self):
        self.playlist.add_song(self.song)
        self.assertIn(self.song, self.playlist.listOfSongs)
    def test_sort_playlist_asc(self):
        self.playlist.add_song(Song("Liebe Ist Fur Alle Da", "Rammstein", 2009))
        self.playlist.add_song(Song("Du Hast", "Rammstein", 1998))
        self.playlist.sort_playlist("ASC")
        self.assertEqual(self.playlist.listOfSongs[0].songTitle, "Du Hast")
    def test_sort_playlist_desc(self):
        self.playlist.add_song(Song("Liebe Ist Fur Alle Da", "Rammstein", 2009))
        self.playlist.add_song(Song("Du Hast", "Rammstein", 1998))
        self.playlist.sort_playlist("DESC")
        self.assertEqual(self.playlist.listOfSongs[0].songTitle, "Liebe Ist Fur Alle Da")
    def test_shuffle_playlist(self):
        self.playlist.add_song(Song("A", "Artist", 2020))
        self.playlist.add_song(Song("B", "Artist", 2020))
        self.playlist.add_song(Song("C", "Artist", 2020))
        original_order = [
            song.songTitle
            for song in self.playlist.listOfSongs
        ]
        self.playlist.shuffle_playlist()
        shuffled_order = [
            song.songTitle
            for song in self.playlist.listOfSongs
        ]
        self.assertNotEqual(original_order, shuffled_order)

if __name__ == '__main__':
    unittest.main()
