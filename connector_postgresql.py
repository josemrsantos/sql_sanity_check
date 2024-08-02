import psycopg2


class PostgreSQLConnector:
    def __init__(self, db_params=None):
        self.db_params = db_params
        self.connection = None
        self.cursor = None
        self.closed = True

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.db_params)
            print(self.connection)
            self.cursor = self.connection.cursor()
            print(self.cursor)
            self.closed = False
            print(f"Connected to PostgreSQL database at {self.db_params['host']}")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        if self.connection and not self.closed:
            self.cursor.close()
            self.connection.close()
            self.closed = True
            print("Connection closed")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()