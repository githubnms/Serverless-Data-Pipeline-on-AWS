import boto3, json, uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
customer_table = dynamodb.Table('CustomerRecords')
ingestion_log = dynamodb.Table('IngestionLog')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    records = body['records']
    batch_id = str(uuid.uuid4())

    for r in records:
        customer_table.put_item(Item={
            'record_id': str(uuid.uuid4()),
            'batch_id': batch_id,
            'data': r,
            'status': 'ingested',
            'timestamp': datetime.utcnow().isoformat()
        })

    ingestion_log.put_item(Item={
        'batch_id': batch_id,
        'date': datetime.utcnow().strftime('%Y-%m-%d'),
        'records_received': len(records),
        'timestamp': datetime.utcnow().isoformat()
    })

    return {'statusCode': 200, 'body': json.dumps({'batch_id': batch_id, 'ingested': len(records)})}