from pymongo import MongoClient



def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://mongodbdatabase:chanuk@john.v1qrb.mongodb.net/"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   return client


####setting up mongodb
dbclient = get_database()
questionstable = dbclient["pastpapers"]["questions"]
paperstable = dbclient["pastpapers"]["papers"]


def search_table(index_name, table, field_name, query, sort, subject, ptype):
    pipeline = [
        {
            '$search': {
                'index': index_name,
                'text': {
                'query': query,
                'path': {
                    'wildcard': "*"
                    }
                },
                'highlight': {
                    'path': field_name
                }   
            }
        },

        {
            '$project': {
                'content': 1,
                'papercode': 1,
                'qno': 1,
                'subject': 1,
                'type': 1,
                'highlights': {
                    '$meta': 'searchHighlights'
                }
            }
        },
        {
            '$sort': {'highlights.score': int(sort)}  # Sort by score in descending order
        }
    ]

    if subject is not None:
        pipeline.insert(1, {'$match': {'subject': subject}})
    if ptype is not None:
        pipeline.insert(1, {'$match': {'type': ptype}})
    result = table.aggregate(pipeline)

    result_list = []
    for doc in result:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
        result_list.append(doc)

    return list(result_list)


def find_paper(index_name, table, papercode, ptype):
    pipeline = [
        {
            '$project': {
                'content': 1,
                'papercode': 1,
                'qno': 1,
                'subject': 1,
                'type': 1,
                'highlights': {
                    '$meta': 'searchHighlights'
                }
            }
        },
        {
            '$sort': {'qno': 1}  # Sort by score in descending order
        }
    ]    

    if papercode is not None:
        pipeline.insert(1, {'$match': {'papercode': papercode}})

    result = table.aggregate(pipeline)
    result_list = []
    for doc in result:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
        result_list.append(doc)

    return list(result_list)






