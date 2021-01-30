import boto3
from botocore.exceptions import ClientError


ssm = boto3.client('ssm')


def put_parameter(secret):

    try:
        ssm.put_parameter(**secret)
    except ClientError as e:
        raise Exception(e)
