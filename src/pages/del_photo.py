import streamlit as st
import pandas as pd
from database.pgadd import del_from_pg_by_id

df = pd.read_sql(
    """SELECT * FROM "cards_meta" """,
    con="postgresql://postgres:school21@localhost:5555/postgres"
)

df.head()


# Отображение таблицы с пользователями
st.write("Таблица с пользователями:")
st.write(df)

id = st.text_input("Id на удаление")

del_button = st.button("Удалить запись")

rel_button = st.button("Обновить таблицу")

if del_button:
    if del_from_pg_by_id("cards_meta",id):
        st.success(f"Фотография '{id}' успешно сохранена.")


