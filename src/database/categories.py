from sqlalchemy import text

def get_categories(db):
    sql = f"""SELECT id, name, description
              FROM categories 
              WHERE show=TRUE;"""
    result = db.session.execute(text(sql)).fetchall()

    return result

def get_category_id(category, db):
    sql = 'SELECT id FROM categories WHERE name = (:category)'
    id = int(db.session.execute(text(sql), {'category':category}).fetchone()[0])
    return id