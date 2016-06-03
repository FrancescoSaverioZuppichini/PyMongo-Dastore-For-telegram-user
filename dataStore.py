from pymongo import MongoClient
import datetime


class DataStore:
    def __init__(self, url='localhost', port='27017'):
        self.url = url
        self.port = int(port)
        self.client = MongoClient(self.url, self.port)
        self.db = self.client['my-database-name']

    def storeUser(self, user):
        # user need to be a json eg {'name': 'Mario','age': 24}
        # you MUST pass the telegram user_id in a field tg_user_id
        # and it must be unique
        # add the storing date can be usefull
        user['date'] = datetime.datetime.utcnow()
        user_id = self.db.users.insert_one(user)
        # it returns the inserted_user id
        return user_id

    def getUser(self, tg_user_id):
        return self.db.users.find_one({'tg_user_id': tg_user_id})

    def removeUser(self, tg_user_id):
        # return the deleted user
        return self.db.users.remove({'tg_user_id': tg_user_id})

    def getAllUser(self):
        users = []
        for user in self.db.users.find():
            users.append(user)
        # it returns an array with all users
        return users

    def dropUsers(self):
        # this will remove all user from the DB
        self.db.users.drop()



