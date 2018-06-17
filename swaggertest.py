from esipy import App

app = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")

from esipy import EsiClient

client = EsiClient(
    retry_requests=True,  # set to retry on http 5xx error (default False)
    headers={'User-Agent': 'Gc4be9375d12d45288bced3dd57e9aae1'},
    raw_body_only=True,  # default False, set to True to never parse response and only return raw JSON string content.
)

# generate the operation tuple
# the parameters given are the actual parameters the endpoint requires
route_find = app.op['get_route_origin_destination'](
    origin=30002187,
    destination=30000142,
    flag='shortest'
)

raw_response = client.request(route_find, raw_body_only=True)

print(raw_response.raw)


