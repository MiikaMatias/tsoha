import math
import re
from sqlalchemy import text

def calculate_entropy(password):
    character_set = set(password)
    charset_size = len(character_set)
    password_length = len(password)
    
    try:
        entropy = password_length * math.log2(charset_size)
    except ValueError:
        return 0
    return entropy

def email_invalid(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return not re.match(regex, email)

def email_exists(email, db):
    sql = "SELECT email FROM users"
    email_list = db.session.execute(text(sql)).fetchall()
    return email in [email[0] for email in email_list]

def username_exists(username, db):
    sql = "SELECT username FROM users"
    username_list = db.session.execute(text(sql)).fetchall()
    return username in [username[0] for username in username_list]

def get_wrong_string(email, username, password, retype_password, db):
    wrong_string = ""
    if email_invalid(email):
        wrong_string += "invalid_email=True&"
    if email_exists(email, db):
        wrong_string += "email_exists=True&"
    if username_exists(username, db):
        wrong_string += "username_exists=True&"
    if calculate_entropy(password) < 30:
        wrong_string += "weak_pass=True&"
    if len(username) > 45 or len(username) < 2: 
        wrong_string += "invalid_username=True&"
    if password != retype_password: 
        wrong_string += "incorrect_password=True&"
    if len(password) > 95:
        wrong_string += "invalid_pass=True"

    if len(wrong_string) > 1 and wrong_string[-1] == "&":
        wrong_string = wrong_string[:-1]

    return wrong_string
