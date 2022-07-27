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





    def import_mdit_plugins(app: Sphinx, docname: str, content: List[str]) -> None:
        
        from markdown_it import MarkdownIt
        from .wikilinks import wikilinks_plugin
        pass
        
        from docutils import nodes
        from myst_parser.sphinx_parser import MystParser
                    
        md = MarkdownIt().use(wikilinks_plugin)

    app.connect('source-read', import_mdit_plugins)
    

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }