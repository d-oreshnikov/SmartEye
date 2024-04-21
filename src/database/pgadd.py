import psycopg2
from database.config import *
from loguru import logger

def add_meta_to_table(card : dict)->None:
    """
        add meta to bd table with meta

        param:
                card  : dict with meta
        
        return:
                Nan
    """
    try:
        fields = list(card.keys())
        items = list(card.values())
        conn = psycopg2.connect(
            host=postgres_host,
            port=postgres_port,
            database="postgres",
            user="postgres",
            password="school21")

        pg_insert_query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(
            db_info.name,
            ','.join(fields),
            ','.join('%s' for item in items)
        )

        cur = conn.cursor()
        try:
            cur.execute(pg_insert_query, (items))
        except ValueError:
            card['comment'] = ''
        conn.commit()
        cur.close()
        conn.close()
        logger.info(f"meta for added to pg")
    except Exception as e:
        logger.error(f"There is a problem with inserting to pg for card ", exc_info=1)



def add_photos_to_table(photo : str, id_in_file : int)->None:
    
    """
        add photo to bd table with photos

        param:
                photo  : path to photo
                id_in_file : id to make link with meta table
        
        return:
                Nan
    """
    try:
        conn = psycopg2.connect(
            host=postgres_host,
            port=postgres_port,
            database="postgres",
            user="postgres",
            password="school21")

        fields = ['card_id', 'photo']
        pg_insert_query = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(
            db_photo.name,
            ','.join(fields),
            ','.join('%s' for item in fields)
        )

        cur = conn.cursor()


        card = {
                'card_id': id_in_file,
                'photo': photo
        }

        items = list(card.values())
        
        try:
            cur.execute(pg_insert_query, (items))
        except ValueError:
            card['comment'] = ''

        conn.commit()
        cur.close()
        conn.close()
        logger.info(f'photo added')
        
    except Exception as e:
        logger.error(f"There is a problem with inserting photo to pg for card", exc_info=1)


def get_dict_from_database(table_name, key_column, value_column):

    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(
    host=postgres_host,
    port=postgres_port,
    database="postgres",
    user="postgres",
    password="school21")

    # Создаем курсор
    cursor = conn.cursor()

    # Выполняем запрос для выборки данных из таблицы
    cursor.execute(f"SELECT {key_column}, {value_column} FROM {table_name}")

    # Получаем результаты запроса
    results = cursor.fetchall()

    # Закрываем курсор и соединение
    cursor.close()
    conn.close()

    # Создаем словарь
    data = {}

    # Заполняем словарь данными из результатов запроса
    for key, value in results:
        data[key] = value

    # Возвращаем словарь
    return data

def get_card_info(table_name, hash_value):

    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(
    host=postgres_host,
    port=postgres_port,
    database="postgres",
    user="postgres",
    password="school21")

    # Создаем курсор
    cursor = conn.cursor()

    # Выполняем запрос для выборки данных из таблицы
    cursor.execute(f"SELECT last_name, first_name, middle_name FROM {table_name} where photo_id = '{hash_value}'")

    # Получаем результаты запроса
    results = cursor.fetchall()

    # Закрываем курсор и соединение
    cursor.close()
    conn.close()

    # Создаем словарь
    # Заполняем словарь данными из результатов запроса

    # Возвращаем словарь
    return results