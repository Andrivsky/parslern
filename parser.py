import requests
from bs4 import BeautifulSoup


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
    if link.startswith('https://market.yandex.ru'):
        url =link +'&how=aprice'+'&contentRegion=' + region
        answer = get_data_from_html(get_html(url))
    else:
        answer = 'Ссылка указана не верно'
    return answer
