from flask import Flask
from database import get_account_id, get_user_id, list_account, list_users

app = Flask(__name__)

@app.route("/")
def index():

    data = [
        {
        "connection": "ok",
        "routes": {
            "user_routes": {
                "/user/id_user": "get users by id",
                "method": "GET",
                "/list_users": "get all user",
                "method": "GET"
            },
            "accounts_routes": {
                "/accounts/id_account": "get accounts by id",
                "method": "GET",
                "/list_accounts": "get all accounts",
                "method": "GET"
            }
        }
    }
    ]

    return data

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
