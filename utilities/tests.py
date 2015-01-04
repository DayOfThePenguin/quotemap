import unittest
import console

class ConsoleTest(unittest.TestCase):

    def test_get_terminal_size(self):
        (width, height) = console.getTerminalSize()
        print("width: %i characters" % (width))
        print("height: %i characters" % (height))

if __name__ == '__main__':
    unittest.main()
