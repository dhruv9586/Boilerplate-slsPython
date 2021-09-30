import json
import boto3
import os

s3Client = boto3.client('s3')
BUCKET = os.environ['BUCKET_NAME']


def handler(event, context):
    try:
        key = event['key']
        response = s3Client.delete_object(
            Bucket=BUCKET,
            Key=key
        )
        print(response)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "File successfully Deleted."})
        }
    except Exception as error:
        print("Error occured while deleting object :: ", error)
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Error occured while deleting object"})
        }
