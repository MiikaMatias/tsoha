from flask import Flask, Blueprint

app = Flask(__name__)

threads=[0,1,2,3]

@app.route('/threads/<int:id>')
def get_users(id):
    if id not in threads:
        return "Thread not found", 404
    return "thread" + str(id)

@app.route("/")
def index():
    return """
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
        <p>
            <p> 
                one 
            <p>
            <p> 
                two 
            <p>
            <p> 
                three 
            <p>
            <p> 
                four 
            <p>
            <p> 
                five 
            <p>
        </p>
    </h1>
</body>
"""
