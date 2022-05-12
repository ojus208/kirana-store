from twilio.rest import Client

 
account_sid = 'ACff2f5338c88cc45acb9a2379c70ea764' 
auth_token = '816ee09c9236948c98ed15919d2c0079' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG1574e76754c59bedfc49ae4d6e45461d', 
                              body='your otp is 5555 dont share it with anyone form kiranastore',      
                              to='+919165130008' 
                          ) 
 
print(message.sid)