# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'qleap'
copyright = '2026, Avery Hogrefe and Jonathan Le'
author = 'Avery Hogrefe and Jonathan Le'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax"
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

toc_object_entries_show_parents = 'all'

# Quantum Macros

mathjax3_config = {
    "tex": {
        "macros": {
            "ket": ["\\left|#1\\right\\rangle", 1],
            "bra": ["\\left\\langle#1\\right|", 1],
            "braket": ["\\left\\langle#1\\right\\rangle", 1],
            "ketbra": ["\\left|#1\\right\\rangle\\left\\langle#2\\right|", 2],
            "tensor": ["#1 \\otimes #2", 2],
        }
    }
}