from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    PLAINTEXT = "plaintext"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"


class TextNode:

    def __init__(self, text: str, text_type: "TextType", url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: "TextNode"):  # pyright: ignore[reportIncompatibleMethodOverride]
         cond1 = self.text == other.text
         cond2 = self.text_type == other.text_type
         cond3 = self.url == other.url
         return cond1 and cond2 and cond3
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type not in TextType:
        raise NotImplementedError("Nonexistant text type")
    match text_node.text_type:
        case TextType.PLAINTEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
