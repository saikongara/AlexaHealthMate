from flask import Flask
from flask_ask import Ask, statement, question, session
# import os
import logging
# import json
# import requests
# import time
# import unidecode

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)

# Start and restart the session
@ask.launch
@ask.intent("AMAZON.StartOverIntent")
def start_skill():
    welcome_message = " Hi there! This is Alexa. " \
                      " Now I am going to share some tachnical details involved in developing me." \
                      " Do you wanna start Sai? "
    return question(welcome_message)


@ask.intent("AMAZON.HelpIntent")
def help():
    help_message = "I am here to help Sai to present his work"
    return statement(help_message)

# # Initiation of Chest pain
# @ask.intent("FirstIntent")
# def First():
#     first_question = " Well ! I don't care. " \
#                      " If you don't like it, you may leave. " \
#                      " Are you staying, or leaving ? "
#     return question(first_question)
#
# @ask.intent("GetStartedIntent")
# def getStarted():
#     started_message = " Good. " \
#                       " let's get into work. " \
#                       " You wanna start ?"
#     return question(started_message)

@ask.intent("TechUsedIntent")
def technologyUsed():
    tech_message = " Firstly, he created an Amazon development portal to build a skill. " \
                   " The logic behind the operation of Alexa was Lambda function, which was built using flask ask API in python. " \
                   " Then the code was deployed into AWS, using Zaapa user, which was created from AWS I A M console. " \
                   " Is that all Sai ? or did I miss anything ?"
    return question(tech_message)

@ask.intent("DifficultiesIntent")
def difficulties():
    difficulties_message = " Oh ya! " \
                           " But its not we, its you who faced the difficulties. I simply took rest. " \
                           " Ok. Let's get back into our business. " \
                           " Its been a bit difficulty to create lambda function in AWS, and integrate with the skill. " \
                           " Alternately, we tried using n g rok to create a URL for locally executed lambda function. " \
                           " But the connection was not stable. " \
                           " Anything else team ? "
    return question(difficulties_message)

@ask.intent("StepsFollowedIntent")
def stepsFollowed():
    steps_message = "Sure. " \
                    " The steps he followed are, " \
                    " Step 1, Created a virtual environment locally, and installed all the required dependencies. " \
                    " Step 2, Created Lambda function locally in pyCharm, using flask a p i of python. " \
                    " Step 3, Created I A M account in AWS, and deployed code using Zaapa user which provides a static URL. " \
                    " Step 4, Opened a free tier Amazon developer account, and created an Alexa skill in it. " \
                    " Step 5, He provided the intentSchema as a JSON file to the Skill, and built it. " \
                    " Step 6, Later on Configured the skill with lambda function, using Zappa provided URL. " \
                    " What's next ? "
    return question(steps_message)


@ask.intent("TestReadyIntent")
def testReady():
    test_message = " Oh! Testing! Now the device is ready to test, using echo sim.i o virtually, or, using physical devices like Echo, or, Echo dot," \
                   " by connecting with same amazon account's user i d, and password. " \
                   " Actually, the intention while beginning was to implement Machine Learning libraries," \
                   " and Google APIs to incorporate. Which you can see in my next upgrade "
    return question(test_message)


@ask.intent("SendOffIntent")
@ask.intent("AMAZON.StopIntent")
def sendOff():
    sendoff_message = " Pleasure is mine. " \
                      " And by the way, Don't forget, I have my share of applause. "
    return statement(sendoff_message)


if __name__ == '__main__':
    app.run(debug=True)