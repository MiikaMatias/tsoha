from sqlalchemy import text

def get_categories(db):
    sql = f"""SELECT id, name, description
              FROM categories 
              WHERE show=TRUE;"""
    result = db.session.execute(text(sql)).fetchall()

    return result

def get_category_id(category, db):
    sql = "SELECT id FROM categories WHERE name = (:category)"
    id = int(db.session.execute(text(sql), {"category":category}).fetchone()[0])
    return id

def get_description(category, db):
    sql = "SELECT description FROM categories WHERE name = (:category)"
    desc = db.session.execute(text(sql), {"category":category}).fetchone()[0]
    return desc

def allowed_categories(db):
    sql = "SELECT name FROM categories"
    cats = db.session.execute(text(sql)).fetchall()
    return [cat[0] for cat in cats]
