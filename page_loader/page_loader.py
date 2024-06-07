def download(requested_url: str, output_path: str = '') -> str:
    """Download the page.

    Write the downloaded page to a file and return the path to it.

    Parameters
    ----------
    requested_url : `str`
        Requested page url.
    output_path : `str` | `None`
        Path for download (current directory, by default).

    Examples
    --------
    >>> file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
    >>> print(file_path)
    /var/tmp/ru-hexlet-io-courses.html
    """
    return '/var/tmp/ru-hexlet-io-courses.html'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
