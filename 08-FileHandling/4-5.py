import re

email = 'email.txt'

with open(email) as file:
    content = file.read()

sender_pattern = 'From:.*<(.+)>'
recipient_pattern = 'To:.*<(.+)>'
subject_pattern = 'Subject: (.+)'
body_pattern = '\n\n(.+)'

sender = re.search(sender_pattern, content)
recipient = re.search(recipient_pattern, content)
subject = re.search(subject_pattern, content)
body = re.search(body_pattern, content, re.DOTALL)  #re.DOTALL for multi-line body capture

sender = sender.group(1).strip()
recipient = recipient.group(1).strip()
subject = subject.group(1).strip()
body = body.group(1).strip()

print(sender)
print(recipient)
print(subject)
print(body)