import requests
from global_vars import *
from bs4 import BeautifulSoup as bs


def GetIndexByAddress(address: str) -> str:
    """Возвращает индекс почтового отделения по адресу"""

    # Формируем запрос
    url = f"http://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}"\
        f"&geocode={address}&format=json"
    response = requests.get(url).json()

    # Если в ответе что-то есть..
    if response:
        # Парсим индекс первого адреса из json
        index = (response["response"]
                 ["GeoObjectCollection"]["featureMember"]
                 [0]["GeoObject"]["metaDataProperty"]
                 ["GeocoderMetaData"]
                 ["Address"].get(
                                "postal_code",
                                "Индекс по данному адресу не найден"))
        return index

    else:
        return "Произошла ошибка! Повторите попытку позже."


def GetPostByIndex(index: str) -> str:
    """Возвращает адрес почтового отделения, к которому относится индекс"""

    # Формируем запрос
    url = f"https://indexphone.ru/post-offices/{index}"
    response = requests.get(url)

    # Если связь с сервером установлена
    if response.status_code == 200:
        soup = bs(response.text, "html.parser")

        # Находим все элементы, опысывающие индекс
        post_address_info = soup.find_all(
                                        'div',
                                        class_='post-offices-item-content')

        # Берём нужную информацию и структурируем её
        return post_address_info[2].text.rstrip(" ").lstrip(" ")
    else:
        return "Произошла ошибка! Повторите попытку позже."


def GetPostInfoByAddress(address: str) -> str:
    """Возвращает кортеж в виде (индекс, адрес почтового отделения)"""

    # Получаем индекс по адресу
    index = GetIndexByAddress(address)
    # Врзвращаем полученный индекс и адрес ОПС по этому индексу
    return (index, GetPostByIndex(index))
