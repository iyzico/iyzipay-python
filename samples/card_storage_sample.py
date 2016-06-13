# coding=utf-8
import unittest
import iyzipay


class CardStorageSample(unittest.TestCase):
    def runTest(self):
        self.should_create_user_and_add_card()
        self.should_create_card()
        self.should_delete_card()
        self.should_retrieve_cards()

    def should_create_user_and_add_card(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456'
        request['email'] = 'email@email.com'
        request['externalId'] = 'external id'

        card_information = dict([('cardAlias', 'card alias')])
        card_information['cardNumber'] = '5528790000000008'
        card_information['expireYear'] = '2030'
        card_information['expireMonth'] = '12'
        card_information['cardHolderName'] = 'John Doe'
        request['card'] = card_information

        # make request
        card = iyzipay.Card()
        card_response = card.create(request, options)

        # print response
        print(card_response.read().decode('utf-8'))

    def should_create_card(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456'
        request['cardUserKey'] = 'card user key'

        card_information = dict([('cardAlias', 'card alias')])
        card_information['cardNumber'] = '5528790000000008'
        card_information['expireYear'] = '2030'
        card_information['expireMonth'] = '12'
        card_information['cardHolderName'] = 'John Doe'
        request['card'] = card_information

        # make request
        card = iyzipay.Card()
        card_response = card.create(request, options)

        # print response
        print(card_response.read().decode('utf-8'))

    def should_delete_card(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456'
        request['cardToken'] = 'card token'
        request['cardUserKey'] = 'card user key'

        # make request
        card = iyzipay.Card()
        card_response = card.delete(request, options)

        # print response
        print(card_response.read().decode('utf-8'))

    def should_retrieve_cards(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456'
        request['cardUserKey'] = 'card user key'

        # make request
        card_list = iyzipay.CardList()
        card_list_response = card_list.retrieve(request, options)

        # print response
        print(card_list_response.read().decode('utf-8'))