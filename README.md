# 📧 Serverless Contact Form with AWS Lambda, API Gateway & SES

A serverless backend for a **contact form** that accepts user input from a static website, processes it with **AWS Lambda**, and sends email notifications via **Amazon SES**.  
This project demonstrates how to build and deploy a **serverless API** with email delivery and CORS-enabled communication.

---

## Features
- Static frontend form → API Gateway → Lambda → SES → Email delivery  
- Supports both API Gateway proxy and non-proxy integration  
- Configurable sender/recipient emails via Lambda **environment variables**  
- **CORS enabled** for frontend integration  
- CloudWatch logging for debugging  

---

## Architecture

[ HTML Contact Form ] 
        │
        ▼
[ API Gateway Endpoint ]
        │
        ▼
[ AWS Lambda Function (Python) ]
        │
        ▼
[ Amazon SES → Deliver Email ]

## Project Structure

├── frontend/
│   └── index.html   # Static contact form
    └── assets       # Directory with site images
├── lambda/
│   └── handler.py   # Python Lambda function
└── README.md        # Documentation

## Setup Guide

1. Create an S3 Bucket for Hosting (Optional for Demo)

Create an S3 bucket (e.g. my-portfolio-contact-form)

Enable static website hosting

Upload index.html

2. Create Lambda Function

Runtime: Python 3.12

Paste handler.py code

Add environment variables:

SOURCE_EMAIL → verified email in SES

DEST_EMAIL → recipient email

3. Attach IAM Policy

Give Lambda permission to send emails with SES. Example policy:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ses:SendEmail",
      "Resource": "*"
    }
  ]
}

4. Configure Amazon SES

Verify sender email address

(If still in sandbox) verify the destination email too

If production access → you can send to anyone

5. Create API Gateway

Create a REST API

Method: POST

Integration: Lambda function

Enable CORS

6. Deploy API

Create a deployment stage (e.g., prod)

Copy the invoke URL

7. Update Frontend

Set form’s fetch() to use the API Gateway endpoint:
## It ahould look like this

fetch("https://<api-id>.execute-api.<region>.amazonaws.com/prod/contact", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    message: document.getElementById("message").value,
  }),
})

## Testing

Open frontend form

Fill in details → click submit

Check CloudWatch Logs:

Event data printed

"SES Response" with a MessageId = success

## Live Demo
https://d1zpe4aoogzml8.cloudfront.net/#contact

