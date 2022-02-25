from secretfile import *
from twilio.rest import Client


def send_sms(text,number):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=text,
        from_=sms_number,
        to=f'+91{number}'
    )
    print(message.sid)
