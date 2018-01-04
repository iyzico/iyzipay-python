import unittest
import iyzipay

class PKIBuilderTest(unittest.TestCase):

    def test_append_when_value_available(self):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append('key', 'value')
        self.assertEqual(pki_builder.get_request_string(), '[key=value]')

    def test_append_when_value_not_available(self):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append('key')
        self.assertEqual(pki_builder.get_request_string(), '[]')

    def test_append_when_value_empty(self):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append('key', '')
        self.assertEqual(pki_builder.get_request_string(), '[]')
