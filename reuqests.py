#request api data using normal requests module rather than esipy
ori = str(input('Starting system:'))
dest = str(input('Ending system:'))
def getroute(ori, dest):
  import requests
  import string
  url="https://esi.evetech.net/latest/route/O/D/?datasource=tranquility&flag=shortest"
  url = url.replace('O', ori)
  url = url.replace('D', dest)
  print(url)
  response = requests.get(url, verify=True)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
  data = response.json()
  print(data)
  return data
getroute(ori, dest)
