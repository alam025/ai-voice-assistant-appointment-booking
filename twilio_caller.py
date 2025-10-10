from twilio.rest import Client

# Use your actual Twilio details
TWILIO_SID = "TWILIO_SID"
TWILIO_AUTH_TOKEN = "6TWILIO_AUTH_TOKEN"
TWILIO_PHONE = "TWILIO_PHONE"  # Your Twilio number (no spaces!)
TO_PHONE = "+TO_PHONE"     # Your number (must be verified in trial mode)

# Your FastAPI public ngrok URL (copied from ngrok terminal)
TWIML_URL = "TWIML_URL"

def make_call():
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    call = client.calls.create(
        to=TO_PHONE,
        from_=TWILIO_PHONE,
        url=TWIML_URL
    )

    print("✅ Call initiated! SID:", call.sid)

if __name__ == "__main__":
    make_call()
