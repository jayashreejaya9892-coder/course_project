
import unittest
from library import books, add_book, display_books

class TestLibrary(unittest.TestCase):

    def setUp(self):
        books.clear()

    def test_add_book(self):
        books.append({
            "id": "B101",
            "name": "Python Programming",
            "author": "John Smith",
            "available": True
        })

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["id"], "B101")

    def test_book_availability(self):
        books.append({
            "id": "B102",
            "name": "Java Programming",
            "author": "James",
            "available": True
        })

        self.assertTrue(books[0]["available"])

    def test_book_issue_status(self):
        books.append({
            "id": "B103",
            "name": "C Programming",
            "author": "Dennis",
            "available": False
        })

        self.assertFalse(books[0]["available"])


if __name__ == "__main__":
    unittest.main()
