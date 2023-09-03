from sqlalchemy import text
import base64
from database.helpers import make_image_readable_thread



def get_thread_answers(thread_id, db):
    sql = f"SELECT id FROM messages WHERE id = (:id) AND show=TRUE;"
    result = db.session.execute(text(sql), {"id":thread_id}).fetchall()
    print(result)
    return len(result)

def get_threads_by_category(db, category):
    sql = """SELECT threads.id, threads.owner_id, threads.image_id, threads.title, threads.created_at, threads.content, users.username, images.image_data, COUNT(messages.id) AS message_count
        FROM threads 
        JOIN users ON users.id = threads.owner_id
        JOIN categories ON threads.category_id = categories.id
        JOIN images ON threads.image_id = images.id
        LEFT JOIN messages ON threads.id = messages.thread_id
        WHERE threads.show = TRUE AND categories.name = (:category)
        GROUP BY threads.id, threads.owner_id, threads.image_id, threads.title, threads.created_at, threads.content, users.username, images.image_data
        ORDER BY message_count DESC;
        """
    result = db.session.execute(text(sql), {"category": category}).fetchall()
    return make_image_readable_thread(result)

def get_thread_ids(db):
    sql = f"SELECT id FROM threads WHERE show=TRUE;"
    result = db.session.execute(text(sql)).fetchall()
    return result

def get_threads_by_username(username, db):
    sql = """SELECT 
    counts.message_count,
    threads.id, threads.owner_id, threads.image_id, threads.title, threads.created_at, threads.content, users.username, categories.name
    FROM threads
    LEFT JOIN (
        SELECT thread_id, COUNT(*) AS message_count 
        FROM messages 
        GROUP BY messages.owner_id, messages.thread_id
    ) AS counts ON threads.id = counts.thread_id
    LEFT JOIN users ON users.id = threads.owner_id
    LEFT JOIN categories ON categories.id = threads.category_id
    WHERE users.username = (:username) AND threads.show=TRUE;
    """
    result = db.session.execute(text(sql), {"username":username}).fetchall()
    return result

def get_thread_by_id(id, category, db):
    sql = f"""SELECT threads.id, threads.owner_id, threads.image_id, threads.title, threads.created_at, threads.content, users.username, images.image_data
            FROM threads 
            JOIN users ON users.id = threads.owner_id
            JOIN categories ON threads.category_id=categories.id
            JOIN images ON threads.image_id=images.id
            WHERE threads.id = (:id) AND threads.show=TRUE AND categories.name=(:category);
            """
    result = db.session.execute(text(sql), {"id":id, "category":category}).fetchone()

    thread_id, owner_id, image_id, title, created_at, content, username, image_data = result
    image_data_base64 = base64.b64encode(image_data).decode("utf-8")
    
    thread_dict = {
        "id": thread_id,
        "owner_id": owner_id,
        "image_id": image_id,
        "title": title,
        "created_at": created_at,
        "content": content,
        "username": username,
        "image_data_base64": image_data_base64
    }
    
    return thread_dict  

def insert_thread(owner_id, title, image_id, content, category_id, db):
    sql = """INSERT INTO threads (owner_id, title, image_id, content, category_id, created_at) 
                VALUES (:owner_id, :title, :image_id, :content, :category_id, NOW());"""
    db.session.execute(text(sql), {"owner_id":owner_id, "title": title, "image_id":image_id,"content":content, "category_id":category_id})
    db.session.commit()

def delete_thread(id, owner_id, db):
    sql = """UPDATE threads
            SET show=FALSE
            WHERE id = (:id)
            AND owner_id = (:owner_id);"""

    db.session.execute(text(sql), {"owner_id":owner_id, "id": id})
    db.session.commit()