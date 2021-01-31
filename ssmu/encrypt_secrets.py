from .aws_utils.kms import KMS
from pathlib import Path
import json


def encrypt_data(profile, region, keyid, file, stage, output):

    try:
        file_to_encrypt = Path(file)
        where_to_save = Path(output)
        save_full_path = where_to_save / f'secret.{stage}'

        file_bytes = open(file, 'rb')
        file_contents = json.load(open(file_to_encrypt, 'rb'))
        # Making sure they have a secrets array.
        secrets = file_contents['secrets']

        kms = KMS(profile, region, keyid, file_bytes)

        encrypted_data = kms.encrypt_file()

        with open(save_full_path, 'wb') as f:
            f.write(encrypted_data)
            f.close()

    except KeyError:
        print('Not a valid json structure. You must have a secrets array.')
    except Exception as e:
        print(f'Issue with file. {e}')
