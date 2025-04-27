import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    
    def testeq(self):
        props = {"bgcolor" : "red", "color" : "black"}
        hn = HTMLNode("h1", "hello", props = props )
        self.assertEqual(hn.props, props)

    def test_no_args(self):
        hn = HTMLNode()
        self.assertEqual(hn.props_to_html(), '')

    def test_eq(self):
        hn = HTMLNode("a", "link")
        hn2 = HTMLNode("a", "link")
        self.assertEqual(hn.tag, hn2.tag)
        self.assertEqual(hn.value, hn2.value)

class TextParentNode(unittest.TestCase):    

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
class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "link", {"href" : "google.com", "color" : "red"})
        self.assertEqual(node.to_html(), '<a href="google.com" color="red">link</a>')

    
class TestTexttoHTML(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_img(self):
        node = TextNode("This is an img node", TextType.IMG, url="lirililarila.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {"src" : "lirililarila.png", "alt" : "This is an img node"})
        self.assertEqual(html_node.to_html(), '<img src="lirililarila.png" alt="This is an img node"></img>')


if __name__ == "__main__":
    unittest.main()
