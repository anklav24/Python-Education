import unittest
from testing.unittest.cooking.main import nitro_salt


class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_mass(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(800), 8)

    def test_nitro_salt_returns_integer(self):
        self.assertIsInstance(nitro_salt(1000.341), int)

    def test_nitro_salt_receives_string_returns_integer(self):
        self.assertEqual(nitro_salt("1000"), 10)

    def test_nitro_salt_receives_alpha_string_returns_zero(self):
        self.assertEqual(nitro_salt('qwerty'), 0)


if __name__ == '__main__':
    unittest.main()
