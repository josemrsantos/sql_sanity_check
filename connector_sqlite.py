import sqlite3


class SQLiteDB:
    def __init__(self, db_path=':memory:'):
        self.db_path = db_path
        self.connection = None
        self.cursor = None
        self.closed = True

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            self.closed = False
            print(f"Connected to SQLite database at {self.db_path}")
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        if self.connection and not self.closed:
            self.connection.close()
            self.closed = True
            print("Connection closed")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
