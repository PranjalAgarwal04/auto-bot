# AutoBot 🛺

This is the WhatsApp bot for booking an auto rickshaw.

## Pre-requisites 💡

- [ ] [OpenAI](https://platform.openai.com/overview)
  - [ ] Credit card
- [ ] [twilio](https://www.twilio.com/en-us)
  - [ ] WhatsApp
  - [ ] Phone number
- [ ] [aws](https://aws.amazon.com/)
- [ ] [ngrok](https://ngrok.com/)
- [ ] [Python](https://www.python.org/)
- [ ] [pip](https://pip.pypa.io/en/stable/)
- [ ] [Ubuntu](https://ubuntu.com/)
- [ ] Costs `$0.0002` per request

## Block Diagram 🗺️

![Diagram](./assets/images/block-diagram.png?raw=true "Diagram")

## Usage ⚙️

- Open two terminal and connect to  `EC2` in both terminals

  ```bash
  ssh -i "<key pair file name>" ubuntu@ec2-54-199-116-65.ap-northeast-1.compute.amazonaws.com
  ```

- Give super user access in both terminals

    ```bash
    sudo su
    ```

- In one terminal run `flask` app

  ```bash
  python3 user.py
  ```

- In another terminal run `ngrok`

  ```bash
  ngrok http 5000
  ```

## How to Build a Chatbot ⚒️

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
    chmod 400 <key pair file name>
    ```

  - Connect to `EC2` instance by copying `Example` command in terminal.

    ```bash
    ssh -i "<key pair file name>" ubuntu@ec2-54-199-116-65.ap-northeast-1.compute.amazonaws.com
    ```

  - In `EC2 Instance` Terminal
    - Switch to super user

      ```bash
      super su
      ```

    - Update `apt` package manager

      ```bash
      apt update
      ```

    - Upgrade `apt` package manager

      ```bash
      apt upgrade -y
      ```

    - Install `pip`

      ```bash
      apt install python3-pip -y
      ```

    - Create `requirements.txt` file and write all dependencies in it.

      ```bash
      nano requirements.txt
      ```

      ```txt
      Flask
      openai
      twilio
      pyngrok
      ```

      - Press `Ctrl+s` to save and `Ctrl+x` to exit.
    - Install dependencies

      ```bash
      python3 -m pip install -r requirements.txt
      ```

    - Install `ngrok`

      ```bash
      ngrok
      ```

    - Goto [ngrok](https://dashboard.ngrok.com/get-started/setup)
dashboard > `Getting Started` > `Your Authtoken` and copy your token.
    - In `EC2` terminal connect to `ngrok`

      ```bash
      ngrok authtoken <your ngrok token>
      ```

    - Export `openAI` api key

      ```bash
      export OPENAI_API_KEY=<your openAI api key>
      ```

    - You can run `printenv` to check if `OPENAI_API_KEY` is set.
    - Create `flask` script in `EC2`

      ```bash
      nano main.py
      ```

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

      - Press `Ctrl+s` to save and `Ctrl+x` to exit.

    - Change settings in `EC2` console
      - Go back to `Instance ID` and click on `Security` > `Security Groups` and click on security Group ID
      - Click on `Edit Inbound Rules` > `Add rule`
      - Select `Custom TCP` in `Type` and `5000` in `Port Range` and `Source` as `Anywhere-IPv4` and click on `Save rules`
    - Open a new terminal and connect to `EC2` instance

      ```bash
      ssh -i "<key pair file name>" ubuntu@ec2-54-199-116-65.ap-northeast-1.compute.amazonaws.com
      ```

    - Run `flask` app in one terminal

        ```bash
        python3 main.py
        ```

    - Run `ngrok` in another terminal

        ```bash
        ngrok http 5000
        ```

      - Copy the `Forwarding` `url` and add route `/chatgpt` in url

          ```bash
          https://<random string>.ngrok-free.app/chatgpt
          ```

    - Visit twilio sandbox and add `ngrok` url in `When a message comes in` section.

## References 📑

- [Machine Learning Hub](https://youtu.be/Fej2wb4YHes)
- [Data Stream](https://youtu.be/mNMv3WNgp0c)

## Authors 🧿

- [@pranjal](https://github.com/PranjalAgarwal04)
- [@prajesh](https://github.com/prajeshElEvEn)
