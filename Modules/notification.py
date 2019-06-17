<<<<<<< HEAD
from plyer import notification
import praw

information = []
#Reading info.txt
read = open("info.txt", "r")
line = read.readlines()
for info in line:
    information.append(info)
#Storing info into strings
id = information[2].replace('\n', '')
secret = information[3].replace('\n', '')
username = information[0].replace('\n', '')
password = information[1].replace('\n', '')
#Logging in
reddit = praw.Reddit(client_id=id,
                     client_secret=secret,
                     password=password,
                     user_agent='modules bot',
                     username=username)

notification.notify(title="Test", message="test", timeout=10)

for message in reddit.inbox.stream():
    if message.was_comment:
        notification.notify(title="Comment from " + str(message.author), message=str(message.body),timeout=10)
    else:
=======
from plyer import notification
import praw

information = []
#Reading info.txt
read = open("info.txt", "r")
line = read.readlines()
for info in line:
    information.append(info)
#Storing info into strings
id = information[2].replace('\n', '')
secret = information[3].replace('\n', '')
username = information[0].replace('\n', '')
password = information[1].replace('\n', '')
#Logging in
reddit = praw.Reddit(client_id=id,
                     client_secret=secret,
                     password=password,
                     user_agent='modules bot',
                     username=username)

notification.notify(title="Test", message="test", timeout=10)

for message in reddit.inbox.stream():
    if message.was_comment:
        notification.notify(title="Comment from " + str(message.author), message=str(message.body),timeout=10)
    else:
>>>>>>> ba76d6fab1e714dc09e9a2024f05246978ee5f0b
        notification.notify(title="Message from " + str(message.author), message=str(message.subject) + "\n" + "\n" + str(message.body), timeout=10)