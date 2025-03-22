"""Config file to read from .env."""

import os

from dotenv import load_dotenv


load_dotenv()


DATABASE_SCHEMA_NAME = os.getenv("DATABASE_SCHEMA_NAME", "app")
DATABASE_URL = f"postgresql://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"

DATABASE_CARDS_META_TABLE_NAME = os.getenv("DATABASE_CARDS_META_TABLE_NAME", "")
DATABASE_CARDS_PHOTO_TABLE_NAME = os.getenv("DATABASE_CARDS_PHOTO_TABLE_NAME", "")
