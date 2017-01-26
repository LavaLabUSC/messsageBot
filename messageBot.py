import json
import os
import time
from slackclient import SlackClient
import random
from botId import bot

# constants
AT_BOT = "<@" + bot.id + ">"
EXAMPLE_COMMAND = "match"

rawMessages = open("inData.txt").read()
inMessages = json.loads(rawMessages)

# instantiate Slack & Twilio clients
slack_client = SlackClient(bot.token)

#get all users object
allUsers = slack_client.api_call("users.list")
allUserMembers = allUsers["members"]

def buildMessage(inMessage):
	message = {}

	for each in allUserMembers: # i really shouldn't be doing this EACH message... super inefficient.
		try:
			if each["profile"]["email"] == inMessage["email"]:
				message["userId"] = each["id"]
			# else:
				# print("bad")
		except:
			print("probably hit a bot...")
	
	message["text"] = inMessage["message"]

	return message


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("messagebot starting")
        for each in inMessages:
        	message = buildMessage(each)
        	print(message)
        	print("\n")
        	slack_client.api_call("chat.postMessage",channel=message["userId"],text=message["text"],as_user=True)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
