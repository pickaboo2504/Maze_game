# setup_db.py
import sqlite3

def create_table():
    # Connect to the SQLite database (it will create a new one if it doesn't exist)
    conn = sqlite3.connect('highscores.db')
    cursor = conn.cursor()

    # Create a table for high scores
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS highscores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT NOT NULL,
        score INTEGER NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Table 'highscores' created successfully.")

if __name__ == "__main__":
    create_table()
