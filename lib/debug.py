#!/usr/bin/env python3
import ipdb

# Import your classes
from classes.models import Article
from classes.models import Author
from classes.models import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Initialize sample instances
    author1 = Author("Jessica Mwangi")
    author2 = Author("John Doe")
    author3 = Author("Jane Smith")

    mag1 = Magazine("Tech Today", "Technology")
    mag2 = Magazine("Health Matters", "Health")
    mag3 = Magazine("Finance World", "Finance")

    article1 = Article(author1, mag1, "AI Revolution")
    article2 = Article(author1, mag2, "Healthy Living Tips")
    article3 = Article(author2, mag1, "Future of Robotics")
    article4 = Article(author3, mag3, "Investment Strategies")
    article5 = Article(author1, mag1, "The Rise of Quantum Computing")
    article6 = Article(author3, mag1, "Cybersecurity Trends")

    # Test methods and outputs
    print("Author1 Articles:", [article.title for article in author1.articles()])
    print("Author1 Magazines:", [mag.name for mag in author1.magazines()])
    print("Author1 Topic Areas:", author1.topic_areas())

    print("Magazine1 Articles:", [article.title for article in mag1.articles()])
    print("Magazine1 Contributors:", [author.name for author in mag1.contributors()])
    print("Magazine1 Article Titles:", mag1.article_titles())
    print("Magazine1 Contributing Authors:", [author.name for author in mag1.contributing_authors() or []])

    new_article = author2.add_article(mag2, "Mental Health Awareness")
    print("New Article Title:", new_article.title)

    print("Article1 Title:", article1.title)
    print("Article1 Author:", article1.author.name)
    print("Article1 Magazine:", article1.magazine.name)

    # Use ipdb for debugging
    ipdb.set_trace()  # This is where the debug session will start
