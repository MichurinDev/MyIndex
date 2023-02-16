import sqlite3


def SaveAddress(
        db_path: str, username: str,
        title: str, address: str, index: str) -> int:
    """Добавляет в БД новую строку с адресов, индексом и описанием
    0 - успешно добавлено
    1 - сохранение с таким названием уже добавлено"""

    # Подключение к БД
    con = sqlite3.connect(db_path)
    # Создание курсора
    cur = con.cursor()

    try:
        # Добавляем в БД строку
        cur.execute(
            f"INSERT INTO address_data VALUES (?, ?, ?, ?)",
            (username, title, address, index)
            )
        con.commit()
        con.close()

        return 0
    except sqlite3.IntegrityError:
        # Если сохранение с таким названием уже добавлено
        return 1


def DeleteAddress(db_path: str, username: str, title: str) -> int:
    """Удаляет сохранение
    0 - успешно удалено"""

    # Подключение к БД
    con = sqlite3.connect(db_path)
    # Создание курсора
    cur = con.cursor()

    cur.execute(f'DELETE FROM address_data WHERE username = "{username}" \
                AND title = "{title}"')
    con.commit()
    con.close()

    return 0
