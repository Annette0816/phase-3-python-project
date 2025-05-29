from models.__init__ import CURSOR, CONN

class Artist:
    all = {}

    def __init__(self, name , stage_name,  id=None):
        self.id = id
        self.name = name
        self.stage_name = stage_name
        Artist.all[self.id] = self

    def __repr__(self):
        return f"<Artist {self.id}: {self.name} aka {self.stage_name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError("Name  must be a non-empty string.")
    

    @property
    def stage_name(self):
        return self._stage_name

    @stage_name.setter
    def stage_name(self, value):
        if isinstance(value, str) and len(value):
            self._stage_name = value
        else:
            raise ValueError("Stage name  must be a non-empty string.")
    

    def albums(self):
      from models.album import Album
      return [album for album in Album.all.values() if album.artist.id == self.id]

    def songs(self):
     from models.song import Song
     return [song for song in Song.all.values() if song.artist.id == self.id]

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS artists (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                stage_name TEXT NOT NULL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS artists")
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO artists (name,stage_name)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.stage_name))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, stage_name):
        artist = cls(name, stage_name)
        artist.save()
        return artist
        
    @classmethod
    def find_by_id(cls, id):
        row = CURSOR.execute("SELECT * FROM artists WHERE id = ?", (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        row = CURSOR.execute("SELECT * FROM artists WHERE name = ?", (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def find_by_stage_name(cls, name):
        row = CURSOR.execute("SELECT * FROM artists WHERE stage_name = ?", (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def all_artists(cls):
        rows = CURSOR.execute("SELECT * FROM artists").fetchall()
        return [cls.instance_from_db(row) for row in rows]
   
    @classmethod
    def all_artists_by_stage_name(cls):
        rows = CURSOR.execute("SELECT * FROM artists ORDER BY stage_name DESC").fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def all_artists_by_name(cls):
        rows = CURSOR.execute("SELECT * FROM artists ORDER BY name").fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def instance_from_db(cls, row):
        return cls(row["name"], row["stage_name"], row["id"])

