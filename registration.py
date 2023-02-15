import sqlite3
import hashlib


def MD5Hashing(line: str) -> str:
    """Возвращает MD5 хэш строки"""
    return hashlib.md5(line.encode()).hexdigest()


def Registration(db_path: str, login: str, password: str) -> int:
    """Добавление новой строки регданных пользователя
    с проверкой на дубликаты имён пользователя
    0 - регистрация прошла успешно
    1 - пользователь с таким логином уже зарегистрирован"""

    # Подключение к БД
    con = sqlite3.connect(db_path)
    # Создание курсора
    cur = con.cursor()

    try:
        # Добавляем в БД строку с регданными пользователя
        cur.execute(
            f"INSERT INTO user_registration_data VALUES (?, ?)",
            (login, MD5Hashing(password))
            )
        con.commit()
        con.close()

        return 0
    except sqlite3.IntegrityError:
        # Если пользователь с таким логином уже зарегистрирован
        return 1


def Authentication(db_path: str, login: str, password: str) -> int:
    """0 - при успешной авторизации
    1 - неверный пароль
    2 - пользователь с таким логином не зарегистрирован"""

    # Подключение к БД
    con = sqlite3.connect(db_path)
    # Создание курсора
    cur = con.cursor()

    # Пробегаемся по всем строкам
    for loginInDB, passwordInDB in \
            cur.execute(f"SELECT * FROM user_registration_data"):
        # Если совпадает по логину
        if login == loginInDB:
            # Если правильный пароль
            if MD5Hashing(password) == passwordInDB:
                return 0
            # Емли пароль неверный
            else:
                return 1
    # Если такого логина не найдено
    else:
        return 2
