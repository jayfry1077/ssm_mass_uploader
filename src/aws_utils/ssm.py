import boto3
from botocore.exceptions import ClientError


class SSM:
    def __init__(self, profile=str, region=str):
        self.profile = profile
        self.region = region
        self.session = boto3.Session(
            profile_name=self.profile, region_name=self.region)
        self.ssm = self.session.client('ssm')

    def put_parameter(self, secret):

        try:
            self.ssm.put_parameter(**secret)
        except ClientError as e:
            raise Exception(e)
