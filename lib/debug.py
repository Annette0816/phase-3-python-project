import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lib.models.__init__ import CONN, CURSOR
from lib.models.artist import Artist
from lib.models.album import Album
from lib.models.song import Song
import ipdb


Song.drop_table()
Album.drop_table()
Artist.drop_table()

Artist.create_table()
Album.create_table()
Song.create_table()

artist = Artist.create("Beyoncé Knowles", "Beyoncé")
album = Album.create("Renaissance", "2022")
song = Song.create("Break My Soul", "ft. Beyoncé", artist, album)

ipdb.set_trace()
