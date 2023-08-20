from flask import Flask, request
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from database.threads import get_threads, get_thread_by_id, get_threads_by_username, get_thread_ids
from database.messages import get_messages
from database.users import insert_user, password_compare, get_user_id
from sqlalchemy.sql import text
from tools.validate import get_wrong_string
from tools.tools import get_latests_path
from os import getenv

SECRET_KEY = getenv('SECRET_KEY')
POSTGRES_PASSWORD = getenv('PASSWORD_DOCKER_SQL')
POSTGRES_NAME = getenv('POSTGRES_NAME')
DATABASE_NAME = getenv('DATABASE_NAME')
POSTGRES_HOST_PORT=getenv('POSTGRES_HOST_PORT')
POSTGRES_PORT=getenv('POSTGRES_PORT')
POSTGRES_CONTAINER_NAME=getenv('POSTGRES_CONTAINER_NAME')
#DATABASE_URL = f'postgresql://{POSTGRES_NAME}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_HOST_PORT}/{DATABASE_NAME}'
DATABASE_URL = f"postgresql://{POSTGRES_NAME}:password@localhost:{POSTGRES_PORT}/{POSTGRES_NAME}"

app = Flask(__name__)

app.secret_key = SECRET_KEY

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def landing():
    return render_template('landing.html', threads=get_threads_by_username(session['username'], db))

@app.route('/threads/<int:id>', methods=['GET'])
def get_thread(id):
    threads = [thread[0] for thread in get_thread_ids(db)]
    if id not in threads:
        return "Thread not found", 404
    return render_template("thread.html", thread=get_thread_by_id(id, db), messages=get_messages(id, db))

@app.route("/loginpage", methods=['GET'])
def loginpage():
    args = request.args
    return render_template('login.html', incorrect_pass=args.get('incorrect_pass'))

@app.route("/threads", methods=['GET'])
def index():
    args = request.args
    return render_template("frontpage.html", threads=get_threads(db), incorrect_pass=args.get('incorrect_pass'))

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
    username = request.form["username"]
    password = request.form["password"]
    latest_path = get_latests_path(request.referrer)

    if password_compare(username, password, db):
        session["username"] = username
        return redirect("/threads")
    else:
        if latest_path == '/threads':
            return redirect("/threads?incorrect_pass=True")
        elif latest_path == '/loginpage':
            return redirect("/loginpage?incorrect_pass=True")

@app.route("/logout", methods=['GET'])
def logout():
    del session["username"]
    return redirect("/threads")

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
        insert_user(email,username, password, db)
        return redirect('/loginpage')
    else:
        return redirect(f'/register/menu?{wrong_string}')
    
@app.route("/sendmessage/<int:id>", methods=['POST'])
def send_message(id):
    owner_id = get_user_id(session['username'], db)
    content = request.form['content']
    # migrate to components | rename components
    sql = "INSERT INTO messages (thread_id, owner_id, content, created_at) VALUES (:id, :owner_id, :content, NOW());"
    db.session.execute(text(sql), {"id":id, "owner_id":owner_id, "content":content})
    db.session.commit()
    return redirect(f'/threads/{id}')

@app.route("/createthread", methods=['POST'])
def create_thread():
    owner_id = get_user_id(session['username'], db)
    title = request.form['title']
    content = request.form['content']
    # migrate to components | rename components
    sql = "INSERT INTO threads (owner_id, title, content, created_at) VALUES (:owner_id, :title, :content, NOW());"
    db.session.execute(text(sql), {"owner_id":owner_id, "title": title, "content":content})
    db.session.commit()
    return redirect(f'/threads')

