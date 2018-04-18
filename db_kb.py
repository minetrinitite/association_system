import pymongo

SERVER = 'localhost' #ip address of mongo instance
PORT = 32768
DB_NAME = 'knowledge_base'
DB_COLLECTION = 'knowledge_collection'


def db_kb_insert(date, keys, text, comment, association, diagnosis, article, same_words, previous_words, new_words,
                 server, port, db_name, db_collection):
    conn = pymongo.MongoClient(server, port)
    db = conn[db_name]
    coll = db[db_collection]

    doc = {"date": date,
           "keys": keys,
           "text": text,
           "comment": comment,
           "association": association,
           "diagnosis": diagnosis,
           "article": article,
           "same words": same_words,
           "previous words": previous_words,
           "new words": new_words}

    coll.save(doc)


def db_kb_find(server, port, db_name, db_collection):
    conn = pymongo.MongoClient(server, port)
    db = conn[db_name]
    coll = db[db_collection]

    for men in coll.find():
        print(men)
