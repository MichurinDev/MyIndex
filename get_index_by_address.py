import requests

def GetIndexByAddress(address: str) -> str:
    url = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json"
    response = requests.get(url).json()

    if response:
        index = response["response"]["GeoObjectCollection"]\
            ["featureMember"][0]["GeoObject"]\
            ["metaDataProperty"]["GeocoderMetaData"]\
            ["Address"].get("postal_code", "Индекс по данному адресу не найден")
        return index

    else:
        return "Произошла ошибка! Повторите попытку позже."
