# Create main.py with FastAPI initialization

# Add all necessary imports

from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Add /voice endpoint structure

 #Add complete TwiML XML response
 
 # Add pause after greeting
 
 # Add fallback message
@app.post("/voice", response_class=PlainTextResponse)
def voice_response():
    return """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="Polly.Joanna" language="en-US">
        Hello, this is your virtual assistant calling on behalf of John Doe to schedule a consultation with Dr. Smith.
    </Say>
    <Pause length="1"/> 
    <Gather numDigits="1" action="/process" method="POST">
        <Say voice="Polly.Joanna" language="en-US">
            Please press 1 for Monday morning, 2 for Tuesday afternoon, or 3 for Wednesday evening.
        </Say>
    </Gather>
    <Say voice="Polly.Joanna">We didn’t receive any input. Goodbye!</Say>
</Response>
"""
# Add Gather element for input

# Add /process endpoint

# Add if-elif-else logic

@app.post("/process", response_class=PlainTextResponse)
def process_response(Digits: str = Form(...)):
    if Digits == "1":
        msg = "Your appointment is set for Monday at 10 AM."
    elif Digits == "2":
        msg = "Your appointment is set for Tuesday at 2 PM."
    else:
        msg = "Sorry, no appointments are available for that day."

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">{msg}</Say>
</Response>"""
from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/voice", response_class=PlainTextResponse)
def voice_response():
    return """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="Polly.Joanna" language="en-US">
        Hello, this is your virtual assistant calling on behalf of John Doe to schedule a consultation with Dr. Smith.
    </Say>
    <Pause length="1"/>
    <Gather numDigits="1" action="/process" method="POST">
        <Say voice="Polly.Joanna" language="en-US">
            Please press 1 for Monday morning, 2 for Tuesday afternoon, or 3 for Wednesday evening.
        </Say>
    </Gather>
    <Say voice="Polly.Joanna">We didn’t receive any input. Goodbye!</Say>
</Response>
"""

@app.post("/process", response_class=PlainTextResponse)
def process_response(Digits: str = Form(...)):
    if Digits == "1":
        msg = "Your appointment is set for Monday at 10 AM."
    elif Digits == "2":
        msg = "Your appointment is set for Tuesday at 2 PM."
    else:
        msg = "Sorry, no appointments are available for that day."

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">{msg}</Say>
</Response>"""
