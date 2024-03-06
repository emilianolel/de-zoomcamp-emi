{{
    config(
        materialized='table'
    )
}}

with fhv_trips as (
    select *
    from {{ ref('stg_fhv_trips') }}
),
dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)
select fhv_trips.dispatching_base_num, 
    fhv_trips.pickup_datetime, 
    fhv_trips.dropoff_datetime,
    fhv_trips.pulocationid, 
    pickup_zone.borough as pickup_borough, 
    pickup_zone.zone as pickup_zone, 
    fhv_trips.dolocationid, 
    dropoff_zone.borough as dropoff_borough, 
    dropoff_zone.zone as dropoff_zone,
    fhv_trips.sr_flag, 
    fhv_trips.affiliated_base_number
from fhv_trips
inner join dim_zones as pickup_zone
on fhv_trips.pulocationid = pickup_zone.locationid
inner join dim_zones as dropoff_zone
on fhv_trips.dolocationid = dropoff_zone.locationid

-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
