import unittest
from testing.full_name import full_name


class NameTestCase(unittest.TestCase):
    """Tests for the full_name.py func"""

    def test_first_last_middle(self):
        """Name looks like 'Name Lastname Middle'"""
        format_name = full_name('Name', 'Lastname', 'Middle')
        self.assertEqual(format_name, 'Name Lastname Middle')

    def test_first_last_name(self):
        """Name looks like 'Name Lastname'"""
        format_name = full_name('Name', 'Lastname')
        self.assertEqual(format_name, 'Name Lastname')


if __name__ == "__name__":
    unittest.main()

# Run from CLI
# python -m unittest rle
