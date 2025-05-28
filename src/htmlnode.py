class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html is not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ""
        for key in self.props:
            html_string += f'{key}="{self.props[key]}" '
        return html_string.rstrip()

    def __eq__(self, node):
        return (
            self.tag == node.tag
            and self.value == node.value
            and self.children == node.children
            and self.props == node.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
