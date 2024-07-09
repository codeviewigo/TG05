import sqlite3

db_name = './database/users.db'


def init_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER UNIQUE,
            name TEXT,
            category1 INTEGER,
            category2 INTEGER,
            category3 INTEGER,
            expenses1 REAL,
            expenses2 REAL,
            expenses3 REAL
        )
    ''')
    conn.commit()
    conn.close()


def get_user(telegram_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE tg_id = ?', (telegram_id,))

    user = cursor.fetchone()
    conn.close()

    if user:
        return user
    else:
        return None


def add_user(telegram_id, full_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (tg_id, name)
        VALUES (?, ?)
    ''', (telegram_id, full_name))
    conn.commit()
    conn.close()


def update_user(telegram_id, category1, expenses1, category2, expenses2, category3, expenses3):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users
        SET category1 = ?, expenses1 = ?, category2 = ?, expenses2 = ?, category3 = ?, expenses3 = ?
        WHERE tg_id = ?
    ''', (category1, expenses1, category2, expenses2, category3, expenses3, telegram_id))
    conn.commit()
    conn.close()


def get_users():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')

    rows = cursor.fetchall()
    conn.close()

    users = []
    for row in rows:
        users.append({
            'id': row[0],
            'tg_id': row[1],
            'category1': row[2],
            'expenses1': row[3],
            'category2': row[4],
            'expenses2': row[5],
            'category3': row[6],
            'expenses3': row[7]
        })

    return users
