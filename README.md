#DataStore 
## Store user with pymongo

###How to use it
Install mongoDB, see https://www.mongodb.com/

Install *pymongo*, go to your shell and type:
```
pip3 install pymongo
```
You can find an example in *example.py*
####Import the file
Store the file in your current directory and in your program write

````
from dataStore import DataStore
````

This will import the *DataStore* class in your code.

####Create a Dastore Object
You need to create an object from the *Datastore* class, just write

````
myDataStore = DataStore()
````
####Store a user

You need to pass a json to the *DataStore.storeUser* method.

```
user1 = {'name' : 'Mario','tg_user_id':1}
myDataStore.storeUser(user1)

```

**Remember** since you need to link your DB to telegram user, you need to store the unique telegram user ID into a field called 'tg_user_id'. Otherwise the class will not work.

####Get a user
You need the unique telegram user id, and then you can call

```
myDataStore.getUser(<a_user_telegram_id>)
```

####Get all users
easy peasy

```
myDataStore.getAllUser()
```
It will return an array of users' json
####Remove a user

```
myDataStore.removeUser(<a_user_telegram_id>)
```

It will return the removed user

####Remove all users

```
myDataStore.dropUsers()
```
