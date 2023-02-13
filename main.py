# Пример кода для получения информации по адресу
from get_post_info_by_address import GetPostInfoByAddress

HomeAddress = input("Введите адрес: ")
PostOfficeIndex, PostOfficeAddress = GetPostInfoByAddress(HomeAddress)

print(f"""Введённый адрес: {HomeAddress}
Индекс: {PostOfficeIndex}
Адрес ОПС: {PostOfficeAddress}""")
