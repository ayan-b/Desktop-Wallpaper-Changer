import sys

from mock import patch
from pytest import raises


def test_version_option():
    test_args = ["dwc", "--version"]
    with raises(SystemExit):
        with patch.object(sys, "argv", test_args):
            from dwc.main import main

            main()
