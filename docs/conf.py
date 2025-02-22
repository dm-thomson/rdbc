# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RDBC Figures'
copyright = '2025, D. Thomson'
author = 'D. Thomson'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_theme_options = {
#     'nosidebar': True,
#     "rightsidebar": "true",
#     "relbarbgcolor": "black"
# }
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        # 'searchbox.html',
    ]
}
html_static_path = ['_static']
