import requests
  
url = "https://{{oktaURL}}/api/v1/logs"

querystring = {"since":"2018-06-01","until ":" 2018-07-01","filter":'eventType eq "user.session.start" and outcome.result eq "SUCCESS"'}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': "SSWS {{OktaAPIKey}}",
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
count_list = []

for elem in data:
    uuid = elem.get('actor').get('id')
    count_list.append(uuid)

unique_count_list = set(count_list)
unique_count = len(unique_count_list)
print(unique_count_list)
print(unique_count)
