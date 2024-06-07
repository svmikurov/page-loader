import requests

from page_loader.path import PathManager


def download(requested_url: str, output_path: str = '') -> str:
    """Download the page.

    Write the downloaded page to a file and return the path to it.

    Parameters
    ----------
    requested_url : `str`
        Requested page url.
    output_path : `str` | `None`
        Path for page download (current directory, by default).

    Return
    ------
    file_path : `str`
        The relative path to downloaded page.

    Example
    -------
    file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
    print(file_path)    => '/var/tmp/ru-hexlet-io-courses.html'
    """
    path_manager = PathManager(requested_url, output_path)
    file_path = path_manager.file_path
    page = requests.get(requested_url).text

    with open(file_path, 'w') as file:
        file.write(page)

    return file_path
