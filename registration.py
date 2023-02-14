import sqlite3
import hashlib


def MD5Hashing(line: str) -> str:
    """Возвращает MD5 хэш строки"""
    return hashlib.md5(line.encode()).hexdigest()


def Registration(db_path: str, name: str, login: str, password: str) -> int:
    """Добавление новой строки регданных пользователя
    с проверкой на дубликаты имён пользователя
    0 - регистрация прошла успешно
    1 - пользователь с таким логином уже зарегистрирован"""

    # Подключение к БД
    con = sqlite3.connect(db_path)

    # Создание курсора
    cur = con.cursor()

    # Пробегаемся по всем строкам
    for _, loginInDB, _ in \
            cur.execute(f"SELECT * FROM user_registration_data"):
        # Если такая пара сайт-логин внесена
        if loginInDB == MD5Hashing(login):
            # Выдаем ошибку
            con.close()
            return 1
    else:  # А если нет..
        cur.execute(
            f"INSERT INTO user_registration_data VALUES (?, ?, ?)",
            (name, MD5Hashing(login), MD5Hashing(password))
            )  # Вносим :)
        con.commit()
        con.close()

        return 0


def Authentication(db_path: str, login: str, password: str):
    """Имя пользователя - при успешной авторизации
    1 - неверный пароль
    2 - пользователь с таким логином не зарегистрирован"""
    # Подключение к БД
    con = sqlite3.connect(db_path)

    # Создание курсора
    cur = con.cursor()

    # Пробегаемся по всем строкам
    for nameInDB, loginInDB, passwordInDB in \
            cur.execute(f"SELECT * FROM user_registration_data"):
        # Если такая пара сайт-логин внесена
        if MD5Hashing(login) == loginInDB:
            if MD5Hashing(password) == passwordInDB:
                return nameInDB
            else:
                return 1
    else:
        return 2
