from wc import wordcount

# Unittest test case
import unittest

class WordCountTest(unittest.TestCase):
    def test_simple_sentences(self):
        self.assertEqual(wordcount(""), 0)
        self.assertEqual(wordcount("a"), 1)
        self.assertEqual(wordcount("hello world"), 2)
        self.assertEqual(wordcount("the quick brown fox jumps over the lazy dog"), 9)

    def test_punctuation(self):
        self.assertEqual(wordcount("!"), 1)
        self.assertEqual(wordcount("... ... ..."), 3)
        self.assertEqual(wordcount("bla bla bla..."), 3)

    def test_nbsp(self):
        # the space here is a Unicode non-breaking space (U+00A0)
        self.assertEqual(wordcount("non-breaking space"), 2)
        #                                       ^


# Pytest test case

def test_simple_sentences():
    assert wordcount("") == 0
    assert wordcount("a") == 1
    assert wordcount("hello world") == 2
    assert wordcount("the quick brown fox jumps over the lazy dog") == 9

def test_punctuation():
    assert wordcount("!") == 1
    assert wordcount("... ... ...") == 3
    assert wordcount("bla bla bla...") == 3

def test_nbsp():
    # the space here is a Unicode non-breaking space (U+00A0
    assert wordcount("non-breaking space") == 2
    #                             ^
