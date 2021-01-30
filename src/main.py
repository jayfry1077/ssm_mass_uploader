import json
import utils.ssm_funcs as ssm


def main():

    secrets = json.load(open('secrets_to_upload.json', 'r'))

    try:
        for secret in secrets['secrets']:
            ssm.put_parameter(secret)

        print('Secrets Uploaded.')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
