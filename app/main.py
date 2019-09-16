
from elasticsearch import Elasticsearch 

# Connect to the elastic cluster
es=Elasticsearch([{ 'host':'elasticsearch-master', 'port':9200}])

# mappings = {
#     "mappings": {
#         "properties": {
#             "location": {
#                 "type": "geo_shape"
#             }
#         }
#     }
# }

mappings = {
    "properties": {
        "employee": {
             "properties": {
                 "location": {
                     "type": "geo_point"
                 }
             }
         }
    }
}

# mappings = {
#   "mappings": {
#     "properties": {
#       "about": {
#         "type": "text",
#         "fields": {
#           "keyword": {
#             "type": "keyword",
#             "ignore_above": 256
#           }
#         }
#       },
#       "age": {
#         "type": "long"
#       },
#       "first_name": {
#         "type": "text",
#         "fields": {
#           "keyword": {
#             "type": "keyword",
#             "ignore_above": 256
#           }
#         }
#       },
#       "interests": {
#         "type": "text",
#         "fields": {
#           "keyword": {
#             "type": "keyword",
#             "ignore_above": 256
#           }
#         }
#       },
#       "last_name": {
#         "type": "text",
#         "fields": {
#           "keyword": {
#             "type": "keyword",
#             "ignore_above": 256
#           }
#         }
#       },
#       "location": {
#         "type": "geo_shape"
#       },
#       "text": {
#         "type": "text",
#         "fields": {
#           "keyword": {
#             "type": "keyword",
#             "ignore_above": 256
#           }
#         }
#       }
#     }
#   }
# }
es.indices.create(index='megacorp', body=mappings)

e1={
    "first_name":"nitin",
    "last_name":"panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
}
print(e1)

res = es.index(index='megacorp', doc_type='employee', id=1, body=e1)

# Let's insert some more documents
e2={
    "first_name" :  "Jane",
    "last_name" :   "Smith",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
}
e3={
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
}
# res=es.index(index='megacorp',doc_type='employee',id=2,body=e2)
# res=es.index(index='megacorp',doc_type='employee',id=3,body=e3)


e4={
    "first_name" :  "David",
    "last_name" :   "Example",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "reading" ],
    "text": "Geo-point as an object",
    "location": { 
        "lat": 51.9838608,
        "lon": 5.875533
    }
}
res=es.index(index='megacorp',doc_type='employee',id=4,body=e4)

if __name__ == '__main__':
    print("Hello World!")