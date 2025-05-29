from models.__init__ import CURSOR, CONN
from models.artist import Artist
class Album:
    all = {}

    def __init__(self, title, release_date, artist, id=None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.artist = artist

    def __repr__(self):
        return f"<Album {self.id}: {self.title}  {self.release_date} by {self.artist.stage_name}>"

    @property
    def title(self):
        return self._title

    @title.setter
    def  title(self, value):
        if isinstance(value, str) and len(value):
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string.")

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        if isinstance(value, str) and len(value):
            self._release_date = value
        else:
            raise ValueError("Release date must be a non-empty string.")

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        from models.artist import Artist
        if isinstance(value, Artist):
            self._artist = value
        else:
            raise ValueError("Artist must be an instance of Artist.")
   
    def songs(self):
     from lib.models.song import Song
     return [song for song in Song.all.values() if song.album.id == self.id]

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS albums (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                release_date TEXT NOT NULL,
                artist_id INTEGER,
                FOREIGN KEY (artist_id) REFERENCES artists(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS albums")
        CONN.commit()

    def save(self):
       sql = """
        INSERT INTO albums (title, release_date, artist_id)
        VALUES (?, ?, ?)
    """
       CURSOR.execute(sql, (self.title, self.release_date, self.artist.id))
       CONN.commit()
       self.id = CURSOR.lastrowid
       type(self).all[self.id] = self

    @classmethod
    def create(cls, title, release_date, artist):
     album = cls(title, release_date, artist)
     album.save()
     return album

    @classmethod
    def find_by_id(cls, id):
        row = CURSOR.execute("SELECT * FROM albums WHERE id = ?", (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        row = CURSOR.execute("SELECT * FROM albums WHERE title = ?", (title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_release_date(cls, release_date):
        row = CURSOR.execute("SELECT * FROM albums WHERE release_date = ?", (release_date,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def all_albums(cls):
        rows = CURSOR.execute("SELECT * FROM albums").fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    
    @classmethod
    def instance_from_db(cls, row):
         artist = Artist.find_by_id(row["artist_id"])
         if not artist:
                raise ValueError(f"Artist with id {row['artist_id']} not found.")
         return cls(row["title"], row["release_date"],artist, row["id"])

   