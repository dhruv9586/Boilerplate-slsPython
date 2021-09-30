import json
import boto3
import os

s3Client = boto3.client('s3')
BUCKET = os.environ['BUCKET_NAME']


def handler(event, context):
    try:
        data = open('package.json', 'rb')
        s3Client.put_object(
            Bucket=BUCKET,
            Body=data,
            Key="package.json"
        )

        body = {
            "message": "File uploaded successfully!"
        }

        return {
            "statusCode": 200,
            "body": json.dumps(body)
        }

    except Exception as error:
        print("Error ocured while uploading in s3 :: ", error)
        return {
            "statusCode": 400,
            "body": "{'message' : 'File not uploaded!!'}"
        }
