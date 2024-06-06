# https://www.sphinx-doc.org/en/master/tutorial/describing-code.html#including-doctests-in-your-documentation
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'page-loader'
copyright = '2024, Sergei Mikurov'
author = 'Sergei Mikurov'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    # https://www.sphinx-doc.org/en/master/tutorial/describing-code.html#including-doctests-in-your-documentation
    'sphinx.ext.doctest',
    # https://www.sphinx-doc.org/en/master/tutorial/automatic-doc-generation.html#reusing-signatures-and-docstrings-with-autodoc
    'sphinx.ext.autodoc',
    # https://www.sphinx-doc.org/en/master/tutorial/automatic-doc-generation.html#generating-comprehensive-api-references
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
