import telepot
from telepot.loop import MessageLoop
import time
import pprint
import requests
import json
from requests.auth import HTTPBasicAuth
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

def send_message(message):
    url = 'https://api.apifonica.com/v2/accounts/accc20bb584-3c1a-36cd-a49d-72b11795db36/messages'
    data = {
        "from": "3584573975908",
        "to": "380997150894",
        "text": message,
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url=url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(
        'accc20bb584-3c1a-36cd-a49d-72b11795db36',
        'autc451038d-783c-3076-8a28-a32bc653aa08'
    ))


bot = telepot.Bot('380236716:AAHqW3fXH7-5WaJ1x8ma1-JhnN-_8fH0yl8')
state = {}
info_message = '''
Present Simple обозначает действия, которые происходят в настоящее время, но не привязаны к моменту речи.


⇒ Чтобы составить утвердительное предложение с местоимениями I/we/you/they или с существительными, необходимо:

1.Поставить на первое место I/we/you/they или существительное(-ые) во множественном числе;
2. Глагол;
3. Остальные слова.

⇒ Чтобы составить утвердительное предложение с местоимениями he/she/it или с существительным, необходимо:

1.Поставить на первое место he/she/it или существительное в единственном числе;
2. Глагол с окончанием -s, -es;
3. Остальные слова.

⇒ Обратите внимание на формы to be и to have в Present Simple.

Глагол to be – быть, существовать, являться, находиться. Его формы: am/is/are.
- I употребляется только с am;
- He/she/it или существительное в единственном числе употребляются с is;
- We/you/they или существительное во множественном числе употребляются с are.

Глагол to have – иметь, обладать. Его формы: have/has.
- I/we/you/they или существительное во множественном числе употребляются с have;
- He/she/it или существительное в единственном числе употребляются с has.

I know something.
Я знаю что-то.

You look fine.
Ты выглядишь прекрасно.

I prefer cash.
Я предпочитаю наличные.
'''

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg['text']

    if text == '/help':
        send_message("All mentors are busy now")

    if content_type == 'text':
        if text == '/start':
            bot.sendMessage(chat_id, 'Select language for learning',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="English"), KeyboardButton(text="Deutch")],
                                    [KeyboardButton(text="Russian"), KeyboardButton(text="Ukrainian")],
                                    [KeyboardButton(text="Spainish"), KeyboardButton(text="Frence")],
                                    [KeyboardButton(text="Italian"), KeyboardButton(text="Dutch")],
                                ],
                                one_time_keyboard=True
                            ))
            return

    sid = str(chat_id)
    state[sid] = -1
    if text == 'English':
        bot.sendMessage(chat_id, 'Select topic for learning',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                [KeyboardButton(text="Present Simple"), KeyboardButton(text="Present Continiouse")],
                                [KeyboardButton(text="Present Perfect"), KeyboardButton(text="Past Simple")],
                                [KeyboardButton(text="Past Continiouse"), KeyboardButton(text="Past Perfect")],
                                [KeyboardButton(text="Future Simple"), KeyboardButton(text="Future Continiouse")],
                            ],
                            one_time_keyboard=True
                        ))

        return
    elif text == 'Present Simple':
        bot.sendMessage(chat_id, info_message)
        bot.sendMessage(chat_id, "Now lets practice\nTry to solve some tasks")
        bot.sendMessage(chat_id, 'У нас ничего нет!\nWe ____ nothing')
        state[sid] = 0
        return
    elif state[sid] == 0:
        if 'have' == text.lower():
            bot.sendMessage(chat_id, 'Good job!\n\nКуда они идут?\nWhere ____ they go')
            state[sid] = 1
        else:
            bot.sendMessage(chat_id, 'Wrong!\nPlease try again')
    elif state[sid] == 1:
        if 'do' == text.lower():
            bot.sendMessage(chat_id, 'Great!\n\nЭто не меняет ничего\nIt ____ change nothing')
            state[sid] = 2
        else:
            bot.sendMessage(chat_id, 'Wrong!\nPlease try again')
    elif state[sid] == 2:
        if 'does' == text.lower():
            bot.sendMessage(chat_id, 'Awesome, you end Present Simple topic success!')
            state[sid] = 3
        else:
            bot.sendMessage(chat_id, 'Wrong!\nPlease try again')



MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
