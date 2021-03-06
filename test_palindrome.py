from palindrome import palindrome

# Unittest test case
import unittest

class PalindromeTests(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(palindrome("bob"))
        self.assertTrue(palindrome("racecar"))
        self.assertTrue(palindrome("amanaplanacanalpanama"))
        self.assertTrue(palindrome(""))

    def test_non_palindromes(self):
        self.assertFalse(palindrome("submarine"))
        self.assertFalse(palindrome("\t "))

    # Make sure non-ASCII characters are handled properly.
    def test_utf8_multibyte(self):
        self.assertTrue(palindrome("ð"))
        self.assertTrue(palindrome("ðâ¹ï¸ð"))
        self.assertFalse(palindrome("ðâ¹ï¸"))

    # Make sure Unicode extended grapheme clusters are handled properly.
    def test_grapheme(self):
        # 'b' + 'o' + combining acute accent + 'b'
        self.assertTrue(palindrome("boÌb"))
        # man + zero-width joiner + woman + ZWJ + boy
        self.assertTrue(palindrome("ð¨âð©âð¦"))


# Pytest test case
def test_simple_palindromes():
    assert palindrome("bob")
    assert palindrome("racecar")
    assert palindrome("amanaplanacanalpanama")
    assert palindrome("")

def test_non_palindromes():
    assert not palindrome("submarine")
    assert not palindrome("\t ")

# Make sure non-ASCII characters are handled properly.
def test_utf8_multibyte():
    assert palindrome("ð")
    assert palindrome("ðâ¹ï¸ð")
    assert not palindrome("ðâ¹ï¸")

# Make sure Unicode extended grapheme clusters are handled properly.
def test_grapheme():
    # 'b' + 'o' + combining acute accent + 'b'
    assert palindrome("boÌb")
    # man + zero-width joiner + woman + ZWJ + boy
    assert palindrome("ð¨âð©âð¦")
