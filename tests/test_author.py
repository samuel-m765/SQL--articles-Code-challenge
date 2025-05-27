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

if __name__ == "__main__":
    unittest.main()

