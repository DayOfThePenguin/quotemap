import unittest

class MainTest(unittest.TestCase):

    def test_import_quote_class(self):
        self.assert(q = Quote(12, "quote", "comment"))

if __name__ == '__main__':
    unittest.main()
