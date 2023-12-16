use mongodb::{
    bson::{extjson::de::Error, oid::ObjectId, doc},
    results::{InsertOneResult, UpdateResult, DeleteResult},
    sync::{Client, Collection}
};

use crate::models::user_model::User;

pub struct MongoRepo {
    col: Collection<User>
}

impl MongoRepo{
    pub fn init() -> Self {
        let uri = "mongodb://root:password@localhost:27017";
        let client = Client::with_uri_str(uri).unwrap();
        let db = client.database("rustDB");
        let col: Collection<User> = db.collection("User");
        MongoRepo { col }
   }

   pub fn create_user(&self, new_user: User) -> Result<InsertOneResult, Error>{
        let new_doc = User {
            id: None,
            name: new_user.name,
            location: new_user.location,
            title: new_user.title

        };
        let user = self
        .col
        .insert_one(new_doc, None)
        .ok()
        .expect("Error Creating User");
        Ok(user)
   }

   pub fn get_user(&self, id: &str) -> Result<User, Error> {
        let object_id = ObjectId::parse_str(id).unwrap();
        let filter = doc! {"_id" : object_id};
        let user_detail = self.col
        .find_one(filter,None).ok().expect("Error getting user info");
        Ok(user_detail.unwrap())
   }

   pub fn update_user(&self, id:&str, new_user: User) -> Result<UpdateResult, Error>{
    let object_id = ObjectId::parse_str(id).unwrap();
    let filter = doc! {"_id" : object_id};
    let new_doc = doc !{
        "$set": {
            "id" : new_user.id,
            "name" : new_user.name,
            "location" : new_user.location,
            "title" : new_user.title
        }
    };
    let update_doc = self.col
    .update_one(filter, new_doc, None)
    .ok()
    .expect("Error updating user");
    Ok(update_doc)
   }

   pub fn delete_user(&self, id:&str) -> Result<DeleteResult, Error>{
        let obj_id = ObjectId::parse_str(id).unwrap();
        let filter = doc! {"_id": obj_id};
        let user_detail = self.col
        .delete_one(filter, None)
        .ok()
        .expect("Error deleting user");
    Ok(user_detail)
   }
}