import unittest

from markdown_to_html import markdown_to_html_node


class TestMDHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_headings(self):
        message = """
This is **bolded** paragraph

1. This is another paragraph with _italic_ text and `code` here
2. This is the same paragraph on a new line

3. This is not a ulist

1.Not an ordered list

>TwoTypes
- In one

>This is a quote
> This is also a quote

-Not a list

- This is a list
- with items

#Not a Heading

# Heading

## Heading

### Heading

#### Heading

##### Heading

###### Heading

####### Not a Heading

```
This is a code block
```

```This? State Property?
This ain't no state property, this is private ```
property


"""

        node = markdown_to_html_node(message)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><p>This is <b>bolded</b> paragraph</p><ol><li>This is another paragraph with <i>italic</i> text and <code>code</code> here</li><li>This is the same paragraph on a new line</li></ol><p>3. This is not a ulist</p><p>1.Not an ordered list</p><p>&gt;TwoTypes - In one</p><blockquote>This is a quote
This is also a quote</blockquote><p>-Not a list</p><ul><li>This is a list</li><li>with items</li></ul><p>#Not a Heading</p><h1>Heading</h1><h2>Heading</h2><h3>Heading</h3><h4>Heading</h4><h5>Heading</h5><h6>Heading</h6><p>####### Not a Heading</p><pre><code>This is a code block
</code></pre><p><code>This? State Property? This ain't no state property, this is private </code> property</p></div>""",
        )
