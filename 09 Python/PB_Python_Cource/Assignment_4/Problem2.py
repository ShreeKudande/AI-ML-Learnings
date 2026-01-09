#Create a class Book with the following attributes:
#title, author, list of reviews,
#and add methods to: add a new review, count reviews, display all reviews

class Book:
    title = "LEVEL UP!"
    author = "Rob Dial"

    review_count = 0

    def __init__(self, add_new_review):
        self.add_new_review = add_new_review
        Book.review_count += 1

    @classmethod
    def get_count(cls):
        print(f"There are {cls.review_count} reviews.")

    def get_reviews(self):
        print(f"{self.add_new_review}")

r1 = Book("It's a great book!")
r2 = Book("I loved it!")

r1.get_reviews()
r2.get_reviews()

Book.get_count()

