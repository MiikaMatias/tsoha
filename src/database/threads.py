from sqlalchemy import text

def get_thread_answers(thread_id, db):
    sql = f"SELECT id FROM messages WHERE id = (:id) AND show=TRUE;"
    result = db.session.execute(text(sql), {"id":thread_id}).fetchall()
    print(result)
    return len(result)

def get_threads_by_category(db, category):
    sql = """SELECT threads.id, threads.owner_id, threads.title, threads.created_at, threads.content, users.username 
             FROM threads 
             JOIN users ON users.id = threads.owner_id
             JOIN categories ON threads.category=categories.id
             WHERE threads.show=TRUE AND categories.name=(:category);"""
    result = db.session.execute(text(sql), {"category":category}).fetchall()
    return result

def get_thread_ids(db):
    sql = f"SELECT id FROM threads WHERE show=TRUE;"
    result = db.session.execute(text(sql)).fetchall()
    return result

def get_threads_by_username(username, db):
    sql = """SELECT 
    counts.message_count,
    threads.id, threads.owner_id, threads.title, threads.created_at, threads.content, users.username, categories.name
    FROM threads
    LEFT JOIN (
        SELECT thread_id, COUNT(*) AS message_count 
        FROM messages 
        GROUP BY messages.owner_id, messages.thread_id
    ) AS counts ON threads.id = counts.thread_id
    LEFT JOIN users ON users.id = threads.owner_id
    LEFT JOIN categories ON categories.id = threads.category
    WHERE users.username = (:username) AND threads.show=TRUE;
"""
    result = db.session.execute(text(sql), {"username":username}).fetchall()
    return result

def get_thread_by_id(id, category, db):
    sql = f"""SELECT threads.id, threads.owner_id, threads.title, threads.created_at, threads.content 
            FROM threads 
            JOIN categories ON threads.category=categories.id
            WHERE threads.id = (:id) AND threads.show=TRUE AND categories.name=(:category);
            """
    result = db.session.execute(text(sql), {"id":id, "category":category}).fetchone()
    return result