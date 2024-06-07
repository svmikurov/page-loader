"""
Create file and directory paths by downloaded page url.
"""

import logging
import os
import re
from functools import cached_property
from urllib.parse import urlparse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(module)s...%(funcName)s -> %(message)s',
    datefmt="%H:%M:%S",
)


class PathManager:
    """Create path names.

    Use for create path names from ``requested_url`` and ``output_path``
    instant attributes.

    Parameters
    ----------
    requested_url : `str`
        Requested page url.
    output_path : `str` | `None`
        Path for download (current directory, by default).

    Attributes
    ----------
    _hyphen_requested_url : `str`
        Requested page url without schema, separated by a hyphen.

    Examples
    --------
    >>> # Instantiating and attributes for inner use.
    >>> path_manager = PathManager('https://ru.hexlet.io/courses', '/var/tmp')

    >>> # To get the download path.
    >>> path_manager.file_path
    '/var/tmp/ru-hexlet-io-courses.html'
    """

    def __init__(self, requested_url: str, output_path: str = None) -> None:
        self.output_path = output_path or ''
        self._hyphen_requested_url = self._create_hyphen_name(requested_url)

    @staticmethod
    def _create_hyphen_name(path: str) -> str:
        """Create name, separated by a hyphen.

        Removes schema in url if it any.
        Replaces any symbols in name string by hyphen.

        Parameters
        ----------
        path : `str`
            Page url or file (directory) path to separate by a hyphen.

        Return
        ------
        hyphen_name : `str`
            Url hostname with path if it any
            or file (directory) path name, separated by a hyphen.
        """
        path_name, ext = os.path.splitext(path)
        # the name must not contain the schema
        path_name: str = urlparse(path_name)._replace(scheme='').geturl()

        name_parts: list = re.sub(r'[^a-z0-9]', '-', path_name).split('-')
        hyphen_name: str = '-'.join(filter(None, name_parts)).lower() + ext

        return hyphen_name

    @cached_property
    def _hyphen_page_name(self) -> str:
        """The name of the file, separated by a hyphen,
        storing the downloaded page (`str`, read-only)."""
        return self._hyphen_requested_url + '.html'

    @property
    def file_path(self):
        """Relative path to the file where the downloaded page is stored.
        (`str`, read-only)."""
        return os.path.join(self.output_path, self._hyphen_page_name)
