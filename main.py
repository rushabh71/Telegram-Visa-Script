#Python scipt which uses Telethon - Telegram API to find messsages containing
#keywords like Go, Open, Opened, etc. which indicates visa slots opening.
#Upon finding these keywords in message it will play sound.

#@author Rushabh Patel

#Importing modules and install required libraries, if gives an error
from telethon import TelegramClient, events, utils
from pygame import mixer
import threading
import time
import datetime

date = 'Unknown'

#IMPORTANT : Use your api_id and api_hash by signing at 'https://my.telegram.org/auth'
api_id = 00000
api_hash = 'abcd0123456'
th = None
sound = None

mixer.init()

print('---------------------------------------------------------')
print('STARTED AT', datetime.datetime.now(), 'JAI MATA JI /\\')
print('---------------------------------------------------------')
print()
print('Select sound length:')
print(' 1. Short')
print(' 2. Long')
sip = input('Enter : ')
print()

if(sip=='1'):
    sound = 'C:/Users/rusha/Desktop/short_alarm.mp3' #short sound file path. NOTE: USE ONLY FORWARD SLASHES IN PATH
elif(sip=='2'):
    sound = 'C:/Users/rusha/Desktop/alarm.mp3' #long sound file path
else:
    sound = 'C:/Users/rusha/Desktop/short_alarm.mp3' #default sound file path

def alert():
    if('Mumbai Visa Prep & Experience' in date or 'F1 visa interview Experiences' in date):
        #Not playing sound, showing alert for visa experience groups messages
        return
    print('FOUND GO AT', datetime.datetime.now(), ' | ', date)
    mixer.music.load(sound)
    mixer.music.play()
    stop_alert()

def stop_alert():
    time.sleep(5) #Playing sound for 5 secs. You can change according to your need
    mixer.music.stop()

#Starting client
client = TelegramClient('session_name', api_id, api_hash)
client.start()


#Setting up async handlers to find pattern in messages

@client.on(events.NewMessage(pattern="go+|Go+|GO+"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    if ('logout' not in event.raw_text and 'Logout' not in event.raw_text and 'LOGOUT' not in event.raw_text):
        th = threading.Thread(target=alert())
        th.start()

@client.on(events.NewMessage(pattern=".+go|.+Go|.+GO"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    if ('logout' not in event.raw_text and 'Logout' not in event.raw_text and 'LOGOUT' not in event.raw_text):
        th = threading.Thread(target=alert())
        th.start()

@client.on(events.NewMessage(pattern="open+|Open+|OPEN+"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()

@client.on(events.NewMessage(pattern=".+open|.+Open|.+OPEN"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()

@client.on(events.NewMessage(pattern="opened+|Opened+|OPENED+"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()

@client.on(events.NewMessage(pattern=".+opened|.+Opened|.+OPENED"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()

@client.on(events.NewMessage(pattern="available+|Available+|AVAILABLE+"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    if('not' not in event.raw_text and 'Not' not in event.raw_text):
        th = threading.Thread(target=alert())
        th.start()

@client.on(events.NewMessage(pattern=".+available|.+Available|.+AVAILABLE"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    if ('not' not in event.raw_text and 'Not' not in event.raw_text):
        th = threading.Thread(target=alert())
        th.start()

@client.on(events.NewMessage(pattern="nov+|Nov+|NOV+"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()

@client.on(events.NewMessage(pattern=".+nov|.+Nov|.+NOV"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()

@client.on(events.NewMessage(pattern="dec+|Dec+|DEC+"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()

@client.on(events.NewMessage(pattern=".+dec|.+Dec|.+DEC"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()

@client.on(events.NewMessage(pattern="mar+|Mar+|MAR+"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()

@client.on(events.NewMessage(pattern=".+mar|.+Mar|.+MAR"))
async def handler(event):
    global date
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)
    date = chat_title + ' : ' + event.raw_text
    th = threading.Thread(target=alert())
    th.start()


client.run_until_disconnected() #Program will run until stopped by user






