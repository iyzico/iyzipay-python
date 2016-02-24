import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.Card import Card
from src.Iyzipay.Model.CardList import CardList


class CardStorageSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_create_user_and_add_card()
        self.should_create_card()
        self.should_delete_card()
        self.should_retrieve_cards()

    def should_create_user_and_add_card(self):
        card_information = {'card_alias': 'card alias',
                            'card_holder_name': 'John Doe',
                            'card_number': '5528790000000008',
                            'expire_month': '12',
                            'expire_year': '2030'}
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'email': 'email@email.com',
                   'external_id': 'external id',
                   'card': card_information}

        card = Card.create(request, BaseSample.options)

        pprint.pprint(card)

    def should_create_card(self):
        card_information = {'card_alias': 'card alias',
                            'card_holder_name': 'John Doe',
                            'card_number': '5528790000000008',
                            'expire_month': '12',
                            'expire_year': '2030'}
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'card_user_key': 'myCardUserKey',
                   'card': card_information}

        card = Card.create(request, BaseSample.options)

        pprint.pprint(card)

    def should_delete_card(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'card_token': 'myCardToken',
                   'card_user_key': 'myCardUserKey'}

        card = Card.delete(request, BaseSample.options)

        pprint.pprint(card)

    def should_retrieve_cards(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'card_user_key': 'myCardUserKey'}
        card_list = CardList.retrieve(request, BaseSample.options)

        pprint.pprint(card_list)
