import unittest


class Article:
    def __init__(self, title, author_id, magazine_id):
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

class TestArticle(unittest.TestCase):
    def test_article_creation(self):
        article = Article("Quantum Computing Explained", author_id=1, magazine_id=10)
        self.assertEqual(article.title, "Quantum Computing Explained")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 10)

    def test_article_title_is_string(self):
        article = Article("AI and the Future", author_id=2, magazine_id=20)
        self.assertIsInstance(article.title, str)

    def test_article_author_and_magazine_ids_are_int(self):
        article = Article("Deep Learning", author_id=3, magazine_id=30)
        self.assertIsInstance(article.author_id, int)
        self.assertIsInstance(article.magazine_id, int)

if __name__ == "__main__":
    unittest.main()
