import requests
import misc
import json
from parser import result
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
        send_message(chat_id,result(link=a,region='b'))
    else:
        send_message(chat_id, 'Чтобы начать работу бота введите команду "\pars"')


if __name__ == '__main__':
    main()
