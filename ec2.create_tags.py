#Author: ~_~
#Create date: 11/11/2019
#The Script is designed to assign Tags on existing EC2 resources.

import boto3
import sys

ec2=boto3.client('ec2')
instances=ec2.describe_instances(InstanceIds=())

#List referenced in ec2.create_tags:
ids=[]
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        ids.append(instance['InstanceId'])

#Fill in 'Value' where appropriate; syntax after 'Key' is interchangeable,
#Example - 'Name' can be changed to 'Hostname' where appropriate
ec2.create_tags(
    Resources=ids,
    Tags=[
        {
            'Key': 'Name',
            'Value': '<hostname>'
        },
        {
            'Key': 'Owner',
            'Value': '<primarysmtp@domain.com>'
        },
        {
            'Key': 'Env',
            'Value': '<prod|dev|qa|test|psup|sandbox>'
        },
        {
            'Key': 'App',
            'Value': '<AppName>'
        },
        {
            'Key': 'SiteCode',
            'Value': '<SCD>'
        },
    ]
)