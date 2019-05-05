import unittest

from dwc import main


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = main.create_parser()

    def test_interactive(self):
        parsed = self.parser.parse_args(["-i"])
        assert parsed.interactive is True

    def test_options(self):
        parsed = self.parser.parse_args(["0"])
        assert parsed.option == "0"
