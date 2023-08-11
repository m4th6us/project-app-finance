from flask import Flask
from database import get_account_id, get_user_id, list_account, list_users

app = Flask(__name__)

@app.route("/user/<int:id_user>")
def get_users(id_user):

    data = get_user_id(id_user)
    return {"connection": "ok", "data": data}

@app.route("/accounts/<int:id_account>")
def get_accounts(id_account):

    data = get_account_id(id_account)
    print(data)
    return {"connection": "ok", "data": data}

@app.route("/list_users")
def get_users_list():  # Renomeada para evitar conflito com a rota

    data = list_users()
    print(data)
    return {"connection": "ok", "data": data}

@app.route("/list_accounts")
def get_account_list():

    data = list_account()
    print(data)
    return {"connection": "ok", "data": data}

app.run()
