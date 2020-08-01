#!/usr/bin/python3
import os
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
dynamoDB = boto3.resource("dynamodb")
table = dynamoDB.Table("ses-notifications")


def lambda_handler(event, context):
    for record in event['Records']:
        handle_notification(record["body"])

def handle_notification(message):

    item = {
        "sender": sender,
        "subject": subject,
        "message_id": message['mail']['messageId'],
        "recipients": recipients,
        "email_tags": email_tags,
        "event_time": message['notificationType'],
        "event_type": event_type
    }

    try:
        table.put_item(Item = item)
    except Exception as e:
        logger.error("Exception! Message: %s" % e)
