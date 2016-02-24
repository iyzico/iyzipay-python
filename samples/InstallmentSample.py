import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.InstallmentInfo import InstallmentInfo


class InstallmentSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_retrieve_installment_info()
        self.should_retrieve_installment_info_for_all_banks()

    def should_retrieve_installment_info(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'bin_number': '456721',
                   'price': '1'}

        installment_info = InstallmentInfo.retrieve(request, BaseSample.options)

        pprint.pprint(installment_info)

    def should_retrieve_installment_info_for_all_banks(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'price': '1'}

        installment_info = InstallmentInfo.retrieve(request, BaseSample.options)

        pprint.pprint(installment_info)
