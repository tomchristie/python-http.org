import datetime

# -- Project information -----------------------------------------------------

project = "Python HTTP Working Group"
copyright = f"{datetime.date.today().year}, Python HTTP Working Group"
author = "Python HTTP Working Group"


# -- General configuration ---------------------------------------------------

master_doc = "index"
source_suffix = ".rst"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_theme_options = {
    "description": "",
    "show_powered_by": False,
    "font_family": "'Roboto', Georgia, sans-serif",
    "head_font_family": "'Fira Sans', sans-serif",
}
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
    ]
}