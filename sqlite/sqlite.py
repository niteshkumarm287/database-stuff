import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)


# Create / connect to a database file
conn = sqlite3.connect("memory.db")

# Create a table
conn.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt TEXT,
    response TEXT
)
""")

# Insert data
for i in range(10):
  conn.execute("INSERT INTO chats (prompt, response) VALUES (?, ?)", ("Hello", "Hi there!"))
  conn.commit()

# Fetch data
for row in conn.execute("SELECT * FROM chats limit 5"):
    logging.info(row)

conn.close()
