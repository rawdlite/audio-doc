# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Rawdlite Audio'
copyright = '2021, T.Roth'
author = 'tom roth'

release = '0.2'
version = '0.2.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

extensions.append('sphinx.ext.todo')
todo_include_todos=True

