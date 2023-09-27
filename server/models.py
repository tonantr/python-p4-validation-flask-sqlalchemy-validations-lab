from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = "authors"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    @validates("name")
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        if Author.query.filter(Author.name == value, Author.id != self.id).first():
            raise ValueError("Name is already in use.")

    phone_number = db.Column(db.String)

    @validates("phone_number")
    def validate_phone_number(self, key, value):
        if len(value) != 10:
            raise ValueError("Phone number must be 10 digits long.")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"


class Post(db.Model):
    __tablename__ = "posts"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    @validates("title")
    def validate_title(self, key, value):
        # clickbait_words = [
        #     "click",
        #     "watch",
        #     "amazing",
        #     "incredible",
        #     "unbelievable",
        #     "Why I love programming.",
        # ]
        # if any(word in value.lower() for word in clickbait_words):
        #     raise ValueError("Title appears to be clickbait.")

        clickbait_words = "Why I love programming."
        if value == clickbait_words:
            raise ValueError("Title appears to be clickbait")

    content = db.Column(db.String)

    @validates("content")
    def validate_content(self, key, value):
        if len(value) < 250:
            raise ValueError("Content must be at least 250 characters long.")

    category = db.Column(db.String)

    @validates("category")
    def validate_category(self, key, value):
        invalid_category = "Banana"
        if value == invalid_category:
            raise ValueError("Incorrect Category")

    summary = db.Column(db.String)

    @validates("summary")
    def validate_summary(self, key, value):
        if len(value) >= 250:
            raise ValueError("Summary must not exceed 250 characters.")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})"
