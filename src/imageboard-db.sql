CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    pass VARCHAR(300) NOT NULL,
    email VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50),
    description VARCHAR(400),
    show BOOLEAN DEFAULT TRUE
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users(id),
    category INTEGER REFERENCES categories(id),
    title VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW(),
    content VARCHAR(5000),
    show BOOLEAN DEFAULT TRUE
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    image_data BYTEA,
    title VARCHAR(50)
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    thread_id INTEGER REFERENCES threads(id),
    owner_id INTEGER REFERENCES users(id),
    content VARCHAR(5000),
    attachment_id INTEGER REFERENCES images(id),
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
