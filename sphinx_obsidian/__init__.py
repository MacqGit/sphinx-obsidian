from typing import TYPE_CHECKING

__version__ = "0.0.1"

if TYPE_CHECKING:
    from sphinx.application import Sphinx

def setup(app):
    """Initialize Sphinx extension."""

    from sphinx_obsidian.sphinx_parser import ObsidianMystParser
    from myst_parser import setup_sphinx
    
    app.add_source_suffix(".md", "markdown")
    app.add_source_parser(ObsidianMystParser)

    setup_sphinx(app)

    return {"version": __version__, "parallel_read_safe": True}
