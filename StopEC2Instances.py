#Creating and running a ECS instance though python boto 3

import boto3

client = boto3.client('ec2')

response = client.run_instances(
    ImageId='ami-0b5eea76982371e91',
    InstanceType='t2.micro',
    MinCount= 1,
    MaxCount= 1,
    KeyName='Week14KeyPair'
)


for instance in response ['Instances']:
    print("Instance ID created is : {} Instance Type is :{}".format(instance['InstanceId'],instance['InstanceType']))


#Stop Ec2 Instances

import boto3

client = boto3.client('ec2')

response = client.stop_instances(
    InstanceIds=[
        'i-0f34423b2af8875ea',
    ],
)

print(response)
