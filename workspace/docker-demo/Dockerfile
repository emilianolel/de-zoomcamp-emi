FROM python:3.9

RUN apt-get install wget gzip

RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app

RUN mkdir /app/landing/

COPY file_uploader.py file_uploader.py

ENTRYPOINT [ "bash", "file_uploader.py" ]
