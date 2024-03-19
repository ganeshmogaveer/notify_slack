from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Initialize WebClient with your bot token
client = WebClient(token="xoxb-6728127657139-6816430362804-O6DQM0etWSLApRb9qjOekin3")

# Define the channel ID where you want to send the message
channel_id = "C06MGL8T3LL"

# Define the message you want to send
message = " BUSY_tool.collabo.rakuten.co.jp(1) Service: ssg-SOG_Service Urgency: ↑︎ High More actions"

try:
    # Call the chat.postMessage method to send a message to the channel
    response = client.chat_postMessage(channel=channel_id, text=message)
    print("Message sent successfully:", response["ts"])
except SlackApiError as e:
    print("Error sending message:", e.response["error"])
