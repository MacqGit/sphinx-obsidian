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

# TODO: Test if not external link
    #
    # Link reference
    #
    # if "references" not in state.env:
    #     return False

    # if pos < maximum and state.srcCharCode[pos+1] == 0x5B:  # /* [ */
        #
        # Inline link
        #

        # might have found a valid shortcut link, disable reference parsing
        #parseReference = False

        # [[  <href>  ]]
        #   ^^ skipping these spaces
        # pos += 2
        # while pos < maximum:
        #     code = state.srcCharCode[pos]
        #     if not isSpace(code) and code != 0x0A:
        #         break
        #     pos += 1
        #
        # if pos >= maximum:
        #     return False

        # [[  <href>  ]]
        #     ^^^^^^ parsing link destination
        # start = pos
        # res = state.md.helpers.parseLinkDestination(state.src, pos, state.posMax)
        # if res.ok:
        #     href = state.md.normalizeLink(res.str)
        #     if state.md.validateLink(href):
        #         pos = res.pos
        #     else:
        #         href = ""

            # [link](  <href>  "title"  )
            #                ^^ skipping these spaces
            # start = pos
            # while pos < maximum:
            #     code = state.srcCharCode[pos]
            #     if not isSpace(code) and code != 0x0A:
            #         break
            #     pos += 1

            # [link](  <href>  "title"  )
            #                  ^^^^^^^ parsing link title
            # res = state.md.helpers.parseLinkTitle(state.src, pos, state.posMax)
            # if pos < maximum and start != pos and res.ok:
            #     title = res.str
            #     pos = res.pos
            #
            #     # [link](  <href>  "title"  )
            #     #                         ^^ skipping these spaces
            #     while pos < maximum:
            #         code = state.srcCharCode[pos]
            #         if not isSpace(code) and code != 0x0A:
            #             break
            #         pos += 1

        # if pos >= maximum or state.srcCharCode[pos] != 0x5D:  # /* ] */)
        #     # parsing a valid shortcut link failed, fallback to reference
        #     parseReference = True

    #     pos += 1        
    #
    #
    #
    #     pos = state.md.helpers.parseLinkLabel(state, pos)
    #     if pos >= 0:
    #         label = state.src[start:pos]
    #         pos += 1
    #     else:
    #         pos = labelEnd + 1
    #
    # else:
    #     pos = labelEnd + 1
    #
    # # covers label == '' and label == undefined
    # # (collapsed reference link and shortcut reference link respectively)
    # if not label:
    #     label = state.src[labelStart:labelEnd]
    #
    # label = normalizeReference(label)
    #
    # ref = (
    #     state.env["references"][label] if label in state.env["references"] else None
    # )
    # if not ref:
    #     state.pos = oldPos
    #     return False
    #
    # href = ref["href"]
    # title = ref["title"]

    #
    # We found the end of the link, and know for a fact it's a valid link
    # so all that's left to do is to call tokenizer.
    #
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
