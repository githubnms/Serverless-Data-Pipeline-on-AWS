CREATE DATABASE customer_etl;


CREATE EXTERNAL TABLE customer_contacts( 
    id STRING,
    customer_id STRING,
    name STRING,
    email STRING,
    phone STRING,
    address STRING,
    country STRING,
    city STRING,
    zipcode STRING,
    message STRING,
    created_at STRING
    )
    
    ROW FORMAT SERDE
    'org.openx.data.jsonserde.JsonSerDe'
    
    LOCATION
    's3://etl-source-meenakshi/customer/';