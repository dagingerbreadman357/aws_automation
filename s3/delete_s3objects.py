import boto3

s3 = boto3.client('s3')

# Delete single object
#s3.delete_object(Bucket='kje-bucket021323', Key='list-script.py'
#)

#print("Deletion Complete")


# Delete multiple objects

import os
import glob

# list all objects in this bucket in the objects varialble

objects=s3.list_objects(Bucket='kje-bucket021323') ['Contents']

# iterate through items in objects variable for deletion

for object in objects :
    s3.delete_object(Bucket='kje-bucket021323',
    Key=object['Key'])
    
print("Deletion Complete")

