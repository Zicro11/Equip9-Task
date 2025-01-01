import os

import boto3
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Load environment variables
load_dotenv()

app = Flask(__name__)

# AWS S3 configuration
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

BUCKET_NAME = os.getenv("BUCKET_NAME")

@app.route("/list-bucket-content/<path:path>", methods=["GET"])
@app.route("/list-bucket-content/", defaults={"path": ""}, methods=["GET"])
def list_bucket_content(path):
    
    """
    Lists the contents of the specified S3 bucket path.
    If no path is specified, it lists the top-level contents of the bucket.
    """
    
    try:
        # Fetch bucket contents
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=path, Delimiter="/")

        # Extract folders and files
        folders = [
            prefix["Prefix"][len(path) :] for prefix in response.get("CommonPrefixes", [])
        ]
        files = [
            content["Key"][len(path) :]
            for content in response.get("Contents", [])
            if content["Key"] != path  # Exclude the folder itself
        ]
        # Return combined list of files and folders
        return jsonify({"content": folders + files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)
