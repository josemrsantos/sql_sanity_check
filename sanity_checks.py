import os
from output_default import DefaultOutput


class SanityCheck:
    """
    Main Sanity Check class: It expects to receive in the parameters:
      * A connection, that should already have the connection sorted and have a fetch_sql_result method implemented
      * An optional output_objects that should be a list of Output objects. Each of those objects need to have the
        methods log (generic logging of the value string) and error (this should not only log the value string,
         but also set a 'failed' event, when appropriate)
    This is a class with a self-invoking run method upon instantiation, so simply creating the ephemeral object
    with
    SanityCheck(test_path='./my_sql_tests/', connection=postgres_connection_object)
    would run all SQL test files that are inside the my_sql_tests folder and output the name of the file, its contents
    and any results returned from running the SQL code.
    IMPORTANT
    If any result is returned from any executed SQL code, the script will fail with an Exception. Refer to the Readme
    file on how these tests should be created.
    """
    def __init__(self, tests_path=None, connector=None, output_objects=None):
        if output_objects is None:
            default_output = DefaultOutput()
            self.output_objects = [default_output]
        else:
            self.output_objects = output_objects
        self.connector = connector
        self.tests_path = tests_path
        test_name = None
        test_result = None
        self.data = []
        self.sql_files = []
        self.run()

    def log(self, test_name, test_result=None, code=None):
        for output_object in self.output_objects:
            output_object.log(test_name, test_result, code)

    def error(self, test_name, test_result, code):
        for output_object in self.output_objects:
            output_object.error(test_name, test_result,  code)

    def get_sql_files(self):
        for filename in os.listdir(self.tests_path):
            with open(os.path.join(self.tests_path, filename), "r", encoding="utf-8") as sql_file:
                sql_code = sql_file.read()
                data_item = {'filename': filename, 'sql_code': sql_code, 'result': None}
                self.data.append(data_item)

    def execute_sql(self):
        with self.connector as conn:
            for item in self.data:
                sql_code = item['sql_code']
                self.log(item['filename'])
                result = conn.execute_query(sql_code)
                if result:
                    item['result'] = result

    def check_results(self):
        error_found = False
        for item in self.data:
            if item['result'] is not None:
                error_found = True
                self.error(item['filename'], item['result'], item['sql_code'])
            else:
                self.log(item['filename'], 'No error found', item['sql_code'])
        if error_found:
            raise Exception("Error found in SQL tests")

    def run(self):
        # Get all SQL files and its content
        self.get_sql_files()
        # Execute all SQL code
        self.execute_sql()
        # Output errors or exit without
        self.check_results()


def main():
    raise Exception('This is a library and should not be executed directly. Please read the documentation.')


if __name__ == "__main__":
    main()
