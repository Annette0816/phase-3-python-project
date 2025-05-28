from models.__init__ import CURSOR, CONN

class Song:
    all = {}

    def __init__(self, title, features, artist, album, id=None):
        self.id = id
        self.title = title
        self.features = features
        self.artist = artist
        self.album= album

    def __repr__(self):
        return f"<Song {self.id}: {self.title} ft. {self.features}>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value):
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string.")
  
    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, value):
        if isinstance(value, str) and len(value):
            self._features = value
        else:
            raise ValueError("Features must be a non-empty string.")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                features TEXT ,
                artist_id INTEGER,
                album_id INTEGER,
                FOREIGN KEY (artist_id) REFERENCES artists(id),
                FOREIGN KEY (album_id) REFERENCES albums(id)
)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS songs")
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (title, features, album_id, artist_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.title,self.features ,self.album.id, self.artist.id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, features, album , artist):
        song = cls(title, features, album, artist)
        song.save()
        return song

    @classmethod
    def find_by_id(cls, id):
        row = CURSOR.execute("SELECT * FROM songs WHERE id = ?", (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        row = CURSOR.execute("SELECT * FROM songs WHERE title = ?", (title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_features(cls, features):
        row = CURSOR.execute("SELECT * FROM songs WHERE features = ?", (features,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_artist(cls, artist):
        row = CURSOR.execute("SELECT * FROM songs WHERE artist_id = ?", (artist.id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_album(cls, album):
        row = CURSOR.execute("SELECT * FROM songs WHERE album_id = ?", (album.id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def all_songs(cls):
        rows = CURSOR.execute("SELECT * FROM songs").fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        from models.artist import Artist
        from models.album import Album
        artist = Artist.find_by_id(row["artist_id"])
        album = Album.find_by_id(row["album_id"])
        return cls(row["title"], row["features"], artist, album, row["id"])
