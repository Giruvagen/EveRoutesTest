#request api data using normal requests module rather than esipy
def getID():
  oriname = str(input('Starting system:'))
  destname = str(input('Ending system:'))
  import json
  import requests
  urlI = "https://esi.evetech.net/latest/universe/ids/?datasource=tranquility"
  dataI = json.dumps([oriname,destname])
  I = requests.post(url = urlI, data = dataI)
  if I.status_code != 200:
     print('Status:', response.status_code, 'Problem with the request. Exiting.')
     exit()
  idobj = I.json()
  ids = []
  for on in idobj['systems']:
    ii = [on['id']]
    ids.append(ii)
  print(ids)
  oriid = ids[0][0]
  destid = ids[1][0]
  print(oriid,destid)
  locs = [str(oriid),str(destid)]
  print(locs)
  return locs
def getRoute(locs):
  import requests
  import string
  urlR="https://esi.evetech.net/latest/route/O/D/?datasource=tranquility&flag=shortest"
  urlR = urlR.replace('O', locs[0])
  urlR = urlR.replace('D', locs[1])
  response = requests.get(urlR, verify=True)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
  data = response.json()
  return data
def routeNames():
  import json
  import requests
  route = getRoute(getID())
  print(route)
  dataR = json.dumps(route)
  urlR = "https://esi.evetech.net/latest/universe/names/?datasource=tranquility"
  R = requests.post(url = urlR, data = dataR)
  if R.status_code != 200:
     print('Status:', response.status_code, 'Problem with the request. Exiting.')
     exit()
  routeN = R.json()
  routeO = []
  for ns in routeN:
    na = ns['name']
    routeO.append(na)
  final = ''
  for out in routeO:
    final += out + ' to '
  return final
#not currently used below
def getNames(ori,dest):
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
