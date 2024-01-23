import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os


class FileUploader:

    SAMPLE_ROWS = 10
    CHUNK_SIZE = 100000

    def __init__(self, params):

        self.user = params.user
        self.password = params.password
        self.host = params.host
        self.port = params.port
        self.database_name = params.db
        self.table_name = params.table
        self.data_path = params.csv_path
        self.database_url = f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}'
        self.csv_url = params.csv_url if params.csv_url is not None else ''
        self.csv_name = params.csv_name if params.csv_name is not None else ''
        self.engine = create_engine(self.database_url)
        self.data_path_name = self.data_path + self.csv_name


        if params.csv_url is not None:
            self._download_data()
        
        self.df_sample = pd.read_csv(self.data_path_name, nrows=FileUploader.SAMPLE_ROWS)
        self.df_iterator = self._get_dataframe_iterator()

    
    def _download_data(self):
        os.system(f'wget {self.csv_url} -O {self.data_path_name}.gz')
        os.system(f'gunzip {self.data_path_name}')

    
    def show_dataframe_ddl(self):

        print(pd.io.sql.get_schema(self.df_sample, name=self.table_name, con=self.engine))
    

    def show_dataframe_sample(self):

        print(self.df_sample.head())
    

    def _get_dataframe_iterator(self):

        df_iter = pd.read_csv(self.data_path_name, iterator=True, chunksize=FileUploader.CHUNK_SIZE)
        return df_iter
    

    @staticmethod
    def _insert_dataframe_chunk(self, df):

        start_time = time()
        
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

        df.to_sql(name=self.table_name, con=self.engine, if_exists='append')

        end_time = time()

        process_time = end_time - start_time

        print(f'Inserted another Chunk... Took: {process_time}')
    

    def _insert_clean_dataframe_chunk(self, df):

        start_time = time()

        df.to_sql(name=self.table_name, con=self.engine, if_exists='append')

        end_time = time()

        process_time = end_time - start_time

        print(f'Inserted another Chunk... Took: {process_time}')
    

    # Overwrites table if exists
    def create_table(self):

        self.df_sample.head(n=0).to_sql(name=self.table_name, con=self.engine, if_exists='replace')
        print('Table created!')
    

    def insert_df_to_table(self):

        for chunk in self.df_iterator:
            self._insert_dataframe_chunk(self, df=chunk)
    

    def insert_clean_df_to_table(self):
        
        for chunk in self.df_iterator:
            self._insert_clean_dataframe_chunk(df=chunk)


if __name__ == '__main__':

    
    parser = argparse.ArgumentParser(description='Ingest CSV to Postgrace Database.')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', type=int, help='port for postgres')
    parser.add_argument('--db', help='database name')
    parser.add_argument('--table', help='table name')  
    parser.add_argument('--csv_path', help='path of the csv to be ingested.') 
    parser.add_argument('--csv_url', help='url of the file to be downloaded')
    parser.add_argument('--csv_name', help='name of the file to be downloaded')

    args = parser.parse_args()


    upload_file = FileUploader(args)
    
    upload_file.show_dataframe_ddl()

    upload_file.show_dataframe_sample()

    upload_file.create_table()

    upload_file.insert_df_to_table()
