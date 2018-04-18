# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# Fix for error "cannot import name 'make_admonition'".
# https://github.com/spinus/sphinxcontrib-images/issues/41
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx.util import compat
compat.make_admonition = BaseAdmonition



# -- Project information -----------------------------------------------------

project = 'LADM_COL Assistant'
copyright = '2018, Agencia de Implementación'
author = 'Fernando Pineda'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinxcontrib.images',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# 'alabaster,,agogo,sphinxdoc,scrolls,traditional,nature,haiku,pyramid,bizstyle'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a lhtml_theme = "classic"
# documentation.
#
# html_theme_options = {}
# for sphinx_rtd_theme
html_theme_options = {
    'display_version': 'true',
    'sticky_navigation': 'true'
}

# for Alabaster
# html_theme_options = {
#     'fixed_sidebar': 'true',
# }

# for Classic
# html_theme_options = {
#     'stickysidebar': 'true',
# }

# for bizstyle
# html_theme_options = {
#     'stickysidebar': 'true',
# }


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ladm_a_docsdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ladm_a_docs.tex', 'ladm\\_a\\_docs Documentation',
     'Fernando Pineda', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ladm_a_docs', 'ladm_a_docs Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ladm_a_docs', 'ladm_a_docs Documentation',
     author, 'ladm_a_docs', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------
import sys,os
sys.path.insert(0, os.path.abspath(".."))

images_config = {
    'override_image_directive': True,
    'default_image_width': '100%'
    }

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False
gettext_enables = ['index']
gettext_ignore_index = False
