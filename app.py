import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

salutations_list = ["hi", "hello", "hey", "morning", "afternoon", "evening", "howdy", "greetings", "what's up", "yo", "sup"]
alternatives = ["all", "y'all", "folks", "people", "everybody", "everyone", "pals", "team"]

def say_stats(client, channel_id, time, numGuys:
    client.chat_scheduleMessage(
        channel=channel_id,
        post_at=time,
        text="You've sent 'hey guys' or something similar {0} times in the past two weeks. For a more inclusive alternative, how about trying 'hey {1}' in the future?".format(numGuys, alternatives.choice())
    )

def calculate_stats()

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))