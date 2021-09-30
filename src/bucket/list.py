import json
import boto3
import os

s3Client = boto3.client('s3')
BUCKET = os.environ['BUCKET_NAME']


def handler(event, context):
    try:
        res = s3Client.list_objects(
            Bucket=BUCKET,
            MaxKeys=2
        )
        print(json.dumps(res, default=str))
        response = {
            "message": "List successfully fetched.",
            "response": res
        }
        return {
            "statusCode": 200,
            "body": json.dumps(response, sort_keys=True, default=str)
        }
    except Exception as error:
        print("Error occured while listing object :: ", error)
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Error occured while listing object"})
        }
