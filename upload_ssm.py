from aws_utils.ssm import SSM
from aws_utils.kms import KMS
import argparse
import json

parser = argparse.ArgumentParser(description='Session options for boto3.')
parser.add_argument('-keyid', '-k', type=str, help='KMS key id.')
parser.add_argument('--profile', '--p', type=str, default='default',
                    help='Name of profile in your aws credentails file. Default is "default"')
parser.add_argument('--region', '--r', type=str, default='us-east-1',
                    help='Region you want your ssm credentials uploaded to. Default is us-east-1')
parser.add_argument('-file', '-f', type=str, default='encrypted_file',
                    help='File that contains encrypted secrets.')

args = parser.parse_args()


def main(profile, region, keyid, file):

    file_bytes = open(file, 'rb')
    decrypt = KMS(profile, region, keyid, file_bytes)
    ssm_upload = SSM(profile, region)
    secrets = json.loads(decrypt.decrypt_file())['secrets']

    try:
        for secret in secrets:
            ssm_upload.put_parameter(secret)

        print('Secrets Uploaded.')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main(args.profile, args.region, args.keyid, args.file)
