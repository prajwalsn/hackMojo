import pymysql
import json

def get_connection():
    db = pymysql.connect(host = "localhost",
                        user= "root",
                        password="",
                        db = "hackMojoB" )
    if(db):
        print("Successfully connected to DB",db)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        if(cursor):
            return cursor
        else:
            print("FATAL ! Cursor creation falied")
    else:
        print("Error")



def get_movie_names():
    cursor = get_connection()
    cursor.execute("Select * from test")
    result = cursor.fetchall()
    return json.dumps(result)