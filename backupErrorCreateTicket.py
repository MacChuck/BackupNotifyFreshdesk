import mmap,re
import requests,json

api_key = ""
domain = ""
password = "x"

ticketRequester = 'example@example.com'
ticketSubject = 'TEST - backup has errors'
ticketBody = 'The backup for EXAMPLE has failed or completed with errors. Please see the attached log file.'

ticketGroupID = 0

backupLogHasErr = False

def createTicket():
  multipart_data = {
    'email': (None, ticketRequester),
    'subject': (None, ticketSubject),
    'description': (None, ticketBody),
   'attachments[]': ('backup.txt', open('backup.log', 'rb'), 'text/plain'),
   'status': (None, '2'),
   'priority': (None, '2'),
   'group_id': (None, ticketGroupID)
  }

  r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets", auth = (api_key, password), files = multipart_data)

  if r.status_code == 201:
    print("Ticket created successfully, the response is given below")
    print("Location Header : " + r.headers['Location'])
    print("x-request-id : " + r.headers['x-request-id'])
  else:
    print("Failed to create ticket, errors are displayed below,")
    response = json.loads(r.content)
    print(response)

    print("x-request-id : " + r.headers['x-request-id'])
    print("Status Code : " + str(r.status_code))

with open('backup.log', 'rb', 0) as file, \
     mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    if (re.search(br'(?i)error', s)) or (re.search(br'(?i)notice', s)):
        backupLogHasErr = True

if backupLogHasErr:
  createTicket()
