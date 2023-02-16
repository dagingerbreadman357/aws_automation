import boto3

# to create VPC

vpc = boto3.client('ec2')                   # be sure to call "ec2" and not vpc

vpc.create_vpc(CidrBlock='10.1.0.0/16')     # CidrBlock is the only field that is required

print("VPC has been created")               # I added for visual confirmation when return is 0