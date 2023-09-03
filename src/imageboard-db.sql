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

/*
INSERT INTO users (username, pass, email)
VALUES
    ('Bimba', 'Bimba', 'bimba@example.com'),
    ('Jane Doe', 'JaneDoe', 'jd@example.com'),
    ('John Smith', 'JohnSmith', 'John_Smith@example.com'),
    ('Axel', 'Axel', 'Axel@example.com');

INSERT INTO threads (owner_id, category, title, content)
VALUES (1, 1, 'Introduction Thread', 'Hello, I am new here. Nice to meet you all!'),
       (2, 1, 'New Member Introduction', 'Hello, I just joined the community. Excited to be here!'),
       (2, 2, 'Latest Smartphone Releases', 'Lets discuss the latest smartphone releases and features.'),
       (3, 3, 'Favorite Travel Destinations', 'Share your favorite travel destinations and memorable experiences.');

INSERT INTO messages (thread_id, owner_id, content)
VALUES
    (1, 1, 'Welcome to the forum, Bimba!'),
    (1, 2, 'Hi Bimba, nice to meet you!'),
    (1, 3, 'Hello everyone!'),
    (2, 2, 'Hey there! Welcome to the community.'),
    (2, 3, 'Hello Jane Doe, glad to have you here.'),
    (3, 2, 'I just got the new smartphone XYZ, and its amazing!'),
    (3, 3, 'Im thinking of upgrading my phone soon. Tell me more about it!'),
    (4, 3, 'I recently visited Japan, and it was an incredible experience!'),
    (4, 4, 'Japan is on my travel bucket list. Any tips for first-time travelers?');
*/
