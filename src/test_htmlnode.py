import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html1 = HTMLNode("a", "This is html text", {"href": "https://chiquito.com", "width": 1920})
        html2 = HTMLNode("a", "This is html text", {"href": "https://grandecito.com", "width": 1080})
        html3 = HTMLNode("a", "This is html text", {"href": "https://medianito.com", "width": 1440})

        self.assertEqual(html1.props_to_html(), " href=https://chiquito.com width=1920")
        self.assertEqual(html2.props_to_html(), " href=https://grandecito.com width=1080")
        self.assertEqual(html3.props_to_html(), " href=https://medianito.com width=1440")

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        node1 = LeafNode("a", "Hello, worlds!", {"href": "https://chiquito.com", "width": 1920})
        node2 = LeafNode("b", "Hola, mi mundo!", {"href": "https://medianito.com", "width": 1440})

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node1.to_html(), "<a href=https://chiquito.com width=1920>Hello, worlds!</a>")
        self.assertEqual(node2.to_html(), "<b href=https://medianito.com width=1440>Hola, mi mundo!</b>")
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
