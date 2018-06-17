#request api data using normal requests module rather than esipy
import requests
url="https://esi.evetech.net/latest/route/30000142/30002187/?datasource=tranquility&flag=shortest"
response = requests.get(url, verify=True)
if response.status_code != 200:
  print('Status:', response.status_code, 'Problem with the request. Exiting.')
  exit()
data = response.json()
print(data)
