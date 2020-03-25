from flask import Flask
from flask_ask import Ask, statement, question, session
import os
import logging
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
COUNTER = 0

def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)

# Start and restart the session
@ask.launch
@ask.intent("AMAZON.StartOverIntent")
def start_skill():
    global COUNTER
    COUNTER += 0
    welcome_message = " Welcome to the Optum medical triage!  You can ask me about your symptoms and I will try to assist you. " \
                      " If this is an emergency I would suggest you to call 9 1 1. " \
                      " What is your worst symptom ? Choose from Chest pain, Nausea, Shortness of breath and Fever."
    return question(welcome_message)

# Repeat the session
@ask.intent("RepeatProcessIntent")
def restartQuestionnaire():
    restart_message = "Choose some other symptoms. Choose one among. " \
                      "Chest pain, Nausea, Shortness of breath and Fever."
    return question(restart_message)

# Ending the conversation
@ask.intent("NoContinuationIntent")
@ask.intent("AMAZON.StopIntent")
def noContinuation():
    no_continuation_message = "Okay, got it! I am calculating your score. It is "
    if COUNTER > 15:
        return statement(no_continuation_message + str(COUNTER) + ". You should probably go see a doctor.")
    elif COUNTER > 6 & COUNTER <= 12:
        return statement(no_continuation_message + str(COUNTER) + ". Go to the closest urgent care for examination.")
    else:
        return statement(no_continuation_message + str(COUNTER) + ". You'll hopefully feel better. "
                                                                  "monitor for the next few days. Get some rest "
                                                                  "and stay hydrated.")

@ask.intent("AMAZON.HelpIntent")
def help():
    help_message = "I can assist you in finding the right care, but you need to answer a few of my questions to understand your problem better and help you. " \
                    "If it is an Emergency, I would suggest you to call 9 1 1 immediately"
    return statement(help_message)

# Initiation of Chest pain
@ask.intent("ChestIntent")
def chestFirst():
    global COUNTER
    COUNTER += 3
    chest_question = "Oh dear! Can you rate your pain on a scale of 1 to 10 ?"
    return question(chest_question)


@ask.intent("ChestGreaterThanSeven")
def chestGreaterThanSeven():
    emergency_chest_greater_than_seven = "You need Emergency care! call 9 1 1!"
    return statement(emergency_chest_greater_than_seven)


@ask.intent("ChestFiveToSeven")
def chestFiveToSeven():
    global COUNTER
    COUNTER += 2
    emergency_to_doctor = "It could be an Emergency!! Seek medical care as soon as possible!"
    return statement(emergency_to_doctor)


@ask.intent("ChestOneToFour")
def chestOneToFour():
    global COUNTER
    COUNTER += 1
    ask_radiates = "Does the pain radiate? Choose between it radiates and it does not radiate. "
    return question(ask_radiates)


@ask.intent("ChestRadiates")
def chestRadiates():
    affirmative = "Its an Emergency! call 9 1 1!"
    return statement(affirmative)


@ask.intent("ChestRadiatesNegative")
def chestRadiatesNegative():
    global COUNTER
    COUNTER += 1
    taste_question = "Okay, Do you have a metallic or coppery taste in your mouth? Choose between Mettalic, Coppery and its something different."
    return question(taste_question)


@ask.intent("MetallicCoppery")
def chestMetallicCoppery():
    affirmative_coppery = "Its possibily an Emergency! call 9 1 1, or seek imediate medical care."
    return statement(affirmative_coppery)


@ask.intent("NotMetallicCoppery")
def chestNotMetallicCoppery():
    negative_confirmation = "Ah, I see! Tell me more of your other symptoms? Are you ok with that ? Choose between yes or no."
    return question(negative_confirmation)

# Initiation of Nausea
@ask.intent("NauseaIntent")
def nauseaFirst():
    global COUNTER
    COUNTER += 2
    vomit_message = "Have you vomited? Choose between I have vomited or I have not vomited"
    return question(vomit_message)


@ask.intent("NauseaCan")
def nauseaCanAssumeVomit():
    global COUNTER
    COUNTER += 1
    sudden_onset = "Was it a sudden onset? Choose between 'sudden' and 'not sudden'"
    return question(sudden_onset)


@ask.intent("NauseaSuddenOnset")
def nauseaSuddenOnset():
    global COUNTER
    COUNTER += 1
    other_symptoms = "Are there any other symptoms that you are experiencing today? Choose between yes and no."
    return question(other_symptoms)


@ask.intent("NauseaNotSuddenOnset")
def nauseaNotSuddenOnset():
    others = "Do you have any other symptoms? Choose between yes and no."
    return question(others)


@ask.intent("NoVomitingIntent")
def nauseaNoVomitIntent():
    global COUNTER
    COUNTER += 1
    no_vomit = "Glad that you have not vomited. Is it safe to assume that you do not have stomach pain?" \
               "Choose between safe and not safe. "
    return question(no_vomit)


@ask.intent("NoStomachAche")
def nauseaNoStomachAche():
    no_ache = "Are you sure that you do not have a stomach ache? Choose between yes and no."
    return question(no_ache)


@ask.intent("StomachAche")
def nauseaStomachAche():
    ache_statement = "Ouch, that is unfortunate! Do you have any other symptoms? Choose between yes and no."
    return question(ache_statement)

# Initiation of Shortness in Breath
@ask.intent("BreathShortness")
def breathFirst():
    global COUNTER
    COUNTER += 3
    pressure_tightness = "Do you have pressure or tightness in your chest? Choose between yes I do , or no I don't."
    return question(pressure_tightness)


@ask.intent("NoBreathShortness")
def noBreathShortness():
    global COUNTER
    COUNTER += 1
    cough_check = "Do you have cough? Choose between positive and negative."
    return question(cough_check)


@ask.intent("BreathCoughIntent")
def breathCough():
    global COUNTER
    COUNTER += 1
    breath_cough = "Okay, Can I confirm that you have a cough? Choose between right and wrong."
    return question(breath_cough)


@ask.intent("NoCoughIntent")
def breathNoCough():
    breath_no_cough = "Ok, I understand , Do you have any other symptoms? Choose between yes and no."
    return question(breath_no_cough)


# Initiation of Fever
@ask.intent("FeverIntent")
def feverFirst():
    global COUNTER
    COUNTER += 2
    temperature_check = "Did you check your temperature? If yes, Choose among 'Greater than hundred and five', 'between hundred and hundred and five','less than hundred'. " \
                        " If not, say no and check your temperature. " \
                        " Don't own a thermometer? " \
                        " I found few on Amazon with good reviews. " \
                        " With Amazon prime now, I can have it to your door within an hour. "
    return question(temperature_check)

@ask.intent("TemperatureIntentHigh")
def feverTemperatureHigh():
    return statement("This sounds like an emergency. Call 9 1 1, or seek imediate medical care!")

@ask.intent("TemperatureIntentMedium")
def feverTemperatureMedium():
    global COUNTER
    COUNTER += 2
    return statement("You should probably see a doctor at a nearby clinic.  The closest is Minutt Clinic at 8251 Columbine Rd, Eden Prairie, MN 55344. " \
                        "Current wait time is 18 minutes")

@ask.intent("TemperatureIntentLow")
def feverTemperatureLow():
    global COUNTER
    COUNTER += 1
    return question("Take some medicine and rest. That should be good. " \
                 "Do you have any other symptoms? Choose between yes and no.")


if __name__ == '__main__':
    app.run(debug=True)