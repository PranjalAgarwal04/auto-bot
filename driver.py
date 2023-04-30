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


@app.route('/chatgpt', methods=['POST'])
def chatgpt():

    # gets the query from whatsapp
    incoming_query = request.values.get('Body', '').lower()

    if (incoming_query == "hi" or incoming_query == "hello" or incoming_query == "hey"):
        answer = """*Booking request!*
    Delhi -> Mumbai
    Requested by: Pranjal(+91 6393318060)
    Rent: Rs. 500
    Distance: 1400 km

    What do you want to do?:
    -> ```accept``` - To accept the request
    -> ```decline``` - To decline the request
    -> ```wait``` - To wait for sometime"""
    elif (incoming_query == "accept"):
        answer = """Enter the OTP"""
    elif (incoming_query == "4554"):
        answer = """Ride started!"""
    elif (incoming_query == "decline"):
        answer = """You've declined the request!"""
    elif (incoming_query == "wait"):
        answer = """You've asked to wait. Will contact you soon!"""
    else:
        # calls for chatgpt to answer the query
        answer = generate_response(incoming_query)

    # sends the answer back to whatsapp
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
