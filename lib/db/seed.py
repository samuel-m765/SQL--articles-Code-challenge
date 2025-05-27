from lib.models.author import Author
from lib.models.magazine import Magazine

def seed():
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    author1.add_article(magazine1, "The Future of AI")
    author2.add_article(magazine2, "Nutrition Tips for 2025")

if __name__ == "__main__":
    seed()
