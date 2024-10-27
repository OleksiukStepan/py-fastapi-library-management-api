from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    bio = Column(String)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    summary = Column(String)
    publication_date = Column(Date)
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship(Author, back_populates="books", lazy="joined")
