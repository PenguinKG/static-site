from splitter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)
from textnode import TextNode, TextType


def text_to_textnodes(text: str) -> list[TextNode]:
    split_bold = split_nodes_delimiter([TextNode(text, TextType.PLAINTEXT)], "**", TextType.BOLD)
    split_italic = split_nodes_delimiter(split_bold, "_", TextType.ITALIC)
    split_code = split_nodes_delimiter(split_italic, "`", TextType.CODE)
    split_image = split_nodes_image(split_code)
    split_link = split_nodes_link(split_image)

    return split_link
