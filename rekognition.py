#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
from botocore.exceptions import ClientError

class Rekog:
    def __init__(self):
        self.client = boto3.client('rekognition')

    def detect_text(self, photo, bucket):
        response = self.client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
        obj = boto3.resource('s3').Object(bucket, photo)
        obj.delete()
        return [x['DetectedText'] for x in response['TextDetections']]

    def upload_file(self, file_name, bucket):
        try:
            boto3.client('s3').upload_file(file_name, bucket, file_name)
        except ClientError:
            return False
        return True