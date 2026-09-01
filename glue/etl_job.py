import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

SOURCE_PATH = "s3://serverless-pipeline-v1/raw-records/"
TARGET_PATH = "s3://serverless-pipeline-v1/processed-parquet/"

# NOTE: source files are written as JSON Lines (one object per line) by export_handler.py
df = spark.read.json(SOURCE_PATH)

df_clean = df.dropna(subset=["record_id"])

if "sentiment" in df_clean.columns:
    df_clean.write.mode("overwrite").partitionBy("sentiment").parquet(TARGET_PATH)
else:
    df_clean.write.mode("overwrite").parquet(TARGET_PATH)

job.commit()