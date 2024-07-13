# import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackOutput:
    """ Slack output class: Sends the output to a Slack channel, either it being a log or an error, but the output of
        the log will be simpler
        Both the token and the channel need to be provided when instantiating the class.
    """

    def __init__(self, token, channel):
        self.channel = channel
        self.client = WebClient(token=token)

    def post_message(self, message):
        """ Sends a message to the Slack channel
        """
        self.client.chat_postMessage(
            channel=self.channel,
            text=message
        )

    def log(self, test_name, test_result=None, code=None):
        text_message = ''
        if test_result is None:
            text_message = f'Running {test_name}'
        elif test_result == []:
            text_message = f'{test_name} has returned no error'
        self.post_message(f"[sql_sanity_checks] {text_message}")

    def error(self, test_name, test_result, code):
        text_message = f'Errors returned for the test {test_name}. Please check the logs for more information.'
        self.post_message(f"[sql_sanity_checks] {text_message}")
