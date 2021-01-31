from .aws_utils.kms import KMS
import json


def encrypt_data(keyid, file, output, profile, region):

    try:
        file_bytes = open(file, 'rb')
        file_contents = json.loads(file)
        # Making sure they have a secrets array.
        secrets = file_contents['secrets']
        kms = KMS(profile, region, keyid, file_bytes)

    except KeyError:
        print('Not a valid json structure. You must have a secrets array.')
    except Exception as e:
        print(f'Issue with file. {e}')
