# Helix Core Python Trigger (p4d-slack-trigger)

A Python trigger to send messages into slack when users commit changes.

## How To Use

- Save the .py file in a directory that perforce user have access
- Set the +x to the file 'chmod +x p4d-slack-trigger.py'
- Install the requeired libraries (json, requests)
- Change the variables values 'POST_URL' and 'CHANNEL'
- Use 'p4 triggers' to configure the trigger like the example below

p4d-slack-trigger change-submit //depot/... "/p4/p4d-slack-trigger.py %serverport% %change% %user%"`
