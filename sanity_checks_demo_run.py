import sanity_checks
import connector_sqlite
import output_slack
import output_default
import os


# This is the main function that will run the sanity checks
# It will connect to the SQLite database, run the tests and output the results
# It will also send the results to a Slack channel
def main():
    db_path = "./demo/Chinook.db"  # Adjust the path as necessary
    tests_path = "./sql_tests/"  # Adjust the path as necessary
    # Instantiate the SQLite connector
    db_connector = connector_sqlite.SQLiteDBConnector(db_path)
    # Config for the Slack output
    slack_token = os.getenv('SLACK_TOKEN')
    slack_channel = os.getenv('SLACK_CHANNEL')
    # Run the SanityCheck
    sanity_checks.SanityCheck(tests_path=tests_path,
                              connector=db_connector,
                              output_objects=[output_default.DefaultOutput(),
                                              output_slack.SlackOutput(token=slack_token, channel=slack_channel)])


if __name__ == "__main__":
    main()
