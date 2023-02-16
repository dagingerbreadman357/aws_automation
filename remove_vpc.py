import boto3

vpc = boto3.client('ec2')








#response = vpc.delete_vpc(
#    VpcId='string',
#    DryRun=True|False
#)