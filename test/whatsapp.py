# Download the
import os
from twilio.rest import Client

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello, there!',
    to='whatsapp:+916393318060'
)

print(message.sid)
