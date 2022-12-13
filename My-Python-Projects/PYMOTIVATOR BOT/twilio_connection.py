from twilio.rest import Client 
from config import account_sid,auth_token,phone_number

def set_twilio_connection(account_sid,auth_token):
    """
    Sets a twilio connection for whatsapp and sends message

    """
    client = Client(account_sid, auth_token) 
    return client

def send_whatsapp_text(Client,quote):
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=quote,      
                              to='whatsapp:+918762049044' 
                            ) 
    return message.sid

client=set_twilio_connection(account_sid,auth_token)
 

    
