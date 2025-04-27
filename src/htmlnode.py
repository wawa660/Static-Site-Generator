from textnode import TextType


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ''
        return ' ' + ' '.join([f'{key}="{self.props[key]}"' for key in self.props])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have value")
        if self.tag is None:
            return self.value
        tagstr = f"<{self.tag}{self.props_to_html()}>"
        engtagstr = f"</{self.tag}>"
        return f"{tagstr}{self.value}{engtagstr}"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag = tag, children = children, props = props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        tagstr = f"<{self.tag}{self.props_to_html()}>"
        engtagstr = f"</{self.tag}>"
        innerhtmlstring = ''
        for child in self.children:
            innerhtmlstring += child.to_html()
        return tagstr + innerhtmlstring + engtagstr


def text_node_to_html_node(text_node):
    text = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text)
        case TextType.BOLD:
            return LeafNode('b', text)
        case TextType.ITALIC:
            return LeafNode('i', text)
        case TextType.CODE:
            return LeafNode("code", text)
        case TextType.LINK:
            return LeafNode('a', text, {"href" : text_node.url})
        case TextType.IMG:
            return LeafNode("img", value='', props={"src" : text_node.url, "alt" : text})
        case _:
            raise ValueError("Invalid TextType")