#!/usr/bin/env python

"""
A minimal front end to the Docutils Publisher, producing HTML slides using
the S5 template system.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives import images

directives._directive_registry['dot'] = ('dot', 'Dot')
images.Image.option_spec['height'] = \
        directives.length_or_percentage_or_unitless


description = ('Generates S5 (X)HTML slideshow documents from standalone '
               'reStructuredText sources.  ' + default_description)

publish_cmdline(writer_name='s5', description=description)
