import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("kje-bucket021323-1")  # no underscores in bucket name
response = bucket.create(
    ACL='private',                                # options 'private'|'public-read'|'public-read-write'|'authenticated-read'
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'         # current region attached to user acct
    },
    
)
    
print(response)