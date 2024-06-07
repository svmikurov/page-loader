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

github_user = "svmikurov"
github_repo_name = "page-loader"  # auto-detected from dirname if blank
github_version = "main"
conf_py_path = "/docs/source/"   # with leading and trailing slash

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
    # https://myst-parser.readthedocs.io/en/v0.17.1/index.html
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


myst_enable_extensions = [
  "colon_fence",
]


# HTML context:
from os.path import basename, dirname, realpath     # noqa: E402

html_context = {
    "display_github": True,
    "github_user": github_user,
    # Auto-detect directory name.  This can break, but
    # useful as a default.
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}
