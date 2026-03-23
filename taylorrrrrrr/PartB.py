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


if __name__ == '__main__':
    unittest.main()
