import os
import pandas as pd
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s -%(message)s",
    filemode="a"
)

engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5433/inventory_db")

def ingest_db(df, table_name, engine):
    """This function will ingest df into db table"""
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Loaded: {table_name}")

def load_raw_data():
    """Load CSVs as df and ingest into DB"""
    start = time.time()
    
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            df = pd.read_csv('data/' + file)
            logging.info(f'Ingesting {file} into db')
            ingest_db(df, file[:-4], engine)

    end = time.time()
    total_time = (end - start) / 60
    print(total_time)
    logging.info('------------------------Ingestion Complete-----------------------------')
    logging.info(f'Total time taken: {total_time} minutes')


if __name__ == '__main__':
    load_raw_data()
