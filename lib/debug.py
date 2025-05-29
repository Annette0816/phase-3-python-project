
from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.album import Album
from models.song import Song
import ipdb


Song.drop_table()
Album.drop_table()
Artist.drop_table()

Artist.create_table()
Album.create_table()
Song.create_table()

artist = Artist.create("Beyoncé Knowles", "Beyoncé")
album = Album.create("Renaissance", "2022-07-29",artist)
song = Song.create("Break My Soul", "ft. Beyoncé", artist, album)

ipdb.set_trace()
