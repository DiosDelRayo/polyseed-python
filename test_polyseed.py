import unittest
import polyseed

class TestMyModule(unittest.TestCase):
    # Your test cases will go here

    def test_crypt(self):
        # Test the my_function from mymodule
        SEED = 'label cart fee spice decorate next holiday stand mom clown cool huge repeat expire giraffe own'
        PRIVATE_KEY = 'd421f95837686c00c0ff5f8f898cbafb85a35e58b1a305d9ba1e2609838ca416'
        PASSWORD = 'testpassword1'
        ps = polyseed.recover(SEED, None)
        key1 = ps.keygen().hex()
        ps.crypt(PASSWORD)
        ps.crypt(PASSWORD)
        key2 = ps.keygen().hex()
        self.assertEqual(key1, key2)
        self.assertEqual(key1, PRIVATE_KEY)
        self.assertEqual(key2, PRIVATE_KEY)

    def test_recovery(self):
        # Test the my_function from mymodule
        SEED = 'label cart fee spice decorate next holiday stand mom clown cool huge repeat expire giraffe own'
        PRIVATE_KEY = 'd421f95837686c00c0ff5f8f898cbafb85a35e58b1a305d9ba1e2609838ca416'
        ps = polyseed.recover(SEED, None)
        key = ps.keygen().hex()
        self.assertEqual(key, PRIVATE_KEY)

    def test_recovery_with_password_basic(self):
        # Test the my_function from mymodule
        SEED = 'spatial rail welcome across void office income maple win canyon spy peanut lazy woman section age'
        PRIVATE_KEY = '7f4c69b3e58ed453cff8f51afac64ef7c21682f1c37656f181b48cd8a945e6b8'
        PASSWORD = 'testpassword1'
        ps = polyseed.polyseed.Polyseed.decode(SEED)
        self.assertTrue(ps.is_encrypted())
        ps.crypt(PASSWORD)
        key = ps.keygen().hex()
        self.assertEqual(key, PRIVATE_KEY)

    def test_recovery_with_password(self):
        # Test the my_function from mymodule
        SEED = 'spatial rail welcome across void office income maple win canyon spy peanut lazy woman section age'
        PRIVATE_KEY = '7f4c69b3e58ed453cff8f51afac64ef7c21682f1c37656f181b48cd8a945e6b8'
        PASSWORD = 'testpassword1'
        ps = polyseed.recover(SEED, PASSWORD)
        key = ps.keygen().hex()
        self.assertEqual(key, PRIVATE_KEY)

    def test_recovery_with_wrong_password(self):
        # Test the my_function from mymodule
        SEED = 'spatial rail welcome across void office income maple win canyon spy peanut lazy woman section age'
        PRIVATE_KEY = '7f4c69b3e58ed453cff8f51afac64ef7c21682f1c37656f181b48cd8a945e6b8'
        PASSWORD = 'testpassword2'
        ps = polyseed.recover(SEED, PASSWORD)
        key = ps.keygen().hex()
        self.assertNotEqual(key, PRIVATE_KEY)

    def test_recovery_missing_password(self):
        # Test the my_function from mymodule
        SEED = 'spatial rail welcome across void office income maple win canyon spy peanut lazy woman section age'
        triggered: bool = False
        with self.assertRaises(polyseed.exceptions.PolyseedMissingPasswordException):
            ps = polyseed.recover(SEED, None)

    def test_create(self):
        def notsorandom(size: int) -> bytes:
            return b'A' * size
        ps = polyseed.polyseed.Polyseed.create(random=notsorandom)
        self.assertEqual(ps.keygen().hex(), 'a46fceb3c871c54e9771151f6e79c7f15d7216227bd51aa8679b257282c9d2bd')

    def test_generate_recover_key(self):
        ps1 = polyseed.generate(None)
        key1 = ps1.keygen().hex()
        phrase = ps1.encode()
        ps2 = polyseed.recover(phrase, None)
        key2 = ps2.keygen().hex()
        self.assertEqual(key1, key2)

    def test_generate_recover_key_with_pasword(self):
        PASSWORD = 'testpassword1'
        ps1 = polyseed.polyseed.Polyseed.create()
        phrase = ps1.encode()
        key1 = ps1.keygen().hex()
        ps1.crypt(PASSWORD)
        phrase1 = ps1.encode()
        ps2 = polyseed.polyseed.Polyseed.decode(phrase1)
        ps2.crypt(PASSWORD)
        phrase2 = ps2.encode()
        key2 = ps2.keygen().hex()
        self.assertEqual(phrase, phrase2)
        self.assertEqual(key1, key2)



if __name__ == '__main__':
    unittest.main()
