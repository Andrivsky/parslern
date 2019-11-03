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
    except:
        title = '-'
    return title
    try:
        price = soup.find('div', class_='snippet-card__info').find('div',class_ = 'price').text
    except:
        price = '-'
    return price
    try:
        product_url = soup.find('a', class_='snippet-card__header-link').get('href').strip('//')
    except:
        product_url = '-'
    return product_url


def result(link=str,region=str):
    if link.startswith('https://market.yandex.ru'):
        url =link +'&how=aprice'+'&contentRegion=' + region
        answer = str(get_data_from_html(get_html(url)))
    else:
        answer = 'Не правильная ссылка'
    return answer
