import unittest
import bin.script as tumblr



class TumblTest(unittest.TestCase):
    
    def test__getpost_empty(self):
        self.assertEqual(tumblr.get_posts("http://batty.tumblr.com/"), [])
    
    def test_getpost_list(self):
    	self.assertEqual(isinstance(tumblr.get_posts("http://batty.tumblr.com/"), list), True)

    def test_getinfo_dict(self):
    	self.assertEqual(isinstance(tumblr.get_info("http://batty.tumblr.com/"), dict), True)

    def test_getinfo_url(self):
    	self.assertEqual(tumblr.get_info("http://batty.tumblr.com/")['url'], "http://batty.tumblr.com/")

    def test_getinfo_posts(self):
    	self.assertEqual(tumblr.get_info("http://batty.tumblr.com/")['total_posts'], 0)


tester = TumblTest()
tester.test__getpost_empty()
tester.test_getpost_list()
tester.test_getinfo_dict()
tester.test_getinfo_url()
tester.test_getinfo_posts()
