import sqlite3



# SQLite conversion
sqlite_ddl = """
CREATE TABLE faceDetect_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT,
    updated_at TEXT
);
"""

# Connect to SQLite database
conn = sqlite3.connect('faceDetect.db')
cursor = conn.cursor()

# Execute SQLite DDL statement
cursor.executescript(sqlite_ddl)

# Commit and close connection
conn.commit()
conn.close()

print("SQL Server DDL converted to SQLite and executed successfully.")
