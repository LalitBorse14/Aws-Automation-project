#Create s3 bucket 
import boto3

s3 = boto3.client('s3')
bucket_name = 'my-automation-bucket11'
s3.create_bucket(Bucket=bucket_name)
print(f'Bucket {bucket_name} created.')


# Upload file to s3 bucket
import boto3

s3 = boto3.client('s3')
bucket_name = 'my-automation-bucket11'
file_name = 'myfile.txt'

s3.upload_file(file_name, bucket_name, file_name)
print(f'{file_name} uploaded to {bucket_name}')
