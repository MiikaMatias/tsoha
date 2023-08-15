from flask import Flask, request
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from components.threads import get_threads

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///postgres"
db = SQLAlchemy(app)
threads=[0,1,2,3,4]

@app.route("/db")
def database():
    result = db.session.execute(text("SELECT content FROM messages"))
    messages = result.fetchall()
    return render_template("index.html", count=len(messages), messages=messages) 

@app.route('/threads/<int:id>')
def get_users(id):
    if id not in threads:
        return "Thread not found", 404
    return "thread" + str(id) + "!!!"

@app.route("/")
def index():
    base_url = request.base_url

    return f"""
<head>
    <title>
        Messageboard
    </title>
</head>
<body>
    <h1>
        <center>
            Messageboard
        </center>
        <h2>
            Threads
        </h2>
            {get_threads(base_url, threads)}
    </h1>
</body>
"""
