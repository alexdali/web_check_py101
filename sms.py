import log_srv
import os

from twilio.rest import Client
from dotenv import load_dotenv

logger = log_srv.get_logger(__name__)

def send_sms(msg_text):
    """
    send sms
    """
    load_dotenv()

    TWILIO_NUM_PHONE = os.getenv('TWILIO_NUM_PHONE')
    VERIFIED_NUM_PHONE = os.getenv('VERIFIED_NUM_PHONE')
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
      body=msg_text,
      from_=TWILIO_NUM_PHONE,
      to=VERIFIED_NUM_PHONE
    )


    return message.sid

if __name__ == "__main__":
    print(send_sms('Hi, just test'))