import unittest


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.id = id(self)

class Article:
    def __init__(self, title, author_id, magazine_id):
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

class Author:
    def __init__(self, name):
        self.name = name
        self.id = id(self)
        self.articles = []

    def add_article(self, magazine, title):
        article = Article(title, self.id, magazine.id)
        self.articles.append(article)
        return article


class TestAuthor(unittest.TestCase):
    def test_add_article(self):
        author = Author("Alice")
        magazine = Magazine("Tech Today", "Technology")

        article = author.add_article(magazine, "Quantum Computing Explained")

        self.assertEqual(article.title, "Quantum Computing Explained")
        self.assertEqual(article.author_id, author.id)
        self.assertEqual(article.magazine_id, magazine.id)

    def test_author_can_have_multiple_articles(self):
        author = Author("Alice")
        magazine1 = Magazine("Tech Today", "Technology")
        magazine2 = Magazine("Science Weekly", "Science")

        article1 = author.add_article(magazine1, "Quantum Computing Explained")
        article2 = author.add_article(magazine2, "The Future of AI")

        self.assertEqual(len(author.articles), 2)
        self.assertIn(article1, author.articles)
        self.assertIn(article2, author.articles)

class TestMagazine(unittest.TestCase):
    def test_magazine_creation(self):
        mag = Magazine("Tech Today", "Technology")
        self.assertEqual(mag.name, "Tech Today")
        self.assertEqual(mag.category, "Technology")
        self.assertIsInstance(mag.id, int)

class TestArticle(unittest.TestCase):
    def test_article_creation(self):
        author = Author("Alice")
        magazine = Magazine("Tech Today", "Technology")

        article = Article("Quantum Computing Explained", author.id, magazine.id)
        self.assertEqual(article.title, "Quantum Computing Explained")
        self.assertEqual(article.author_id, author.id)
        self.assertEqual(article.magazine_id, magazine.id)

if __name__ == "__main__":
    unittest.main()
