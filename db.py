import sqlite3

conn = sqlite3.connect("movies.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS movies (
    movie_id TEXT,
    file_id TEXT
)
""")
conn.commit()

def save_movie(movie_id, file_id):
    cur.execute("INSERT INTO movies VALUES (?,?)", (movie_id, file_id))
    conn.commit()

def get_movie(movie_id):
    cur.execute("SELECT file_id FROM movies WHERE movie_id=?", (movie_id,))
    return cur.fetchone()
