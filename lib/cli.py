from models.__init__ import CONN
from models.artist import Artist
from models.album import Album
from models.song import Song
from helpers import print_artists, print_albums, print_songs

def create_artist():
    name = input("Enter artist's real name: ")
    stage_name = input("Enter artist's stage name: ")
    artist = Artist.create(name, stage_name)
    CONN.commit()
    print("Artist created!")

def create_album():
    print_artists()
    artist_id = input("Enter artist ID for the album: ")
    artist = Artist.find_by_id(int(artist_id))
    if not artist:
        print("Artist not found.")
        return
    title = input("Enter album title: ")
    release_date = input("Enter release date (YYYY-MM-DD): ")
    album = Album.create(title, release_date, artist)
    CONN.commit()
    print(" Album created!")

def create_song():
    print_artists()
    artist_id = input("Enter artist ID for the song: ")
    artist = Artist.find_by_id(int(artist_id))
    if not artist:
        print(" Artist not found.")
        return

    print_albums(artist)
    album_id = input("Enter album ID for the song: ")
    album = Album.find_by_id(int(album_id))
    if not album:
        print(" Album not found.")
        return

    title = input("Enter song title: ")
    features = input("Enter featured artists (or leave blank): ")
    song = Song.create(title, features, artist, album)
    CONN.commit()
    print("Song created!")

def view_all_artists():
    print(" All Artists:")
    print_artists()

def view_artist_albums():
    print_artists()
    artist_id = input("Enter artist ID to view albums: ")
    artist = Artist.find_by_id(int(artist_id))
    if artist:
        print_albums(artist)
    else:
        print("Artist not found.")

def view_all_songs():
    print(" All Songs:")
    print_songs()

def main():
    while True:
        print(" Record Label CLI")
        print("1. Create Artist")
        print("2. Create Album")
        print("3. Create Song")
        print("4. View All Artists")
        print("5. View Artist's Albums")
        print("6. View All Songs")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_artist()
        elif choice == "2":
            create_album()
        elif choice == "3":
            create_song()
        elif choice == "4":
            view_all_artists()
        elif choice == "5":
            view_artist_albums()
        elif choice == "6":
            view_all_songs()
        elif choice == "7":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
