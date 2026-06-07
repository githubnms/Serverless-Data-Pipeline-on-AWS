# Serverless-Data-Pipeline-on-AWS

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?style=for-the-badge&logo=amazonaws&logoColor=black)
![Amazon EC2](https://img.shields.io/badge/Amazon_EC2-Compute-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-Serverless-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)
![API Gateway](https://img.shields.io/badge/API_Gateway-REST_API-FF4F00?style=for-the-badge&logo=amazonapigateway&logoColor=white)
![DynamoDB](https://img.shields.io/badge/DynamoDB-NoSQL-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon_S3-Object_Storage-569A31?style=for-the-badge&logo=amazons3&logoColor=white)
![AWS Glue](https://img.shields.io/badge/AWS_Glue-ETL-FF9900?style=for-the-badge&logo=amazonaws&logoColor=black)
![Amazon Athena](https://img.shields.io/badge/Amazon_Athena-SQL_Analytics-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![QuickSight](https://img.shields.io/badge/Amazon_QuickSight-Dashboard-00A1C9?style=for-the-badge&logo=amazonaws&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-02569B?style=for-the-badge)
![ETL](https://img.shields.io/badge/ETL-Pipeline-6A5ACD?style=for-the-badge)
![Serverless](https://img.shields.io/badge/Serverless-Architecture-E7157B?style=for-the-badge)
![SDLC](https://img.shields.io/badge/SDLC-Practices-6A5ACD?style=for-the-badge)

# Overview

- Designed and deployed a serverless data pipeline on AWS using Lambda, API Gateway, DynamoDB, S3, Glue, and Athena to automate end-to-end customer data collection and analytics at scale.

- Engineered a REST-based ingestion layer using Flask and API Gateway routing real-time customer records into DynamoDB with concurrent Lambda triggers, reducing manual processing time by ~60%.

- Built ETL workflows using AWS Glue and Athena to process and query structured datasets, enabling dashboard reporting via QuickSight — reducing report generation from hours to under 5 minutes.

# Tech Stack

### Backend
- Python 3.12
- AWS Lambda
- REST API (API Gateway)

### Database
- Amazon DynamoDB

### Data Storage
- Amazon S3

### ETL & Analytics
- AWS Glue
- Amazon Athena
- SQL

### Cloud & Deployment
- Amazon EC2
- IAM
- Gunicorn
- Nginx

# How to Run

- 1 Clone Repository

git clone <YOUR_GITHUB_URL>

cd aws-serverless-etl-platform

- 2 Create Virtual Environment

python3 -m venv venv

- 3 Activate Environment

source venv/bin/activate

- 4 Install Dependencies

pip install -r flask-app/requirements.txt

- 5 Update API Gateway URL

nano flask-app/app.py

- Replace:
- API_URL=YOUR_API_URL

- 6 Run Flask Application

cd flask-app
python3 app.py

- Application Runs At

http://EC2_PUBLIC_IP:5000

## Future Enhancements

- Add authentication and authorization
- Automate ETL scheduling using EventBridge
- Add real-time analytics dashboard
- Enable monitoring using CloudWatch
- Implement CI/CD deployment pipeline

## Author

Meenakshi Sundaram N <br>
B.Tech Information Technology