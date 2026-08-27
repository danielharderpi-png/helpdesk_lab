import requests
import random
import time

url = "http://192.168.1.165/osticket/api/http.php/tickets.json"
headers = {
    # MAKE SURE TO PASTE YOUR ACTUAL API KEY INSIDE THE QUOTES BELOW
    "X-API-Key": "3382252BADEEDE7A58EC6F264AD1059B" 
}

# The chaotic roster of a standard office
names = ["Bob in Accounting", "Sarah from HR", "Dave in Sales", "New Hire John"]

# Real-world issues users actually submit
issues = [
    ("Locked out again", "data:text/plain,I typed my password wrong 3 times and now it says my account is locked. Help!"),
    ("Blue screen of death", "data:text/plain,My computer just crashed and there is a sad face on the screen."),
    ("Where is my file?", "data:text/plain,I saved a document to my desktop and now it is gone. Did I get hacked?"),
    ("Coffee spill", "data:text/plain,I spilled my dark roast on the keyboard and now the spacebar is sticky.")
]

print("Starting the ticket blaster... brace the database!")

# A standard loop to create 10 random tickets
for i in range(10):
    # Pick a random person and a random issue from the lists above
    random_name = random.choice(names)
    random_issue_subject, random_issue_message = random.choice(issues)

    ticket_data = {
        "name": random_name,
        "email": "helpme@localhost.com",
        "subject": random_issue_subject,
        "message": random_issue_message,
        "ip": "192.168.1.191", 
        "topicId": "1" 
    }

    response = requests.post(url, json=ticket_data, headers=headers)

    if response.status_code == 201:
        print(f"[{i+1}/10] Ticket created for {random_name}: {response.text}")
    else:
        print(f"[{i+1}/10] Failed! Code {response.status_code}")
    
    # This sleep timer prevents you from accidentally DDoS-ing your own server
    time.sleep(2) 

print("Finished blasting!")