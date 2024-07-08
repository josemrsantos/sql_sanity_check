from sanity_checks import DefaultOutput
from textwrap import dedent


class TestDefaultOutput:
    def test_log(self, capsys):
        default_output = DefaultOutput()
        default_output.log('test1')
        captured = capsys.readouterr()
        assert captured.out == "test1\n"

    def test_error(self, capsys):
        default_output = DefaultOutput()
        default_output.error('test1', 'file1')
        captured = capsys.readouterr()
        expected = dedent(f""" 
        ********************** ERROR ****************************\n
        * IN file1\n
        test1\n
        *********************************************************\n
        """)
        assert captured.err == expected
