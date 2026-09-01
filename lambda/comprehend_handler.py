import boto3
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

dynamodb = boto3.resource('dynamodb')
customer_table = dynamodb.Table('CustomerRecords')
processing_log = dynamodb.Table('ProcessingLog')

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_label(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        return 'POSITIVE'
    elif compound <= -0.05:
        return 'NEGATIVE'
    else:
        return 'NEUTRAL'

def lambda_handler(event, context):
    batch_counts = {}

    for record in event['Records']:
        if record['eventName'] != 'INSERT':
            continue

        new_image = record['dynamodb']['NewImage']
        record_id = new_image['record_id']['S']
        batch_id = new_image['batch_id']['S']
        text = new_image['data']['S']

        try:
            sentiment = get_sentiment_label(text)

            customer_table.update_item(
                Key={'record_id': record_id},
                UpdateExpression='SET sentiment = :s, #st = :status',
                ExpressionAttributeNames={'#st': 'status'},
                ExpressionAttributeValues={':s': sentiment, ':status': 'processed'}
            )

            batch_counts.setdefault(batch_id, {'processed': 0, 'failed': 0})
            batch_counts[batch_id]['processed'] += 1

        except Exception as e:
            print(f"Error processing record {record_id}: {e}")
            batch_counts.setdefault(batch_id, {'processed': 0, 'failed': 0})
            batch_counts[batch_id]['failed'] += 1

    for batch_id, counts in batch_counts.items():
        processing_log.put_item(Item={
            'batch_id': batch_id,
            'date': datetime.utcnow().strftime('%Y-%m-%d'),
            'records_processed': counts['processed'],
            'records_failed': counts['failed'],
            'timestamp': datetime.utcnow().isoformat()
        })

    return {'statusCode': 200}