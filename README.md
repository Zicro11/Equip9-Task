Hello Team,

My name is Rohit Umesh Nair

Task Details:-

Part 1: HTTP Service
Develop an HTTP service in any programming language of your choice. The service should expose the following endpoint: Endpoint: GET http://IP:PORT/list-bucket-content/
● Functionality:
○ This endpoint returns the content of an S3 bucket for the specified path.
○ If no path is specified, the top-level content of the bucket is returned.
○ The response should be in JSON format.
Part 2: Terraform Deployment
Write a Terraform layout to provision AWS infrastructure and deploy the HTTP service created in Part 1.
● The Terraform code should:
1.	Create and configure the necessary AWS resources.
2.	Deploy the service to AWS (e.g., using EC2, ECS, Lambda, or any other appropriate AWS service).
________________________________________
Here the steps I used to accomplish this Task
steps :
1.	First create AWS account.
2.	Create IAM User and permission or group policies which required for EC2 and S3 Bucket.
3.	After that generate Access key and Secret Access key of this IAM user.
4.	After that download AWS CLI and Terraform extension.
5.	Setup AWS CLI and Terraform.
6.	After that provide AWS Authentication on your local Machine by using CMD.
7.	After environment completly setup moving toward assignment 1st task.
8.	So, open code editor like VScode.
9.	Create one folder for assignment first Part.
10.	In this folder add DATA-FOLDERS which you want to upload in S3 Bucket.
11.	Now create an s3 bucket from the aws console
12.	Now upload the directories and files (objects) to the s3 bucket from the console
 	
 	![image](https://github.com/user-attachments/assets/f3791789-50e1-4db1-b9a9-a2387709f3cf)
 

13.	Now to call and retrieve data form s3 bucket used following steps :
14.	create python file app.py.
15.	befor that install python related packages like (Boto3, flask, jsionify, dotenv)
16.	for this use command ( pip install package-name ).
17.	after that write python code. In this file app.py import all packages like (Boto3, flask, jsionify, dotenv).
18.	after that define and configure S3 bucket details like Bucket-name, Access-key, Secrete-Access-key, region.).
19.	After that write a python function to call GET method which display or return S3 bucket data in jsion format.
20.	After that, At the end of this file define the PORT in which you wan to run your application app.py .
21.	After that run app.py file it provides you api to retrieve data using port .
  ![image](https://github.com/user-attachments/assets/009f5407-3e58-458f-9bf7-1f8cf6196f00)

23.	After that used curl command to get data on terminal. ( curl http://127..0.0.1:5000/list-bucket-content )
    ![image](https://github.com/user-attachments/assets/4d99acf3-c8ab-4f08-a27e-7b571ae65462)

25.	After running this API on browser it will provide you output in json format.
 	 
26.	if you want to explore bucket content again edit this api and run on browser.
 
![image](https://github.com/user-attachments/assets/7a18795d-f361-4c07-a837-fc7b91b6a96f)



S3 Bucket Objects:
 	 ![image](https://github.com/user-attachments/assets/844bef28-656f-4aac-9c62-d95f744392d1)

________________________________________


SECOND TASK 

32.	Now its time to complete 2nd task.
33.	For this task create folder 
34.	In this folder add your terraform files main.tf 
35.	Now first open git bash and generate ssh public key (developer-key) cy using ssh-keygen command.
36.	After that copy developer-key and developer-key.pub and in 2nd-Task folder.
37.	After that for aws configuration use aws configure command in the  
38.	After that create files like ec2_userdata.sh, main.tf, output.tf and variable.tf.
39.	So, in variables.tf file define all variables.
40.	After that in main.tf file create security group in this open 5000 port on both inbound and outbound rule.
41.	After that write a terraform code to create ec2 instance in this provide path of file ec2_userdata.sh for user_data keyword which you was declare in aws_instance.
42.	After that in ec2_userdata.sh file write all linux command and shell script for installing packages in ec2-instance like python3, boto3, flask, etc.
43.	After successfully written terraform and python code . Run the terraform commands to deploy virtual machine.
44.	Terraform command already mentioned in first task copy it.
45.	When successfully deploying VM it gives you public ip address.
Terraform-code 
Main.tf
 ![image](https://github.com/user-attachments/assets/ac8455cd-26c0-4658-89bc-ef02a61f98db)

 	Variables.tf
 ![image](https://github.com/user-attachments/assets/fe31d12e-81c1-4e16-a510-1700e2b3b81c)
	 
 	HTTP-server instance
![image](https://github.com/user-attachments/assets/b38049b5-bb4d-43d2-8b7e-48bddf16710b)

 
46.	After that copy this ip address and paste it with application port number on browser.
47.	After that it will return similar output of first task in jsion format.




Ec2-ip-output
 	 ![image](https://github.com/user-attachments/assets/5e8a7f70-9243-45a8-825a-a1328c235a5d)

________________________________________

Video demonstration of the Task
https://drive.google.com/drive/folders/1DRtsatgd7yvprQuY9HVtj16C-hPwphia?usp=drive_link
The task is completed successfully.
Thanks…..
________________________________________
