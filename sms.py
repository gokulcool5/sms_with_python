from twilio.rest import Client

account_sid = 'ACb9d9eccf9c4ec1a1abdcc8d76505bc00'
auth_token = 'be092a93c18bbdf24c0159791d83285b'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18703760938',
    body='this is for fun so no problem',
    to='+918438888352'
)

print(message.sid)