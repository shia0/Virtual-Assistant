
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import workalendar



listener = sr.Recognizer()
Ai = pyttsx3.init()
voices = Ai.getProperty('voices')
Ai.setProperty('voice', voices[1].id)


def talk(text):
    Ai.say(text)
    Ai.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Laura' in command:
                command = command.replace('Laura', '')
                print(command)
    except:
        pass
    return command


def run_lara():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'hello laura' in command:
        talk('Welcome!, how may I help you')
    elif 'can you hear me' in command:
        talk('Yes, I can hear you!')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        date = datetime.datetime.today().strftime("%B %d, %Y")
        talk("Today's Date is "+ date)
    elif 'what is your name' in command:
        talk('My Name is Laura')
    elif 'how are you' in command:
        talk('I am Well, How can I halp you today?')
    elif 'who is' in command:
        people = command.replace('people','')
        info = wikipedia.summary(people, 1)
        talk(info)
    elif 'where' in command:
        places = command.replace('where is', '')
        info = wikipedia.summary(places, 1)
        talk(info)
    elif 'when' in command:
        events = command.replace('when', '')
        info = wikipedia.summary(events, 1)
        talk(info)
    elif 'how' in command:
        reason = command.replace('how', '')
        info = wikipedia.summary(reason, 1)
        talk(info)
    elif 'what is' in command:
        things = command.replace('what is', '')
        info = wikipedia.summary(things, 1)
        talk(info)
    elif 'why' in command:
        clause = command.replace('why', '')
        info = wikipedia.summary(clause, 1)
        talk(info)
    else:
        talk('Please say the command again.')


while True:
    run_lara()
