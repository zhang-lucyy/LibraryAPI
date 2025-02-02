DROP SCHEMA IF EXISTS library CASCADE;
DROP TABLE IF EXISTS reserve;
DROP TABLE IF EXISTS checkout;
DROP TABLE IF EXISTS library_stock;
DROP TABLE IF EXISTS libraries;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id SERIAL NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    contact_info TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    session_key TEXT DEFAULT '' NOT NULL
);

CREATE TABLE inventory(
    book_id SERIAL NOT NULL PRIMARY KEY,
    title TEXT NOT NULL,
    book_type TEXT NOT NULL,
    author TEXT NOT NULL,
    publish_date INTEGER DEFAULT NULL,
    summary TEXT DEFAULT '' NOT NULL,
    copies INTEGER DEFAULT 0 NOT NULL
);

CREATE TABLE libraries(
    library_id SERIAL NOT NULL PRIMARY KEY,
    library_name TEXT NOT NULL
);

CREATE TABLE library_stock(
    library_id INTEGER,
    book_id INTEGER,
    book_copies INTEGER,
    FOREIGN KEY(library_id) REFERENCES libraries(library_id),
    FOREIGN KEY(book_id) REFERENCES inventory(book_id)
);

CREATE TABLE checkout(
    library_id INTEGER,
    book_id INTEGER,
    user_id INTEGER,
    check_out_date DATE,
    due_date DATE DEFAULT NULL,
    return_date DATE DEFAULT NULL,
    late_fees DECIMAL DEFAULT 0.0,
    FOREIGN KEY(library_id) REFERENCES libraries(library_id),
    FOREIGN KEY(book_id) REFERENCES inventory(book_id),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE reserve(
    library_id INTEGER,
    reserve_book_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY(library_id) REFERENCES libraries(library_id),
    FOREIGN KEY(reserve_book_id) REFERENCES inventory(book_id),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO users(name, contact_info, username, password) VALUES
    ('Ada Lovelace', 'ALovelace@gmail.com', 'lovelace12', 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'),
    --('Mary Shelley', 'MShelley@gmail.com', 'shelley60'),
    ('Jackie Gleason', 'JGleason@gmail.com', 'gleason34', '8a81c03957705caeceb1c2f201533609bec95d9a1c8bdcefad5bf96aad64295d8ce486e943dc82f1ea503ee48663d7a1f52ef99aba87b0c9f1fbb913a81a0925');
    --('Art Garfunkel', 'AGarfunkel@gmail.com', 'garfunkel87');

INSERT INTO inventory(title, book_type, author, publish_date, summary, copies) VALUES
    ('Figuring', 'Non-fiction', 'Maria Popova', 2019,
        'Explores the complexities of love and the human search for truth and meaning', 5),
    ('In Defence of Witches', 'Non-fiction', 'Mona Chollet', 2022,
        'Explores how women who assert their powers are too often seen as a threat to men and society', 3),
    ('Scary Smart', 'Non-fiction', 'Mo Gawdat', 2021,
        'Explores the future of artificial intelligence', 7),
    ('The Princess Spy', 'Non-fiction', 'Larry Loftis', 2022,
        'Follows the hidden history of an ordinary American girl who became one of the most daring WWII spies', 2),
    ('The Dead Romantics', 'Fiction', 'Ashley Poston', 2022,
        'The main character is a ghostwriter for a romance novelist', 6),
    ('The Lord of the Rings', 'Fiction', 'J.R.R. Tolkien', 1954, 
        'A group of heroes set forth to save their world', 1),
    ('The Lightning Thief', 'Fiction', 'Rick Riordan', 2005, 
        'A 12 year-old boy who learns that his true father is Poseidon', 4),
    ('To Kill a Mockingbird', 'Fiction', 'Harper Lee', 1960,
        'Chronicles the childhood of Scout and Jem Finch', 1),
    ('Frankenstein', 'Fiction', 'Mary Shelley', 1818,
        'A young scientist who creates a sapient creature in an scientific experiment', 1),
    ('The Winds of Winter', 'Fiction', 'George R.R. Martin', 2023,
        'Sixth novel in the epic fantasy series A Song of Ice and Fire', 4);

INSERT INTO libraries(library_name) VALUES
    ('Penfield'),
    ('Fairport'),
    ('Henrietta'),
    ('Pittsford');

INSERT INTO library_stock(library_id, book_id, book_copies) VALUES
    --Penfield
    (1, 1, 4),
    (1, 3, 1),
    (1, 4, 1),
    (1, 5, 2),
    (1, 6, 0),
    (1, 7, 1),
    (1, 10, 1),

    --Fairport
    (2, 2, 1),
    (2, 3, 3),
    (2, 4, 1),
    (2, 5, 2),
    (2, 7, 1),
    (2, 8, 1),
    (2, 10, 1),

    --Henrietta
    (3, 1, 1),
    (3, 2, 1),
    (3, 3, 2),
    (3, 5, 1),
    (3, 7, 2),
    (3, 8, 1),
    (3, 10, 1),

    --Pittsford
    (4, 2, 1),
    (4, 3, 1),
    (4, 5, 1),
    (4, 9, 1),
    (4, 10, 1);

INSERT INTO checkout(library_id, book_id, user_id, check_out_date, due_date, return_date) VALUES
    --Ada checked out "In Defence of Witches"
    (1, 2, 1, '2020-09-05', DEFAULT,'2020-09-07'),
    (3, 5, 1, '2020-09-08', '2020-09-22', DEFAULT),
    --Mary checked out "Scary Smart"
    --(3, 3, 2, '2020-09-08', DEFAULT, '2020-09-15'),
    --Jackie checked out "The Lightning Thief" and "To Kill a Mockingbird"
    (4, 7, 2, '2020-09-10', DEFAULT, '2020-09-20'),
    (4, 8, 2, '2020-09-11', DEFAULT, '2020-09-24');