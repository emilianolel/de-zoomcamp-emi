with 

source as (

    select * from {{ source('staging', 'fhv_trips') }}
),

renamed as (

    select
        dispatching_base_num,
        pickup_datetime,
        dropoff_datetime,
        pulocationid,
        dolocationid,
        sr_flag,
        affiliated_base_number

    from source

)

select * from renamed
where date(pickup_datetime) between "2019-01-01" and "2019-12-31"
