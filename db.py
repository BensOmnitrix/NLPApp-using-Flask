import json

class Database:

    def insert(self,name,email,password):

        with open('users.json','r') as rf:
            users = json.load(rf)

            if email not in users:
                users[email] = [name,password]
            else:
                return 0

        with open('users.json','w') as wf:
            json.dump(users,wf,indent=4)
            return 1
        
    def search(self,email,password):
        with open('users.json','r') as rf:
            users = json.load(rf)

            if email in users and users[email][1] == password:
                return 1
            else:
                return 0
            
    def db_return_name(self,email):
        with open('users.json','r') as rf:
            users = json.load(rf)

            return users[email][0]