# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "UK TRE"
copyright = "2023, UK TRE"
author = "UK TRE"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = ["fieldlist", "linkify"]
myst_linkify_fuzzy_links = False

# Automatically create anchors for in-page headings up to level 3
myst_heading_anchors = 4

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://pydata-sphinx-theme.readthedocs.io/en/stable/

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_logo = "_static/uktre-logo.svg"
html_favicon = "_static/uktre-logo.svg"

html_theme_options = {
    "footer_start": ["copyright"],
    "footer_end": ["footer-links"],
}

# -- Link checker configuration

linkcheck_ignore = [
    # GitHub CI linkchecker seems to be blocked
    r"https://www.turing.ac.uk/.*",
    r"https://www.hpe.com/.*",
    r"https://csrc.nist.gov/.*",
    # Currently down
    r"https://www.goldacrereview.org/",
    r"https://www.rd-alliance.org/trusted-research-environments-sensitive-data-fairness-closed-data-and-processes",
]

# These pages use in-page JavaScript anchors which aren't seen by the link checker
linkcheck_anchors_ignore_for_url = [
    r"https://www\.swansea\.ac\.uk/the-university/location/",
    r"https://arewemeetingyet\.com/.+",
]
