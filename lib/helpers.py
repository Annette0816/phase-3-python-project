from models.artist import Artist
from models.album import Album
from models.song import Song

def print_artists():
    artists = list(Artist.all.values()) if Artist.all else []
    if not artists:
        print("No artists found.")
    else:
        for artist in artists:
            print(f"[{artist.id}] {artist.name} a.k.a {artist.stage_name}")

def print_albums(artist):
    albums = artist.albums() if artist else []
    if not albums:
        print("No albums found for this artist.")
    else:
        for album in albums:
            print(f"[{album.id}] {album.title} ({album.release_date})")

def print_songs():
    songs = Song.all_songs()
    if not songs:
        print("No songs found.")
    else:
        for song in songs:
            print(f"[{song.id}] {song.title} - {song.artist.stage_name} ft. {song.features}")
