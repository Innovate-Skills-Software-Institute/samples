from pymongo import  MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://root:password@localhost:27017/')
database = client['mydb']
collection = database['user']

# Create or Insert
new_document = {
    'name' : 'John Doe',
    'age' : 30,
    'email' : 'john.doe@example.com'
}

result = collection.insert_one(new_document)
print(f"Inserted Document Id : {result.inserted_id}")

# Read Operation

# Read All
all_documents = collection.find()

for document in all_documents:
    print(document)

query = { 'name' : 'John Doe'}
result = collection.find_one(query)

if result:
    print(result)
else:
    print("Document not found.")

# Update operation

update_query = { 'name' : 'John Doe' }
update_data = { '$set' : { 'age': 31, 'email':'john.doe.updated@example.com'}}
result = collection.update_one(update_query, update_data)
query = { 'name' : 'John Doe'}
result = collection.find_one(query)

if result:
    print(result)
else:
    print("Document not found.")

# Delete Operation
query = { 'name' : 'John Doe'}
result = collection.find_one(query)

if result:
    print(result)
else:
    print("Document not found.")
delete_qry = {'name' : 'John Doe'}
result = collection.delete_one(delete_qry)
result = collection.find_one(query)

if result:
    print(result)
else:
    print("Document not found.")
