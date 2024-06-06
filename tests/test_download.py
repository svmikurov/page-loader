from page_loader import download


def test_download():
    """Test page download.

    TODO: fix obviously false assert
    """
    file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
    assert '/var/tmp/ru-hexlet-io-courses.html' == file_path
