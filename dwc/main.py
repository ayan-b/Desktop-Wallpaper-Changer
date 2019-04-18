import argparse

import dwc.dwc as dwc


def main():
    """
    Program entry point
    """
    parser = create_parser()
    options = vars(parser.parse_args())
    if options["interactive"]:
        dwc.throw_choices()
    else:
        dwc.change_background(int(options["option"]))
    

def create_parser():
    """
    Construct the program options
    """
    parser = argparse.ArgumentParser(
        prog="dwc", description="Change your desktop wallpaper daily!"
    )
    parser.add_argument(
        "-op",
        "--option",
        help="The source for the wallpaper"
    )
    parser.add_argument(
        "-i",
        "--interactive",
        help="Interactively choose the source",
        action="store_true"
    )
    return parser
