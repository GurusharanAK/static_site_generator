from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value is not provided")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, node):
        return (
            self.tag == node.tag
            and self.value == node.value
            and self.props == node.props
        )

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
