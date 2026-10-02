import unittest
from iyzipay.pki_builder import PKIBuilder
from iyzipay.iyzipay_resource import IyzipayResource


class TestPKIBuilder(unittest.TestCase):
    def test_pki_builder_append(self):
        builder = PKIBuilder("")
        builder.append("locale", "tr")
        builder.append("conversationId", "123456789")
        pki_str = builder.get_request_string()
        self.assertEqual(pki_str, "[locale=tr,conversationId=123456789]")

    def test_pki_builder_append_price(self):
        builder = PKIBuilder("")
        builder.append_price("price", "10.50")
        pki_str = builder.get_request_string()
        self.assertEqual(pki_str, "[price=10.5]")

    def test_pki_builder_append_array(self):
        builder = PKIBuilder("")
        builder.append_array("items", ["[id=1]", "[id=2]"])
        pki_str = builder.get_request_string()
        self.assertEqual(pki_str, "[items=[[id=1], [id=2]]]")

    def test_payment_card_pki(self):
        card = {
            "cardHolderName": "John Doe",
            "cardNumber": "5528790000000008",
            "expireYear": "2030",
            "expireMonth": "12",
            "cvc": "123",
            "registerCard": "0",
            "cardAlias": "my card",
            "cardToken": "token123",
            "cardUserKey": "userKey123",
        }
        pki_str = IyzipayResource.payment_card_pki(card)
        self.assertIn("cardHolderName=John Doe", pki_str)
        self.assertIn("cardNumber=5528790000000008", pki_str)
        self.assertIn("cvc=123", pki_str)


if __name__ == "__main__":
    unittest.main()
