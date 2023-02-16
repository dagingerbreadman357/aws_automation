import boto3

s3 = boto3.client('s3')

# Delete single object
response = s3.delete_object(
    Bucket='kje-bucket021323',
    Key='6KwNCresized.png'
)

# Delete multiple objects

for object in s3:
    s3.delete_object(
        Bucket='kje-bucket021323',
        Key=s3['Key']
)