import pymysql
import json

"""
Util function to create db connection
"""
def get_connection():
    db = pymysql.connect(host = "localhost",
                        user= "root",
                        password="",
                        db = "hackMojoB" )
    if(db):
        print("Successfully connected to DB",db)
        return db
    else:
        raise("FATAL ! Couldnot connect to database")


"""
Method to get video names from db
"""
def get_movie_names():
    mysql = get_connection()
    cur = mysql.cursor(pymysql.cursors.DictCursor)
    cur.execute("Select * from Video")
    result = cur.fetchall()
    return json.dumps(result)


"""
Get set of videos based on pack_id
"""
def get_videos(pack_id):
    mysql = get_connection()
    cur = mysql.cursor(pymysql.cursors.DictCursor)
    print("----------",pack_id)
    cur.execute("select pack.title,pack.pack_id,video.price_day from pack, pack_content, video where pack.pack_id = pack_content.pack_id and pack_content.video_id = video.video_id and pack.pack_id = %s",pack_id)    
    result = cur.fetchall()
    return json.dumps(result)

"""
Method to get video packs
"""
def get_video_packs():
    mysql = get_connection()
    cur = mysql.cursor(pymysql.cursors.DictCursor)
    #cur.execute("select pack.title,pack.pack_id from pack, pack_content, video where pack.pack_id = pack_content.pack_id and pack_content.video_id = video.video_id ")
    cur.execute("select pack.pack_id,title from  pack_content natural join pack group by pack.pack_id,title")
    result = cur.fetchall()
    return json.dumps(result)