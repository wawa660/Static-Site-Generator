import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    
    def test1(self):
        props = {"bgcolor" : "red", "color" : "black"}
        hn = HTMLNode("h1", "hello", props = props )
        self.assertEqual(hn.props_to_html(), ' bgcolor="red" color="black"')

    def test2(self):
        hn = HTMLNode()

    def test3(self):
        hn = HTMLNode("a", "link")
        hn2 = HTMLNode("a", "link")
        self.assertEqual(hn.tag, hn2.tag)
        self.assertEqual(hn.value, hn2.value)


if __name__ == "__main__":
    unittest.main()
