import unittest

from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader

spec = spec_from_loader("base64url", SourceFileLoader("base64url", "./base64url"))
base64url = module_from_spec(spec)
spec.loader.exec_module(base64url)

class TestBase64URL(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(base64url.decode('SGVsbG8gd29ybGQ='), b'Hello world')

    def test_decode_no_padding(self):
        self.assertEqual(base64url.decode('SGVsbG8gd29ybGQ'), b'Hello world')

    def test_decode_empty_string(self):
        self.assertEqual(base64url.decode(''), b'')

    def test_encode(self):
        self.assertEqual(base64url.encode(b'Hello world'), 'SGVsbG8gd29ybGQ=')

    def test_encode_trimmed(self):
        self.assertEqual(base64url.encode(b'Hello world', trim=True), 'SGVsbG8gd29ybGQ')

if __name__ == "__main__":
    unittest.main()
