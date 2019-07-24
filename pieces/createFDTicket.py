import requests
import json

api_key = "" #FD API Key here
domain = "" FD Domain
password = "x"

ticketGroupID = 0 #ID of FD Group

headers = { 'Content-Type' : 'application/json' }

ticket = {
    'subject' : 'ticket subject',
    'description' : 'ticket body',
    'email' : 'example@example.com',
    'priority' : 2,
    'status' : 2,
    'group_id': ticketGroupID
}

r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets", auth = (api_key, password), headers = headers, data = json.dumps(ticket))

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
