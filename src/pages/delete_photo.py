import streamlit as st
import pandas as pd
from database.pgadd import del_from_pg_by_id

df = pd.read_sql(
    """SELECT * FROM "cards_meta" """,
    con="postgresql://postgres:school21@localhost:5555/postgres"
)

df.head()
# Определение параметров темы
primary_color = "#FF4B4B"
background_color = "#F5A700"
secondary_background_color = "#D48B09"
text_color = "#1C1C1C"
font = "Serif"

# Применение цветов к элементам интерфейса
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Отображение таблицы с пользователями
st.write("Таблица с пользователями:")
st.write(df)

id = st.text_input("Id на удаление")

col1, col2 = st.columns([10,10])  # Adjust column ratios as needed

with col1:
    del_button = st.button("Удалить запись", )

with col2:
    rel_button = st.button("Обновить таблицу")


if del_button:
    if del_from_pg_by_id("cards_meta",id):
        st.success(f"Фотография '{id}' успешно сохранена.")