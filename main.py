import telepot
# bot = telepot.Bot('438470483:AAHA23OcsaEl_KSjW0DUOkU84crogUS2CO8')
bot = telepot.Bot('380236716:AAHqW3fXH7-5WaJ1x8ma1-JhnN-_8fH0yl8')


from telepot.loop import MessageLoop
import time
state = {}

def handle(msg):
    
    id = msg['from']['id']
    sid = str(id)
    text = msg['text']
    evaled=False
    if text=='/start':
        bot.sendMessage(id, 'Hello. Welcome to acmPyBot. here you will know about basic opertions in python. Lets try with +(plus) for axample 2+3')
        state[sid]=0
        return
    # print(msg['text'], msg['from']['id'])
    try:
        bot.sendMessage(id, 'Hey, here are your results '+str(eval(text)))
        evaled = True
    except:
        bot.sendMessage(id,'you have some errors in expression')
    
    print state
    if evaled:
        if state[sid]==0:
            if '+' in text:
              bot.sendMessage(id,'super. you know + already. also there is a - (minus). try to use it for example 4-1 ')
              state[sid]=1
        if state[sid]==1:
            if '-' in text:
              bot.sendMessage(id,'super. you know - already. you can combine it in any random order, like 42+4-7+8 - 12 +1 ')
              state[sid]=2
        if state[sid]==2:
            if '-' in text and '+' in text:
              bot.sendMessage(id,' you know + and - simultenously. you are awesome')
              state[sid]=3
            
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
