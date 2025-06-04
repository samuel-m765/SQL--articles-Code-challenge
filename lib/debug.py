# lib/debug.py

from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def reset_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(open("lib/db/schema.sql").read())
    conn.commit()
    conn.close()
    print("Database schema reset.")

def seed_data():
    author1 = Author(name="Samuel Mbogo")
    author1.save()

    mag1 = Magazine(name="Tech Today", category="Technology")
    mag1.save()

    article1 = Article(title="AI in Africa", author_id=author1.id, magazine_id=mag1.id)
    article1.save()

    print("Sample data inserted.")

if __name__ == "__main__":
    reset_db()
    seed_data()

    print("\nAll Articles:")
    for article in Article.all():
        print(f"{article.id}: {article.title} by Author ID {article.author_id} in Magazine ID {article.magazine_id}")
