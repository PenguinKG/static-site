import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is a text node", TextType.BOLD)
        node6 = TextNode("This is not the same text node", TextType.BOLD)
        node7 = TextNode("This is a text node", TextType.BOLD, "https://4kstore.com")
        node8 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node5, node6)
        self.assertNotEqual(node7, node8)
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAINTEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
if __name__ == "__main__":
    unittest.main()
