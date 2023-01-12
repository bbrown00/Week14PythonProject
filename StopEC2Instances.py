#Stop Ec2 Instances

import boto3

client = boto3.client('ec2')

response = client.stop_instances(
    InstanceIds=[
        'i-0f34423b2af8875ea',
    ],
)

print(response)