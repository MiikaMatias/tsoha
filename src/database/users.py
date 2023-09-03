from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash

def insert_user(email, username, password, db):
    sql = "INSERT INTO users (username, pass, email, created_at) VALUES (:username, :password, :email, NOW());"
    hashword = generate_password_hash(password)
    db.session.execute(text(sql), {"username":username, "password": hashword, "email":email})
    db.session.commit()

    sql_for_id = "SELECT id FROM users WHERE username=(:username)"
    id = db.session.execute(text(sql_for_id), {"username":username}).fetchone()[0]
    return id

def password_compare(username, password, db):
    sql = 'SELECT pass FROM users WHERE username = (:username)'
    hashword = db.session.execute(text(sql), {'username':username}).fetchone()[0]

    return check_password_hash(hashword, password)

def get_user_id(username, db):
    sql = 'SELECT id FROM users WHERE username = (:username)'
    id = int(db.session.execute(text(sql), {'username':username}).fetchone()[0])
    return id