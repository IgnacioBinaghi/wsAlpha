from mailjet_rest import Client
import os
import pprint


def remove_mailjet(user_mail):
	api_key = '62ab7bb78295b072593fbf3c793118ca'
	api_secret = '6a18f10c1dd466f55e8bf221b87e706f'

	mailjet = Client(auth=(api_key, api_secret), version='v3')

	email = user_mail
	listID = '29238'
	action = 'remove' # or unsub??

	data = {
    		'Action': action,
    		'Contacts': [ { "Email": email } ]
	}

	result = mailjet.contactslist_managemanycontacts.create(id=listID, data=data)
	# print(result.status_code)
	# print(result.json())

def unsubcribe_mailjet(user_mail):
	api_key = '62ab7bb78295b072593fbf3c793118ca'
	api_secret = '6a18f10c1dd466f55e8bf221b87e706f'

	mailjet = Client(auth=(api_key, api_secret), version='v3')

	email = user_mail
	listID = '26947'
	action = 'unsub'

	data = {
    		'Action': action,
    		'Contacts': [ { "Email": email } ]
	}

	result = mailjet.contactslist_managemanycontacts.create(id=listID, data=data)
	# print(result.status_code)
	# print(result.json())
