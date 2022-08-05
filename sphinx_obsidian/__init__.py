__version__ = "0.0.2"

def setup(app):
    """Initialize Sphinx extension."""

    from sphinx_obsidian.sphinx_parser import ObsidianMystParser
    from myst_parser.sphinx_ext.main import setup_sphinx
    
    setup_sphinx(app, load_parser=False)
        
    app.add_source_suffix(".md", "markdown")
    app.add_source_parser(ObsidianMystParser)

    return {"version": __version__, "parallel_read_safe": True}
