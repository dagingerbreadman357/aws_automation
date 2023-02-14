import boto3


resource = boto3.client('s3')

resource.upload_file(
    Filename="/home/ec2-user/environment/redpython/list-script.py",                    # path to the file that need to be uploaded
    Bucket="kje-bucket021323",                                                         # name of the bucket file will be uploaded to
    Key="list-script.py"                                                               # name of file=key  value=content of file
    )

