#Create Python file and run it 
# Specify your own ami id which you want 

import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-0abcd1234abcd5678',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='MyKeyPair'
)
print(f'Created instance: {instance[0].id}')
