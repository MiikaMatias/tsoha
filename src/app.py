from flask import Flask, request, flash, redirect, render_template, session, abort
from flask_sqlalchemy import SQLAlchemy
from database.threads import (
    get_threads_by_category, get_thread_by_id, get_threads_by_username,
    get_thread_ids, insert_thread, delete_thread
)
from database.messages import get_messages, insert_message, delete_message
from database.categories import (
    get_categories, get_category_id, get_description, allowed_categories
)
from database.users import insert_user, password_compare, get_user_id
from database.images import upload_image
from sqlalchemy.sql import text
from tools.validate import get_wrong_string
from os import environ as env
import base64
import logging
from secrets import token_hex

SECRET_KEY = env['SECRET_KEY']
DATABASE_USERNAME = env['DATABASE_USERNAME']
DATABASE_PASSWORD = env['DATABASE_PASSWORD']
DATABASE_PORT = env['DATABASE_PORT']
DATABASE_SERVICE = env['DATABASE_SERVICE_NAME']
DATABASE_NAME = env['DATABASE_NAME']

DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_SERVICE}:{DATABASE_PORT}/{DATABASE_NAME}"

app = Flask(__name__)

app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db = SQLAlchemy(app)


@app.context_processor
def context_processor():
    return dict(categories=get_categories(db))


@app.route('/', methods=['GET'])
def landing():
    try:
        return render_template('landing.html', threads=get_threads_by_username(session['username'], db))
    except KeyError:
        return redirect('/threads/General')


@app.route('/threads/<string:category>/<int:id>', methods=['GET'])
def get_thread(category, id):

    if category not in allowed_categories(db):
        abort(404)

    threads = [thread[0] for thread in get_thread_ids(db)]
    if id not in threads:
        return "Thread not found", 404
    return render_template("thread.html", thread=get_thread_by_id(id, category, db), messages=get_messages(id, db), category=category, id=id)


@app.route("/threads/<string:category>", methods=['GET'])
def index(category):

    if category not in allowed_categories(db):
        abort(404)

    args = request.args
    desc = get_description(category, db)
    user = ''
    if 'username' in session:
        user = session['username']
    threads = list(get_threads_by_category(db, category))

    return render_template("frontpage.html", threads=threads, incorrect_pass=args.get('incorrect_pass'),
                           current_category=category, category_description=desc,
                           current_user=user)


@app.route("/register/menu", methods=['GET'])
def register_menu():
    args = request.args

    return render_template('register.html', incorrect_pass=args.get('incorrect_pass'),
                           weak_pass=args.get('weak_pass'),
                           invalid_username=args.get('invalid_username'),
                           invalid_pass=args.get('invalid_pass'),
                           invalid_email=args.get('invalid_email'),
                           email_exists=args.get('email_exists'),
                           username_exists=args.get('username_exists'))


@app.route("/login", methods=["POST"])
def login():
    try:
        username = request.form["username"]
        password = request.form["password"]
        id = get_user_id(username, db)
        if password_compare(username, password, db):
            session["username"] = username
            session["user_id"] = id
            session["csrf_token"] = token_hex(16)
            return redirect("/threads")
    except TypeError:
        return redirect(f'{request.referrer}?incorrect_pass=True')


@app.route("/logout", methods=['GET'])
def logout():
    del session["username"]
    del session["user_id"]
    del session["csrf_token"]
    return redirect(request.referrer)


@app.route("/nodb", methods=['GET'])
def nodb():
    return "nodb"


@app.route("/register", methods=['POST'])
def register():
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    retype_password = request.form["retype_password"]

    wrong_string = get_wrong_string(email, username, password, retype_password, db)

    if len(wrong_string) == 0:
        id = insert_user(email, username, password, db)
        session["username"] = username
        session["user_id"] = id
        session["csrf_token"] = token_hex(16)
        return redirect(f'/')
    else:
        return redirect(f'/register/menu?{wrong_string}')


@app.route("/sendmessage/<string:category>/<int:id>", methods=['POST'])
def send_message(category, id):

    if category not in allowed_categories(db):
        abort(404)

    try:
        owner_id = session['user_id']
    except KeyError:
        flash('Please sign in to send messages', 'error')
        return redirect(f'/threads/{category}/{id}')

    image_id = 1
    if 'image' in request.files:
        image = request.files['image']
        image_id = upload_image(image, db)
    else:
        abort(403)

    content = request.form.get('content')
    if not content:
        flash('Write content', 'error')
        return redirect(f'/threads/{category}/{id}')

    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

    insert_message(id, owner_id, image_id, content, db)

    return redirect(f'/threads/{category}/{id}')


@app.route("/createthread/<string:category>", methods=['POST'])
def create_thread(category):

    if category not in allowed_categories(db):
        abort(404)

    try:
        owner_id = session['user_id']
    except KeyError:
        flash('Please sign in to make threads', 'error')
    category_id = get_category_id(category, db)

    image_id = 1
    if 'image' in request.files:
        image = request.files['image']
        image_id = upload_image(image, db)
    else:
        abort(403)

    title = ''
    if 'title' in request.form:
        title = request.form['title']
    else:
        flash('write a title', 'error')
        return redirect('/threads')

    content = ''
    if 'content' in request.form:
        content = request.form['content']
    else:
        flash('write content', 'error')
        return redirect('/threads')

    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

    insert_thread(owner_id, title, image_id, content, category_id, db)
    return redirect(f'/threads/{category}')


@app.route('/deletemessage', methods=['POST'])
def delete_message():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    id = request.form['msg_id']
    owner_id = session['user_id']

    delete_message(id, owner_id, db)

    return redirect(request.referrer)


@app.route('/deletethread', methods=['POST'])
def delete_thread():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

    id = request.form['thread_id']
    owner_id = session['user_id']

    delete_thread(id, owner_id, db)

    return redirect(request.referrer)
