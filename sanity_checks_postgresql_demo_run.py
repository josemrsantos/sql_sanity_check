import connector_postgresql
import sanity_checks
import output_default
import os


# This is the main function that will run the sanity checks
# It will connect to the PostgreSQL database, run the tests and output the results
# It will also send the results to a Slack channel
def main():
    db_params = {
        "host": "localhost",
        "port": 5432,
        "database": "chinook",
        "user": "postgres"
    }
    tests_path = "./sql_tests/PostgreSQL/"
    # Instantiate the PostgreSQL connector
    db_connector = connector_postgresql.PostgreSQLConnector(db_params)
    # Run the SanityCheck
    sanity_checks.SanityCheck(tests_path=tests_path,
                              connector=db_connector,
                              output_objects=[output_default.DefaultOutput()])


if __name__ == "__main__":
    main()
