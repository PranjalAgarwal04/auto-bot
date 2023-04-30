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
        answer = """*Booking request!*
Delhi -> Mumbai
Requested by: Pranjal(8791224496)
Rent: Rs. 120
Distance: 6 km

What do you want to do?:
    -> ```accept``` - To accept the request
    -> ```decline``` - To decline the request
    -> ```wait``` - To wait for sometime"""
    elif (q == "accept"):
        answer = """Enter the OTP"""
    elif (q == "4554"):
        answer = """Ride started!"""
    elif (q == "end"):
        answer = """Ride ended!
How was your experience with the customer?
Rate from 1 - 5."""
    elif (q == "1" or q == "2" or q == "3" or q == "4" or q == "5"):
        answer = """Thanks for giving us the feedback!
Your valuable feedback means a lot to us."""
    elif (q == "decline"):
        answer = """You've declined the request!"""
    elif (q == "wait"):
        answer = """You've asked to wait. Will contact you soon!"""
    else:
        # calls for chatgpt to answer the query
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
