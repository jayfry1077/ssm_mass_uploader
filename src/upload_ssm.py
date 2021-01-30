import json
from botocore import parsers
from aws_utils.ssm import SSM
import argparse

parser = argparse.ArgumentParser(description='Session options for boto3.')
parser.add_argument('--profile', '--p', type=str, default='default',
                    help='Name of profile in your aws credentails file. Default is "default"')
parser.add_argument('--region', '--r', type=str, default='us-east-1',
                    help='Region you want your ssm credentials uploaded to. Default is us-east-1')

args = parser.parse_args()


def main(profile, region):

    secrets = json.load(open('secrets_to_upload.json', 'r'))
    ssm_upload = SSM(profile, region)

    try:
        for secret in secrets['secrets']:
            ssm_upload.put_parameter(secret)

        print('Secrets Uploaded.')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main(args.profile, args.region)
