Usage
=====

Tutorial
--------

page-loader CLI
^^^^^^^^^^^^^^^

``page-loader`` is a command line utility that downloads pages from the
Internet and saves them it in the specified **existing** directory
(by default, in the program launch directory ``os.getcwd()``).

Along with the page, it downloads all resources (images, styles and js)
making it possible to open the page without the Internet.

Displays the full path to the downloaded file.

Where:

``-o`` ``--output``    output dir flag

``/var/tmp``           specified **existing** directory

``https://ru.hexlet.io/courses``    page URL

.. code-block:: console

    (.venv) $ page-loader -o /var/tmp https://ru.hexlet.io/courses
    INFO:root:requested url: https://ru.hexlet.io/courses
    INFO:root:output path: /var/tmp
    INFO:root:write html file: /var/tmp/ru-hexlet-io-courses.html
    INFO:root:create directory for assets: /var/tmp/ru-hexlet-io-courses_files
    Downloading: |████████████████████████████████| 100.0% (eta: 0)
    Page was downloaded as '/var/tmp/ru-hexlet-io-courses.html'

page_loader library
^^^^^^^^^^^^^^^^^^^

The library provides the ``page_loader`` module with the ``download()``
function, the call of which downloads a page from the network into the
specified **existing** directory and returns the full path to the
downloaded file, including the name of the file itself.
The library can be installed as a dependency and used in your code.

.. code-block:: console

    from page_loader import download

    file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
    print(file_path)  # => '/var/tmp/ru-hexlet-io-courses.html'

How-to guide
------------

How creates names
^^^^^^^^^^^^^^^^^

How creates directories
^^^^^^^^^^^^^^^^^^^^^^^


Explanation
-----------

To get path names use the ``PathManager`` class:

.. autoclass:: page_loader.path.PathManager
   :members:
   :undoc-members:
   :private-members:
   :special-members: __init__,


Reference
---------
