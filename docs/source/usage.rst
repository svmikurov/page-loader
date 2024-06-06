Usage
=====

Installation
------------

To use **page-loader**, first install it using Makefile:

.. code-block:: console

   (.venv) $ make package-install

Download page
-------------

To download page use the ``download()`` function:

.. py:function:: download(url, path)

    Saves a page and returns the path to that page.

    :param url: URL of the requested page.
                By default this is the current directory.
    :type url: str
    :param path: Path to save the page.
    :type path: str
    :return: Path to the downloaded page.
    :rtype: str

Doctest
-------

>>> from page_loader import download
>>> file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
>>> print(file_path)
/var/tmp/ru-hexlet-io-courses.html