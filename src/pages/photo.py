import streamlit as st
from PIL import Image
import numpy as np
import io
from database.pgadd import add_photos_to_table, add_meta_to_table
from utils.encoder import face_encoder
from utils.hash import get_hash

st.title("Загрузка фотографии")


last_name = st.text_input("Фамилия")
first_name = st.text_input("Имя")
middle_name = st.text_input("Отчество")
group = st.text_input("Должность")


uploaded_file = st.file_uploader("Выберите файл", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    st.image(image, caption='Загруженная фотография', use_column_width=True)

    save_button = st.button("Сохранить фотографию")

    if save_button:
        # filename = uploaded_file.name
        # upload_dir = "uploads"
        # if not os.path.exists(upload_dir):
        #     os.makedirs(upload_dir)
        # image.save(os.path.join(upload_dir, filename))
        # st.success(f"Фотография '{filename}' успешно сохранена.")

        image_np = np.array(image)
        image_bytes = io.BytesIO()
        image.save(image_bytes, format=image.format)
        image_bytes = image_bytes.getvalue()


        card = {
            "last_name" : last_name,
            "first_name" : first_name,
            "middle_name" : middle_name,
            "das": group,
            "embedding": face_encoder(image_np),
            "photo_id": get_hash(last_name+first_name+middle_name)
        }

        add_meta_to_table(card)
        add_photos_to_table(image_bytes, card["photo_id"])

        st.success(f"Фотография '{card}' успешно сохранена.")
