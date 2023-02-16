import boto3

# how to upload a single file

s3 = boto3.client('s3')

s3.upload_file(
    Filename="/home/ec2-user/environment/redpython/list-script.py",                    # path to the file that need to be uploaded
    Bucket="kje-bucket021323",                                                         # name of the bucket file will be uploaded to
    Key="list-script.py"                                                               # name of file=key  value=content of file
    )

# "upload multiple files"

#import os
#import glob

#s3 = boto3.client('s3')

#cwd = os.getcwd()
#cwd = cwd+'/'

#files = glob.glob(cwd + "*.py")

#for file in files:
#    s3.upload_file(
#    Filename = file,
#    Bucket="kje-bucket021323",
#    Key=file.split("/") [-1]
#    )