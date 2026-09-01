import boto3, json
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
ingestion_log = dynamodb.Table('IngestionLog')
processing_log = dynamodb.Table('ProcessingLog')
BUCKET = 'serverless-pipeline-v1'

def lambda_handler(event, context):
    target_date = datetime.utcnow().strftime('%Y-%m-%d')

    ingested = ingestion_log.scan(
        FilterExpression='#d = :d',
        ExpressionAttributeNames={'#d': 'date'},
        ExpressionAttributeValues={':d': target_date}
    )['Items']

    processed = processing_log.scan(
        FilterExpression='#d = :d',
        ExpressionAttributeNames={'#d': 'date'},
        ExpressionAttributeValues={':d': target_date}
    )['Items']

    total_in = sum(i['records_received'] for i in ingested)
    total_out = sum(p['records_processed'] for p in processed)

    report = {
        'date': target_date,
        'total_ingested': total_in,
        'total_processed': total_out,
        'discrepancy': total_in - total_out,
        'match_rate_percent': round((total_out / total_in) * 100, 2) if total_in else 0
    }

    s3.put_object(
        Bucket=BUCKET,
        Key=f'reconciliation-reports/{target_date}.json',
        Body=json.dumps(report, indent=2)
    )

    return report