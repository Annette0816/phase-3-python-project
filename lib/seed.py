from lib.models.artist import Artist
from lib.models.album import Album
from lib.models.song import Song


Artist.drop_table()
Album.drop_table()
Song.drop_table()

Artist.create_table()
Album.create_table()
Song.create_table()
s
artist1 = Artist.create("Aubrey Graham", "Drake")
artist2 = Artist.create("Onika Maraj", "Nicki Minaj")


album1 = Album.create("Take Care", "2011-11-15", artist1)
album2 = Album.create("Pink Friday", "2010-11-22", artist2)


Song.create("Marvins Room", "None", artist1, album1)
Song.create("Moment 4 Life", "Drake", artist2, album2)

print("Database seeded successfully!")
