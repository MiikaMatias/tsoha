from flask import Flask, request

from components.threads import get_threads

app = Flask(__name__)

threads=[0,1,2,3,4]

@app.route('/threads/<int:id>')
def get_users(id):
    if id not in threads:
        return "Thread not found", 404
    return "thread " + str(id)

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
