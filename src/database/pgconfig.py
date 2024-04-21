import psycopg2
from database.config import postgres_host, postgres_port, list_of_db
from loguru import logger
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


logger.info('Connecting to Postgres...')
try:
        conn= psycopg2.connect(
        host=postgres_host,
        port=postgres_port,
        database="postgres",
        user="postgres",
        password="school21")

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
except:
        logger.error('No connection to postgres', exc_info=1)
        raise SystemExit


logger.info('Connecting to Postgres...Done')


for bd in list_of_db:
    try:
        logger.info(f'Trying to create table {bd.name}...')

        create_table_query = '''CREATE TABLE {0} ({1});'''.format(bd.name,
                             ", ".join([f"{field} {data_type}" for field, data_type in bd.fields.items()]))
        cursor.execute(create_table_query)
        logger.info(f'Table {bd.name} created')

    except (Exception, Error) as error:
        if type(error) == psycopg2.errors.DuplicateTable:
            logger.warning(f'Table {bd.name} already exists')
        else:
            logger.error(error)