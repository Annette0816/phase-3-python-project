#  Record Label CLI

A beginner-friendly Python CLI (Command-Line Interface) application to manage a simple record label database using OOP and SQLite. You can create artists, albums, and songs, and view them using a menu-driven interface.

##  Features

- Create an Artist with real name and stage name
- Create an Album associated with an Artist
- Create a Song linked to an Artist and an Album
- View all Artists
- View Albums for a specific Artist
- View all Songs with Artist and Feature details

##  Project Structure

.
├── lib/
│ ├── cli.py 
│ ├── helpers.py 
│ ├── debug.py 
│ └── models/
│ ├── init.py 
│ ├── artist.py 
│ ├── album.py 
│ └── song.py 
└── README.md 

##  Requirements

- Python 3.x
- SQLite3 (included with Python)
- `ipdb` for debugging (optional)

Install `ipdb` with pip:

```bash
pip install ipdb

## GETTING STARTED 
1. -Clone the project
git clone <your-repo-url>
cd <your-project-folder>

2. Set up the database

3.Run the database
  python lib/debug.py

4. Run the CLI
python lib/cli.py

