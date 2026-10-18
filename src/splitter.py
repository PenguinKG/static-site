import re

from textnode import TextNode, TextType


def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter:str, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAINTEXT:
            new_nodes.append(node)
        else:
            if node.text.count(delimiter)%2 != 0:
                raise ValueError("Unclosed delimiter")

            even = False

            for value in node.text.split(delimiter):
                if not even and value != "":
                    subnode = TextNode(value, TextType.PLAINTEXT)
                    new_nodes.append(subnode)
                elif value != "":
                    subnode = TextNode(value, text_type)
                    new_nodes.append(subnode)
                even = not even
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
        else:
            texto = node.text
            for image in images:
                sections = texto.split(f"![{image[0]}]({image[1]})", 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], node.text_type))
                new_nodes.append(TextNode(image[0], TextType.IMAGES, image[1]))
                texto = sections[1]
            if sections[-1]:  # pyright: ignore[reportPossiblyUnboundVariable]
               new_nodes.append(TextNode(sections[-1], node.text_type))   # pyright: ignore[reportPossiblyUnboundVariable]
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
        else:
            texto = node.text
            sections = texto
            for link in links:
                sections = texto.split(f"[{link[0]}]({link[1]})", 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], node.text_type))
                new_nodes.append(TextNode(link[0], TextType.LINKS, link[1]))
                texto = sections[1]
            if sections[-1]:
               new_nodes.append(TextNode(sections[-1], node.text_type))

    return new_nodes
