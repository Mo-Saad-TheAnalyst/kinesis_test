import datetime
import json
import random
import boto3

STREAM_NAME = "test_tiker_data"


def get_data():
    return {
        'EVENT_TIME': datetime.datetime.now().isoformat(),
        'TICKER': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'PRICE': round(random.random() * 100, 2)}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            DeliveryStreamName=stream_name,
            Record=json.dumps(data)
            )


if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('firehose'))
