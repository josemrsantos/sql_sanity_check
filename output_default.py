import sys


class DefaultOutput:
    """ Default output class: It simply prints the string.
    """

    @staticmethod
    def log(test_name, test_result=None, code=None):
        if test_result is None:
            reason = f'Running {test_name}'
        else:
            reason = f"""
+++++++++++++++++++++++++++++++++++++++++++++++++++
Test: {test_name}
{code}
Has returned: {test_result} 
+++++++++++++++++++++++++++++++++++++++++++++++++++"""
        print(reason)

    @staticmethod
    def error(test_name, test_result, code):
        output_error_text = f"""
********************** ERROR ****************************
---------------
Test: {test_name}
{code}
Has returned: {test_result} 
---------------
*********************************************************
        """
        sys.stderr.write(f"{output_error_text}")
