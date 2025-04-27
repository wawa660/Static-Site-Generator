import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    
    def test1(self):
        props = {"bgcolor" : "red", "color" : "black"}
        hn = HTMLNode("h1", "hello", props = props )
        self.assertEqual(hn.props, props)

    def test2(self):
        hn = HTMLNode()
        self.assertEqual(hn.props_to_html(), '')

    def test3(self):
        hn = HTMLNode("a", "link")
        hn2 = HTMLNode("a", "link")
        self.assertEqual(hn.tag, hn2.tag)
        self.assertEqual(hn.value, hn2.value)
    
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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "link", {"href" : "google.com", "color" : "red"})
        self.assertEqual(node.to_html(), '<a href="google.com" color="red">link</a>')

if __name__ == "__main__":
    unittest.main()
