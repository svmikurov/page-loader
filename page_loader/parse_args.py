import argparse
import os


def parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        prog='page-loader',
        description='Page loader',
    )
    parser.add_argument(
        'requested_url',
        metavar='requested_url',
        help='Requested page url'
    )
    parser.add_argument(
        '-o', '--output',
        default=os.getcwd(),
        help='Path for page download (current directory, by default)',
    )
    args = parser.parse_args()

    return args
