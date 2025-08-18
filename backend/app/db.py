import sqlite3

# Start connection to database
db_file = "nba.sqlite"

def get_db_connection(): 
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn