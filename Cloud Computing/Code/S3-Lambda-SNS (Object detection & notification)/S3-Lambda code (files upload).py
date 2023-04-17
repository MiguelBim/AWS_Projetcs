# ITESO, rights reserved
# Code created for the lambda practice of the Cloud Computing Course
# Mtro. Miguel Ojeda


# Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts.
# In this project it will be used to trigger the mail using Amazon SES service from lambda, loading files into S3
import boto3

# This is our lambda function with two inputs (event & context); event will be trigger, corresponding to a context
def lambda_handler(event, context):

    #Access to the file inserted in the S3 bucket in order to extract the file name
    file_name = event['Records'][0]['s3']['object']['key']
    # Access to the S3 service in order to extract the bucket name from AWS
    bucket_name = event['Records'][0]['s3']['bucket']['name']

    print("Bucket details: ")
    print("Event details : ", event)
    print("File name : ", file_name)
    print("Bucket name : ", bucket_name)

    subject = "Event from " + bucket_name

    # Creation of the client in order to use the SES service
    client = boto3.client("ses")

    # Body of our email
    body =  """
                <br>
                
                Your lambda function has been triggered! This is a notification that you defined in order to inform you about a new file in a S3 Bucket
                
                The file {} was inserted in the {} bucket.
            """.format(file_name, bucket_name)

    # Message to print the subject and the body, source and destination definition
    message = {"Subject":{"Data": subject}, "Body":{"Html": {"Data": body}}}
    source_email = "miguel.ojeda@iteso.mx"
    destination_email = {"ToAddresses":["miguel.ojeda@iteso.mx"]}

    # Source and destination e-mail. For this example the source and destination will be the same
    response = client.send_email(Source = source_email,
                                 Destination = destination_email,
                                 Message = message)

    # Print to lambda
    print("The email to miguel.ojeda@iteso.mx was successfully sent. Lambda Notification")
