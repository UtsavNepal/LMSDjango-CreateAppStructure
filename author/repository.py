from .models import Author

class AuthorRepository:
    @staticmethod
    def get_all_authors():
        return Author.objects.all()

    @staticmethod
    def get_author_by_id(author_id):
        return Author.objects.get(AuthorId=author_id)

    @staticmethod
    def create_author(name, bio):
        return Author.objects.create(Author_Name=name, Bio=bio)
