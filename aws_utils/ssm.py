import boto3
from botocore.exceptions import ClientError


class SSM:
    def __init__(self, profile=str, region=str, stage=str):
        self.session = boto3.Session(
            profile_name=profile, region_name=region)
        self.ssm = self.session.client('ssm')
        self.stage = stage

    def put_parameter(self, secret):

        try:
            secret_with_stage = {k: v.format(
                STAGE=self.stage) for (k, v) in secret.items()}
            self.ssm.put_parameter(**secret_with_stage)

        except ClientError as e:
            raise Exception(e)
