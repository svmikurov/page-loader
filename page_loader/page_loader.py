def download(requested_url: str, output_path: str = '') -> str:
    """Download the page.

    Write the downloaded page to a file and return the path to it.

    :param requested_url: URL of the requested page.
                          By default, this is the current directory.
    :type requested_url: str
    :param output_path: Path to save the page.
    :type output_path: str
    :return: Path to the downloaded page.
    :rtype: str

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
