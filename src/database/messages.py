from sqlalchemy import text

def get_messages(id, db):
    sql = f"""SELECT messages.id, messages.thread_id, messages.owner_id, messages.content, messages.created_at, users.username 
              FROM messages 
              JOIN users ON users.id = messages.owner_id 
              WHERE messages.thread_id = (:id) AND messages.show=TRUE;"""
    result = db.session.execute(text(sql), {'id':id}).fetchall()

    print(result)
    return result