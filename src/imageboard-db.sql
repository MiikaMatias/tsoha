CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    pass VARCHAR(300) NOT NULL,
    email VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO users (username, pass, email)
VALUES ('user', 'pass', 'testuser@example.com');

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW(),
    content VARCHAR(5000),
    show BOOLEAN DEFAULT TRUE
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    image_data BYTEA
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    thread_id INTEGER REFERENCES threads(id) ON DELETE CASCADE,
    owner_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    content VARCHAR(5000),
    attachment_id INTEGER REFERENCES images(id),
    created_at TIMESTAMP DEFAULT NOW(),
    show BOOLEAN DEFAULT TRUE
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY
);
