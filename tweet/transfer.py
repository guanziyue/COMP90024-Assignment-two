import couchdb
import numpy as np
address = "http://admin:admin@115.146.86.154:5984/"
couch = couchdb.Server(address)
db = couch['truetweet']  # existing
otherdb=couch['tryano']
for id in db:
     a=np.random.rand((1))
     if a>0.9:
        doc=db.get(id)
        print (doc['_id'])
        doc.pop('_rev')
        otherdb.save(doc)
