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
        answer = """*Hello!*
    How may I help you?
    Type the commands below to get started:
    -> ```book``` - To book an auto
    -> ```report``` - To report an issue
    -> ```help``` - To get help"""
    elif (q == "book"):
        answer = """*Book an auto*
    Enter your current location."""
    elif (q == "report"):
        answer = """*Report an issue*
    Please write down your issue."""
    elif (q == "help"):
        answer = """*Help*
    By sending ```hi/hello/hey```, the bot gets activated. Then, you can book an auto to reach to your final destination. In case of any issue, kindly select ```report``` option and the issue will be resolved as soon as possible."""
    elif (q == "delhi"):
        answer = """You chose ```Delhi``` as your current location.
    Tell me your destination."""
    elif (q == "mumbai"):
        answer = """You chose ```Mumbai``` as your destination.

    Looking for the nearest auto driver...

    *Auto Located!*
    Driver: Ramesh
    Auto number: DL 01 AB 1234
    Contact number: 9876543210"""
    else:
        # calls for chatgpt to answer the query
        answer = generate_response(q)


@app.route('/chatgpt', methods=['POST'])
def chatgpt():

    # gets the query from whatsapp
    incoming_query = request.values.get('Body', '').lower()

    answer = check(incoming_query)

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
