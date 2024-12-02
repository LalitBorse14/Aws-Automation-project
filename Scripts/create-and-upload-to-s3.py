#Create s3 bucket 
import boto3

# Initialize the S3 client
s3 = boto3.client('s3', region_name='ap-south-1')

# Bucket name
bucket_name = 'lalitborse12345'

try:
    # Create the S3 bucket with the correct region
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )
    print(f"Bucket {bucket_name} created successfully!")
except Exception as e:
    print(f"Error: {e}")



# Upload file to s3 bucket
import boto3

s3 = boto3.client('s3')
bucket_name = 'lalitborse12345'
file_name = 'myfile.txt'

s3.upload_file(file_name, bucket_name, file_name)
print(f'{file_name} uploaded to {bucket_name}')
