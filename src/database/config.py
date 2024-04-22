from collections import namedtuple


# postgres config host and port
postgres_host='localhost'
postgres_port=5555


# Struct for Databaases
Database = namedtuple('Database', ['name', 'fields'])


# names and fields of databases to make them in Postgres

db_info = Database(
    name='cards_meta', 
    fields={ 
            "id" : "SERIAL PRIMARY KEY",
            "last_name"  : "text",
            "first_name" : "text" ,
            "middle_name" : "text" ,
            "das" : "text",
            "embedding" : "DOUBLE PRECISION[]",
            "photo_id" : "text UNIQUE"
    }
)

db_photo = Database(
    name= 'photos',
    fields={
            "id" : "SERIAL PRIMARY KEY",
            "card_id" : "text REFERENCES cards_meta(photo_id)",
            "photo" : "bytea"
    }
)

# list of databases to make them in postgres(pgconfig.py)
list_of_db = [db_info, db_photo]