import json
import boto3
import uuid

from datetime import datetime

dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("CustomerContacts")
s3=boto3.client("s3")

BUCKET="etl-source-meenakshi"

def lambda_handler(event,context):

 body=json.loads(event["body"])
 uid=str(uuid.uuid4())
 item={
  "id":uid,
  "customer_id":body["id"],
  "name":body["name"],
  "email":body["email"],
  "phone":body["phone"],
  "address":body["address"],
  "country":body["country"],
  "city":body["city"],
  "zipcode":body["zipcode"],
  "message":body["message"],
  "created_at":
 
 str(datetime.now())
 }

 table.put_item(Item=item)
 s3.put_object(Bucket=BUCKET,
               Key=f"customer/{uid}.json",
               Body=json.dumps(item)
               )
 return{
  "statusCode":200
  }