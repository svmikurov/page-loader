"""Create file and directory paths by downloaded page url."""
import logging
import os
import re
from urllib.parse import urlparse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(module)s...%(funcName)s -> %(message)s',
    datefmt="%H:%M:%S",
)


class PathManager:
    """Create paths name by url.

    For create path names used ``requested_url`` and ``output_path``
    instant attributes.

    Parameters
    ----------
    requested_url : `str`
        Requested page url.
    output_path : `str` | `None`
        Path for download (current directory, by default).

    Examples
    --------
    >>> # Instantiating and attributes for inner use.
    >>> path_manager = PathManager('https://ru.hexlet.io/courses', '/var/tmp')

    >>> # To get the download path.
    >>> path_manager.download_page_path
    '/var/tmp/ru-hexlet-io-courses.html'

    >>> # To get the host url link for download assets.
    >>> path_manager.get_host_link('https://ru.hexlet.io/packs/runtime.js')
    'https://ru.hexlet.io/packs/runtime.js'
    >>> path_manager.get_host_link('/packs/runtime.js')
    'https://ru.hexlet.io/packs/runtime.js'
    >>> path_manager.get_host_link('/courses')
    'https://ru.hexlet.io/courses'

    >>> # To get the local link relative path value for a downloaded page.
    >>> path_manager.create_local_link('https://ru.hexlet.io/packs/runtime.js')
    'ru-hexlet-io-courses_files/ru-hexlet-io-packs-runtime.js'
    >>> path_manager.create_local_link('packs/runtime.js')
    'ru-hexlet-io-courses_files/ru-hexlet-io-packs-runtime.js'
    >>> path_manager.create_local_link('/courses')
    'ru-hexlet-io-courses_files/ru-hexlet-io-courses.html'

    >>> # Te get the absolute path to write page and its assets.
    >>> path_manager.write_page_path
    ... # doctest: +ELLIPSIS
    '.../page-loader/src/var/tmp/ru-hexlet-io-courses.html'
    >>> path_manager.create_write_file_path('https://ru.hexlet.io/packs/runtime.js')    # noqa: E501
    ... # doctest: +ELLIPSIS
    '.../page-loader/src/var/tmp/ru-hexlet-io-courses_files/ru-hexlet-io-packs-runtime.js'
    >>> path_manager.create_write_file_path('/packs/runtime.js')
    ... # doctest: +ELLIPSIS
    '.../page-loader/src/var/tmp/ru-hexlet-io-courses_files/ru-hexlet-io-packs-runtime.js'
    >>> path_manager.create_write_file_path('/courses')
    ... # doctest: +ELLIPSIS
    '.../page-loader/src/var/tmp/ru-hexlet-io-courses_files/ru-hexlet-io-courses.html'
    """

    def __init__(self, requested_url: str, output_path: str = None) -> None:
        """Constructor."""
        self.requested_url = requested_url
        self.output_path = output_path or ''
        self._hyphen_path_name = self.create_hyphen_name(requested_url)

    @staticmethod
    def create_hyphen_name(path: str) -> str:
        """Create name with replaced any symbols at string by hyphen."""
        path_name, ext = os.path.splitext(path)
        # the name must not contain the schema
        path_name: str = urlparse(path_name)._replace(scheme='').geturl()

        name_parts: list = re.sub(r'[^a-z0-9]', '-', path_name).split('-')
        hyphen_name: str = '-'.join(filter(None, name_parts)).lower() + ext

        return hyphen_name
