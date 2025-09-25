import json
import boto3
import os

ses = boto3.client('ses')

def lambda_handler(event, context):
    print("Event:", event)  # Debug log

    try:
        # If API Gateway proxy integration: event['body'] exists
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            # Direct integration (no proxy), event is already parsed
            body = event

        name = body.get('name')
        email = body.get('email')
        message = body.get('message')

        source_email = os.environ['SOURCE_EMAIL']
        dest_email = os.environ['DEST_EMAIL']
        print(f"Sending from {source_email} to {dest_email}")

        response = ses.send_email(
            Source=source_email,
            Destination={'ToAddresses': [dest_email]},
            Message={
                'Subject': {'Data': f"New Contact from {name}"},
                'Body': {
                    'Text': {'Data': f"Name: {name}\nEmail: {email}\nMessage: {message}"}
                }
            }
        )

        print("SES Response:", response)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'message': 'Message sent successfully'})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
