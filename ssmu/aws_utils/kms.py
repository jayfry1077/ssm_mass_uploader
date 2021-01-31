import boto3
from botocore.exceptions import ClientError


class KMS:

    def __init__(self, profile, region, keyid, file):
        self.session = boto3.Session(
            profile_name=profile, region_name=region)
        self.kms = self.session.client('kms')
        self.keyid = keyid
        self.file = file.read()

    def decrypt_file(self):

        try:
            data = self.kms.decrypt(
                CiphertextBlob=self.file,
                KeyId=self.keyid
            )

            return data['Plaintext']

        except ClientError as e:
            raise Exception(e)

    def encrypt_file(self):

        try:
            response = self.kms.encrypt(
                KeyId=self.keyid,
                Plaintext=self.file,
            )

            return response['CiphertextBlob']

        except ClientError as e:
            raise Exception(e)
