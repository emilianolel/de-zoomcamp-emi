``` sql
-- HOMEWORK WEEK 3

-- 840402
select count(*) from dez-workspace-emi.nytaxi.external_green_tripdata;

-- ext: 0B | mat: 6.41 MB
select count(distinct pulocation_id) as dis_ext
from dez-workspace-emi.nytaxi.external_green_tripdata;

select count(distinct pulocation_id) as dis_mat
from dez-workspace-emi.nytaxi.green_tripdata_non_partitoned;

-- fare_amount = 0: 1622
select count(*) from dez-workspace-emi.nytaxi.external_green_tripdata where fare_amount = 0;

-- 2
CREATE OR REPLACE TABLE dez-workspace-emi.nytaxi.green_tripdata_partitoned_clustered_hw
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY pulocation_id AS
SELECT * FROM dez-workspace-emi.nytaxi.external_green_tripdata;

-- mat: 12.82MB | part: 1.12MB
select count(distinct pulocation_id) as dis_mat
from dez-workspace-emi.nytaxi.green_tripdata_non_partitoned
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

select count(distinct pulocation_id) as dis_mat
from dez-workspace-emi.nytaxi.green_tripdata_partitoned_clustered_hw
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

-- 0B. Because it is already stored in the metadata
select count(*) from dez-workspace-emi.nytaxi.green_tripdata_non_partitoned;
```
