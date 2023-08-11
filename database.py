import mysql.connector 
from mysql.connector import errorcode


def connection():

    try:
        connect = mysql.connector.connect(host='localhost', user='root', password='', database='app_finance')
        print("Conectou")

        cursor = connect.cursor()

        return connect, cursor
    
    except mysql.connector.Error as error:

        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database não existe")
        elif error.errno == errorcode.          ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)

def get_user_id(id_user):

    CONNECTION, CURSOR = connection()

    CURSOR.execute(f"SELECT * FROM user WHERE id_user = {id_user}")
    return_user = CURSOR.fetchall()

    dict_users = {}
    list_users = []
    for users in return_user:
        dict_users = {
            "id_user": users[0],
            "name": users[1],
            "password": users[2]
        }
        list_users.append(dict_users)
    
    CURSOR.close()
    CONNECTION.close()
    return list_users


def get_account_id(id_account):

    CONNECTION, CURSOR = connection()

    CURSOR.execute(f"SELECT * FROM bank_account WHERE id_account = {id_account}")
    return_account = CURSOR.fetchall()

    dict_accounts = {}
    list_acounts = []

    for account in return_account:
        dict_accounts = {
            "id_account": account[0],
            "type_account": account[1],
            "bank_account": account[2],
            "id_user": account[3]
        }
        list_acounts.append(dict_accounts)
    
    CURSOR.close()
    CONNECTION.close()
    return list_acounts

def list_users():

    CONNECTION, CURSOR = connection()

    CURSOR.execute(f"SELECT * FROM user")
    return_user = CURSOR.fetchall()

    dict_users = {}
    list_users = []
    for users in return_user:
        dict_users = {
            "id_user": users[0],
            "name": users[1],
            "password": users[2]
        }
        list_users.append(dict_users)
    
    CURSOR.close()
    CONNECTION.close()
    return list_users

def list_account():

    CONNECTION, CURSOR = connection()

    CURSOR.execute(f"SELECT * FROM bank_account")
    return_accounts = CURSOR.fetchall()

    dict_accounts = {}
    list_acounts = []

    for account in return_accounts:
        dict_accounts = {
            "id_account": account[0],
            "type_account": account[1],
            "bank_account": account[2],
            "id_user": account[3]
        }
        list_acounts.append(dict_accounts)
    
    CURSOR.close()
    CONNECTION.close()
    return list_acounts