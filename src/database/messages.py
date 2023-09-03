from sqlalchemy import text
from database.helpers import make_image_readable_message


def get_messages(id, db):
    sql = f"""SELECT messages.id, messages.thread_id, messages.owner_id, messages.created_at, messages.content, users.username, images.image_data
              FROM messages 
              JOIN users ON users.id = messages.owner_id 
              JOIN images ON messages.image_id = images.id
              WHERE messages.thread_id = (:id) AND messages.show = TRUE;"""
    result = db.session.execute(text(sql), {'id': id}).fetchall()

    return make_image_readable_message(result)


def insert_message(thread_id, owner_id, image_id, content, db):
    sql = """INSERT INTO messages (thread_id, owner_id, image_id, content, created_at) 
                VALUES (:thread_id, :owner_id, :image_id, :content, NOW());"""
    db.session.execute(text(sql), {"thread_id": thread_id, "owner_id": owner_id, "image_id": image_id, "content": content})
    db.session.commit()


def delete_message(owner_id, id, db):
    sql = """UPDATE messages
            SET show = FALSE
            WHERE id = (:id)
            AND owner_id = (:owner_id);"""

    db.session.execute(text(sql), {"owner_id": owner_id, "id": id})
    db.session.commit()
