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

    def test_append_price_when_value_available(self):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append_price('price', 100)
        self.assertEqual(pki_builder.get_request_string(), '[price=100.0]')

    def test_append_price_when_value_not_available(self):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append_price('price')
        self.assertEqual(pki_builder.get_request_string(), '[]')

    def test_append_price_when_value_empty(self):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append_price('price', '')
        self.assertEqual(pki_builder.get_request_string(), '[]')

    def test_append_array_when_value_available(self):
        enabledInstallments = ['2', '3', '6', '9']
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append_array('data', enabledInstallments)
        self.assertEqual(pki_builder.get_request_string(), '[data=[2, 3, 6, 9]]')

    def test_append_array_when_value_not_available(self):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append_array('data')
        self.assertEqual(pki_builder.get_request_string(), '[]')

    def test_append_array_when_value_empty(self):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append_array('data', [])
        self.assertEqual(pki_builder.get_request_string(), '[]')
