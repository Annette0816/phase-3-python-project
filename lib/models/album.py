from models.__init__ import CURSOR, CONN

class Album:
    all = {}

    def __init__(self, title, genre, id=None):
        self.id = id
        self.title = title
        self.genre = genre
       

    def __repr__(self):
        return f"<Album {self.id}: {self.title} : {self.genre}>"

    # @property
    # def title(self):
    #     return self._title

    # @title.setter
    # def name(self, value):
    #     if isinstance(value, str) and len(value):
    #         self._title = value
    #     else:
    #         raise ValueError("Title must be a non-empty string.")

    # @property
    # def genre(self):
    #     return self._genre
    # @genre.setter
    # def genre(self, value):
    #     if isinstance(value, str) and len(value):
    #         self._genre = value
    #     else:
    #         raise ValueError("Genre must be a non-empty string.")

   
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS albums (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                genre TEXT NOT NULL
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS albums")
        CONN.commit()

    def save(self):
        sql = "INSERT INTO albums (title, genre) VALUES (?, ?)"
        CURSOR.execute(sql, (self.title, self.genre))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, genre):
        album = cls(title, genre)
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
    def find_by_genre(cls, genre):
        row = CURSOR.execute("SELECT * FROM albums WHERE genre = ?", (genre,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def all_albums(cls):
        rows = CURSOR.execute("SELECT * FROM albums").fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    
    @classmethod
    def instance_from_db(cls, row):
        return cls(row["title"], row["genre"], row["id"])

   