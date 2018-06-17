#this is test code for accessing the Eve Online Swagger API
from esipy import EsiApp
esi_app = EsiApp()
app = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")

from esipy import EsiClient

client = EsiClient(
    retry_requests=True,  # set to retry on http 5xx error (default False)
    headers={'User-Agent': 'Gc4be9375d12d45288bced3dd57e9aae1'},
    raw_body_only=False,  # default False, set to True to never parse response and only return raw JSON string content.
)

# generate the operation tuple
# the parameters given are the actual parameters the endpoint requires
route_find = app.op['get_route'](
    destination=30000142,
    origin=30002187,
    flag='shortest'
)

# do the request
response = client.request(route_find)

# use it: response.data contains the parsed result of the request.
print(response.data)

# to get the headers objects, you can get the header attribute
print (response.header)
