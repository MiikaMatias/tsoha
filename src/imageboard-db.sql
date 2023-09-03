CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    pass VARCHAR(300) NOT NULL,
    email VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    image_data BYTEA DEFAULT NULL
);

INSERT INTO images (image_data)
VALUES (E'\\x48656C6C6F2C205468697320697320612073616D706C6520737472696E67206F662062696E61727920646174612C20616E64206974206B656570732074686520657965732C20747275652C20616E642069742773207265616C6C7920636F6F6C2E'::bytea);


CREATE TABLE categories (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50),
    description VARCHAR(400),
    show BOOLEAN DEFAULT TRUE
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users(id),
    image_id INTEGER REFERENCES images(id),
    category_id INTEGER REFERENCES categories(id),
    title VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW(),
    content VARCHAR(5000),
    show BOOLEAN DEFAULT TRUE
);


CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    thread_id INTEGER REFERENCES threads(id),
    owner_id INTEGER REFERENCES users(id),
    image_id INTEGER REFERENCES images(id),
    content VARCHAR(5000),
    created_at TIMESTAMP DEFAULT NOW(),
    show BOOLEAN DEFAULT TRUE
);

INSERT INTO categories (name, description) VALUES
    ('General', 'A place to discuss anything and everything.'),
    ('Technology', 'Discuss the latest tech trends and gadgets.'),
    ('Travel', 'Share your travel experiences and tips.'),
    ('Food', 'Talk about your favorite recipes and culinary adventures.'),
    ('Gaming', 'Chat about your favorite video games and strategies.'),
    ('Books', 'Discuss books, authors, and literary works.'),
    ('Music', 'Share your favorite music, artists, and concerts.'),
    ('Fitness', 'Get advice on staying fit and healthy.'),
    ('Movies', 'Talk about the latest films and TV series.'),
    ('Art', 'Showcase your artwork and discuss creative projects.');