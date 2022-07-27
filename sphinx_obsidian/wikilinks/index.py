"""Process wikilinks"""
import re
import os
from typing import Any, Callable, Dict, Optional

from markdown_it import MarkdownIt
from markdown_it.common.utils import isSpace, normalizeReference
from markdown_it import ruler
from markdown_it.rules_inline import StateInline

# VALID_WIKI_PATTERN = re.compile(r"\[\[([^\]\[]+)\]\]")
VALID_WIKI_PATTERN = re.compile(r'\[\[([^\]\[\:\|]+)\]\]')
# FILENAME = re.compile(r'^(?:.*\/)*([^\/\r\n]+?|)(?=(?:\.[^\/\r\n.]*)?$)')

def wikilinks_plugin(md: MarkdownIt) -> None:
    """Plugin to parse wikilink type links

    It parses URI's stored between /* [[...]] */

    .. code-block:: md

        [[wikilink]]

    """
#    frontMatter = make_front_matter_rule()
    md.inline.ruler.before(
        "link",
        "wikilink",
        wikilink,
    )

def wikilink(state: StateInline, silent: bool) -> bool:

    title = ""
    label = None
    oldPos = state.pos
    maximum = state.posMax
    start = state.pos
    pos = start
    parseReference = True

     # check name
    match = VALID_WIKI_PATTERN.match(state.src[state.pos :])
    if not match:
        return False
    href = link = match.group(1)
    label = os.path.basename(link)

    if not silent:
        # state.pos = labelStart
        # state.posMax = labelEnd

        token = state.push("link_open", "a", 1)
        token.attrs = {"href": href}

        if title:
            token.attrSet("title", title)

        # note, this is not part of markdown-it JS, but is useful for renderers
        if label and state.md.options.get("store_labels", False):
            token.meta["label"] = label

#        state.md.inline.tokenize(state)

        token = state.push("link_close", "a", -1)

    state.pos = state.posMax
    state.posMax = maximum
    return True
