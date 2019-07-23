import requests
import json

api_key = "" #FD API Key
domain = "" #FD Domain
password = "x"

ticketRequester = 'example@example.com'
ticketSubject = 'subject'
ticketBody = 'body'
ticketGroupID = 0

multipart_data = {
  'email': (None, ticketRequester),
  'subject': (None, ticketSubject),
  'description': (None, ticketBody),
  'attachments[]': ('test.txt', open('test.txt', 'rb'), 'text/plain'),
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
