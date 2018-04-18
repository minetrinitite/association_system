import pymongo

SERVER = '192.168.99.100' #ip address of mongo instance
PORT = 32768
DB_NAME = 'ehb_base'
DB_COLLECTION = 'ehb_collection'


def db_ehb_insert(name, date_of_issue, date_of_birth, address_of_registration, diagnoses,
                  server, port, db_name, db_collection):
    conn = pymongo.MongoClient(server, port)
    db = conn[db_name]
    coll = db[db_collection]

    doc = {"name": name,
           "date_of_issue": date_of_issue,
           "date_of_birth": date_of_birth,
           "address_of_registration": address_of_registration,
           "diagnoses": [diagnoses]
           }
    coll.save(doc)


def db_ehb_find(name, server, port, db_name, db_collection):
    conn = pymongo.MongoClient(server, port)
    db = conn[db_name]
    coll = db[db_collection]
    for patient in coll.find({"name": name}):
        return patient["diagnoses"]

    print('done')
