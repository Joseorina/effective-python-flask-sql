import sqlite3
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
        
    @classmethod
    def find_by_username(cls, username):
        pass
    
    @classmethod
    def find_by_id(cls, _id):
        pass        