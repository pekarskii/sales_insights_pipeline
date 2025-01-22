import pandas as pd
import psycopg2
from psycopg2 import sql

# Параметры подключения к PostgreSQL
DB_PARAMS = {
    "dbname": "your_database",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
}

# Загрузка данных из CSV
def extract_data(file_path):
    print("Загрузка данных из CSV...")
    data = pd.read_csv(file_path)
    return data

# Очистка и преобразование данных
def transform_data(data):
    print("Очистка данных...")
    # Удаление дубликатов
    data = data.drop_duplicates()
    # Обработка пропущенных значений
    data = data.fillna({"column_name": "default_value"})  # Замените "column_name" и "default_value" на ваши данные
    # Добавление новых столбцов (пример)
    data["processed_date"] = pd.to_datetime("today")
    return data

# Загрузка данных в PostgreSQL
def load_data(data, table_name):
    print("Загрузка данных в PostgreSQL...")
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()

    # Создание таблицы (пример)
    cursor.execute(sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            id SERIAL PRIMARY KEY,
            column1 TEXT,
            column2 NUMERIC,
            processed_date TIMESTAMP
        )
    """).format(sql.Identifier(table_name)))

    # Загрузка данных
    for _, row in data.iterrows():
        cursor.execute(sql.SQL("""
            INSERT INTO {} (column1, column2, processed_date)
            VALUES (%s, %s, %s)
        """).format(sql.Identifier(table_name)), (row['column1'], row['column2'], row['processed_date']))

    conn.commit()
    cursor.close()
    conn.close()

# Основной ETL-процесс
def etl_process(file_path, table_name):
    data = extract_data(file_path)
    transformed_data = transform_data(data)
    load_data(transformed_data, table_name)
    print("ETL-процесс завершен.")

if __name__ == "__main__":
    # Укажите путь к файлу и имя таблицы
    FILE_PATH = "sales_data.csv"  # Замените на реальный путь к файлу
    TABLE_NAME = "sales_data"

    etl_process(FILE_PATH, TABLE_NAME)
