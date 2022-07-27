from myst_parser.sphinx_parser import MystParser
from sphinx_obsidian.main import create_md_parser
from docutils import nodes
from myst_parser.sphinx_renderer import SphinxRenderer
from markdown_it.token import Token

from docutils import nodes

class ObsidianMystParser(MystParser):
    
    def parse(self, inputstring: str, document: nodes.document) -> None:
        """Parse source text.

        :param inputstring: The source string to parse
        :param document: The root docutils node to add AST elements to

        """
        config = document.settings.env.myst_config
        parser = create_md_parser(config, SphinxRenderer)
        parser.options["document"] = document
        env: dict = {}
        tokens = parser.parse(inputstring, env)
        if not tokens or tokens[0].type != "front_matter":
            # we always add front matter, so that we can merge it with global keys,
            # specified in the sphinx configuration
            tokens = [Token("front_matter", "", 0, content="{}", map=[0, 0])] + tokens
        parser.renderer.render(tokens, parser.options, env)
