# Equip9 Interview Round 1 Assingment Part 1

# Flask S3 bucket Content service

This is a Python Flask-based HTTP service that interacts with an AWS S3 bucket to list its contents. It provides a RESTful API endpoint to view the files and directories within an S3 bucket.

# Features

List the top-level contents (files and folders) of an S3 bucket.
List the contents of a specific folder within the S3 bucket.
Handles errors gracefully, including invalid paths and missing configurations.

# Technologies Used

Python: Programming language for the server.
Flask: Web framework for building the HTTP API.
Boto3: AWS SDK for Python to interact with the S3 bucket.
dotenv: To manage environment variables securely.

# Prerequisites

Before running this project, ensure you have:
Python 3.7+ installed.
An AWS account with an S3 bucket.
AWS credentials (Access Key ID and Secret Access Key).
The following Python libraries installed:
flask
boto3
python-dotenv

# To install the libraries, run 

(Bash)
pip install flask boto3 python-dotenv

# Create an S3 Bucket in AWS

Log in to the AWS Management Console.

Navigate to the S3 service.

Click on Create Bucket.

Provide a unique bucket name (my-s3-bucket).

Select your preferred region.

Click Create Bucket.

# Setting Up an Environment Variables

Create a .env file in the root directory of your project and add the following:

(AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=your_aws_region
BUCKET_NAME=your_bucket_name)

Replace your_aws_access_key_id, your_aws_secret_access_key, your_aws_region, and your_bucket_name with your actual AWS credentials and bucket name.

# Start the Flask Server

(Bash)
python app.py

The server will start on http://127.0.0.1:5000.

# API Endpoints

(Curl / any Browser)
Endpoint: GET /list-bucket-content/<path>

# List Top-Level Bucket Contents

(Curl / any Browser)
GET http://127.0.0.1:5000/list-bucket-content/

# List Contents of a specific Folder:

(Curl / any Browser)
GET http://127.0.0.1:5000/list-bucket-content/dir1/

