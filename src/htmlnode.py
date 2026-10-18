class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props: dict | None = None,
        children: list["HTMLNode"] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        props = ""
        for key in self.props:
            props += f" {key}={self.props[key]}"

        return props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict | None = None,
    ):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("The leaf node has no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,
        tag: str,
        children: list[HTMLNode],
        props: dict | None = None
    ) -> None:
        super().__init__(tag, None, props, children)
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("The node has no tag")
        if not self.children:
            raise ValueError("The parent node has no children")
        children_html = ""
        for node in self.children:
            children_html += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
