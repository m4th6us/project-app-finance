from database import connection

CURSOR = connection()

def get_user_id(id_user):

    CURSOR.execute(f"SELECT * FROM user WHERE id_user = {id_user}")
    return_user = CURSOR.fetchall()
    print(return_user)


get_user_id(1)

