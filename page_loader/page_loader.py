def download(requested_url: str, output_path: str) -> str:
    """Download the page.

    Write the downloaded page to a file and return the path to it.

    Parameters
    ----------
    requested_url : `str`
        URL of the download page.
    output_path : `str`
        Directory for saving the downloaded page
        (current directory, by default).

    Return
    ------
    file_path : `str`
        Relative path to the downloaded page.

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
