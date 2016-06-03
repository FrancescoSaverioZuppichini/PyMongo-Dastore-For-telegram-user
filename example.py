from dataStore import DataStore

user1 = {'name' : 'Mario','tg_user_id':1}
user2 = {'name' : 'Mario','tg_user_id':2}

myDataStore = DataStore()
# remove all previous users
myDataStore.dropUsers()
myDataStore.storeUser(user1)
myDataStore.storeUser(user2)
print(myDataStore.getAllUser())

# remove user2
myDataStore.removeUser(user2['tg_user_id'])
print(myDataStore.getUser(user2['tg_user_id'])) #will print None
print(myDataStore.getAllUser())

# remove all users
myDataStore.dropUsers()
print(myDataStore.getAllUser())
