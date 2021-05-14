import os
import datetime

from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

conversations_store = {}
salutations_list = ["hi", "hello", "hey", "morning", "afternoon", "evening", "howdy", "greetings", "what's up", "yo", "sup"]
alternatives = ["all", "y'all", "folks", "people", "everybody", "everyone", "pals", "team"]

def say_stats(client, channel_id, time, numGuys):
    client.chat_scheduleMessage(
        channel=channel_id,
        post_at=time,
        text="You've sent 'hey guys' or something similar {} times in the past two weeks. For a more inclusive alternative, how about trying 'hey {}' in the future?".format(numGuys, alternatives.choice())
    )

def grab_message_history(channel_id):
    result = client.conversations_history(
        channel=channel_id,
        oldest=datetime.timedelta(days=-14)
        )

    conversation_history = result["messages"]

    # Print results
    print("{} messages found in {}".format(len(conversation_history), channel_id))


def fetch_conversations():
    try:
        # Call the conversations.list method using the WebClient
        result = client.conversations_list()
        save_conversations(result["channels"])

    except SlackApiError as e:
        logger.error("Error fetching conversations: {}".format(e))


# Put conversations into the JavaScript object
def save_conversations(conversations):
    conversation_id = ""
    for conversation in conversations:
        # Key conversation info on its unique ID
        conversation_id = conversation["id"]

        # Store the entire conversation object
        # (you may not need all of the info)
        conversations_store[conversation_id] = conversation


@app.message("digest")
def get_digest(message, say):
    ack()
    # Grab message history
    fetch_conversations()
    for conversation_id, conversation in conversations_store.items():
        print(conversation_id, conversation)
    say(f"Hey there <@{message['user']}>!")

'''
@app.command("/hey_bot_digest")
def get_digest(ack, say, client):
    ack()
    # Grab message history
    fetch_conversations()
    for conversation_id, conversation in conversations_store.items():
        print(conversation_id, conversation)
'''

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))