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

    if (incoming_query == "hi"):
        answer = "Hi, I am a chatbot. Ask me anything."
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
