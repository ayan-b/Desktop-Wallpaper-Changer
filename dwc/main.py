import argparse

import dwc.dwc as dwc
from dwc import _version


def main():
    """
    Program entry point
    """
    parser = create_parser()
    options = vars(parser.parse_args())
    if options["interactive"]:
        dwc.throw_choices()
    else:
        dwc.change_background(int(options["option"]), activate_search=False)


def create_parser():
    """
    Construct the program options
    """
    parser = argparse.ArgumentParser(
        prog="dwc", description="Change your desktop wallpaper daily!"
    )
    parser.add_argument(
        "option",
        help="The source for the wallpaper",
        nargs="?",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        help="Interactively choose the source",
        action="store_true"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {v}".format(v=_version.__version__),
    )
    return parser
