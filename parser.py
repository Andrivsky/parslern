# import requests
# from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return (response.text)


def get_data_from_html(html):
    soup = BeautifulSoup(html,'lxml')
    first_ad = soup.find('div',class_='snippet-card__content')
    try:
        title = first_ad.find('span', class_='snippet-card__header-text').text
        print(title)
    except:
        title = '-'
        print(title)
    try:
        price = soup.find('div', class_='snippet-card__info').find('div',class_ = 'price').text
        print(price)
    except:
        price = '-'
        print(price)
    try:
        product_url = soup.find('a', class_='snippet-card__header-link').get('href').strip('//')
        print(product_url)
    except:
        product_url = '-'
        print(product_url)


def result(link,region):
    #print('Укажите ссылку на товар с я.маркета')
    #link = input()
    if link.startswith('https://market.yandex.ru'):
        #print('Выберете регион') #231 - питер 2 - москва
        #region = input(str())
        #https://market.yandex.ru/product--smartfon-samsung-galaxy-a20/415763024/offers?local-offers-first=0
        url =link +'&how=aprice'+'&contentRegion=' + region
        answer = get_data_from_html(get_html(url))
    else:
        answer = 'Ссылка указана не верно'
        #https://market.yandex.ru/product--smartfon-samsung-galaxy-a20/415763024/offers?local-offers-first=0
    return answer
#result('https://market.yandex.ru/product--smartfon-samsung-galaxy-a20/415763024/offers?local-offers-first=0','2')
#if __name__ == '__main__':
#    result(link='https://market.yandex.ru/product--smartfon-samsung-galaxy-a20/415763024/offers?local-offers-first=0',region='2')