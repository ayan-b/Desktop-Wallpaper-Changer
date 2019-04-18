import sys,os
from dwc import debug


def test_human_readable_size():
    actual = debug.human_readable_size(5)
    expected = "5.00 bytes"
    assert actual == expected
