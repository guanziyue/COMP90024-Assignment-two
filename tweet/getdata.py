import requests
import couchdb
from requests.auth import HTTPDigestAuth
url='http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/geoindex'
para={'include_docs':'true','reduce':'false','skip':'0','limit':'1'}

message=requests.get(url,para,auth=('readonly', 'ween7ighai9gahR6'))
print(message.json())