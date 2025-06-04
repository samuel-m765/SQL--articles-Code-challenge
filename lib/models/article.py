# lib/models/article.py

from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute(
                """
                INSERT INTO articles (title, author_id, magazine_id)
                VALUES (?, ?, ?)
                """,
                (self.title, self.author_id, self.magazine_id)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                """
                UPDATE articles
                SET title = ?, author_id = ?, magazine_id = ?
                WHERE id = ?
                """,
                (self.title, self.author_id, self.magazine_id, self.id)
            )

        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(**row) if row else None

    @classmethod
    def find_by_title(cls, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
        row = cursor.fetchone()
        conn.close()
        return cls(**row) if row else None

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        rows = cursor.fetchall()
        conn.close()
        return [cls(**row) for row in rows]

    @property
    def author(self):
        from lib.models.author import Author
        return Author.find_by_id(self.author_id)

    @property
    def magazine(self):
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Title must be a non-empty string.")
        self._title = value
