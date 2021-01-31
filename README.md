# ssm_mass_uploader

Command line tool that will encrypt ssm secrets locally via AWS KMS and uploads encrypted data to ssm.

## How to use

1. You create a secrets file on your local machine. Example.

```json
{
  "secrets": [
    {
      "Name": "/super/secret/parameter",
      "Value": "42",
      "Type": "SecureString",
      "Overwrite": true
    }
  ]
}
```

For parameter options see [boto 3 put parameter docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.put_parameter)

1. Encrypting the file locally

python -m ssmu -e -k {kms_id} -f path/to/file/{unencrypted_file.json} -s {stage} --o path/to/save

will output a file named secret.{stage}

1. Upload the encrypted file to ssm

python -m ssmu -u -k {kms_id} -f path/to/file/secret.stage -s stage

Note: Windows and linux \ vs /

---

## json to put in 'secrets_to_upload'

Note: Tags are not required, but if you do include them, then the key values are required

```json
{
  "Name": "String [REQUIRED]",
  "Description": "String [NOT REQUIRED]",
  "Value": "String [REQUIRED]",
  "Type": "String'|'StringList'|'SecureString [REQUIRED]",
  "KeyId": "String [NOT REQUIRED]",
  "Overwrite": "BOOLEAN [NOT REQUIRED]",
  "AllowedPattern": "String [NOT REQUIRED]",
  "Tags": [
    {
      "Key": "String [REQUIRED]",
      "Value": "String [REQUIRED]"
    }
  ],
  "Tier": "'Standard'|'Advanced'|'Intelligent-Tiering' [NOT REQUIRED]",
  "Policies": "String [NOT REQUIRED]",
  "DataType": "String [NOT REQUIRED]"
}
```

---

## Examples

### Basic Examples

```json
{
  "secrets": [
    {
      "Name": "/this/is/super/secret",
      "Value": "shhhh",
      "Type": "String"
    }
  ]
}
```

```json
{
  "secrets": [
    {
      "Name": "/this/is/super/secret",
      "Value": "shhhh",
      "Type": "SecureString"
    }
  ]
}
```

### Example with Tags

```json
{
  "secrets": [
    {
      "Name": "/this/is/super/secret",
      "Value": "shhhh",
      "Type": "String"
    },
    {
      "Name": "/this/is/another/secret",
      "Value": "hmmmm",
      "Type": "SecureString",
      "Tags": [
        {
          "Key": "Project Name",
          "Value": "Project X"
        }
      ]
    }
  ]
}
```

### Example allowing overwrites, secure string, and tags

Note: You cannot used Overwrite and tags in the same call. You should either add tags on first creation, or add / remove tags later on.

```json
{
  "secrets": [
    {
      "Name": "/this/is/super/secret",
      "Value": "new secret",
      "Type": "String",
      "Overwrite": true
    },
    {
      "Name": "/this/is/another/secret",
      "Value": "hmmmm",
      "Type": "SecureString",
      "Tags": [
        {
          "Key": "Project Name",
          "Value": "Project X"
        }
      ]
    }
  ]
}
```
