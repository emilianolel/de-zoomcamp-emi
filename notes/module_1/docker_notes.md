DOCKER CONTAINERS ZOOMCAMP

docker network create pg-network

docker volume create --name dtc_postgres_volume_local -d local

docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v /workspaces/zoomcamp-2024-emi/dtc_postgres_volume_local:/var/lib/postgresql/data \
-p 5432:5432 \
--network=pg-network \
--name pg-database \
postgres:13

docker run -it \
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
-e PGADMIN_DEFAULT_PASSWORD="root" \
-p 8080:80 \
--network=pg-network \
--name pgadmin \
dpage/pgadmin4

pgcli -h localhost -p 5432 -u root -d ny_taxi


python file_uploader.py \
--user=root \
--password=root \
--host=localhost \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='../landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-02.csv.gz' \
--csv_name='green_tripdata_2019-02.csv'


docker run -it \
--network=pg-network \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='../landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-02.csv.gz' \
--csv_name='green_tripdata_2019-02.csv'


docker run -it \
--network=pg-network \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz' \
--csv_name='green_tripdata_2019-01.csv'


docker-compose up -d

docker-compose down


docker run -it \
--network=pg-network \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv' \
--csv_name='taxi+_zone_lookup.csv'

https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv

python file_uploader.py \
--user=root \
--password=root \
--host=localhost \
--port=5432 \
--db=ny_taxi \
--table=zones \
--csv_path='../landing/' \
--csv_url='https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv' \
--csv_name='taxi+_zone_lookup.csv'


docker run -it \
--network=pg-network \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-03.csv.gz' \
--csv_name='green_tripdata_2019-03.csv'


docker run -it \
--network=pg-network \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz' \
--csv_name='green_tripdata_2019-09.csv'


docker run -it \
--network=pg-network \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz' \
--csv_name='green_tripdata_2019-09.csv'


docker run -it \
--network=pg-network \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz' \
--csv_name='green_tripdata_2019-10.csv'


docker run -it \
--network=docker_sql_pg-network \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-11.csv.gz' \
--csv_name='green_tripdata_2019-11.csv'


docker run -it \
--network=docker_sql_default \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-12.csv.gz' \
--csv_name='green_tripdata_2019-12.csv'


docker run -it \
--network=docker_sql_default \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-05.csv.gz' \
--csv_name='green_tripdata_2019-05.csv'


Execute Ingest File
1. 
docker build -t taxi_ingest:v001 .
2. 
docker compose up -d
3.
docker network ls
3.1
pgcli -h localhost -p 5432 -u root -d ny_taxi
4.
docker run -it \
--network=docker-demo_default \
taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table=green_taxi_trips \
--csv_path='landing/' \
--csv_url='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-02.csv.gz' \
--csv_name='green_tripdata_2019-02.csv'
