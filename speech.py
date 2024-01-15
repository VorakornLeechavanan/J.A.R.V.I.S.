"""Welcome to the coding section for the Genius AI, J.A.R.V.I.S. """
import speech_recognition as sr
import pyttsx3
import os
import openai
from dotenv import load_dotenv

# Constants
OPEN_AI_KEY = os.getenv('OPENAI_KEY')
RECOGNIZER = sr.Recognizer()
MESSAGES = []


def speak_text(cmd):
    """J.A.R.V.I.S. is allowed to speak. """
    engine = pyttsx3.init()
    engine.say(cmd)
    engine.runAndWait()


def record_text():
    """J.A.R.V.I.S. status will be printed during the conversation. """
    while 1:
        try:
            with sr.Microphone() as source2:
                RECOGNIZER.adjust_for_ambient_noise(source2, duration=.2)
                print("I'm listening")

        except sr.RequestError as e:
            print('Could not request results; {0}'.format(e))

        except sr.UnknownValueError:
            print("Unknown Error Occured")


def send_to_chatgpt(msg, model="gpt-3.5-turbo"):
    """Deliver the message from the User to ChatGPT. """
    response = openai.ChatCompletion.create(
                  model=model,
                  messages=msg,
                  max_tokens=100,
                  n=1,
                  stop=None,
                  temperature=.5,
               )

    message = response.choices[0].message.content
    msg.append(response.choices[0].message)
    return message


if __name__ == "__main__":
   load_dotenv()
   openai.api_key = OPEN_AI_KEY

   while 1:
       text = record_text()
       MESSAGES.append({"role": "User", "content": text})

       # Bring the message to ChatGPT
       response = send_to_chatgpt(MESSAGES)
       speak_text(response)

       # Display the ChatGPT result
       print(response)








