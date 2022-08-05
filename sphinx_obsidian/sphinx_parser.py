from myst_parser.parsers.sphinx_ import MystParser

from myst_parser.mdit_to_docutils.sphinx_ import SphinxRenderer, create_warning
from myst_parser.config.main import (
    MdParserConfig,
    TopmatterReadError,
    merge_file_level,
    read_topmatter,
)

from docutils import nodes
from sphinx_obsidian.main import create_md_parser

class ObsidianMystParser(MystParser):
    
    def parse(self, inputstring: str, document: nodes.document) -> None:
        """Parse source text.

        :param inputstring: The source string to parse
        :param document: The root docutils node to add AST elements to

        """
        # get the global config
        config: MdParserConfig = document.settings.env.myst_config

        # update the global config with the file-level config
        try:
            topmatter = read_topmatter(inputstring)
        except TopmatterReadError:
            pass  # this will be reported during the render
        else:
            if topmatter:
                warning = lambda wtype, msg: create_warning(  # noqa: E731
                    document, msg, line=1, append_to=document, subtype=wtype
                )
                config = merge_file_level(config, topmatter, warning)

        parser = create_md_parser(config, SphinxRenderer)
        parser.options["document"] = document
        parser.render(inputstring)
