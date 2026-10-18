import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORD_LIST = "unordered_list"
    ORD_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    final_blocks = []
    for block in blocks:
        if block.strip():
            final_blocks.append(block.strip())
    return final_blocks

def block_to_blocktype(block: str) -> BlockType:
    if re.match(r"#{1,6} ", block) != None:
        return BlockType.HEADING
    elif re.fullmatch(r"`{3}\n(.*?)`{3}", block, re.DOTALL) != None:
        return BlockType.CODE

    lines = block.split("\n")

    quote = True
    ulist = True
    olist = True
    currnum = 1

    for line in lines:
        if line[0] != ">":
            quote = False
            break
    for line in lines:
        if "- " != line[0:2]:
            ulist = False
            break
    for line in lines:
        if f"{currnum}. " != line[0:3]:
            olist = False
            break
        currnum += 1

    if quote:
        return BlockType.QUOTE
    elif olist:
        return BlockType.ORD_LIST
    elif ulist:
        return BlockType.UNORD_LIST

    return BlockType.PARAGRAPH
