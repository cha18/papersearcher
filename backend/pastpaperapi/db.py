from pymongo import MongoClient
from dotenv import load_dotenv
import os

def get_database():
 
    load_dotenv()
    CONNECTION_STRING = os.getenv('CONNECTION_STRING')

    # Create a connection using MongoClient.
    client = MongoClient(CONNECTION_STRING)
 
    return client


####setting up mongodb
dbclient = get_database()
# questionstable = dbclient["pastpapers"]["questions"]
paperstable = dbclient["pastpapers"]["papers"]

def search_table(index_name, table, field_name, query, sort, subject_code, ptype):
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
                'year': 1,
                'month': 1,
                'content': {
                    '$filter': {
                        'input': '$content',
                        'as': 'tuple',
                        'cond': {
                            '$regexMatch': {
                                'input': { '$arrayElemAt': ['$$tuple', 1] },  # Access the 2nd element of the tuple
                                'regex': query,
                                'options': 'i'
                            }
                        }
                    }
                },
                'subject_code': 1,
                'paper_code': 1,
                'subject': 1,
                'type': 1,
                'name': 1,
                'highlights': {
                    '$meta': 'searchHighlights'
                }
            }
        },
        {
            '$match': {
                'content': { '$ne': [] }  # Exclude documents with empty content arrays after projection
            }
        },
        {
            '$sort': {'highlights.score': int(sort)}
        }
    ]



    if subject_code is not None:
        pipeline.insert(1, {'$match': {'subject_code': subject_code}})
    if ptype is not None:
        pipeline.insert(1, {'$match': {'type': ptype}})
    result = table.aggregate(pipeline)

    result_list = []
    for doc in result:
        doc['_id'] = str(doc['_id'])
        result_list.append(doc)

    return list(result_list)



def find_paper(index_name, table, subject_code):
    pipeline = [
        {
            '$project': {
                'content': 1,
                'subject_code': 1,
                'subject': 1,
                'year': 1,
                'month': 1,
                'type': 1,
                'highlights': {
                    '$meta': 'searchHighlights'
                }
            }
        },
        {
            '$sort': {'year': 1}  # Sort by score in descending order
        }
    ]    

    if subject_code is not None:
        pipeline.insert(1, {'$match': {'subject_code': subject_code}})

    result = table.aggregate(pipeline)
    result_list = []
    for doc in result:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
        result_list.append(doc)

    return list(result_list)






