import sanity_checks
import connector_sqlite


def main():  # This still has a bug. Will fix later.
    db_path = "./demo/my_database.sqlite"  # Adjust the path as necessary
    tests_path = "./tests/sql_tests"  # Adjust the path as necessary
    # Instantiate the SQLite connector
    db_connector = connector_sqlite.SQLiteConnector(db_path)
    # Run the SanityCheck
    sanity_checks.SanityCheck(tests_path=tests_path, connector=db_connector)


if __name__ == "__main__":
    main()