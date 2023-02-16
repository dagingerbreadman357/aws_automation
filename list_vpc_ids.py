import boto3

# how to get vpc ID's

vpc = boto3.client('ec2')               # 

response = vpc.describe_vpcs()

vpcs = response['Vpcs']                 # creating Vpcs as the Key for the list

#print(len(vpcs))                       # print number of vpcs

# itertate through VPCS
for vpc in vpcs:
    print(vpc['VpcId'])                 # creating VpcId as the value to the key to differentiate each VPC