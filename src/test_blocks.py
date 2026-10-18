import unittest

from blocks import BlockType, block_to_blocktype, markdown_to_blocks


class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
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
        blocks = markdown_to_blocks(md)

        blocktypes = [block_to_blocktype(block) for block in blocks]

        self.assertEqual(blocktypes[0], BlockType.PARAGRAPH)
        self.assertEqual(blocktypes[1], BlockType.ORD_LIST)
        self.assertEqual(blocktypes[2], BlockType.PARAGRAPH)
        self.assertEqual(blocktypes[3], BlockType.PARAGRAPH)
        self.assertEqual(blocktypes[4], BlockType.PARAGRAPH)
        self.assertEqual(blocktypes[5], BlockType.QUOTE)
        self.assertEqual(blocktypes[6], BlockType.PARAGRAPH)
        self.assertEqual(blocktypes[7], BlockType.UNORD_LIST)
        self.assertEqual(blocktypes[8], BlockType.PARAGRAPH)
        self.assertEqual(blocktypes[9], BlockType.HEADING)
        self.assertEqual(blocktypes[10], BlockType.HEADING)
        self.assertEqual(blocktypes[11], BlockType.HEADING)
        self.assertEqual(blocktypes[12], BlockType.HEADING)
        self.assertEqual(blocktypes[13], BlockType.HEADING)
        self.assertEqual(blocktypes[14], BlockType.HEADING)
        self.assertEqual(blocktypes[15], BlockType.PARAGRAPH)
        self.assertEqual(blocktypes[16], BlockType.CODE)
        self.assertEqual(blocktypes[17], BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()
