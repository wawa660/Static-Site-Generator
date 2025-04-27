class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
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
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
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