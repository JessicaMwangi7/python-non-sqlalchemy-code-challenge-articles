class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()}) or None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles] or None

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        return [author for author in set(authors) if authors.count(author) > 2] or None


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        author.articles().append(self)
        magazine.articles().append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        self._magazine = new_magazine
