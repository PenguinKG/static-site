import re

from blocks import (
    BlockType,
    block_to_blocktype,
    markdown_to_blocks,
)
from htmlnode import ParentNode
from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown: str) -> ParentNode:
    div_children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        blo2 = block
        type = block_to_blocktype(block)
        if type != BlockType.QUOTE and ">" in block:
            blo2 = block.replace(">", "&gt;")
        div_children.append(block_to_html_nodes(blo2, type))
    return ParentNode("div", div_children)



def block_to_html_nodes(block: str, type: BlockType):
    match type:
        case BlockType.PARAGRAPH:
            children = [text_node_to_html_node(node) for node in text_to_textnodes(block.replace("\n", " "))]
            return ParentNode("p", children)  # pyright: ignore[reportArgumentType]
        case BlockType.HEADING:
            text_without = block.lstrip("#")
            children = [text_node_to_html_node(node) for node in text_to_textnodes(text_without[1:])]  # pyright: ignore[reportUnboundVariable]
            hashtags = len(block)-len(text_without)  # pyright: ignore[reportArgumentType, reportOptionalMemberAccess]
            return ParentNode(f"h{hashtags}", children)  # pyright: ignore[reportArgumentType, reportOptionalMemberAccess]
        case BlockType.CODE:
            code = text_node_to_html_node(TextNode(block[4:-3], TextType.CODE))
            return ParentNode("pre", [code])
        case BlockType.QUOTE:
            children = []
            split = re.split(r"(?<=\n)", block)
            for line in split:
                newline = text_to_textnodes(line[1:].lstrip())
                children += newline
            listchildren = [text_node_to_html_node(node) for node in children]
            return ParentNode("blockquote", listchildren)  # pyright: ignore[reportArgumentType]
        case BlockType.UNORD_LIST:
            children = []
            for line in block.split("\n"):
                newline = text_to_textnodes(line[2:])
                lineparent = ParentNode("li", [text_node_to_html_node(node) for node in newline])
                children.append(lineparent)
            return ParentNode("ul", children)  # pyright: ignore[reportArgumentType]
        case BlockType.ORD_LIST:
            children = []
            for line in block.split("\n"):
                newline = text_to_textnodes(line[3:])
                lineparent = ParentNode("li", [text_node_to_html_node(node) for node in newline])
                children.append(lineparent)
            return ParentNode("ol", children)
