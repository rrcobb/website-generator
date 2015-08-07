import sys
import unittest
from generator import *

class GeneratorTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_p(self):
        self.assertEqual("<p></p>",
            create_paragraph(""))
        self.assertEqual("<p>Hello, World!</p>",
            create_paragraph("Hello, World!"))

    def test_h(self):
        self.assertEqual("<h1></h1>",
            create_header('',1))
        self.assertEqual("<h2>Subheader</h2>",
            create_header('Subheader',2))
        self.assertEqual("<h3>Here's one with spaces!</h3>",
            create_header("Here's one with spaces!",3))
        self.assertEqual("Testing a non 1-6 value",
            create_header("Testing a non 1-6 value",9))

    def test_a(self):
        self.assertEqual("<a href='http://www.seussville.com/'>Check out this Dr. Seuss Website</a>",
            create_link("Check out this Dr. Seuss Website","http://www.seussville.com/"))

    def test_img(self):
        self.assertEqual("<img src='' />",
            create_image(''))
        self.assertEqual("<img src='http://www.hdwallpapersimages.com/wp-content/uploads/2014/01/Winter-Tiger-Wild-Cat-Images.jpg' />",
            create_image("http://www.hdwallpapersimages.com/wp-content/uploads/2014/01/Winter-Tiger-Wild-Cat-Images.jpg"))
        self.assertEqual("<img src='http://www.hdwallpapersimages.com/wp-content/uploads/2014/01/Winter-Tiger-Wild-Cat-Images.jpg' alt='A fearsome tiger, lounging in the snow' />",
            create_image('http://www.hdwallpapersimages.com/wp-content/uploads/2014/01/Winter-Tiger-Wild-Cat-Images.jpg','A fearsome tiger, lounging in the snow'))

    def test_div(self):
        self.assertEqual("<div><h1>Seussical</h1><p>What would happen if we let musicians reinterpret Dr. Seuss's work?</p></div>",
            create_div("<h1>Seussical</h1><p>What would happen if we let musicians reinterpret Dr. Seuss's work?</p>"))
        self.assertEqual("<div class='silly'>I'm not sure, but it'll be silly!</div>",
            create_div("I'm not sure, but it'll be silly!", div_class="silly"))
        self.assertEqual("<div id='sillypic'><img src='images/sillypic.jpg' /></div>",
            create_div("<img src='images/sillypic.jpg' />", div_id="sillypic"))

    def test_head(self):
        self.assertEqual("<head>Here's the head!</head>",
            create_head("Here's the head!"))

    def test_body(self):
        self.assertEqual("<body>Here's the body!</body>",
            create_body("Here's the body!"))

    def test_page(self):
        self.assertEqual("<!DOCTYPE html><html>Just pretend this is a head and body, full of great things</html>",
            create_page("Just pretend this is a head and body, full of great things"))

    def test_element(self):
        self.assertEqual("<section class='Horton'>I hear a Who!</section>",
            create_element("section","I hear a Who!",{'class':'Horton'}))
        self.assertEqual("<em id='phrase'>I do not like them, Sam I Am!</em>",
            create_element("em","I do not like them, Sam I Am!",{'id':'phrase'}))
        self.assertEqual("<form action='/postdata' method='POST'><button type='submit'>Submit</button></form>",
            create_element("form",create_element("button","Submit",{'type':'submit'}),{'action':'/postdata', 'method':'POST'}))

if __name__ == "__main__":
    unittest.main()
