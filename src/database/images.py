from sqlalchemy import text


def upload_image(uploaded_file, db):
    image_data = uploaded_file.read()

    sql = "INSERT INTO images (image_data) VALUES (:image_data);"
    db.session.execute(text(sql), {"image_data": image_data})
    db.session.commit()

    sql = "SELECT id FROM images WHERE image_data=(:image_data);"
    id = int(db.session.execute(text(sql), {"image_data": image_data}).fetchone()[0])
    return id





