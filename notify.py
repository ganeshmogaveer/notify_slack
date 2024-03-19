import os
import winsound
import pyttsx3
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import time

# Initialize a WebClient instance with your bot token
client = WebClient(token="xoxb-6728127657139-6837010623696-XYieE7EXZAy4E1Jp4mtmPDbJ")

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

def process_message(message):
    message_text = message.get("text", "")
    if "busy" in message_text.lower():
        service_name = extract_service_name(message_text)
        if service_name:
            play_audio_once("C:\\Users\\gouta\\Desktop\\demo\\high alert.mp3")
            speak_service_name(service_name)
    else:
        service_name = extract_service_name(message_text)
        if service_name:
            play_audio_once("C:\\Users\\gouta\\Desktop\\demo\\new alert.mp3")
            speak_service_name(service_name)

def extract_service_name(message_text):
    # Extract and return the service name mentioned in the message
    if "Service:" in message_text:
        service_name = message_text.split("Service:")[1].split("\n")[0].strip()
        return service_name
    return None

def play_audio_once(file_path):
    # Play audio file only once
    if not os.path.exists(file_path):
        return
    winsound.PlaySound(file_path, winsound.SND_FILENAME)

def speak_service_name(service_name):
    # Speak the service name using pyttsx3
    engine.say(service_name)
    engine.runAndWait()

# Function to retrieve the latest message from the Slack channel and process it
def retrieve_latest_message():
    try:
        response = client.conversations_history(channel="C06MGL8T3LL", limit=1)
        messages = response["messages"]
        if messages:
            process_message(messages[0])
            time.sleep(1)  # Wait briefly before ending
    except SlackApiError as e:
        print("Error retrieving messages:", e.response["error"])

if __name__ == "__main__":
    while True:
        retrieve_latest_message()
