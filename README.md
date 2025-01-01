Hello Equip9 Team,

My name is Rohit Umesh Nair

TASK 1: HTTP Service

Part 1: HTTP Service
Develop an HTTP service in any programming language of your choice. The service should expose the following endpoint: Endpoint: GET http://IP:PORT/list-bucket-content/

# Flask S3 bucket Content service

This is a Python Flask-based HTTP service that interacts with an AWS S3 bucket to list its contents. It provides a RESTful API endpoint to view the files and directories within an S3 bucket.

# Features

List the top-level contents (files and folders) of an S3 bucket.
List the contents of a specific folder within the S3 bucket.
Handles errors gracefully, including invalid paths and missing configurations.

# Technologies Used

Python: A programming language for the server.
Flask: Web framework for building the HTTP API.
Boto3: AWS SDK for Python to interact with the S3 bucket.
dotenv: To manage environment variables securely.

# Prerequisites

Before running this project, ensure you have:
Python 3.7+ installed.
An AWS account with an S3 bucket.
AWS credentials (Access Key ID and Secret Access Key).
The following Python libraries were installed:
flask
boto3
python-dotenv

________________________________________


SECOND TASK: Terraform Deployment

Write a Terraform layout to provision AWS infrastructure and deploy the HTTP service
created in Part 1.

#Terraform Deployment for HTTP Service

This project provides a Terraform-based solution to deploy an HTTP service on AWS. The infrastructure includes the following components:
A Virtual Private Cloud (VPC) for secure networking.
A Public Subnet for hosting the service.
An EC2 instance to run the HTTP service (using Nginx).
Security Groups to control access to the service.
This deployment ensures that the service is accessible over HTTP and can be easily extended for HTTPS support.

# Prerequisites

AWS Account:
Ensure you have an active AWS account with appropriate IAM permissions to create resources (VPC, EC2, Security Groups, etc.).

AWS CLI:
Install and configure the AWS CLI with valid credentials using:

AWS configure
Terraform:
Install Terraform (version 1.0 or later).
Download from Terraform Downloads.
Public Key for SSH:

Ensure you have an SSH key pair available for accessing the EC2 instance if needed.

________________________________________

Video demonstration of the Task

DRIVE LINK:
https://drive.google.com/drive/folders/1DRtsatgd7yvprQuY9HVtj16C-hPwphia?usp=drive_link
________________________________________
