# Download the
import os
from twilio.rest import Client

account_sid = 'ACa94cd5cafc5c0bfdb3b259bf4c664cdf'
auth_token = 'f085a3eb99221bd4fab5ec1d84c4d8f2'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello, there!',
    to='whatsapp:+916393318060'
)

print(message.sid)
