import base64
import unittest
from iyzipay.iyzipay_resource import IyzipayResource


class TestIyzipayResource(unittest.TestCase):
    def setUp(self):
        self.resource = IyzipayResource()
        self.secret_key = "test_secret_key"
        self.api_key = "test_api_key"
        self.options = {
            "api_key": self.api_key,
            "secret_key": self.secret_key,
            "base_url": "sandbox-api.iyzipay.com",
        }

    def test_calculate_hmac_sha256_signature_with_strings(self):
        params = ["12345", "TRY", "B67832", "conv123", "24.0", "20.0"]
        sig = self.resource.calculate_hmac_sha256_signature(params, self.secret_key)
        self.assertIsInstance(sig, str)
        self.assertEqual(len(sig), 64)  # SHA256 hex digest length

    def test_calculate_hmac_sha256_signature_with_non_string_types(self):
        # Should gracefully handle numbers and None without raising TypeError
        params = ["12345", None, 24.0, 1, 0]
        sig = self.resource.calculate_hmac_sha256_signature(params, self.secret_key)
        self.assertIsInstance(sig, str)
        self.assertEqual(len(sig), 64)

    def test_verify_signature_returns_true_on_match(self):
        params = ["payment123", "TRY", "100.0"]
        sig = self.resource.calculate_hmac_sha256_signature(params, self.secret_key)
        result = self.resource.verify_signature(params, self.secret_key, sig)
        self.assertIs(result, True)

    def test_verify_signature_returns_false_on_mismatch(self):
        params = ["payment123", "TRY", "100.0"]
        tampered_sig = "a" * 64
        result = self.resource.verify_signature(params, self.secret_key, tampered_sig)
        self.assertIs(result, False)

    def test_verify_signature_with_mixed_types(self):
        params = ["payment123", None, 100.50]
        sig = self.resource.calculate_hmac_sha256_signature(params, self.secret_key)
        result = self.resource.verify_signature(params, self.secret_key, sig)
        self.assertIs(result, True)

    def test_header_immutability_and_thread_safety(self):
        # Verify that get_http_header returns independent copies
        # and does not permanently mutate the class-level header
        initial_keys = set(IyzipayResource.header.keys())

        header1 = self.resource.get_http_header("/payment/test", self.options)
        self.assertIn("Authorization", header1)
        self.assertIn("x-iyzi-rnd", header1)

        # The class-level header must not be mutated
        self.assertEqual(set(IyzipayResource.header.keys()), initial_keys)
        self.assertNotIn("Authorization", IyzipayResource.header)
        self.assertNotIn("x-iyzi-rnd", IyzipayResource.header)

        # Separate calls must return independent dictionaries
        header2 = self.resource.get_http_header("/payment/test", self.options)
        self.assertIsNot(header1, header2)

    def test_strip_zero(self):
        self.assertEqual(IyzipayResource.strip_zero("10.0"), "10")
        self.assertEqual(IyzipayResource.strip_zero("10.5"), "10.5")
        self.assertEqual(IyzipayResource.strip_zero("10"), "10")

    def test_generate_random_string(self):
        rnd = IyzipayResource.generate_random_string(8)
        self.assertEqual(len(rnd), 8)
        self.assertTrue(rnd.isalnum())

        rnd16 = IyzipayResource.generate_random_string(16)
        self.assertEqual(len(rnd16), 16)

    def test_generate_v2_hash(self):
        v2_hash = IyzipayResource.generate_v2_hash(
            self.api_key,
            "/payment/test",
            self.secret_key,
            "random123",
            '{"locale":"tr"}',
        )
        self.assertIsInstance(v2_hash, str)
        # Decodes valid base64
        decoded = base64.b64decode(v2_hash).decode("utf-8")
        self.assertIn(f"apiKey:{self.api_key}", decoded)
        self.assertIn("randomKey:random123", decoded)
        self.assertIn("signature:", decoded)

    def test_generate_v2_hash_with_none_body(self):
        # Handles None body without throwing TypeError
        v2_hash = IyzipayResource.generate_v2_hash(
            self.api_key,
            "/payment/test",
            self.secret_key,
            "random123",
            None,
        )
        self.assertIsInstance(v2_hash, str)


if __name__ == "__main__":
    unittest.main()
