# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'Bluesky Tutorials'
copyright = '2020, Bluesky Contributors'
author = 'Bluesky Contributors'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]

# This is the time limit per *cell*. The timeout may be extended on a
# per-notebook basis by adding
#
# "nbsphinx": {
#   "timeout": 60
# },
#
# to the notebook metadata.
nbsphinx_timeout = 60
nbsphinx_execute = "always"

nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}

.. important::

   You can run this notebook in a `live session <https://mybinder.org/v2/gh/bluesky/tutorials/master?urlpath=lab/tree/{{ docname | urlencode }}>`_ |Binder|
   or view it `on nbviewer <https://nbviewer.jupyter.org/github/bluesky/tutorials/blob/master/{{ docname | urlencode }}>`_
   or `GitHub <https://github.com/bluesky/tutorials/blob/master/{{ docname | urlencode }}>`_.

.. |Binder| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/bluesky/tutorials/master?urlpath=lab/tree/{{ docname | urlencode }}
"""

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
