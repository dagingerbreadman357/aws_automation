import boto3

ec2 = boto3.client('ec2')

# create ec2 instance with minimum required fields

ec2.run_instances(MaxCount=1,
                  MinCount=1,
                  ImageId="ami-0f1a5f5ada0e7da53",                 # us-west-2 ami as of 2/16/23
                  InstanceType="t2.micro",                         # free tier instance size
                  #        KeyName="private-ec2",                  # (optional) name of keypair
                  #        SecurityGroups=["launch-wizard-6"],     # (optional) name of security group
                  #        UserData=boot_apache2_script            # (optional) file to run at boot to update/ install programs
                  )

print("EC2 instance created")
