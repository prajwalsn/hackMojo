#!/usr/bin/python3
from flask import Flask, render_template , flash , redirect , url_for , session ,request, logging
from db import db_utils
import os
import pymysql
from functools import wraps
from passlib.hash import sha256_crypt

template_dir = "/Users/bhargaviv/Desktop/newApp"
app = Flask(__name__,template_folder = template_dir)

mysql = db_utils.get_connection()

@app.route('/',methods=['GET','POST'])
def get_login_page():
    if request.method =="POST":
        #Get Form Fields
        email = request.form['email']
        password_candidate = request.form['password']
        #create a cursor 
        cur = mysql.cursor(pymysql.cursors.DictCursor)

        #Get use by username 
        result = cur.execute("SELECT * FROM USER WHERE email = %s" , [email])
        print(result)
        if result > 0:
            #get stored hash
            data = cur.fetchone()
            password = data['password']
            password = sha256_crypt.encrypt(str(password))
            print("----------",password)
            #Compare the passwords 
            if sha256_crypt.verify(password_candidate,password):
                #Passed
                session['logged_in'] = True
                session['email'] = email

                flash("You are now logged in", 'success')
                return redirect(url_for('index'))
            else:
                error = "Invalid password"
                return render_template('login.html',error=error)
            #Close connection    
            cur.close()
        else:
            error = "Username not found"
            print("-----",error)
            return render_template('login.html',error=error)
    return render_template('login.html')


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash("Unauthorizaed please log in ", 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/index', methods=["GET", "POST"])
@is_logged_in
def index():
    return render_template('index.html')

@app.route('/popup')
def get_popup():
    return render_template('popup.html')

@app.route('/get_movie_names',methods = ["GET"])
def get_movie_names():
    result = db_utils.get_movie_names()
    return result

@app.route('/get_video_pack',methods = ["GET"])
def get_video_pack():
    result = db_utils.get_video_packs()
    return result

@app.route('/get_videos',methods = ["GET"])
def get_videos():
    pack_id = request.args.get('pack_id')
    result = db_utils.get_videos(pack_id)
    return render_template('pack_info.html',result=result)
    #return result

@app.route('/user_history')
@is_logged_in
def user_history():
    user_email = session['email']
    print(user_email)
    cur = mysql.cursor(pymysql.cursors.DictCursor)
    cur1 = mysql.cursor(pymysql.cursors.DictCursor)
    cur.execute('select user_id from user where email = %s',user_email);
    result1 = cur.fetchone()
    print(result1['user_id'])
    cur1.execute('select * from Vd_subscription where user_id = %s',result1['user_id']);
    result = cur1.fetchall()
    print(result)
    cur.close()
    cur1.close()
    return render_template('history.html', result=result)


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('get_login_page'))


@app.route('/subscribe')
def subscribe():
    return "Subscribed"

if __name__ == '__main__':
    app.secret_key='secret123' 
    #print(db_utils.get_movie_names())
    app.run(debug=True)