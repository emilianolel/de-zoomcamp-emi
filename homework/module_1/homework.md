## Module 1 Homework

## Docker & SQL

In this homework we'll prepare the environment 
and practice with Docker and SQL


## Question 1. Knowing docker tags

Run the command to get information on Docker 

```docker --help```

Now run the command to get help on the "docker build" command:

```docker build --help```

Do the same for "docker run".

Which tag has the following text? - *Automatically remove the container when it exits* 

- `--rm`

![docker run --help output](../../assets/module_1/homework/docker_run_--help.png "docker run --help output")


## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use ```pip list``` ). 

What is version of the package *wheel* ?

``` bash
docker run -it --entrypoint=bash python:3.9
```

- 0.42.0

![wheel version](../../assets/module_1/homework/pip_list.png "wheel version")


# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from September 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)


## Question 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

``` sql
SELECT 
	count(*)
FROM
	green_taxi_trips
WHERE
	date(lpep_pickup_datetime) = '2019-09-18'
AND
	date(lpep_dropoff_datetime) = '2019-09-18';
```

- 15612

![question 3](../../assets/module_1/homework/taxi_trips_2019-09-18.png "taxi trips 2019-09-18")

## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

``` sql
SELECT 
	date(lpep_pickup_datetime)
	, sum(trip_distance)
FROM
	green_taxi_trips
WHERE
	date(lpep_pickup_datetime) between '2019-09-01' and '2019-09-30'
GROUP BY
	date(lpep_pickup_datetime)
ORDER BY
	2 DESC
LIMIT 
	1;
```

- 2019-09-26

![question 4](../../assets/module_1/homework/largest_trip_day_2019-09.png "largest trip in 2019-09")

## Question 5. Three biggest pick up Boroughs

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

``` sql
SELECT
    z."Borough"
    , sum(t.total_amount)
FROM
    green_taxi_trips AS t
JOIN
    zones AS z
ON
    t."PULocationID" = z."LocationID"
WHERE
    date(lpep_pickup_datetime) =  '2019-09-18'
GROUP BY
    z."Borough"
HAVING
	sum(t.total_amount) >= 50000
ORDER BY
    2 DESC
LIMIT
    3;
```
 
- "Brooklyn" "Manhattan" "Queens"

![question 5](../../assets/module_1/homework/biggest_pick_up_boroughs.png "biggest pickup boroughs")

## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

``` sql
SELECT
    pz."Zone" as pickup_zone
    , dz."Zone" as dropoff_zone
    , t.tip_amount
FROM
    green_taxi_trips AS t
JOIN
    zones AS pz
ON
    t."PULocationID" = pz."LocationID"
JOIN
    zones AS dz
ON
    t."DOLocationID" = dz."LocationID"
WHERE
    pz."Zone" = 'Astoria'
ORDER BY
    t.tip_amount DESC
LIMIT
    1;
```

- JFK Airport

![question 6](../../assets/module_1/homework/largest_tip.png "largest tip")


## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
Copy the files from the course repo
[here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.

```
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.demo_dataset will be created
  + resource "google_bigquery_dataset" "demo_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "demo_dataset"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = true
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "US"
      + max_time_travel_hours      = (known after apply)
      + project                    = "terraform-demo-emi"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.demo-bucket will be created
  + resource "google_storage_bucket" "demo-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "terraform-demo-emi-tf-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }
          + condition {
              + age                   = 3
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.demo-bucket: Creating...
google_bigquery_dataset.demo_dataset: Creation complete after 1s [id=projects/terraform-demo-emi/datasets/demo_dataset]
google_storage_bucket.demo-bucket: Creation complete after 1s [id=terraform-demo-emi-tf-bucket]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

![question 7.1](../../assets/module_1/homework/terraform_apply.png "terraform apply")

![question 7.2](../../assets/module_1/homework/created_bucket.png "created bucket")

![question 7.3](../../assets/module_1/homework/created_bq_dataset.png "created bq dataset")


## Submitting the solutions

* Form for submitting: https://courses.datatalks.club/de-zoomcamp-2024/homework/hw01
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 29 January, 23:00 CET
