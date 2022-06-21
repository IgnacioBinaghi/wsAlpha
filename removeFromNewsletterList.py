from mailjet_rest import Client
import os

def unsub_mailjet(userEmail):
    api_key = '62ab7bb78295b072593fbf3c793118ca'
    api_secret = '6a18f10c1dd466f55e8bf221b87e706f'

    mailjet = Client(auth=(api_key, api_secret), version='v3')

    email = userEmail
    listID = '26947'
    action = 'unsubcribe' # or 'remove'??

    data = {
        'Action': action,
        'Contacts': [
          {
            "Email": userEmail,
          }
      ]
    }

    result = mailjet.contactslist_managemanycontacts.create(id=listID, data=data)
