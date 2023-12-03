# Assignment 1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"{self.name} (author {self.author}, {self.pages} pages)")
        return


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"{self.name} (chief editor {self.chief_editor})")


mag = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No.6", "Rose Liksom", "192")

mag.print_information()
book.print_information()