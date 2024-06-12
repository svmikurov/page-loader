#!/usr/bin/env python3
from page_loader.parse_args import parse_args
from page_loader import download


def main():
    """Download page."""
    args = parse_args()
    print(download(args.requested_url, args.output))


if __name__ == '__main__':
    main()
