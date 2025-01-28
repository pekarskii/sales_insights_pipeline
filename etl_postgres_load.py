# etl_postgres_load.py
import pandas as pd
from sqlalchemy import create_engine, BigInteger, Integer, String, DECIMAL, Date
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('etl.log'), logging.StreamHandler()]
)

def etl_process():
    try:
        # ========== Extract ==========
        logging.info("Starting ETL process")
        df = pd.read_csv('cleaned_sales_data.csv')
        logging.info(f"Loaded {len(df)} initial records")

        # ========== Transform ==========
        # Удаление дубликатов
        initial_count = len(df)
        df.drop_duplicates(inplace=True)
        removed_dupes = initial_count - len(df)
        logging.info(f"Removed {removed_dupes} duplicates")

        # Обработка пропусков
        numeric_cols = ['price', 'quantity']
        na_before = df[numeric_cols].isna().sum().sum()

        for col in numeric_cols:
            df[col].fillna(df[col].mean(), inplace=True)

        na_after = df[numeric_cols].isna().sum().sum()
        logging.info(f"Fixed {na_before - na_after} missing values")

        # Добавление расчетного поля
        df['total_price'] = df['price'] * df['quantity']
        logging.info("Added total_price column")

        # ========== Load ==========
        # Настройка подключения к PostgreSQL
        DB_CONFIG = {
            'user': 'postgres',
            'password': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'db': 'postgres'
        }

        engine = create_engine(
            f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
            f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['db']}"
        )

        # Обновленный словарь dtype
        dtype_dict = {
            'transaction_id': BigInteger,
            'store_id': Integer,
            'product_id': Integer,
            'category': String(50),
            'price': DECIMAL(10, 2),
            'quantity': Integer,
            'sale_date': Date,
            'total_price': DECIMAL(10, 2)
        }

        # Загрузка данных в БД.
        df.to_sql(
            name='sales',
            con=engine,
            if_exists='replace',
            index=False,
            dtype=dtype_dict
        )

        logging.info(f"Successfully loaded {len(df)} records to PostgreSQL")
        return True

    except Exception as e:
        logging.error(f"ETL process failed: {str(e)}")
        return False

if __name__ == "__main__":
    if etl_process():
        print("ETL completed successfully!")
    else:
        print("ETL failed! Check etl.log for details")