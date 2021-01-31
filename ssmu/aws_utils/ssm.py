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
            self.ssm.put_parameter(**self.__add_stage(secret))

        except ClientError as e:
            raise Exception(e)

    def __add_stage(self, secret):
        staged_secret = {}

        # if you can figure out how to do this with dict comprehension let me know :)
        for k, v in secret.items():
            if type(v) == str:
                staged_secret.update({k: v.format(STAGE=self.stage)})
            else:
                staged_secret.update({k: v})

        return staged_secret
