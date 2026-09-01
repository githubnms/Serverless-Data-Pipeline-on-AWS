import boto3, json
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
customer_table = dynamodb.Table('CustomerRecords')
BUCKET = 'serverless-pipeline-v1'

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    response = customer_table.scan(
        FilterExpression='#st = :status',
        ExpressionAttributeNames={'#st': 'status'},
        ExpressionAttributeValues={':status': 'processed'}
    )
    items = response['Items']
    date_str = datetime.utcnow().strftime('%Y-%m-%d')
    timestamp = datetime.utcnow().timestamp()

    ndjson_lines = '\n'.join(json.dumps(item, default=decimal_default) for item in items)

    s3.put_object(
        Bucket=BUCKET,
        Key=f'raw-records/{date_str}/export-{timestamp}.json',
        Body=ndjson_lines
    )
    return {'exported': len(items)}