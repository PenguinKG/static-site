import unittest

from file_rw import extract_title


class TestMain(unittest.TestCase):
    def test_title_extractor(self):
        md = """
#This is not the title


My chilito is hot


# This is the tru title
"""
        self.assertEqual(extract_title(md), "This is the tru title")
    if __name__ == "__main__":
        unittest.main()
