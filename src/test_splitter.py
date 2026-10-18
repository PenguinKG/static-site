import unittest

from splitter import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
)
from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType


class TestDelimiterSplitter(unittest.TestCase):
    def testdelimiter(self):
        textnode1 = TextNode("This is a `code block` word", TextType.PLAINTEXT)
        textnode2 = TextNode("This is a **bold** **bold2**", TextType.PLAINTEXT)
        textnode3 = TextNode("This is an _italic_ word", TextType.PLAINTEXT)
        textnode4 = TextNode("This is an italic_ word with no valid closers", TextType.PLAINTEXT)
        textnode5 = TextNode("Th`*is is* a _code block_ wor`d", TextType.PLAINTEXT)

        nodes = [textnode1, textnode2, textnode3, textnode4, textnode5]

        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "_", TextType.ITALIC)

        self.assertEqual(split_nodes_delimiter([textnode2], "**", TextType.BOLD)[0].text_type, TextType.PLAINTEXT)
        self.assertEqual(split_nodes_delimiter([textnode2], "**", TextType.BOLD)[1].text_type, TextType.BOLD)

        self.assertEqual(split_nodes_delimiter([textnode1], "`", TextType.CODE)[0].text_type, TextType.PLAINTEXT)
        self.assertEqual(split_nodes_delimiter([textnode1], "`", TextType.CODE)[1].text_type, TextType.CODE)
        self.assertEqual(split_nodes_delimiter([textnode1], "`", TextType.CODE)[2].text_type, TextType.PLAINTEXT)

        self.assertEqual(split_nodes_delimiter([textnode3], "_", TextType.ITALIC)[0].text_type, TextType.PLAINTEXT)
        self.assertEqual(split_nodes_delimiter([textnode3], "_", TextType.ITALIC)[1].text_type, TextType.ITALIC)
        self.assertEqual(split_nodes_delimiter([textnode3], "_", TextType.ITALIC)[2].text_type, TextType.PLAINTEXT)

        self.assertListEqual(
            [
                TextNode("This is a ", TextType.PLAINTEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" ", TextType.PLAINTEXT),
                TextNode("bold2", TextType.BOLD),
            ],
            split_nodes_delimiter([textnode2], "**", TextType.BOLD),
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png and a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAINTEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAINTEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAINTEXT),
                TextNode("second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_final_split(self):
        message = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        textnodes = text_to_textnodes(message)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAINTEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAINTEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAINTEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAINTEXT),
                TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAINTEXT),
                TextNode("link", TextType.LINKS, "https://boot.dev"),
            ],
            textnodes,
        )

if __name__ == "__main__":
    unittest.main()
