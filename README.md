This project models the relationships between Authors, Articles, and Magazines using raw SQL queries in Python, without the use of ORM libraries like SQLAlchemy.

Domain Logic
An Author can write many Articles

A Magazine can publish many Articles

An Article belongs to one Author and one Magazine

There is a many-to-many relationship between Authors and Magazines (via Articles)

 Project Structure
pgsql
Copy
Edit
code-challenge/
├── lib/
│   ├── models/
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
│   ├── db/
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   └── seed.py
│   └── debug.py
├── tests/
│   ├── test_author.py
│   ├── test_article.py
│   └── test_magazine.py
├── scripts/
│   ├── setup_db.py
│   └── run_queries.py
└── README.md
🛠️ Setup Instructions
Option 1: Using pipenv
bash
Copy
Edit
pipenv install pytest sqlite3
pipenv shell
Option 2: Using venv
bash
Copy
Edit
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install pytest
 Database Setup
Using SQLite (recommended)
Edit lib/db/connection.py:

python
Copy
Edit
import sqlite3

def get_connection():
    conn = sqlite3.connect('articles.db')
    conn.row_factory = sqlite3.Row
    return conn
Run schema and seed:

bash
Copy
Edit
python lib/debug.py  # Resets DB and inserts sample data
 Running Tests
Use pytest from the root directory:

bash
Copy
Edit
pytest
To manually inspect your setup:

bash
Copy
Edit
python lib/debug.py
Features
Author
save()

find_by_id(id)

articles()

magazines()

add_article(magazine, title)

topic_areas()

Article
save()

find_by_id(id)

find_by_title(title)

author (property)

magazine (property)

Magazine
save()

find_by_id(id)

articles()

contributors()

article_titles()

contributing_authors()

 Example Schema (lib/db/schema.sql)
sql
Copy
Edit
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS magazines (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER,
    magazine_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (magazine_id) REFERENCES magazines(id)
);
 Git & Version Control
.gitignore Example
markdown
Copy
Edit
env/
*.
*.pyc
Example Commit Messages
feat: implement Article class with save/find methods

fix: correct foreign key constraint for articles

test: add unit tests for Magazine methods

 Bonus Features
Transaction-safe inserts

Complex aggregate queries

Magazine with most contributors

Authors with more than two articles in a magazine

 Submission Checklist
 All tests pass

 Schema and SQL logic implemented correctly

 Classes follow OOP principles

 Committed with meaningful messages

 GitHub repo is clean and well-organized

 Author
Samuel Mbogo
student at moringa school