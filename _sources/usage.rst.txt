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

.. autofunction:: page_loader.page_loader.download


Doctest
-------

>>> from page_loader import download
>>> file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
>>> print(file_path)
/var/tmp/ru-hexlet-io-courses.html