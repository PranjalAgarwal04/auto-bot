from flask import Flask, request, jsonify
import openai
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_response(query):
    model_engine = "text-davinci-002"
    prompt = (f"Q: {query}\n"
              "A:")
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer


def check(q):
    if (q == "hi" or q == "hello" or q == "hey"):
        answer = """*Hello!* how may I help you?

Type:
    -> ```book``` - To book an auto
    -> ```report``` - To report an issue
    -> ```help``` - To get help"""
    elif (q == "book"):
        answer = """*Book an auto*

Enter your *current* location."""
    elif (q == "report"):
        answer = """*Report an issue*

Please write down your issue."""
    elif (q == "help"):
        answer = """*Help*

By sending ```hi/hello/hey```, the bot gets activated. Then, you can book an auto to reach to your final destination. In case of any issue, kindly select ```report``` option and the issue will be resolved as soon as possible."""
    elif (q == "muradnagar"):
        answer = """You chose ```Muradnagar``` as your current location.

Tell me your destination."""
    elif (q == "raj nagar extension"):
        answer = """You chose ```Raj Nagar Extension``` as your destination.

Looking for the nearest auto driver..."""
    elif (q == "otp"):
        answer = """*Auto Located!*
Driver: Suresh
Auto number: DL 34 4859
Contact number: 9645702090
Your OTP for the ride is ```4554```."""
    elif (q == "start"):
        answer = """Ride started!"""
    elif (q == "end"):
        answer = """*Destination Reached!*

Did you enjoy the ride?
Please rate your experience from 1 - 5."""
    elif (q == "1" or q == "2" or q == "3" or q == "4" or q == "5"):
        answer = """Thanks for giving us the feedback!
Your valuable feedback means a lot to us."""
    else:
        answer = generate_response(q)
    return answer


@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    incoming_query = request.values.get('Body', '').lower()
    answer = check(incoming_query)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(answer)
    return str(resp)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )
