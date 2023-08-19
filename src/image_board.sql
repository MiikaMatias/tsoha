CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    pass VARCHAR(300) NOT NULL, 
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO users (username, pass, email, created_at) 
VALUES ('man_1', 'pbkdf2:sha256:600000$OAQs2REBfRnJsekM$ff91d16e0f8372f91bb94918f41d91bb7600e618f2bcb77948345fb1faeea51c', 'my_email@emailservice.com', NOW());
INSERT INTO users (username, pass, email, created_at) 
VALUES ('man_2', 'pbkdf2:sha256:600000$OAQs2REBfRnJsekM$ff91d16e0f8372f91bb94918f41d91bb7600e618f2bcb77948345fb1faeea51c', 'my_email_2@emailservice.com', NOW());

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    owner_id INT, 
    title VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW(),
    content VARCHAR(5000),
    attached_file bytea
);

INSERT INTO threads (owner_id, title, created_at, content) 
VALUES (1, 'hello!', NOW(), 'this is a thread!');
INSERT INTO threads (owner_id, title, created_at, content) 
VALUES (2, 'hello world!', NOW(), 'this is a thread also!');

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    thread_id INT,
    owner_id INT,
    content VARCHAR(5000),
    created_at TIMESTAMP DEFAULT NOW(),
    attached_file bytea
);

INSERT INTO messages (thread_id, owner_id, content, created_at) 
VALUES (1, 1, 'what is up?', NOW());
INSERT INTO messages (thread_id, owner_id, content, created_at) 
VALUES (1, 2, 'chicken butt', NOW());
INSERT INTO messages (thread_id, owner_id, content, created_at) 
VALUES (2, 2, 'hello me!', NOW());