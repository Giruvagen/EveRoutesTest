#request api data using normal requests module rather than esipy
ori = str(input('Starting system:'))
dest = str(input('Ending system:'))
def getroute(ori, dest):
  import requests
  import string
  urlR="https://esi.evetech.net/latest/route/O/D/?datasource=tranquility&flag=shortest"
  urlR = urlR.replace('O', ori)
  urlR = urlR.replace('D', dest)
  print(urlR)
  response = requests.get(urlR, verify=True)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
  data = response.json()
  print(data)
  return data
def getnames(ori,dest):
  import json
  import requests
  urlN = "https://esi.evetech.net/latest/universe/names/?datasource=tranquility"
  dataN = json.dumps([ori,dest])
  N = requests.post(url = urlN, data = dataN)
  if N.status_code != 200:
     print('Status:', response.status_code, 'Problem with the request. Exiting.')
     exit()
  names = N.json()
  name1 = names[0]['name']
  name2 = names[1]['name']
  print('Route from:', name1,'to', name2)
getroute(ori, dest)
getnames(ori, dest)
