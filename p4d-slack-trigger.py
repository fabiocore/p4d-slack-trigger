#!/usr/bin/python3

import json
import requests
import sys
import os

POST_URL='<INSERT_YOUR_WEBHOOK_URL>'
CHANNEL='<INSERT_SLACK_CHANNEL>'

args = sys.argv[1:]

if(not len(args)==3):
    print('Missing arguments... exiting.')
    sys.exit()

serverPort = args[0]
changelist = args[1]
user = args[2]

# get all info about the changelist
stream = os.popen(f'p4 -p {serverPort} describe -s {changelist}')
output = stream.read()

# delete data about affected files information from the output
output_list = output.splitlines()
for index,val in enumerate(output_list):
    if val.startswith('Affected files ...'):
        del output_list[index:]
        del output_list[0]
        break

# format data before send to slack
def list_to_string(my_list):
    str1 = ''
    for element in my_list:
        str1 += element + '\n'
    return str1

title = f'{user} commited {changelist}'
message = {'text': title, 'attachments': [{'text': list_to_string(output_list), 'color': '#F98404'}]}

# send data to slack channel
response = requests.post(
    POST_URL, data=json.dumps(message),
    headers={'Content-Type': 'application/json'}
    )

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is: \n%s'
        %(response.status_code, response.text)
    )