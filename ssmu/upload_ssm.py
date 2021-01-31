from .aws_utils.ssm import SSM
from .aws_utils.kms import KMS
from pathlib import Path
import json


def upload(profile, region, keyid, file, stage):

    file_to_upload = Path(file)
    file_bytes = open(file_to_upload, 'rb')
    decrypt = KMS(profile, region, keyid, file_bytes)
    ssm_upload = SSM(profile, region, stage)
    secrets = json.loads(decrypt.decrypt_file())['secrets']

    try:
        for secret in secrets:
            ssm_upload.put_parameter(secret)

        print('Secrets Uploaded.')
    except Exception as e:
        print(e)
