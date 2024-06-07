import os
from tempfile import TemporaryDirectory

import requests_mock

from page_loader import download

REQUESTED_URL = 'https://ru.hexlet.io/courses'
HTML_FILE_NAME = 'ru-hexlet-io-courses.html'
PAGE_DATA = 'data'


def test_download():
    """Test page download function."""
    with requests_mock.Mocker() as mock:
        mock.get(REQUESTED_URL, text=PAGE_DATA)

        with TemporaryDirectory() as tmpdir:
            current_file_path = download(REQUESTED_URL, tmpdir)
            expected_file_path = os.path.join(tmpdir, HTML_FILE_NAME)
            assert expected_file_path == current_file_path

            with open(current_file_path) as file:
                current_file_data = file.read()
                assert PAGE_DATA == current_file_data
