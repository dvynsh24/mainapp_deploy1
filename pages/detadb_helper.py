from deta import Deta
import streamlit as st

class DBManager:
    # NOTE: while in development, keep this, remove during production
    # DETA_KEY = "d0p9hi6xfzc_jpQJtoURZCgCdGAANpjiQrE8hq2dhBsC"

    def __init__(self, database_name) -> None:
        # NOTE: while in development, keep this, remove during production
        # self.deta = Deta(DBManager.DETA_KEY)
        
        self.deta = Deta(st.secrets["DETA_KEY"])
        # self.deta = Deta(st.secrets["DETA_KEY"])  # NOTE: this will be done when deploying this to cloud
        # NOTE: also create .streamlit folder, place secrets.toml file with the DETA_KEY in it
        # rest will remain the same
        self.db = self.deta.Base(database_name)

    def insert_user(self, username, name, age, gender, email, password):
        return self.db.put(
            {
                "key": username,
                "name": name,
                "age": age,
                "gender": gender,
                "email": email,
                "password": password,
            }
        )

    def get_all_users(self):
        result = self.db.fetch()
        return result.items  # result.count, result.last too

    def get_by_username(self, username):
        return self.db.get(username)

    def update_user(self, username, updates):
        return self.db.update(updates, username)

    def delete_user(self, username):
        return self.db.delete(username)


# test1 = DBManager("anothertest_db")

# test1.insert_user("u2", "new", "alsjdflkasjdflkjaslkd")

# print(test1.get_users())
# print(test1.get_by_username("u1"))
# print(test1.get_by_username("u1")['email'])

# test1.delete_user("u2")
# test1.update_user("u1", updates={"email": "newemail1"})
