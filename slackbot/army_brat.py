import os
import time
from slackclient import SlackClient
import pdb
import webbrowser
# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
MAIN_COMMAND   = "https://github.com/Dhiraj240/wtfpython-web/blob/development/slackbot/Guidelines.md"
INVITE_COMMAND = "https://wtfpython-web-invite.herokuapp.com/"
CONTRI_COMMAND = "https://github.com/wtfpython-web/wtfpython-web/wiki/Workflow"
CAKE_COMMAND   = "https://github.com/wtfpython-web/wtfpython-web/labels/difficulty%2Fcakewalk"
PRO_COMMAND    = "https://github.com/wtfpython-web/wtfpython-web/labels/difficulty%2Fpro"
INTR_COMMAND   = "https://github.com/wtfpython-web/wtfpython-web/labels/difficulty%2Fintermediate"
TOP_COMMAND    ="https://github.com/wtfpython-web/wtfpython-web/labels/difficulty%2Ftopcoder"
ISSUE_COMMAND  = "https://github.com/wtfpython-web/wtfpython-web/issues/new"
ASSIGN_COMMAND = "https://girlscriptgssoc.slack.com/messages/DBE359223/"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Please read this carefully" +"\n"+ MAIN_COMMAND 
                   
    if command.startswith("invite me"):
        response = "If you want to contribute follow this link" +"\n"+ INVITE_COMMAND + "\n" + \
                   " and get an invitation to our organisation using your github handle."

    if command.startswith("guide me"):
        response = "Read our Contributing guidelines" + "\n" + CONTRI_COMMAND

    if command.startswith("issues available"):
        response = "Newcomers Look at these issues"+"\n"+"Cake Walk Issues:"+CAKE_COMMAND+"\n"+"PRO Issues:"+PRO_COMMAND+"\n"+\
                   "Medium Issues:"+INTR_COMMAND+"\n"+"Else feel the heat "+"\n"+"TOPCODER Issues:"+TOP_COMMAND   

    if command.startswith("create issue"):
        response = "Sure..Head on to" + "\n" + ISSUE_COMMAND 

    if command.startswith("assign issue"):
        response= "Ask SatwikKansal....Happy Coding" + "\n" + ASSIGN_COMMAND  

    if command.startswith("copy"):
        message = command[5:]
        response = message

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_messages):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    if slack_messages and len(slack_messages) > 0:
        for message in slack_messages:
            if message and 'text' in message and AT_BOT in message['text']:
                command = message['text'].split(AT_BOT)[1].strip().lower()
                channel = message['channel']
                # return text after the @ mention, whitespace removed
                return command, channel
                       
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Army_Brat connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")