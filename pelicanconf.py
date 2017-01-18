#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Christopher Roach'
SITENAME = 'christopherroach.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Prevent pelican from trying to parse notebook checkpoint files
IGNORE_FILES = ['.ipynb_checkpoints', 'README.md']

# Which files are considered to be markdown files
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ('./plugins',)
PLUGINS = ('ipynb.markup',)

# Turn on categories
DISPLAY_CATEGORIES_ON_MENU = True

# Get rid of the index pages for tags and categories
DIRECT_TEMPLATES = ['index', 'archives']

THEME = "themes/my-blog-theme"
IPYNB_IGNORE_CSS = True