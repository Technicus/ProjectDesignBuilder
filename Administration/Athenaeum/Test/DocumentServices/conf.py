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
import os
import sys
#from ProjectDesignBuilder import __version__
#import recommonmark.Parser

print(f"\nconf.py :: start\n")

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('/home/technicus/Projects/CAD/ProjectDesignBuilder/Test/rst'))
#sys.path.append('/home/technicus/Projects/CAD/ProjectDesignBuilder/Test/rst')
for path in sys.path:
    print(f"{path}")
#print()

# -- Project information -----------------------------------------------------

project = 'ProjectDesignBuilder'
copyright = '2022, Technicus'
author = 'Technicus'

# The full version, including alpha/beta/rc tags
#release = __version__
release = '0.0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.coverage',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'autodocsumm',
    'sphinx.ext.napoleon',
    'myst_parser',
    #'recommonmark',
]


#source_parsers = {
    #'.md': recommonmark,
#}
source_parsers = {
    #'.md': recommonmark.parser.CommonMarkParser,
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    #'.md',
    '.md': 'markdown',
}

autodoc_default_options = {
    'autosummary': True,
}

autodata_content = 'both'

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
#html_theme = 'furo'
#html_theme = 'groundwork'
html_theme = 'sphinx_rtd_theme'
#html_theme = 'classic'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

print(f"\nconf.py :: end")