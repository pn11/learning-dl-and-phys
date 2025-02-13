# -*- coding: utf-8 -*-
#
# KumaROOT documentation build configuration file, created by
# sphinx-quickstart on Sat Jul 11 17:44:03 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import sphinx_rtd_theme

##################################################
## Project information
##################################################

project = 'learning-dl-and-phys'
author = 'pn11'
copyright = '2021, pn11'
version = '0.0.0'
release = '0.0.0'

##################################################
## General configuration
##################################################

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

source_suffix = {'.rst': 'restructuredtext'}
source_encoding = 'utf-8-sig'
master_doc = 'index'
exclude_patterns = []
templates_path = ['_templates']
numfig = True
pygments_style = 'sphinx'

##################################################
## Options for i18n
##################################################
language = 'ja'

#################################################
## Options for sphinx.ext.todo
##################################################
todo_include_todos = True


# 'figure', 'table', 'code-block' に対して
# それぞれ図表番号表示のためのフォーマット文字列を
# 指定する辞書です。(バージョン 1.3 で追加)
numfig_format = {
    'figure' : u'Fig. %s',
    'table' : u'Table %s',
    'code-block' : u'Listing %s'
}
numfig_format['figure'] = u'図 %s'
numfig_format['table'] = u'表 %s'
numfig_format['code-block'] = u'リスト %s'

# 図表番号のスコープです。
# スコープ指定によって、numfig機能が番号付けする範囲を決めます。
# 0 は全てのドキュメントで通し番号を使います。
# 1 はセクション毎の番号付けで、x.1, x.2, x.3, ...のように付与します。
# 2 はサブセクション毎の番号付けで、x.x.1, x.x.2, x.x.3, ...のように付与します。
# デフォルトは 1 です。
numfig_secnum_depth = 1

##################################################
## Options for HTML
##################################################

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
}
#html_theme_path = []
#html_title = None
#html_short_title = None
#html_logo = None
#html_favicon = None
html_static_path = ['_static']
#html_extra_path = []
#html_last_updated_fmt = '%b %d, %Y'
#html_use_smartypants = True
#html_sidebars = {}
#html_additional_pages = {}
#html_domain_indices = True
#html_use_index = True
#html_split_index = False
#html_show_sourcelink = True
#html_show_sphinx = True
#html_show_copyright = True
#html_use_opensearch = ''
#html_file_suffix = None
html_search_language = 'ja'
#html_search_options = {'type': 'default'}
#html_search_scorer = 'scorer.js'
htmlhelp_basename = 'KumaROOTdoc'

#################################################
## Options for Epub output
##################################################

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
#epub_basename = project
#epub_theme = 'epub'
#epub_language = ''
#epub_scheme = ''
#epub_identifier = ''
#epub_uid = ''
#epub_cover = ()
#epub_guide = ()
#epub_pre_files = []
#epub_post_files = []
epub_exclude_files = ['search.html']
#epub_tocdepth = 3
#epub_tocdup = True
#epub_tocscope = 'default'
#epub_fix_images = False
#epub_max_image_width = 0
#epub_show_urls = 'inline'
#epub_use_index = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
