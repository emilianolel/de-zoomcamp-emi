# Docker Containers Zoomcamp

## Docker Basics

### Create Docker Network and Volume 🌐

```bash
docker network create pg-network

docker volume create --name dtc_postgres_volume_local -d local
```

### Run PostgreSQL Container 🐘

```bash
docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v /workspaces/zoomcamp-2024-emi/dtc_postgres_volume_local:/var/lib/postgresql/data \
-p 5432:5432 \
--network=pg-network \
--name pg-database \
postgres:13
```

### Run pgAdmin Container 🚀

```bash
docker run -it \
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
-e PGADMIN_DEFAULT_PASSWORD="root" \
-p 8080:80 \
--network=pg-network \
--name pgadmin \
dpage/pgadmin4
```

### Connect to PostgreSQL using pgcli 💻

```bash
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

### Run Dockerized Python File Uploader for Green Taxi Trips 🚖

```bash
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
```

## Docker Compose

### Start Docker Compose 🚀

```bash
docker-compose up -d
```

### Stop Docker Compose 🛑

```bash
docker-compose down
```

### Run Dockerized Python File Uploader for Taxi Zone Lookup 🚖🗺️

```bash
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
```

## Execute Ingest File

1. Build Docker Image 🛠️

```bash
docker build -t taxi_ingest:v001 .
```

2. Start Docker Compose 🚀

```bash
docker compose up -d
```

3. Check Docker Network 🌐

```bash
docker network ls
```

3.1 Connect to PostgreSQL using pgcli 💻

```bash
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

4. Run Dockerized Python File Uploader for Green Taxi Trips 🚖

```bash
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
```
