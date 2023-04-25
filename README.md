# autoBot

This is the whatsApp bot for booking an auto.

## How to Build a Chatbot

- Create accounts on:
  - [ ] [OpenAI](https://platform.openai.com/overview)
  - [ ] [twilio](https://www.twilio.com/try-twilio)
  - [ ] [aws](https://portal.aws.amazon.com/billing/signup?exp=default&sc_icampaign=acq_aws_takeover-default&sc_ichannel=ha&sc_icontent=awssm-evergreen_pac_default&sc_iplace=hero&trk=ha_awssm-evergreen_pac_default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email)
  - [ ] [ngrok](https://dashboard.ngrok.com/signup)

- Open `twilio` console
  - `Messaging` > `Try it out` > `Send a WhatsApp message`
- Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

- Create `.env` file
  - Get openAI api key from [here](https://platform.openai.com/overview)
  - `Personal` > `View API keys` > `Secret key`
  - Write your openAI api key in `.env` file

    ```env
    OPENAI_API_KEY=<your openAI api key>
    ```

- Create `flask` app script

  ```python
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
      incoming_query = request.values.get('Body', '').lower()
      answer = generate_response(incoming_query)
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
  ```

- Launch `EC2` in `aws`
  - Open AWS console.
  - Search for `ec2` and select `EC2 Virtual Servers in the Cloud`
  - Click on `Instances` > `Launch Instances`
  - Add a name to your instance
  - In `Application and OS Images (Amazon Machine Image)` select `Ubuntu Server 20.04 LTS (HVM), SSD Volume Type`
  - Add `key pair` and download it.
  - In `Network Settings`, `Enable` for `Auto-assign Public IP` and check `Allow HTTPS traffic from the Internet` and `Allow HTTP traffic from the Internet`
  - Click on `Launch Instance`
  - Go back to `Instances` and wait for `Instance State` to change to `Running`
  - Click on `Instance ID` and click on `Connect` and under `SSH client` copy the `3.` command and run it in the terminal opened from folder containing the `.pem` key pair file.

    ```bash
    chmod 400 pranjal-prajesh-autobot.pem
    ```

  - Connect to `EC2` instance by copying `Example` command in terminal.

    ```bash
    ssh -i "pranjal-prajesh-autobot.pem" ubuntu@ec2-54-199-116-65.ap-northeast-1.compute.amazonaws.com
    ```

- Install requirements in `EC2`
- Setup credentials in `EC2`
- Run `flask` app in `EC2`
- Run `ngrok` on same port as `flask` app
- Setup `ngrok` `url` in `twilio` sandbox

## References

- [Machine Learning Hub](https://youtu.be/Fej2wb4YHes)

## Authors

- [@pranjal](https://github.com/PranjalAgarwal04)
- [@prajesh](https://github.com/prajeshElEvEn)
