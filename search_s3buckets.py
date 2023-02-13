import boto3
resource=boto3.resource("s3")
bucket_list = list(resource.buckets.all())     # created variable that contains list of buckets

#len(bucket_list)                              # how many items in the bucket list


#print("This S3 bucket has,", len(bucket_list), "items in this bucket")


for bucket in resource.buckets.all():          # iterate through S3 bucket to identify each bucket by name
    bucket
    
    print(bucket.name)                         # prints only the bucket name in a list
#   print(bucket)                              # prints bucket name per json config