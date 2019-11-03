import requests
import misc
import json
from misc import result
import time

token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'

def get_updates():
    url = URL + 'getupdates'
    response = requests.get(url)
    return response.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id':chat_id,
               'text':message_text}
    return message


def send_message(chat_id, text='Wait'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)

def main():
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['text']
    if text == '\pars':
        send_message(chat_id,'Отправьте ссылку')
        time.sleep(5)
        a = get_message()['text']
        print(a)
        time.sleep(5)
        send_message(chat_id, 'Укажите регион')
        time.sleep(5)
        b = get_message()['text']
        print(b)
        time.sleep(5)
        send_message(chat_id,result(link=a,region='2'))
    else:
        send_message(chat_id, 'Чтобы начать работу бота введите команду "\pars"')
    # with open('updates.json','w')as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()


#https://api.telegram.org/bot976945954:AAFifF-U7bqBCkcHnDpuy-hK4I4zuO_2VH0/sendmessage?chat_id=460967713&text=hi
#https://core.telegram.org/bots/api#making-requests
#https://www.youtube.com/watch?v=iMBuy0INnHQ&list=PLlWXhlUMyooaTZA4vxU9ZRZQPCFxUq9VA&index=4 26 min

    # if text == '\pars':
    #     send_message(chat_id, 'Отправь ссыль')
    #     time.sleep(5)
    #     answer = get_message()
    #     text = answer['text']
    #     link = str(text)
    #     send_message(chat_id, 'Какой регион?')
    #     time.sleep(5)
    #     answer = get_message()
    #     text = str(answer['text'])
    #     time.sleep(5)
    #     if text == '2':
    #         time.sleep(5)
    #         send_message(chat_id, misc.result(link=link,region='2'))
    #     # send_message(chat_id,misc.result('2','2'))

