import boto3

resource=boto3.client("s3")

#resource.list_buckets()                             # shows config for S3 bucket tied to my account
#print(resource.list_buckets())                      # shows config for S3 bucket tied to my account


resource.list_buckets() ["Buckets"]                  # shows only the "Buckets" portion of the config which contains all name and creation date
#print(resource.list_buckets() ["Buckets"])           # shows only the "Buckets" portion of the config which contains all name and creation date

#creation_date = resource.list_buckets() ["Buckets"] [1] ["CreationDate"]    # hardcoded manually to find bucket in the "1" position of table 
#creation_date.strftime('%d%m%y_%H:%M:%s')

#bucket_name = resource.list_buckets() ["Buckets"] [1] ["Name"]

#print(resource.list_buckets())

#print(resource.list_buckets() ["Buckets"] [1] ["Name"])

#print(resource.list_buckets() ["Buckets"] [1] ["CreationDate"])

for bucket in resource.list_buckets() ["Buckets"]:                            # using for loop to automatically give name and creation date of buckets
    print(bucket ["Name"])
    print(bucket ["CreationDate"])
    