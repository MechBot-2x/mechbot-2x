# En src/core/security/aws_secrets.py
   import boto3
   client = boto3.client('secretsmanager')
   response = client.get_secret_value(SecretId='mechbot/prod/db')
