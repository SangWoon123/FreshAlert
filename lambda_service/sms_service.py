# SNS 메시지 전송
import os
import boto3

sns_client=boto3.client('sns',region_name='ap-northeast-1')

def send_sms_message(message):
  sns_client=boto3.client('sns')
  sns_client.publish(
      PhoneNumber=os.environ['PHONE_NUMBER'],
      Message=message
    )

