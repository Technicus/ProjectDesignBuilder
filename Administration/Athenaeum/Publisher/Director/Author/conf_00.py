#!/bin/python
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
#import os
#import sys
#import importlib
from sys import path as sysPath
from os import walk, path, getcwd, system
from projectInterrogation import directoryComprehension, directorySurvey, discovery, projectTreeRegister

# -- Status report -----------------------------------------------------

print('conf.py\n')

# -- Configure system path information -----------------------------------------------------

for directory, path in directoryComprehension().items():
    print('{}:\n  {}\n'.format(directory, path))

print('directories:')
for audit in directorySurvey(directoryComprehension()['dirProjectDesignBuilder_Absolute'])['directories']:
    print('  {}'.format(audit))
print()

for key, registery in projectTreeRegister().items():
    print('{}:'.format(key))
    for register in projectTreeRegister()[key]:
        print('  {}'.format(register))
    print()

# -- Append sysPath -----------------------------------------------------

print('sysPath pre-append:'.format(''))
for path in sysPath:
    print('  {}'.format(path))
for path in projectTreeRegister()['rootBranch']:
    sysPath.append(path)
print('\nsysPath append:'.format(''))
for path in sysPath:
    print('  {}'.format(path))
print('{}'.format(''))

sysPath.append('/home/technicus/Projects/CAD/ProjectDesignBuilder/Builder/Directors')
sysPath.append('/home/technicus/Projects/CAD/ProjectDesignBuilder/Builder/Utilities/Maintenance/')

# -- Import from new sysPath -----------------------------------------------------

from Utility import clear
from ProjectDesignBuilder import __version__
from ClearOperations import cleanPythonOperations

# -- Implement new imports  -----------------------------------------------------

cleanPythonOperations(directoryComprehension()['dirProjectDesignBuilder_Absolute'], True)
#cleanPythonOperations(dirProject, False)

# -- Configure sphinx-apidoc -----------------------------------------------------

system(('sphinx-apidoc -f -o {} {}').format('../../Editors', directoryComprehension()['dirProjectDesignBuilder_Absolute']))

#(('sphinx-apidoc -f -o {} {}').format(dirCurrent, dirWorkingAbs))
##(('sphinx-apidoc -f -o {} {} **/.git').format(dirCurrent, dirWorkingAbs))
##system(('sphinx-apidoc -f -o {} {} {}').format(dirCurrent, dirWorkingAbs, excludes))

##print('\nClear python operation files:\n=============================')
##print('\nupdate index.rst with automodule list:\n======================================')
##for dirWorking, dirs, files in walk(dirProject, topdown=True):
    ##for name in files:
        ##print(name)
        ###sphinx-apidoc -f -o source python
        ##system(('sphinx-apidoc -f -o {} {}').format(dirCurrent, name))
##print('')

##def setup(app):
    ##from sphinx.ext import apidoc
    ##app.connect('builder-inited', lambda _: apidoc.main([
        ##'-o', './api', '-d2', '-feMT', '../src/PROJECT',
    ##]))


# -- Project information -----------------------------------------------------

project = 'ProjectDesignBuilder'
copyright = '2022, Technicus'
author = 'Technicus'

# The full version, including alpha/beta/rc tags
release = __version__

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.coverage',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'autodocsumm',
    #'sphinx.ext.napolean',
]

autodoc_default_options = {
    'autosummary': True,
}

autodata_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
        ##dirRoot = '../../../../../ProjectDesignBuilder'
        #'../../../../../ProjectDesignBuilder/.git',
        #'../../../../../ProjectDesignBuilder/.git/*',
        #'/DesignBuilder/Development/ProjectDesignBuilder/.git',
        #'*.bak',
        #'*.kate-swp',
        #'../.git',
        #'../.git/*',
        #'../Administration/Documentation',
        #'../.*'
        #'*.bak',
        #'../../../../../ProjectDesignBuilder/.git',
        #'../../../../../ProjectDesignBuilder/.git/*',
        #'*.kate-swp',
        #'../../../../../ProjectDesignBuilder/Administration/Documentation',
        #'../../../../../ProjectDesignBuilder/.*'


        #'../_build',
        #'../.git',
        #'../Thumbs.db',
        #'../.DS_Store',
        #'../.venv',
        #'../.git',
        #'../.*',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'groundwork'
html_theme = 'sphinx_rtd_theme'
#html_theme = 'classic'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
