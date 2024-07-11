import sanity_checks
import connector_sqlite


# This is just a demo usage example for a table in a SQLite database
# This is the default DB that comes with SQLite, but I have changed a value in the table InvoiceLine
# to demo the functionality of the SanityCheck class
def main():
    db_path = "./demo/Chinook.db"  # Adjust the path as necessary
    tests_path = "./sql_tests/"  # Adjust the path as necessary
    # Instantiate the SQLite connector
    db_connector = connector_sqlite.SQLiteDB(db_path)
    # Run the SanityCheck
    sanity_checks.SanityCheck(tests_path=tests_path, connector=db_connector)


if __name__ == "__main__":
    main()
