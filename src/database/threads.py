from sqlalchemy import text

def get_thread_answers(thread_id, db):
    sql = f"SELECT id FROM messages WHERE id = (:id);"
    result = db.session.execute(text(sql), {"id":thread_id}).fetchall()
    print(result)
    return len(result)

def get_threads(db):
    sql = """SELECT threads.id, threads.owner_id, threads.title, threads.created_at, threads.content, threads.attached_file, users.username 
             FROM threads 
             JOIN users ON users.id = threads.owner_id;"""
    result = db.session.execute(text(sql)).fetchall()
    return result

def get_thread_ids(db):
    sql = f"SELECT id FROM threads;"
    result = db.session.execute(text(sql)).fetchall()
    return result

def get_threads_by_username(username, db):
    sql = """SELECT 
    counts.message_count,
    threads.id, threads.owner_id, threads.title, threads.created_at, threads.content, threads.attached_file, users.username
    FROM threads
    LEFT JOIN (
        SELECT thread_id, COUNT(*) AS message_count 
        FROM messages 
        GROUP BY messages.owner_id, messages.thread_id
    ) AS counts ON threads.id = counts.thread_id
    LEFT JOIN users ON users.id = threads.owner_id
    WHERE users.username = (:username);
"""
    result = db.session.execute(text(sql), {"username":username}).fetchall()
    return result

def get_thread_by_id(id, db):
    sql = f"SELECT id, owner_id, title, created_at, content, attached_file FROM threads WHERE id = (:id);"
    result = db.session.execute(text(sql), {"id":id}).fetchone()
    return result