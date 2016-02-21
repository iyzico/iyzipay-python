import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.BinNumber import BinNumber


class BinNumberSample(BaseSample, unittest.TestCase):
    def runTest(cls):
        cls.should_retrieve_bin_number()

    def should_retrieve_bin_number(cls):
        request = {'locale' : 'tr',
                   'conversation_id' : '123456789',
                   'bin_number' : '554960'}

        bin_number = BinNumber.retrieve(request, BaseSample.options)

        pprint.pprint(bin_number)
