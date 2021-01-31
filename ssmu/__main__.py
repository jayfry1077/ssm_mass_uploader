from .upload_ssm import *
from .encrypt_secrets import *
import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()

group.add_argument('-u', '--upload', action='store_true')
group.add_argument('-e', '--encrypt', action='store_true')

parser.add_argument('-keyid', '-k', type=str, help='KMS key id.')
parser.add_argument('--profile', '--p', type=str, default='default',
                    help='Name of profile in your aws credentails file. Default is "default"')
parser.add_argument('--region', '--r', type=str, default='us-east-1',
                    help='Region you want your ssm credentials uploaded to. Default is us-east-1')
parser.add_argument('-file', '-f', type=str, default='secret.sandbox',
                    help='File that contains encrypted secrets.')
parser.add_argument('-stage', '-s', type=str, default='dev',
                    help='Stage')

args = parser.parse_args()

if __name__ == '__main__':

    if args.upload:
        upload(args.profile, args.region,
               args.keyid, args.file, args.stage)

    if args.encrypt:
        # do stuff
        pass
