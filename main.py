# Пример кода для получения информации по адресу
from get_post_info_by_address import GetPostInfoByAddress
from registration import Registration, Authentication

HomeAddress = input("Введите адрес: ")
PostOfficeIndex, PostOfficeAddress = GetPostInfoByAddress(HomeAddress)

print(f"""Введённый адрес: {HomeAddress}
Индекс: {PostOfficeIndex}
Адрес ОПС: {PostOfficeAddress}""")

print(Registration("./Data/user_data.db", "Andrew", "MichurinDev", "123"))
print(Authentication("./Data/user_data.db", "MichurinDev", "123"))
