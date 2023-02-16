# Пример кода для получения информации по адресу
from Moduls.get_post_info_by_address import GetPostInfoByAddress
from Moduls.registration import Registration, Authentication
from Moduls.address_save_and_delete import SaveAddress, DeleteAddress

PATH_TO_DB = "./Data/user_data.db"

HomeAddress = input("Введите адрес: ")
PostOfficeIndex, PostOfficeAddress = GetPostInfoByAddress(HomeAddress)

print(f"""Введённый адрес: {HomeAddress}
Индекс: {PostOfficeIndex}
Адрес ОПС: {PostOfficeAddress}""")

print(Registration(PATH_TO_DB, "MichurinDev", "123"))
print(Authentication(PATH_TO_DB, "MichurinDev", "123"))

print(SaveAddress(PATH_TO_DB, "MichurinDev", "Название",
                  "Дружбы 3а", "650040"))
print(DeleteAddress(PATH_TO_DB, "MichurinDev", "Название"))
