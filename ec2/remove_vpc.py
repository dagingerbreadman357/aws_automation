import boto3

vpc = boto3.client('ec2')


delete = vpc.delete_vpc(
    VpcId='vpc-028a6f09f9646f481'         # "VpcId" is the only mandatory field
)


print('The VPC has been deleted')