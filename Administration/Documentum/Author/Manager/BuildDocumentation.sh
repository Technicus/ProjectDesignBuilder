#!/bin/bash


#def cleanPythonOperations(operationPath, remove = False):
    #if(remove == True):
        #system(('cleanpy --all -v {}').format(operationPath))
    #else:
        #system(('cleanpy --list -v {}').format(operationPath))
        #output = sp.getoutput('whoami --version')
        #print (output)
#cleanPythonOperations(operationPath, bool(remove))



# cleanpy --all -v ../../../../../ProjectDesignBuilder

# sphinx-build -b html -c ../../Directors/conf.py '../ProjectDesignBuilder' '../Release/Documentation'
clear; make clean; make html

#
# /home/technicus/Projects/CAD/DesignBuilder/Development/ProjectDesignBuilder/Administration/Documentation/Builders/Builders/Directors/
# /home/technicus/Projects/CAD/DesignBuilder/Development/ProjectDesignBuilder/Administration/Documentation/Builders/Directors
# /home/technicus/Projects/CAD/DesignBuilder/Development/ProjectDesignBuilder/Administration/Documentation/Builders/Directors/conf.py



sphinx-build [options] <sourcedir> <outputdir> [filenames …]

 -b buildername
    The most important option: it selects a builder. The most common builders are:
    html
        Build HTML pages. This is the default builder.
    dirhtml
        Build HTML pages, but with a single directory per document. Makes for prettier URLs (no .html) if served from a webserver.
    singlehtml
        Build a single HTML with the whole content.
    htmlhelp, qthelp, devhelp, epub
        Build HTML files with additional information for building a documentation collection in one of these formats.
    applehelp
        Build an Apple Help Book. Requires hiutil and codesign, which are not Open Source and presently only available on Mac OS X 10.6 and higher.
    latex
        Build LaTeX sources that can be compiled to a PDF document using pdflatex.
    man
        Build manual pages in groff format for UNIX systems.
    texinfo
        Build Texinfo files that can be processed into Info files using makeinfo.
    text
        Build plain text files.
    gettext
        Build gettext-style message catalogs (.pot files).
    doctest
        Run all doctests in the documentation, if the doctest extension is enabled.
    linkcheck
        Check the integrity of all external links.
    xml
        Build Docutils-native XML files.
    pseudoxml
        Build compact pretty-printed “pseudo-XML” files displaying the internal structure of the intermediate document trees.

-a
    If given, always write all output files. The default is to only write output files for new and changed source files. (This may not apply to all builders.)

-E
    Don’t use a saved environment (the structure caching all cross-references), but rebuild it completely. The default is to only read and parse source files that are new or have changed since the last run.

-d path
    Since Sphinx has to read and parse all source files before it can write an output file, the parsed source files are cached as “doctree pickles”. Normally, these files are put in a directory called .doctrees under the build directory; with this option you can select a different cache directory (the doctrees can be shared between all builders).

 -c path
    Don’t look for the conf.py in the source directory, but use the given configuration directory instead. Note that various other files and paths given by configuration values are expected to be relative to the configuration directory, so they will have to be present at this location too.

-n
    Run in nit-picky mode. Currently, this generates warnings for all missing references. See the config value nitpick_ignore for a way to exclude some references as “known missing”.

 -v
    Increase verbosity (loglevel). This option can be given up to three times to get more debug logging output. It implies -T.

-w file
    Write warnings (and errors) to the given file, in addition to standard error.

 --keep-going
    With -W option, keep going processing when getting warnings to the end of build, and sphinx-build exits with exit status 1.


























